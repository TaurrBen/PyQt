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
#TODO 等待改成yaml文件读取
# 读取上级再上级目录的配置文件
# config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.yaml')
# with open(config_path, 'r', encoding='utf-8') as file:
#     config = yaml.safe_load(file)

import os

PROJECTS = ["pro_spider","pro_example1","pro_example2","pro_tcp_udp_web","pro3"]
LOG_FILE_NAME = "logging.ini"
LOG_NUM = 1  #0:root 1:All 2:C 3:F 4：Text

from utils.log import *
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
all_logger,all_handlers = init_loging_config(os.path.join(BASE_DIR,LOG_FILE_NAME))
logger = all_logger[LOG_NUM]
# logger = init_loging_config1("QtProjectManager","debug.log")