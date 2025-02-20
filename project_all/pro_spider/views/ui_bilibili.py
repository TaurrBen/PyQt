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
# File       : ui_bilibili.py
# Time       ：2025.2.20 16:54
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import sys
from .ui.platforms.bilibili.baseui_bilibili import Ui_base_bilibili

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget

class Ui_MainWindow(QWidget,Ui_base_bilibili):
    signal_write_msg = QtCore.pyqtSignal(str)
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.initialUi()

    def initialUi(self):
        pass
        # self.dateEdit_pubtime_begin_s.setDateTime(QtCore.QDateTime.currentDateTime())
        # self.dateEdit_pubtime_begin_s.setCalendarPopup(True)
        # self.dateEdit_pubtime_end_s.setDateTime((QtCore.QDateTime.currentDateTime()))
        # self.dateEdit_pubtime_end_s.setCalendarPopup(True)





    @QtCore.pyqtSlot()
    def aa(self):
        pass

def main():
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

