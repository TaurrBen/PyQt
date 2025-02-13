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
# File       : metadata.py
# Time       ：2025.2.13 7:04
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""

from typing import Optional

from pydantic import BaseModel, Field
class TiebaComment(BaseModel):
    """
        百度贴吧评论
        """
    comment_id: str = Field(..., description="评论ID")
    parent_comment_id: str = Field(default="", description="父评论ID")
    content: str = Field(..., description="评论内容")
    user_link: str = Field(default="", description="用户主页链接")
    user_nickname: str = Field(default="", description="用户昵称")
    user_avatar: str = Field(default="", description="用户头像地址")
    publish_time: str = Field(default="", description="发布时间")
    ip_location: Optional[str] = Field(default="", description="IP地理位置")
    sub_comment_count: int = Field(default=0, description="子评论数")
    note_id: str = Field(..., description="帖子ID")
    note_url: str = Field(..., description="帖子链接")
    tieba_id: str = Field(..., description="所属的贴吧ID")
    tieba_name: str = Field(..., description="所属的贴吧名称")
    tieba_link: str = Field(..., description="贴吧链接")
