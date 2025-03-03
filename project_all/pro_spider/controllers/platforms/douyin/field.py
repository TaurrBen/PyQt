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
# File       : field.py
# Time       ：2025.2.26 22:59
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""

SORT_TYPE_LIST = {
    "default":"0","综合排序":"0",
    "最新发布":"2","最多点赞":"1",
}
SORT_TYPE_LIST_DEFAULT = SORT_TYPE_LIST.get("default")
PUBLISH_TIME_LIST = {
    "default":"0","不限":"0",
    "一天内":"1","一周内":"7", "半年内":"180",
}
PUBLISH_TIME_LIST_DEFAULT = SORT_TYPE_LIST.get("default")
FILTER_DURATION_LIST = {
    "default":"","不限":"",
    "1分钟以下":"0-1","1-5分钟":"1-5", "5分钟以上":"5-10000",
}
FILTER_DURATION_LIST_DEFAULT = SORT_TYPE_LIST.get("default")
SEARCH_RANGE_LIST = {
    "default":"0","不限":"0",
    "关注的人":"3","最近看过":"1", "还未看过":"2",
}
SEARCH_RANGE_LIST_DEFAULT = SORT_TYPE_LIST.get("default")
CONTENT_TYPE_LIST = {
    "default":"0","不限":"0",
    "视频":"1","图文":"2",
}
CONTENT_TYPE_LIST_DEFAULT = SORT_TYPE_LIST.get("default")