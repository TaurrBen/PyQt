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
from PyQt5 import QtCore
class Model(QtCore.QObject):
    #### 1.定义signal ####
    signal_write_msg = QtCore.pyqtSignal(str)

    #### 2.初始化 ####
    def __init__(self):
        super(Model, self).__init__()
        #### 向ctrl暴露的模型 ####
        #### create Qt models for compatible widget types ####
        self.widget_model = QtCore.QStringListModel()
        #### models variables ####
        self.msg = "Hi."

    #### 3.event functions ####
    def set_msg(self,msg):
        if not msg == self.msg:
            #### 设置model具体字段 ####
            self.msg = msg
            #### 发送信号至ctrl中 ####
            self.signal_write_msg.emit(msg)

    def get_msg(self):
        return self.msg
