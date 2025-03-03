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
# File       : tiktok_app.py
# Time       ：2025.3.3 17:25
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
from fastapi import APIRouter, Query, Request, HTTPException  # 导入FastAPI组件
from app.api.models.APIResponseModel import ResponseModel, ErrorResponseModel  # 导入响应模型

from crawlers.tiktok.app.app_crawler import TikTokAPPCrawler  # 导入APP爬虫

router = APIRouter()
TikTokAPPCrawler = TikTokAPPCrawler()


# 获取单个作品数据
@router.get("/fetch_one_video",
            response_model=ResponseModel,
            summary="获取单个作品数据/Get single video data"
            )
async def fetch_one_video(request: Request,
                          aweme_id: str = Query(example="7350810998023949599", description="作品id/Video id")):
    """
    # [中文]
    ### 用途:
    - 获取单个作品数据
    ### 参数:
    - aweme_id: 作品id
    ### 返回:
    - 作品数据

    # [English]
    ### Purpose:
    - Get single video data
    ### Parameters:
    - aweme_id: Video id
    ### Return:
    - Video data

    # [示例/Example]
    aweme_id = "7350810998023949599"
    """
    try:
        data = await TikTokAPPCrawler.fetch_one_video(aweme_id)
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
