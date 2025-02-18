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
# File       : QtWebEngine.py.py
# Time       ：2025.2.11 22:49
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import importlib
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtCore import QCoreApplication

import config
from QtProjectManager.QtProjectManager import Ui_QtProjectManager

class QtProjectManager(QMainWindow,Ui_QtProjectManager):
    def __init__(self,parent=None):
        super(QtProjectManager, self).__init__(parent)
        self.setupUi(self)
        self.connect()
        self.translate()

    ## 信号与槽链接
    def connect(self):
        # 如需传递参数可以修改为connect(lambda: self.click(参数))
        self.pushButton1.clicked.connect(self.on_pushButton)

    ## 槽函数
    def on_pushButton(self):
        pro = "project_all."+self.comboBox.currentText()
        try:
            myModule = importlib.import_module(pro)
            mainWindow = myModule.MainWindow(pro)
        except Exception as e:
            config.logger.error("导入{}失败".format(pro))
    ##
    def translate(self):
        _translate = QCoreApplication.translate

        self.statusbar.showMessage(_translate("QtProjectManager","有问题请联系wx:taurrben1"))
        for index,name in enumerate(config.PROJECTS):
            print(index,name)
            self.comboBox.addItem("")
            self.comboBox.setItemText(index, _translate("QtProjectManager", name))

def main():
    app = QApplication(sys.argv)
    mainWindow = QtProjectManager()
    mainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()