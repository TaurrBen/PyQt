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
# File       : base_config.py
# Time       ：2025.2.13 0:59
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import os

PROJECTS = ["pro_example","pro_example2","pro1","pro3"]
LOG_FILE_NAME = "logging.conf"
LOG_NUM = 1  #0:root 1:CandF 2:C 3:F

from utils.log import logger
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logger = logger.init_loging_config(os.path.join(BASE_DIR,LOG_FILE_NAME))[LOG_NUM]
# logger = logger.init_loging_config1("QtProjectManager","debug.log")