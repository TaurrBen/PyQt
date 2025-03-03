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
# File       : core.py
# Time       ：2025.2.14 23:21
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import asyncio
import threading
import time

from PyQt5 import QtCore
from PyQt5.QtCore import QThread

import config
from utils.spider import AbstractCrawler
from utils.thread.MyQThreading import RunThread, async_RunThread, AsyncioThread
from .platforms import CrawlerFactory

class Controller(QtCore.QObject):

    #### 1.定义暴露属性 ####
    # test = QtCore.pyqtProperty(int, fget=lambda self: self.ui.comboBox_test.currentIndex(),
    #                     fset=lambda self, v: self.ui.comboBox_test.setCurrentIndex(v))
    # test_enabled = QtCore.pyqtProperty(bool, fget=lambda self: self.ui.comboBox_test.isEnabled(),
    #                             fset=lambda self, v: self.ui.comboBox_test.setEnabled(v))
    #### properties for widget value ####
    crawler: AbstractCrawler = None
    @property
    def test(self):
        return object

    @test.setter
    def test(self, value):
        return object

    #### 2.定义signal等变量 ####
    signal_write_msg = QtCore.pyqtSignal(str)

    #### 3.初始化 ####
    def __init__(self, model):
        super(Controller, self).__init__()
        self.model = model
        self.loop = asyncio.new_event_loop()
        self.crawler_thread = AsyncioThread(self.loop)
        self.crawler_thread.start()
        self.setup_bindings()

    def setup_bindings(self):
        #### ctrl slots <----- model signal ####
        self.model.signal_write_msg.connect(lambda str:self.get_msg(str))

    #### 4.槽函数 ####
    #### signal event functions ####
    #### ui signal -----> ctrl slots ####
    def set_msg(self,msg):
        #### 修改model中的字段 ####
        self.model.set_msg(msg)

    #### ctrl slots <----- model signal ####
    def get_msg(self,msg):
        #### 从model中获得字段 ####
        #### 发送信号至view中 ####
        self.signal_write_msg.emit(msg)

