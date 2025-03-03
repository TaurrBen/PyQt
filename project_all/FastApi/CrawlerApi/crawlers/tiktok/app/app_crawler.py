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
# File       : app_crawlers.py
# Time       ：2025.3.3 17:30
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""

import asyncio  # 异步I/O
import time  # 时间操作
import yaml  # 配置文件
import os  # 系统操作

# 基础爬虫客户端和TikTokAPI端点
from crawlers.base_crawler import BaseCrawler
from crawlers.tiktok.app.endpoints import TikTokAPIEndpoints
from crawlers.utils.utils import model_to_query_string

# 重试机制
from tenacity import *

# TikTok接口数据请求模型
from crawlers.tiktok.app.models import (
    BaseRequestModel, FeedVideoDetail
)

# 标记已废弃的方法
from crawlers.utils.deprecated import deprecated

# 配置文件路径
path = os.path.abspath(os.path.dirname(__file__))

# 读取配置文件
with open(f"{path}/config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)


class TikTokAPPCrawler:

    # 从配置文件中获取TikTok的请求头
    async def get_tiktok_headers(self):
        tiktok_config = config["TokenManager"]["tiktok"]
        kwargs = {
            "headers": {
                "User-Agent": tiktok_config["headers"]["User-Agent"],
                "Referer": tiktok_config["headers"]["Referer"],
                "Cookie": tiktok_config["headers"]["Cookie"],
                "x-ladon": "Hello From Evil0ctal!",
            },
            "proxies": {"http://": tiktok_config["proxies"]["http"],
                        "https://": tiktok_config["proxies"]["https"]}
        }
        return kwargs

    """-------------------------------------------------------handler接口列表-------------------------------------------------------"""

    # 获取单个作品数据
    # @deprecated("TikTok APP fetch_one_video is deprecated and will be removed in a future release. Use Web API instead. | TikTok APP fetch_one_video 已弃用，将在将来的版本中删除。请改用Web API。")
    @retry(stop=stop_after_attempt(10), wait=wait_fixed(1))
    async def fetch_one_video(self, aweme_id: str):
        # 获取TikTok的实时Cookie
        kwargs = await self.get_tiktok_headers()
        params = FeedVideoDetail(aweme_id=aweme_id)
        param_str = model_to_query_string(params)
        url = f"{TikTokAPIEndpoints.HOME_FEED}?{param_str}"
        # 创建一个基础爬虫
        base_crawler = BaseCrawler(proxies=kwargs["proxies"], crawler_headers=kwargs["headers"])
        async with base_crawler as crawler:
            response = await crawler.fetch_get_json(url)
            response = response.get("aweme_list")[0]
            if response.get("aweme_id") != aweme_id:
                raise Exception("作品ID错误/Video ID error")
        return response

    """-------------------------------------------------------main------------------------------------------------------"""

    async def main(self):
        # 获取单个作品数据/Fetch single post data
        aweme_id = "7339393672959757570"
        response = await self.fetch_one_video(aweme_id)
        print(response)

        # 占位
        pass


if __name__ == "__main__":
    # 初始化
    TikTokAPPCrawler = TikTokAPPCrawler()

    # 开始时间
    start = time.time()

    asyncio.run(TikTokAPPCrawler.main())

    # 结束时间
    end = time.time()
    print(f"耗时：{end - start}")
