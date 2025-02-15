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

from PyQt5.QtWidgets import QMainWindow

from .ui.tcp_udp_web import Ui_MainWindow

class View(QMainWindow):

    #### properties for widget value ####
    @property
    def test(self):
        return object
    @test.setter
    def test(self, value):
        return object

    def __init__(self, model, ctrl):
        self.ctrl = ctrl
        super(View, self).__init__()
        self.build_ui()

    def build_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####
        # self.ui_example.comboBox_test.setModel(self.model.test_model)

        ### connect widget signals to event functions ####
        self.ui.pushButton_send.clicked.connect(lambda: self.set_myindex(
            index=self.ui.textEdit_send.text(),
        ))
        self.ctrl.myindex_updated.connect(self.update_myindex)

    #### widget signal event functions ####
    def set_myindex(self, index):
        self.ctrl.set_myindex(index)

    def update_myindex(self):
        myindex = self.ctrl.get_myindex()
        print("myindex:", myindex)