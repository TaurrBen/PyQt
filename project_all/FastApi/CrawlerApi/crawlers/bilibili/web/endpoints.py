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
# File       : endpoints.py
# Time       ：2025.3.3 16:39
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
class BilibiliAPIEndpoints:

    "-------------------------------------------------------域名-domain-------------------------------------------------------"
    # 哔哩哔哩接口域名
    BILIAPI_DOMAIN = "https://api.bilibili.com"

    # 哔哩哔哩直播域名
    LIVE_DOMAIN = "https://api.live.bilibili.com"

    "-------------------------------------------------------接口-api-------------------------------------------------------"
    # 作品信息 (Post Detail)
    POST_DETAIL = f"{BILIAPI_DOMAIN}/x/web-interface/view"

    # 作品视频流
    VIDEO_PLAYURL = f"{BILIAPI_DOMAIN}/x/player/wbi/playurl"

    # 用户发布视频作品数据
    USER_POST = f"{BILIAPI_DOMAIN}/x/space/wbi/arc/search"

    # 收藏夹列表
    COLLECT_FOLDERS = f"{BILIAPI_DOMAIN}/x/v3/fav/folder/created/list-all"

    # 收藏夹视频
    COLLECT_VIDEOS = f"{BILIAPI_DOMAIN}/x/v3/fav/resource/list"

    # 用户个人信息
    USER_DETAIL = f"{BILIAPI_DOMAIN}/x/space/wbi/acc/info"

    # 综合热门
    COM_POPULAR = f"{BILIAPI_DOMAIN}/x/web-interface/popular"

    # 每周必看
    WEEKLY_POPULAR = f"{BILIAPI_DOMAIN}/x/web-interface/popular/series/one"

    # 入站必刷
    PRECIOUS_POPULAR = f"{BILIAPI_DOMAIN}/x/web-interface/popular/precious"

    # 视频评论
    VIDEO_COMMENTS = f"{BILIAPI_DOMAIN}/x/v2/reply"

    # 用户动态
    USER_DYNAMIC = f"{BILIAPI_DOMAIN}/x/polymer/web-dynamic/v1/feed/space"

    # 评论的回复
    COMMENT_REPLY = f"{BILIAPI_DOMAIN}/x/v2/reply/reply"

    # 视频分p信息
    VIDEO_PARTS = f"{BILIAPI_DOMAIN}/x/player/pagelist"

    # 直播间信息
    LIVEROOM_DETAIL = f"{LIVE_DOMAIN}/room/v1/Room/get_info"

    # 直播分区列表
    LIVE_AREAS = f"{LIVE_DOMAIN}/room/v1/Area/getList"

    # 直播间视频流
    LIVE_VIDEOS = f"{LIVE_DOMAIN}/room/v1/Room/playUrl"

    # 正在直播的主播
    LIVE_STREAMER = f"{LIVE_DOMAIN}/xlive/web-interface/v1/second/getList"