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
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QMainWindow,QDialog,QWidget

from .ui.tcp_udp_web import Ui_Form

class View(QWidget):
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
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect()
        self.combobox_change()

        #### set Qt model for compatible widget types ####
        # self.ui_example.comboBox_test.setModel(self.model.test_model)

        ####

    #### connect widget signals to event functions ####
    def connect(self):
        ## ui
        self.ui.pushButton_send.clicked.connect(lambda: self.set_myindex(
            index=self.ui.textEdit_send.text(),
        ))
        self.ui.comboBox.currentIndexChanged.connect(self.combobox_change)
        ## ctrl
        self.ctrl.myindex_updated.connect(self.update_myindex)
        self.ctrl.signal_write_msg.connect(self.updata_write_msg)

    #### widget signal event functions ####
    def set_myindex(self, index):
        self.ctrl.set_myindex(index)

    def combobox_change(self):
        _translate = QtCore.QCoreApplication.translate
        if self.ui.comboBox.currentIndex() == 0 or self.ui.comboBox.currentIndex() == 2:
            self.ui.label_sendto.hide()
            self.ui.label_dir.hide()
            self.ui.pushButton_dir.hide()
            self.ui.pushButton_send.show()
            self.ui.lineEdit_ip_send.hide()
            self.ui.textEdit_send.show()
            self.ui.label_port.setText(_translate("TCP-UDP", "端口号:"))

        if self.ui.comboBox.currentIndex() == 1 or self.ui.comboBox.currentIndex() == 3:
            self.ui.label_sendto.show()
            self.ui.label_dir.hide()
            self.ui.pushButton_dir.hide()
            self.ui.pushButton_send.show()
            self.ui.lineEdit_ip_send.show()
            self.ui.textEdit_send.show()
            self.ui.label_port.setText(_translate("TCP-UDP", "目标端口:"))

        if self.ui.comboBox.currentIndex() == 4:

            self.ui.label_sendto.hide()
            self.ui.label_dir.show()
            self.ui.pushButton_dir.show()
            self.ui.pushButton_send.hide()
            self.ui.lineEdit_ip_send.hide()
            self.ui.label_send.hide()
            self.ui.textEdit_send.hide()
            self.ui.label_port.setText(_translate("TCP-UDP", "端口号:"))

    def update_myindex(self):
        myindex = self.ctrl.get_myindex()
        print("myindex:", myindex)

    def updata_write_msg(self, msg):
        # signal_write_msg信号会触发这个函数
        self.textBrowser_recv.insertPlainText(msg)
        # 滚动条移动到结尾
        self.textBrowser_recv.moveCursor(QtGui.QTextCursor.End)