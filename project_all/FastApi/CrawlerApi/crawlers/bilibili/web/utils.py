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
# File       : utils.py
# Time       ：2025.3.3 16:41
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
from urllib.parse import urlencode
from crawlers.bilibili.web import wrid
from crawlers.utils.logger import logger
from crawlers.bilibili.web.endpoints import BilibiliAPIEndpoints

class EndpointGenerator:
    def __init__(self, params: dict):
        self.params = params

    # 获取用户发布视频作品数据 生成enpoint
    async def user_post_videos_endpoint(self) -> str:
        # 添加w_rid
        endpoint = await WridManager.wrid_model_endpoint(params=self.params)
        # 拼接成最终结果并返回
        final_endpoint = BilibiliAPIEndpoints.USER_POST + '?' + endpoint
        return final_endpoint

    # 获取视频流地址 生成enpoint
    async def video_playurl_endpoint(self) -> str:
        # 添加w_rid
        endpoint = await WridManager.wrid_model_endpoint(params=self.params)
        # 拼接成最终结果并返回
        final_endpoint = BilibiliAPIEndpoints.VIDEO_PLAYURL + '?' + endpoint
        return final_endpoint

    # 获取指定用户的信息 生成enpoint
    async def user_profile_endpoint(self) -> str:
        # 添加w_rid
        endpoint = await WridManager.wrid_model_endpoint(params=self.params)
        # 拼接成最终结果并返回
        final_endpoint = BilibiliAPIEndpoints.USER_DETAIL + '?' + endpoint
        return final_endpoint

    # 获取综合热门视频信息 生成enpoint
    async def com_popular_endpoint(self) -> str:
        # 添加w_rid
        endpoint = await WridManager.wrid_model_endpoint(params=self.params)
        # 拼接成最终结果并返回
        final_endpoint = BilibiliAPIEndpoints.COM_POPULAR + '?' + endpoint
        return final_endpoint

    # 获取指定用户动态
    async def user_dynamic_endpoint(self):
        # 添加w_rid
        endpoint = await WridManager.wrid_model_endpoint(params=self.params)
        # 拼接成最终结果并返回
        final_endpoint = BilibiliAPIEndpoints.USER_DYNAMIC + '?' + endpoint
        return final_endpoint


class WridManager:
    @classmethod
    async def get_encode_query(cls, params: dict) -> str:
        params['wts'] = params['wts'] + "ea1db124af3c7062474693fa704f4ff8"
        params = dict(sorted(params.items()))  # 按照 key 重排参数
        # 过滤 value 中的 "!'()*" 字符
        params = {
            k: ''.join(filter(lambda chr: chr not in "!'()*", str(v)))
            for k, v
            in params.items()
        }
        query = urlencode(params)  # 序列化参数
        return query

    @classmethod
    async def wrid_model_endpoint(cls, params: dict) -> str:
        wts = params["wts"]
        encode_query = await cls.get_encode_query(params)
        # 获取w_rid参数
        w_rid = wrid.get_wrid(e=encode_query)
        params["wts"] = wts
        params["w_rid"] = w_rid
        return "&".join(f"{k}={v}" for k, v in params.items())

# BV号转为对应av号
async def bv2av(bv_id: str) -> int:
    table = "fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF"
    s = [11, 10, 3, 8, 4, 6, 2, 9, 5, 7]
    xor = 177451812
    add_105 = 8728348608
    add_all = 8728348608 - (2 ** 31 - 1) - 1
    tr = [0] * 128
    for i in range(58):
        tr[ord(table[i])] = i
    r = 0
    for i in range(6):
        r += tr[ord(bv_id[s[i]])] * (58 ** i)
    add = add_105
    if r < add:
        add = add_all
    aid = (r - add) ^ xor
    return aid

# 响应分析
class ResponseAnalyzer:
    # 用户收藏夹信息
    @classmethod
    async def collect_folders_analyze(cls, response: dict) -> dict:
        if response['data']:
            return response
        else:
            logger.warning("该用户收藏夹为空/用户设置为不可见")
            return {"code": 1, "message": "该用户收藏夹为空/用户设置为不可见"}

if __name__=='__main__':
    print('ok')