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
# Time       ：2025.3.3 17:30
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
class TikTokAPIEndpoints:
    """
    API Endpoints for TikTok
    """

    # 抖音域名 (Tiktok Domain)
    TIKTOK_DOMAIN = "https://www.tiktok.com"

    # 直播域名 (Webcast Domain)
    WEBCAST_DOMAIN = "https://webcast.tiktok.com"

    # 登录 (Login)
    LOGIN_ENDPOINT = f"{TIKTOK_DOMAIN}/login/"

    # 首页推荐 (Home Recommend)
    HOME_RECOMMEND = f"{TIKTOK_DOMAIN}/api/recommend/item_list/"

    # 用户详细信息 (User Detail Info)
    USER_DETAIL = f"{TIKTOK_DOMAIN}/api/user/detail/"

    # 用户作品 (User Post)
    USER_POST = f"{TIKTOK_DOMAIN}/api/post/item_list/"

    # 用户点赞 (User Like)
    USER_LIKE = f"{TIKTOK_DOMAIN}/api/favorite/item_list/"

    # 用户收藏 (User Collect)
    USER_COLLECT = f"{TIKTOK_DOMAIN}/api/user/collect/item_list/"

    # 用户播放列表 (User Play List)
    USER_PLAY_LIST = f"{TIKTOK_DOMAIN}/api/user/playlist/"

    # 用户合辑 (User Mix)
    USER_MIX = f"{TIKTOK_DOMAIN}/api/mix/item_list/"

    # 猜你喜欢 (Guess You Like)
    GUESS_YOU_LIKE = f"{TIKTOK_DOMAIN}/api/related/item_list/"

    # 用户关注 (User Follow)
    USER_FOLLOW = f"{TIKTOK_DOMAIN}/api/user/list/"

    # 用户粉丝 (User Fans)
    USER_FANS = f"{TIKTOK_DOMAIN}/api/user/list/"

    # 作品信息 (Post Detail)
    POST_DETAIL = f"{TIKTOK_DOMAIN}/api/item/detail/"

    # 作品评论 (Post Comment)
    POST_COMMENT = f"{TIKTOK_DOMAIN}/api/comment/list/"

    # 作品评论回复 (Post Comment Reply)
    POST_COMMENT_REPLY = f"{TIKTOK_DOMAIN}/api/comment/list/reply/"
