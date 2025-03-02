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
# File       : core.py
# Time       ：2025.2.22 11:51
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import asyncio
from asyncio import Task
from typing import Union
from datetime import datetime, timedelta
import pandas as pd
from PyQt5.QtCore import QCoreApplication

from playwright.async_api import (async_playwright, Playwright)

import config
from utils.spider import *
from utils.qEvent import *
from project_all.pro_spider.models.platforms.bilibili import store as bilibili_store
from project_all.pro_spider.models.var import crawler_type_var, source_keyword_var

from .client import BilibiliClient
from .exception import DataFetchError
from .login import BilibiliLogin

class BilibiliCrawler(AbstractCrawler):
    playwright:Playwright = None
    browser_context: BrowserContext = None
    context_page: Page = None
    bili_client: BilibiliClient = None

    def __init__(self,parent = None):
        super(BilibiliCrawler, self).__init__()
        self.parent = parent
        self.index_url = "https://www.bilibili.com"
        self.user_agent = get_user_agent()
        self.params = {}

    def load_params(self,params:Dict):
        self.params = params
        config.logger.debug(self.params)
        
    async def start(self):
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()

        playwright_proxy_format, httpx_proxy_format = None, None
        proxy_name =self.params.get("proxy")
        if not proxy_name == "none":
            ip_proxy_pool = await create_ip_pool(config.IP_PROXY_POOL_COUNT, enable_validate_ip=True,proxy_name=proxy_name)
            ip_proxy_info: IpInfoModel = await ip_proxy_pool.get_proxy()
            playwright_proxy_format, httpx_proxy_format = self.format_proxy_info(ip_proxy_info)

        self.playwright=Playwright(await async_playwright().start())
        # async with async_playwright() as playwright:
        if True:
            # Launch a browser context.
            self.browser_context = await self.launch_browser(
                self.playwright.chromium,
                None,
                self.user_agent,
                headless=self.params.get("headless")
            )
            # stealth.min.js is a js script to prevent the website from detecting the crawler.
            await self.browser_context.add_init_script(path="libs/stealth.min.js")
            self.context_page = await self.browser_context.new_page()
            await self.context_page.goto(self.index_url)

            # Create a client to interact with the bilibili website.
            self.bili_client = await self.create_client(httpx_proxy_format)
            if not await self.bili_client.pong():
                login_obj = BilibiliLogin(
                    login_type=self.params.get("login_type"),
                    login_phone="",  # your phone number
                    browser_context=self.browser_context,
                    context_page=self.context_page,
                    cookie_str=self.params.get("cookies"),
                )
                await login_obj.begin(self.params.get("login_type"))
                await self.bili_client.update_cookies(browser_context=self.browser_context)
            crawler_type_var.set(self.params.get("type"))
            config.logger.info("Bilibili Crawler Ready ...")
            event = ViewDataEvent("textBrowser_context", None, self.bili_client.headers,
                                  "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("textBrowser_cookies", None, self.bili_client.cookie_dict,
                                  "for key,value in event.data.items():qwidget.append(f'{key}:{value}')")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_start_search", None, None,
                                  "qwidget.setEnabled(True)")
            QCoreApplication.postEvent(self.parent.ui, event)
            event = ViewDataEvent("pushButton_stop_search", None, None,
                                  "qwidget.setEnabled(False)")
            QCoreApplication.postEvent(self.parent.ui, event)

    async def stop(self):
        if self.playwright:
            await self.context_page.close()
            await self.browser_context.close()
            await self.playwright.stop()
        event = ViewDataEvent("pushButton_load_params", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_start_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_stop_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)

    async def search(self):
        type = self.params.get("type")
        if type == "keywords":
            await self.by_keywords(self.params.get("keyword"))
        elif type == "bvids":
            await self.by_bvids(self.params.get("bvids"))
        elif type == "upuser":
            await self.by_upuser(self.params.get("upuser"))
        else:
            config.logger.error(f"Have not {type}.")
   
    #### keywords \ bvids \ upuser
    async def by_keywords(self,keywords):
        """
        search bilibili video with keywords
        :return:
        """
        config.logger.info("Begin search bilibli keywords")
        bili_limit_count = 20  # bilibili limit page fixed value Max36
        # if config.CRAWLER_MAX_NOTES_COUNT < bili_limit_count:
        #     config.CRAWLER_MAX_NOTES_COUNT = bili_limit_count
        start_page = self.params.get("start_page")  # start page number
        event = ViewDataEvent("pushButton_load_params", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_start_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_stop_search", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)

        for keyword in keywords:
            source_keyword_var.set(keyword)
            config.logger.info(f"Current search keyword: {keyword}")
            for day in pd.date_range(start=self.params.get("pubtime_begin_s"),
                                     end=self.params.get("pubtime_end_s"), freq='D'):
                pubtime_begin_s, pubtime_end_s = await self.get_pubtime_datetime(start=day.strftime('%Y-%m-%d'),
                                                                                 end=day.strftime('%Y-%m-%d'))
                page = 1
                while (page - start_page + 1) * bili_limit_count <= self.params.get("video_count"):
                    # ! Catch any error if response return nothing, go to next day
                    try:
                        config.logger.info(
                            f"search bilibili keyword: {keyword}, date: {day.ctime()}, page: {page}")
                        video_id_list: List[str] = []
                        videos_res = await self.bili_client.search_by_keyword(
                            search_type=self.params.get("search_type"),page=page, page_size=bili_limit_count,
                            order=self.params.get("order_type"), duration=self.params.get("duration"),
                            pubtime_begin_s=pubtime_begin_s, pubtime_end_s=pubtime_end_s,
                            keyword=keyword, tids=self.params.get("tids")
                        )
                        video_list: List[Dict] = videos_res.get("result")

                        semaphore = asyncio.Semaphore(self.params.get("concurrency_num",1))
                        task_list = [
                            self.get_video_info_task(aid=video_item.get("aid"), bvid="", semaphore=semaphore)
                            for video_item in video_list]
                        video_items = await asyncio.gather(*task_list)
                        for video_item in video_items:
                            if not video_item:
                                break
                            video_id_list.append(video_item.get("View").get("aid"))
                            save_content_item = await bilibili_store.update_bilibili_video(
                                video_item,self.params.get("video_items_is_save"))

                            event = ViewDataEvent("self", None, list(save_content_item.values()),
                                                  "self.tableWidget_video_items_addRow(event.data)")
                            QCoreApplication.postEvent(self.parent.ui, event)

                            saver_up_info = await bilibili_store.update_up_info(
                                video_item,self.params.get("video_upuser_items_is_save"))
                            event = ViewDataEvent("self", None, list(saver_up_info.values()),
                                                  "self.tableWidget_upuser_items_addRow(event.data)")
                            QCoreApplication.postEvent(self.parent.ui, event)
                            await self.get_bilibili_video(video_item, semaphore)
                        page += 1
                        await self.batch_get_video_comments(video_id_list)
                    # go to next day
                    except Exception as e:
                        config.logger.error(f"{e}")
                        break
        config.logger.info("Bilibili Crawler finished ...")
        event = ViewDataEvent("pushButton_load_params", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_start_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_stop_search", None, None,
                              "qwidget.setEnabled(False)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_video_items_export", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)
        event = ViewDataEvent("pushButton_video_upuser_items_export", None, None,
                              "qwidget.setEnabled(True)")
        QCoreApplication.postEvent(self.parent.ui, event)

    async def by_bvids(self, bvids_list: List[str]):
        """
        get specified videos info
        :return:
        """
        semaphore = asyncio.Semaphore(self.params.get("concurrency_num",1))
        task_list = [
            self.get_video_info_task(aid=0, bvid=video_id, semaphore=semaphore) for video_id in
            bvids_list
        ]
        video_details = await asyncio.gather(*task_list)
        video_aids_list = []
        for video_detail in video_details:
            if not video_detail:
                break
            video_aids_list.append(video_detail.get("View").get("aid"))
            save_content_item = await bilibili_store.update_bilibili_video(
                video_detail, self.params.get("video_items_is_save"))

            event = ViewDataEvent("self", None, list(save_content_item.values()),
                                  "self.tableWidget_video_items_addRow(event.data)")
            QCoreApplication.postEvent(self.parent.ui, event)

            saver_up_info = await bilibili_store.update_up_info(
                video_detail, self.params.get("video_upuser_items_is_save"))
            event = ViewDataEvent("self", None, list(saver_up_info.values()),
                                  "self.tableWidget_upuser_items_addRow(event.data)")
            QCoreApplication.postEvent(self.parent.ui, event)
            await self.get_bilibili_video(video_detail, semaphore)
        await self.batch_get_video_comments(video_aids_list)
        config.logger.info("Bilibili Crawler finished ...")
    
    async def by_upuser(self, upuser_id: int):
        """
        get videos for a upuser
        :return:
        """
        ps = 30
        pn = 1
        video_bvids_list = []
        while True:
            result = await self.bili_client.get_upuser_videos(upuser_id, pn, ps)
            for video in result["list"]["vlist"]:
                video_bvids_list.append(video["bvid"])
            if (int(result["page"]["count"]) <= pn * ps):
                break
            await asyncio.sleep(random.random())
            pn += 1
        await self.by_bvids(video_bvids_list)
   
    #### Video
    async def get_video_info_task(self, aid: int, bvid: str, semaphore: asyncio.Semaphore) -> Optional[Dict]:
        """
        Get video detail task
        :param aid:
        :param bvid:
        :param semaphore:
        :return:
        """
        async with semaphore:
            try:
                result = await self.bili_client.get_video_info(aid=aid, bvid=bvid)
                return result
            except DataFetchError as ex:
                config.logger.error(f"Get video detail error: {ex}")
                return None
            except KeyError as ex:
                config.logger.error(f"Have not fund note detail video_id:{bvid}, err: {ex}")
                return None

    async def get_video_play_url_task(self, aid: int, cid: int, semaphore: asyncio.Semaphore) -> Union[Dict, None]:
        """
                Get video play url
                :param aid:
                :param cid:
                :param semaphore:
                :return:
                """
        async with semaphore:
            try:
                result = await self.bili_client.get_video_play_url(aid=aid, cid=cid)
                return result
            except DataFetchError as ex:
                config.logger.error(f"Get video play url error: {ex}")
                return None
            except KeyError as ex:
                config.logger.error(f"Have not fund play url from :{aid}|{cid}, err: {ex}")
                return None
    
    async def get_bilibili_video(self, video_item: Dict, semaphore: asyncio.Semaphore):
        """
        download bilibili video
        :param video_item:
        :param semaphore:
        :return:
        """
        if not self.params.get("download_video"):
            config.logger.info(f"Crawling image mode is not enabled")
            return

        video_item_view: Dict = video_item.get("View")
        aid = video_item_view.get("aid")
        cid = video_item_view.get("cid")
        result = await self.get_video_play_url_task(aid, cid, semaphore)
        if result is None:
            config.logger.error("Get video play url failed")
            return
        durl_list = result.get("durl")
        max_size = -1
        video_url = ""
        for durl in durl_list:
            size = durl.get("size")
            if size > max_size:
                max_size = size
                video_url = durl.get("url")
        if video_url == "":
            config.logger.error("Get video url failed")
            return

        content = await self.bili_client.get_video_media(video_url)
        if content is None:
            return
        extension_file_name = f"video.mp4"
        await bilibili_store.store_video(aid, content, extension_file_name)

    #### Video comment
    async def get_video_comments_task(self, video_id: str, semaphore: asyncio.Semaphore):
        """
        get comment for video id
        :param video_id:
        :param semaphore:
        :return:
        """
        async with semaphore:
            try:
                config.logger.info(f"Begin get video_id: {video_id} comments ...")
                # await self.bili_client.get_video_all_comments(
                #     video_id=video_id,
                #     crawl_interval=random.random(),
                #     is_fetch_sub_comments=config.ENABLE_GET_SUB_COMMENTS,
                #     callback=bilibili_store.batch_update_bilibili_video_comments,
                #     max_count=config.CRAWLER_MAX_COMMENTS_COUNT_SINGLENOTES,
                # )
                await self.bili_client.get_video_all_level_comments(
                    video_id=video_id,
                    crawl_interval=random.random(),
                    is_fetch_sub_comments=self.params.get("sub_comment"),
                    callback=bilibili_store.batch_update_bilibili_video_comments,
                    max_count=self.params.get("comment_count"),
                )

            except DataFetchError as ex:
                config.logger.error(f"Get video_id: {video_id} comment error: {ex}")
            except Exception as e:
                config.logger.error(f"May be been blocked, err:{e}")

    async def batch_get_video_comments(self, video_id_list: List[str]):
        """
        batch get video comments
        :param video_id_list:
        :return:
        """
        if not self.params.get("download_comment"):
            config.logger.info(f"Crawling comment mode is not enabled")
            return

        config.logger.debug(f"Video ids:{video_id_list}")
        semaphore = asyncio.Semaphore(self.params.get("concurrency_num",1))
        task_list: List[Task] = []
        for video_id in video_id_list:
            task = asyncio.create_task(self.get_video_comments_task(video_id, semaphore), name=video_id)
            task_list.append(task)
        await asyncio.gather(*task_list)



    async def create_client(self, httpx_proxy: Optional[str]) -> BilibiliClient:
        """
        create bilibili client
        :param httpx_proxy: httpx proxy
        :return: bilibili client
        """
        config.logger.info("Begin create bilibili API client ...")
        cookie_str, cookie_dict = convert_cookies(await self.browser_context.cookies())
        bilibili_client_obj = BilibiliClient(
            proxies=httpx_proxy,
            headers={
                "User-Agent": self.user_agent,
                "Cookie": cookie_str,
                "Origin": "https://www.bilibili.com",
                "Referer": "https://www.bilibili.com",
                "Content-Type": "application/json;charset=UTF-8"
            },
            playwright_page=self.context_page,
            cookie_dict=cookie_dict,
        )
        return bilibili_client_obj

    async def launch_browser(
            self,
            chromium: BrowserType,
            playwright_proxy: Optional[Dict],
            user_agent: Optional[str],
            headless: bool = True
    ) -> BrowserContext:
        """
        launch browser and create browser context
        :param chromium: chromium browser
        :param playwright_proxy: playwright proxy
        :param user_agent: user agent
        :param headless: headless mode
        :return: browser context
        """
        config.logger.info("Begin create browser context ...")
        if self.params.get("is_save_login_state"):
            # feat issue #14
            # we will save login state to avoid login every time
            USER_DATA_DIR = "%s_user_data_dir"
            user_data_dir = os.path.join(os.getcwd(), "data/spider/browser_data",USER_DATA_DIR % "bilibili")
            browser_context = await chromium.launch_persistent_context(
                channel="chrome",
                user_data_dir=user_data_dir,
                accept_downloads=True,
                headless=headless,
                proxy=playwright_proxy,  # type: ignore
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )
            return browser_context
        else:
            # type: ignore
            browser = await chromium.launch(
                channel="chrome",
                headless=headless, proxy=playwright_proxy)
            browser_context = await browser.new_context(
                viewport={"width": 1920, "height": 1080},
                user_agent=user_agent
            )
            return browser_context

    @staticmethod
    def format_proxy_info(ip_proxy_info: IpInfoModel) -> Tuple[Optional[Dict], Optional[Dict]]:
        """
        format proxy info for playwright and httpx
        :param ip_proxy_info: ip proxy info
        :return: playwright proxy, httpx proxy
        """
        playwright_proxy = {
            "server": f"{ip_proxy_info.protocol}{ip_proxy_info.ip}:{ip_proxy_info.port}",
            "username": ip_proxy_info.user,
            "password": ip_proxy_info.password,
        }
        httpx_proxy = {
            f"{ip_proxy_info.protocol}":
                f"http://{ip_proxy_info.user}:{ip_proxy_info.password}@{ip_proxy_info.ip}:{ip_proxy_info.port}"
        }
        return playwright_proxy, httpx_proxy

    async def get_pubtime_datetime(self, start: str = "2025-02-01", end: str = "2025-02-01") -> tuple[str, str]:
        """
        获取 bilibili 作品发布日期起始时间戳 pubtime_begin_s 与发布日期结束时间戳 pubtime_end_s
        ---
        :param start: 发布日期起始时间，YYYY-MM-DD
        :param end: 发布日期结束时间，YYYY-MM-DD

        Note
        ---
        - 搜索的时间范围为 start 至 end，包含 start 和 end
        - 若要搜索同一天的内容，为了包含 start 当天的搜索内容，则 pubtime_end_s 的值应该为 pubtime_begin_s 的值加上一天再减去一秒，即 start 当天的最后一秒
            - 如仅搜索 2024-01-05 的内容，pubtime_begin_s = 1704384000，pubtime_end_s = 1704470399
              转换为可读的 datetime 对象：pubtime_begin_s = datetime.datetime(2024, 1, 5, 0, 0)，pubtime_end_s = datetime.datetime(2024, 1, 5, 23, 59, 59)
        - 若要搜索 start 至 end 的内容，为了包含 end 当天的搜索内容，则 pubtime_end_s 的值应该为 pubtime_end_s 的值加上一天再减去一秒，即 end 当天的最后一秒
            - 如搜索 2024-01-05 - 2024-01-06 的内容，pubtime_begin_s = 1704384000，pubtime_end_s = 1704556799
              转换为可读的 datetime 对象：pubtime_begin_s = datetime.datetime(2024, 1, 5, 0, 0)，pubtime_end_s = datetime.datetime(2024, 1, 6, 23, 59, 59)
        """
        # 转换 start 与 end 为 datetime 对象
        start_day: datetime = datetime.strptime(start, '%Y-%m-%d')
        end_day: datetime = datetime.strptime(end, '%Y-%m-%d')
        if start_day > end_day:
            raise ValueError(
                'Wrong time range, please check your start and end argument, to ensure that the start cannot exceed end')
        elif start_day == end_day:  # 搜索同一天的内容
            end_day = start_day + timedelta(days=1) - timedelta(
                seconds=1)  # 则将 end_day 设置为 start_day + 1 day - 1 second
        else:  # 搜索 start 至 end
            end_day = end_day + timedelta(days=1) - timedelta(seconds=1)  # 则将 end_day 设置为 end_day + 1 day - 1 second
        # 将其重新转换为时间戳
        return str(int(start_day.timestamp())), str(int(end_day.timestamp()))