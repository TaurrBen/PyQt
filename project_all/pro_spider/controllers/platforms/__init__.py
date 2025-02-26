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
# File       : __init__.py
# Time       ：2025.2.22 10:17
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
from utils.spider import AbstractCrawler
from .bilibili import BilibiliCrawler
from .douyin import DouYinCrawler
from .kuaishou import KuaishouCrawler
from .tieba import TieBaCrawler
from .weibo import WeiboCrawler
from .xiaohongshu import XiaoHongShuCrawler
from .zhihu import ZhihuCrawler

class CrawlerFactory:
    CRAWLERS = {
        "bilibili": BilibiliCrawler,
        "douyin":DouYinCrawler,
        "kuaishou":KuaishouCrawler,
        "tieba":TieBaCrawler,
        "weibo":WeiboCrawler,
        "xiaohongshu":XiaoHongShuCrawler,
        "zhihu":ZhihuCrawler
    }

    @staticmethod
    def create_crawler(parent,platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)
        if not crawler_class:
            raise ValueError("Invalid Media Platform Currently only supported xiaohongshu or dy or ks or bili ...")
        return crawler_class(parent)