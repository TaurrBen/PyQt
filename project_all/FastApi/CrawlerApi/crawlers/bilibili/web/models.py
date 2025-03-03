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
# Time       ：2025.3.3 16:40
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import time
from pydantic import BaseModel


class BaseRequestsModel(BaseModel):
    wts: str = str(round(time.time()))


class UserPostVideos(BaseRequestsModel):
    dm_img_inter: str = '{"ds":[],"wh":[3557,5674,5],"of":[154,308,154]}'
    dm_img_list: list = []
    mid: str
    pn: int
    ps: str = "20"


class UserProfile(BaseRequestsModel):
    mid: str


class UserDynamic(BaseRequestsModel):
    host_mid: str
    offset: str
    wts: str = str(round(time.time()))


class ComPopular(BaseRequestsModel):
    pn: int
    ps: str = "20"
    web_location: str = "333.934"


class PlayUrl(BaseRequestsModel):
    qn: str
    fnval: str = '4048'
    bvid: str
    cid: str
