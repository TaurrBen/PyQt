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
# Time       ：2025.2.22 11:35
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
SEARCH_TYPE_LIST = {
    "default":"video",
    "video":"video",
    "media_bangumi":"media_bangumi",
    "media_ft":"media_ft",
    "live":"live",
    "article":"article",
    "bili_user":"bili_user",
}
ORDER_TYPE_LIST = {
    "default":"","综合排序":"",
    "最多播放":"click","最新发布":"pubdate","最多弹幕":"dm","最多收藏":"stow"
}
DURATION_LIST = {
    "default":0,"全部时长":0,
    "10分钟一下":1,"10-30分钟":2,"30-60分钟一下":3,"60分钟以上":4,
}
TIDS_LIST = {
    "default":0,"综合分区":0,
    "动画":1,"番剧":13,"国创":167,"音乐":3,"舞蹈":129,"游戏":4,"知识":36,
    "科技":188,"运动":234,"汽车":223,"生活":160,"美食":211,"动物圈":217,
    "鬼畜":119,"时尚":155,"资讯":202,"娱乐":5,"影视":181,"纪录片":177,
    "电影":23,"电视剧":11,
}

COMMENT_TYPE_LIST = {
    "default":0,
    "mixed":1,"latest":2,"hottest":3,
}