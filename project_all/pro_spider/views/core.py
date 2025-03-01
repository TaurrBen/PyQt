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
# Time       ：2025.2.14 23:22
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import asyncio
import threading
import time

from PyQt5 import QtCore
from PyQt5.QtCore import Qt,QThread
from PyQt5.QtWidgets import QTreeWidgetItem
from pyqt5_plugins.examplebutton import QtWidgets

from utils.thread.MyQThreading import AsyncioThread
from .core_bilibili import View_bilibili
from .core_douyin import View_douyin
from .core_kuaishou import View_kuaishou
from .core_tieba import View_tieba
from .core_weibo import View_weibo
from .core_xiaohongshu import View_xiaohongshu
from .core_zhihu import View_zhihu
from .ui.ui_spider import Ui_spider

import config
from utils.log import *
from ..controllers.platforms import CrawlerFactory

class SpiderViewFactory:
    SpiderUi = {
        "class1":{
            "bilibili": View_bilibili,
            "douyin": View_douyin,
            "kuaishou": View_kuaishou,
        },
        "class2":{
            "tieba": View_tieba,
            "weibo": View_weibo,
        },
        "class3":{
            "xiaohongshu": View_xiaohongshu,
            "zhihu": View_zhihu
        }
    }
    @staticmethod
    def create_spider_view(parent,platform_list:list):
        platform_class = platform_list[0]
        platform_name = platform_list[1]
        spider_view_class = SpiderViewFactory.SpiderUi.get(platform_class).get(platform_name)
        return spider_view_class(parent)

class View():
    def __init__(self, model, ctrl):
        self.ctrl = ctrl
        super(View, self).__init__()
        self.build_ui(self)
        self.ui.show()

    def build_ui(self,parent):
        self.ui = Ui_spider(parent)
        self.instance_view = None
        self.setup_bindings()
        self.initial_datas_load()

    #### connect widget signals to event functions ####
    def setup_bindings(self):
        #### ui signal -----> ui slots ####
        # self.ui.comboBox.currentIndexChanged.connect(self.combobox_change)
        self.ui.pushButton.clicked.connect(self.btn_clicked)
        #### 可形成闭环 ####
        #### ui signal -----? ctrl slots ####
        # self.ui.comboBox.currentIndexChanged.connect(lambda : self.ctrl.set_msg(self.ui.comboBox.currentText()))
        #### ui slots <----- ctrl signal ####
        # self.ctrl.signal_write_msg.connect(lambda str:self.update_msg(str))

    def initial_datas_load(self):
        self.combobox_change()
        self.treeWidget_load()

    #### 3.槽函数 ####
    #### signal event functions ####
    #### ui signal -----> ui slots ####
    # 也可以以这种方式做，但是名字要对应
    # @pyqtSlot()
    # def on_pushButton_clicked(self):
    #     if self.status:
    #         self.close_proxy(True)
    #     else:
    #         self.set_proxy()
    def combobox_change(self):
        _translate = QtCore.QCoreApplication.translate

    def treeWidget_load(self):
        data = SpiderViewFactory.SpiderUi
        for key, value in data.items():
            item = QTreeWidgetItem(self.ui.treeWidget, [key])  # 创建项
            for key1, value1 in value.items():
                QTreeWidgetItem(item, [key1])  # 创建项

    def btn_clicked(self):
        item = self.ui.treeWidget.currentItem()
        if item.childCount():
            return
        platform_list = []
        platform_list.append(item.parent().text(0))
        platform_list.append(item.text(0))
        self.instance_view = SpiderViewFactory.create_spider_view(self, platform_list)
        # 看是否隐藏总界面
        self.ui.hide()
        self.instance_view.ui.show()

    #### ui slots <----- ctrl signal ####
    def update_msg(self,msg):
        print(msg)
