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
import time
from typing import List

from pydantic import BaseModel


# API基础请求模型/Base Request Model
class BaseRequestModel(BaseModel):
    """
    Base Request Model for TikTok API
    """
    iid: int = 7318518857994389254
    device_id: int = 7318517321748022790
    channel: str = "googleplay"
    app_name: str = "musical_ly"
    version_code: str = "300904"
    device_platform: str = "android"
    device_type: str = "SM-ASUS_Z01QD"
    os_version: str = "9"


# Feed视频详情请求模型/Feed Video Detail Request Model
class FeedVideoDetail(BaseRequestModel):
    """
    Feed Video Detail Request Model
    """
    aweme_id: str
