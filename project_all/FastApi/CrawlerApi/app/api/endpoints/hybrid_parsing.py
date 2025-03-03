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
# File       : hybrid_parsing.py
# Time       ：2025.3.3 17:25
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import asyncio

from fastapi import APIRouter, Body, Query, Request, HTTPException  # 导入FastAPI组件

from app.api.models.APIResponseModel import ResponseModel, ErrorResponseModel  # 导入响应模型

# 爬虫/Crawler
from crawlers.hybrid.hybrid_crawler import HybridCrawler  # 导入混合爬虫

HybridCrawler = HybridCrawler()  # 实例化混合爬虫

router = APIRouter()


@router.get("/video_data", response_model=ResponseModel, tags=["Hybrid-API"],
            summary="混合解析单一视频接口/Hybrid parsing single video endpoint")
async def hybrid_parsing_single_video(request: Request,
                                      url: str = Query(example="https://v.douyin.com/L4FJNR3/"),
                                      minimal: bool = Query(default=False)):
    """
    # [中文]
    ### 用途:
    - 该接口用于解析抖音/TikTok单一视频的数据。
    ### 参数:
    - `url`: 视频链接、分享链接、分享文本。
    ### 返回:
    - `data`: 视频数据。

    # [English]
    ### Purpose:
    - This endpoint is used to parse data of a single Douyin/TikTok video.
    ### Parameters:
    - `url`: Video link, share link, or share text.
    ### Returns:
    - `data`: Video data.

    # [Example]
    url = "https://v.douyin.com/L4FJNR3/"
    """
    try:
        # 解析视频/Parse video
        data = await HybridCrawler.hybrid_parsing_single_video(url=url, minimal=minimal)
        # 返回数据/Return data
        return ResponseModel(code=200,
                             router=request.url.path,
                             data=data)
    except Exception as e:
        status_code = 400
        detail = ErrorResponseModel(code=status_code,
                                    router=request.url.path,
                                    params=dict(request.query_params),
                                    )
        raise HTTPException(status_code=status_code, detail=detail.dict())
