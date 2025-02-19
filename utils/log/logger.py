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
# File       : logger.py
# Time       ：2025.2.17 6:58
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import logging
import logging.config
import logging.handlers

def init_loging_config(filename):
    logging.config.fileConfig(filename)
    rootHandle = logging.getLogger("root")
    CAndFHandle = logging.getLogger("CAndFLogger")
    consoleHandle = logging.getLogger("consoleLogger")
    fileHandle = logging.getLogger("fileLogger")
    _logger = rootHandle,CAndFHandle,consoleHandle,fileHandle
    return _logger

def init_loging_config1(logger_name,file_name,level=logging.DEBUG):
    formatter = logging.Formatter(fmt="%(asctime)s - %(name)s - (%(process)d:%(threadName)s:%(thread)d) "
                                      "- (%(pathname)s:%(funcName)s:%(lineno)d) - %(levelname)s - %(message)s",
                                  datefmt='%Y-%m-%d %H:%M:%S')
    _logger = logging.getLogger(logger_name)
    _logger.setLevel(level)
    filehandle = logging.FileHandler(file_name)
    filehandle.setFormatter(formatter)
    _logger.addHandler(filehandle)
    return _logger

if __name__ == "__main__":
    logger = init_loging_config1("c", "bb.log")

    logger.debug('debug级别，一般用来打印一些调试信息，级别最低')
    logger.info('info级别，一般用来打印一些正常的操作信息')
    logger.warning('waring级别，一般用来打印警告信息')
    logger.error('error级别，一般用来打印一些错误信息')
    logger.critical('critical级别，一般用来打印一些致命的错误信息，等级最高')