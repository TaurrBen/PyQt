# 声明：本代码仅供学习和研究目的使用。使用者应遵守以下原则：  
# 1. 不得用于任何商业用途。  
# 2. 使用时应遵守目标平台的使用条款和robots.txt规则。  
# 3. 不得进行大规模爬取或对平台造成运营干扰。  
# 4. 应合理控制请求频率，避免给目标平台带来不必要的负担。   
# 5. 不得用于任何非法或不当的用途。
#   
# 详细许可条款请参阅项目根目录下的LICENSE文件。  
# 使用本代码即表示您同意遵守上述原则和LICENSE中的所有条款。  

# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : client.py
# Time       ：2025.2.22 11:27
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：bilibili 请求客户端
"""

import asyncio
import json
from typing import Any, Callable, Dict, List, Optional, Tuple, Union
from urllib.parse import urlencode

import httpx
from playwright.async_api import BrowserContext, Page

from .exception import DataFetchError
from .field import *
from .help import BilibiliSign
from utils.spider import *


import config



class BilibiliClient(AbstractApiClient):

    def __init__(self,
                 timeout=10,
                 proxies=None,
                 *,
                 headers: Dict[str, str] = None,
                 playwright_page: Page = None,
                 cookie_dict: Dict[str, str] = None,
                 ):
        self.proxies = proxies
        self.timeout = timeout
        self.headers = headers
        self._host = "https://api.bilibili.com"
        self.playwright_page = playwright_page
        self.cookie_dict = cookie_dict

    async def request(self, method, url, **kwargs) -> Any:
        async with httpx.AsyncClient(proxies=self.proxies) as client:
            response = await client.request(method, url, timeout=self.timeout,**kwargs)
        data: Dict = response.json()
        config.logger.debug(f"Request {method}-{url}.")
        if data.get("code") != 0:
            raise DataFetchError(data.get("message", "unkonw error"))
        else:
            return data.get("data", {})

    async def pre_request_data(self, req_data: Dict) -> Dict:
        """
        发送请求进行请求参数签名
        需要从 localStorage 拿 wbi_img_urls 这参数，值如下：
        https://i0.hdslb.com/bfs/wbi/7cd084941338484aae1ad9425b84077c.png-https://i0.hdslb.com/bfs/wbi/4932caff0ff746eab6f01bf08b70ac45.png
        :param req_data:
        :return:
        """
        if not req_data:
            return {}
        img_key, sub_key = await self.get_wbi_keys()
        res = BilibiliSign(img_key, sub_key).sign(req_data)
        config.logger.debug(f"{req_data} -sign- {res}.")
        return res

    async def get_wbi_keys(self) -> Tuple[str, str]:
        """
        获取最新的 img_key 和 sub_key
        :return:
        """
        # 执行js代码
        local_storage = await self.playwright_page.evaluate("() => window.localStorage")
        wbi_img_urls = local_storage.get("wbi_img_urls", "") or local_storage.get(
            "wbi_img_url") + "-" + local_storage.get("wbi_sub_url")
        if wbi_img_urls and "-" in wbi_img_urls:
            img_url, sub_url = wbi_img_urls.split("-")
        else:
            resp = await self.request(method="GET", url=self._host + "/x/web-interface/nav")
            img_url: str = resp['wbi_img']['img_url']
            sub_url: str = resp['wbi_img']['sub_url']
        img_key = img_url.rsplit('/', 1)[1].split('.')[0]
        sub_key = sub_url.rsplit('/', 1)[1].split('.')[0]
        return img_key, sub_key

    async def get(self, uri: str, params=None, enable_params_sign: bool = True) -> Dict:
        final_uri = uri
        if enable_params_sign:
            params = await self.pre_request_data(params)
        if isinstance(params, dict):
            final_uri = (f"{uri}?"
                         f"{urlencode(params)}")
        return await self.request(method="GET", url=f"{self._host}{final_uri}", headers=self.headers)

    async def post(self, uri: str, data: dict) -> Dict:
        data = await self.pre_request_data(data)
        json_str = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        return await self.request(method="POST", url=f"{self._host}{uri}",
                                  data=json_str, headers=self.headers)

    async def pong(self) -> bool:
        """get a note to check if login state is ok"""
        config.logger.info("Begin pong bilibili...")
        ping_flag = False
        try:
            check_login_uri = "/x/web-interface/nav"
            response = await self.get(check_login_uri)
            if response.get("isLogin"):
                config.logger.info("Use cache login state get web interface successfull!")
                ping_flag = True
        except Exception as e:
            config.logger.error(f"Pong bilibili failed: {e}, and try to login again...")
            ping_flag = False
        return ping_flag

    async def update_cookies(self, browser_context: BrowserContext):
        cookie_str, cookie_dict = convert_cookies(await browser_context.cookies())
        self.headers["Cookie"] = cookie_str
        self.cookie_dict = cookie_dict
        return cookie_str, cookie_dict

    async def search_by_keyword(self,
                                search_type:str,
                                page:int,
                                page_size:int,
                                order:str,
                                duration:int,
                                pubtime_begin_s:str,
                                pubtime_end_s:str,
                                keyword:str,
                                tids:str
                                ) -> Dict:

        """
        bilibili web search api
        :param keyword: 搜索关键词
        :return:
        """
        uri = "/x/web-interface/wbi/search/type"
        post_data = {
            "search_type": SEARCH_TYPE_LIST.get(search_type),
            "__refresh__": True,
            "page": page,
            "page_size": page_size,
            "order": ORDER_TYPE_LIST.get(order),
            "duration": duration,
            "pubtime_begin_s": int(pubtime_begin_s),
            "pubtime_end_s": int(pubtime_end_s),
            "platform": "pc",
            "keyword": keyword,
            "tids":TIDS_LIST.get(tids)
        }
        return await self.get(uri, post_data)

    async def get_video_info(self, aid: Union[int, None] = None, bvid: Union[str, None] = None) -> Dict:
        """
        Bilibli web video detail api, aid 和 bvid任选一个参数
        :param aid: 稿件avid
        :param bvid: 稿件bvid
        :return:
        """
        if not aid and not bvid:
            raise ValueError("请提供 aid 或 bvid 中的至少一个参数")
        uri = "/x/web-interface/view/detail"
        params = dict()
        if aid:
            params.update({"aid": aid})
        else:
            params.update({"bvid": bvid})
        return await self.get(uri, params, enable_params_sign=False)

    async def get_video_play_url(self, aid: int, cid: int) -> Dict:
        """
        Bilibli web video play url api
        :param aid: 稿件avid
        :param cid: cid
        :return:
        """
        # TODO : 待处理视频清晰度
        if not aid or not cid or aid <= 0 or cid <= 0:
            raise ValueError("aid 和 cid 必须存在")
        uri = "/x/player/wbi/playurl"
        params = {
            "avid": aid,
            "cid": cid,
            "qn": 80,
            "fourk": 1,
            "fnval": 1,
            "platform": "pc",
        }
        return await self.get(uri, params, enable_params_sign=True)

    async def get_video_media(self, url: str) -> Union[bytes, None]:
        async with httpx.AsyncClient(proxies=self.proxies) as client:
            response = await client.request("GET", url, timeout=self.timeout, headers=self.headers)
            if not response.reason_phrase == "OK":
                config.logger.error(f" request {url} err, res:{response.text}")
                return None
            else:
                return response.content

    #### video comment
    async def get_video_comments(self,video_id: str,order_mode: str = "default",next: int = 0) -> Dict:
        """get video comments
        :param video_id: 视频 ID
        :param order_mode: 排序方式
        :param next: 评论页选择
        :return:
        """
        uri = "/x/v2/reply/wbi/main"
        post_data = {
            "oid": video_id,
            "mode": COMMENT_TYPE_LIST.get(order_mode),
            "type": 1,
            "ps": 20,
            "next": next
        }
        return await self.get(uri, post_data)

    async def get_video_sub_comments(self,
                                     video_id: str,
                                     level_one_comment_id: int,
                                     pn: int,
                                     ps: int,
                                     order_mode:str = "default",
                                     ) -> Dict:
        """get video level two comments
        :param video_id: 视频 ID
        :param level_one_comment_id: 一级评论 ID
        :param order_mode: 排序方式
        :return:
        """
        uri = "/x/v2/reply/reply"
        post_data = {
            "oid": video_id,
            "mode": COMMENT_TYPE_LIST.get(order_mode),
            "type": 1,
            "ps": ps,
            "pn": pn,
            "root": level_one_comment_id,
        }
        result = await self.get(uri, post_data)
        return result

    async def get_video_all_sub_comments(self,
                                         video_id: str,
                                         level_one_comment_id: int,
                                         order_mode: str = "default",
                                         ps: int = 10,
                                         crawl_interval: float = 1.0,
                                         callback: Optional[Callable] = None,
                                         ) -> List:
        """
        get video all level two comments for a level one comment
        :param video_id: 视频 ID
        :param level_one_comment_id: 一级评论 ID
        :param order_mode:
        :param ps: 一页评论数
        :param crawl_interval:
        :param callback:
        :return:
        """
        res = []
        pn = 1
        while True:
            result = await self.get_video_sub_comments(
                video_id, level_one_comment_id, pn, ps, COMMENT_TYPE_LIST.get(order_mode))
            comment_list: List[Dict] = result.get("replies", [])
            if callback:  # 如果有回调函数，就执行回调函数
                await callback(video_id, comment_list)
                res.append(comment_list)
            await asyncio.sleep(crawl_interval)
            if (int(result["page"]["count"]) <= pn * ps):
                return res
            pn += 1

    async def get_video_all_level_comments(self,
                                           video_id: str,
                                           crawl_interval: float = 1.0,
                                           is_fetch_sub_comments=False,
                                           callback: Optional[Callable] = None,
                                           max_count: int = 10,
                                           ) -> List:
        """
        get video all comments include sub comments
        :param video_id:
        :param crawl_interval:
        :param is_fetch_sub_comments:
        :param callback:
        :param max_count: 一次笔记爬取的最大评论数量
        :return:
        """

        result = []
        is_end = False
        next_page = 0
        while not is_end and len(result) < max_count:
            comments_res = await self.get_video_comments(video_id,"default", next_page)
            cursor_info: Dict = comments_res.get("cursor")
            comment_list: List[Dict] = comments_res.get("replies", [])
            is_end = cursor_info.get("is_end")
            next_page = cursor_info.get("next")
            if is_fetch_sub_comments:
                for comment in comment_list:
                    comment_id = comment['rpid']
                    if (comment.get("rcount", 0) > 0):
                        await self.get_video_all_sub_comments(
                            video_id, comment_id, "default", 10, crawl_interval, callback)
            if len(result) + len(comment_list) > max_count:
                comment_list = comment_list[:max_count - len(result)]
            if callback:  # 如果有回调函数，就执行回调函数
                await callback(video_id, comment_list)
            await asyncio.sleep(crawl_interval)
            if not is_fetch_sub_comments:
                result.extend(comment_list)
                continue
        return result


    async def get_upuser_videos(self, upuser_id: int, pn: int, ps: int = 30, order_mode : str = "最新发布") -> Dict:
        """get all videos for a upuser
        :param upuser_id: 创作者 ID
        :param pn: 页数
        :param ps: 一页视频数
        :param order_mode: 排序方式
        :return:
        """
        uri = "/x/space/wbi/arc/search"
        post_data = {
            "mid": upuser_id,
            "pn": pn,
            "ps": ps,
            "order": order_mode,
        }
        result = await self.get(uri, post_data)
        return result
