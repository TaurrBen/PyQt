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
# File       : APIResponseModel.py
# Time       ：2025.3.3 17:26
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
from fastapi import Body, FastAPI, Query, Request, HTTPException
from pydantic import BaseModel
from typing import Any, Callable, Type, Optional, Dict
from functools import wraps
import datetime

app = FastAPI()


# 定义响应模型
class ResponseModel(BaseModel):
    code: int = 200
    router: str = "Endpoint path"
    data: Optional[Any] = {}


# 定义错误响应模型
class ErrorResponseModel(BaseModel):
    code: int = 400
    message: str = "An error occurred."
    support: str = "Please contact us on Github: https://github.com/Evil0ctal/Douyin_TikTok_Download_API"
    time: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    router: str
    params: dict = {}


# 混合解析响应模型
class HybridResponseModel(BaseModel):
    code: int = 200
    router: str = "Hybrid parsing single video endpoint"
    data: Optional[Any] = {}


# iOS_Shortcut响应模型
class iOS_Shortcut(BaseModel):
    version: str
    update: str
    link: str
    link_en: str
    note: str
    note_en: str
