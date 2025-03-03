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
# File       : models.py
# Time       ：2025.3.3 17:30
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
from typing import Any
from pydantic import BaseModel
from urllib.parse import quote, unquote

from crawlers.tiktok.web.utils import TokenManager
from crawlers.utils.utils import get_timestamp


# Model
class BaseRequestModel(BaseModel):
    WebIdLastTime: str = str(get_timestamp("sec"))
    aid: str = "1988"
    app_language: str = "en"
    app_name: str = "tiktok_web"
    browser_language: str = "en-US"
    browser_name: str = "Mozilla"
    browser_online: str = "true"
    browser_platform: str = "Win32"
    browser_version: str = quote(
        "5.0 (Windows)",
        safe="",
    )
    channel: str = "tiktok_web"
    cookie_enabled: str = "true"
    device_id: int = 7380187414842836523
    device_platform: str = "web_pc"
    focus_state: str = "true"
    from_page: str = "user"
    history_len: int = 4
    is_fullscreen: str = "false"
    is_page_visible: str = "true"
    language: str = "en"
    os: str = "windows"
    priority_region: str = "US"
    referer: str = ""
    region: str = "US"  # SG JP KR...
    root_referer: str = quote("https://www.tiktok.com/", safe="")
    screen_height: int = 1080
    screen_width: int = 1920
    webcast_language: str = "en"
    tz_name: str = quote("America/Tijuana", safe="")
    # verifyFp: str = VerifyFpManager.gen_verify_fp()
    msToken: str = TokenManager.gen_real_msToken()


# router model
class UserProfile(BaseRequestModel):
    secUid: str = ""
    uniqueId: str


class UserPost(BaseRequestModel):
    coverFormat: int = 2
    count: int = 35
    cursor: int = 0
    secUid: str


class UserLike(BaseRequestModel):
    coverFormat: int = 2
    count: int = 30
    cursor: int = 0
    secUid: str


class UserCollect(BaseRequestModel):
    cookie: str = ""
    coverFormat: int = 2
    count: int = 30
    cursor: int = 0
    secUid: str


class UserPlayList(BaseRequestModel):
    count: int = 30
    cursor: int = 0
    secUid: str


class UserMix(BaseRequestModel):
    count: int = 30
    cursor: int = 0
    mixId: str


class PostDetail(BaseRequestModel):
    itemId: str


class PostComment(BaseRequestModel):
    aweme_id: str
    count: int = 20
    cursor: int = 0
    current_region: str = "US"


# 作品评论回复 (Post Comment Reply)
class PostCommentReply(BaseRequestModel):
    item_id: str
    comment_id: str
    count: int = 20
    cursor: int = 0
    current_region: str = "US"


# 用户粉丝 (User Fans)
class UserFans(BaseRequestModel):
    secUid: str
    count: int = 30
    maxCursor: int = 0
    minCursor: int = 0
    scene: int = 67


# 用户关注 (User Follow)
class UserFollow(BaseRequestModel):
    secUid: str
    count: int = 30
    maxCursor: int = 0
    minCursor: int = 0
    scene: int = 21
