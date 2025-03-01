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
# File       : core_weibo.py
# Time       ：2025.2.26 23:24
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

from utils.thread.MyQThreading import AsyncioThread
from .ui.platforms.weibo.ui_weibo import Ui_weibo
import config
from utils.log import *
from ..controllers.platforms import CrawlerFactory, WeiboCrawler


class View_weibo():

    #### 1.定义暴露属性 ####
    # test = QtCore.pyqtProperty(int, fget=lambda self: self.ui.comboBox_test.currentIndex(),
    #                     fset=lambda self, v: self.ui.comboBox_test.setCurrentIndex(v))
    # test_enabled = QtCore.pyqtProperty(bool, fget=lambda self: self.ui.comboBox_test.isEnabled(),
    #                             fset=lambda self, v: self.ui.comboBox_test.setEnabled(v))
    #### properties for widget value ####
    @property
    def test(self):
        return object

    @test.setter
    def test(self, value):
        return object

    #### 2.初始化 ####
    def __init__(self, parent):
        self.parent = parent
        self.ctrl = self.parent.ctrl
        self.textBrowser_msg_handler = QTextBrowserHandler()
        super(View_weibo, self).__init__()
        self.build_ui(self.parent)
        self.ui.show()

    def build_ui(self,parent):
        self.ui = Ui_weibo(parent)
        self.setup_bindings()
        self.initial_datas_load()

    #### connect widget signals to event functions ####
    def setup_bindings(self):
        #### ui signal -----> ui slots ####
        # self.ui.comboBox.currentIndexChanged.connect(self.combobox_change)
        self.ui.pushButton_start_search.clicked.connect(self.btn_start_search_clicked)
        self.ui.pushButton_stop_search.clicked.connect(self.btn_stop_search_clicked)
        self.ui.pushButton_load_params.clicked.connect(self.btn_load_params_clicked)

        for handler in config.all_handlers:
            if isinstance(handler, QTextBrowserHandler):
                # 绑定信号到UI更新
                handler.append_log.connect(self.append_log)

        #### 可形成闭环 ####
        #### ui signal -----? ctrl slots ####
        # self.ui.comboBox.currentIndexChanged.connect(lambda : self.ctrl.set_msg(self.ui.comboBox.currentText()))
        #### ui slots <----- ctrl signal ####
        # self.ctrl.signal_write_msg.connect(lambda str:self.update_msg(str))

    def initial_datas_load(self):
        self.combobox_change()

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

    def append_log(self,msg, level):
        if self.ui.checkBox_debug.isChecked():
            color_map = {
                'debug': Qt.gray,
                'info': Qt.black,
                'warning': Qt.yellow,
                'error': Qt.red,
                'critical': Qt.darkCyan
            }
            self.ui.textBrowser_debug.setTextColor(color_map[level])
            self.ui.textBrowser_debug.append(msg)

    def btn_start_search_clicked(self):
        config.logger.info("触发1")
        asyncio.run_coroutine_threadsafe(self.ctrl.crawler.search_by_keyword(), self.ctrl.loop)
        # 向asyncio中增加一个普通函数任务
        # self.ctrl.loop.call_soon_threadsafe(self.printInfo, 'andyshengjl')
        config.logger.info("触发11")

    def btn_stop_search_clicked(self):
        # self.ctrl.thd.stop()
        config.logger.info("触发2")
        asyncio.run_coroutine_threadsafe(self.ctrl.crawler.stop(), self.ctrl.loop)
        config.logger.info("触发22")

    def btn_load_params_clicked(self):
        try:
            self.params = {
                "is_playwright":self.ui.checkBox_is_playwright.isChecked(),
                "headless":self.ui.checkBox_headless.isChecked(),
                "proxy":self.ui.comboBox_proxy_type.currentText(),
                "concurrency_num":int(self.ui.lineEdit_concurrency_num.text()),
                "type":self.ui.comboBox_type.currentText(),

                "keyword":self.ui.lineEdit_keyword.text().split(","),
                "search_type":self.ui.comboBox_search_type.currentText(),
                "order_type":self.ui.comboBox_order_type.currentText(),
                "pubtime_begin_s":self.ui.dateEdit_pubtime_begin_s.date().toString("yyyy-MM-dd"),
                "pubtime_end_s":self.ui.dateEdit_pubtime_end_s.date().toString("yyyy-MM-dd"),
                "duration":self.ui.comboBox_duration.currentIndex(),
                "tids":self.ui.comboBox_tids.currentText(),

                "bvid":self.ui.lineEdit_bvid.text(),
                "other_page":self.ui.radioButton_other_page.isChecked(),

                "upuser":self.ui.label_upuser.text(),
                "upuser_type":self.ui.comboBox_upuser_type.currentText(),

                "download_video":self.ui.checkBox_download_video.isChecked(),
                "download_comment":self.ui.checkBox_download_comment.isChecked(),
                "sub_comment":self.ui.checkBox_download_sub_comment.isChecked(),

                "video_count": int(self.ui.lineEdit_video_count.text()),
                "start_page": [self.ui.checkBox_start_page.isChecked(),
                               int(self.ui.lineEdit_start_page.text())],
                "comment_count":int(self.ui.lineEdit_conment_count.text()),

                "video_items_is_save":self.ui.checkBox_video_items_is_save.isChecked(),
                "video_upuser_items_is_save": self.ui.checkBox_video_upuser_items_is_save.isChecked(),

                "debug":self.ui.checkBox_debug.isChecked()
            }
        except Exception as e:
            config.logger.error(e)
        ## check params
        if not isinstance(self.ctrl.crawler, WeiboCrawler):
            self.ctrl.crawler = CrawlerFactory.create_crawler(self, platform="weibo")
        self.ui.pushButton_video_items_export.setEnabled(False)
        self.ui.pushButton_video_upuser_items_export.setEnabled(False)
        self.ui.pushButton_start_search.setEnabled(False)
        self.ui.pushButton_stop_search.setEnabled(False)
        asyncio.run_coroutine_threadsafe(self.ctrl.crawler.start(), self.ctrl.loop)
        self.ctrl.crawler.load_params(self.params)



    #### ui slots <----- ctrl signal ####
    def update_msg(self,msg):
        print(msg)