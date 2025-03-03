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
# File       : ios_shortcut.py
# Time       ：2025.3.3 17:25
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import os
import yaml
from fastapi import APIRouter
from app.api.models.APIResponseModel import iOS_Shortcut


# 读取上级再上级目录的配置文件
config_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as file:
    config = yaml.safe_load(file)

router = APIRouter()


@router.get("/shortcut", response_model=iOS_Shortcut, summary="用于iOS快捷指令的版本更新信息/Version update information for iOS shortcuts")
async def get_shortcut():
    shortcut_config = config["iOS_Shortcut"]
    version = shortcut_config["iOS_Shortcut_Version"]
    update = shortcut_config['iOS_Shortcut_Update_Time']
    link = shortcut_config['iOS_Shortcut_Link']
    link_en = shortcut_config['iOS_Shortcut_Link_EN']
    note = shortcut_config['iOS_Shortcut_Update_Note']
    note_en = shortcut_config['iOS_Shortcut_Update_Note_EN']
    return iOS_Shortcut(version=str(version), update=update, link=link, link_en=link_en, note=note, note_en=note_en)