# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tcp_tt.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

"""
v2.0计划：
使用布局，不使用绝对坐标；
优化代码；
"""
import sys
import socket
import threading
import ctypes
import inspect
import re
import time

from .ui.tcp_udp_web import Ui_Form

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QDialog

class Ui_TCP(QWidget,Ui_Form):
    # 定义一个信号
    signal_write_msg = QtCore.pyqtSignal(str)

    def __init__(self,num):
        """
        初始化，定义变量
        :param st: StopThreading类创建的对象
        """
        super(Ui_TCP, self).__init__()
        self.setupUi(self)

def main():
    """
    主函数，用于运行程序
    :return: None
    """
    app = QApplication(sys.argv)
    ui = Ui_TCP(1)
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
