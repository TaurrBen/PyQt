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
# File       : aaaa.py
# Time       ：2025.2.15 21:09
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
#####################
# views\MainView.py #
#####################
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtProperty
from untitled import Ui_Form

class MainView(QMainWindow):

    #### properties for widget value ####
    @property
    def test(self):
        return self.ui.comboBox_test.currentIndex()
    @test.setter
    def test(self, value):
        self.ui.comboBox_test.setCurrentIndex(value)

    #### properties for widget enabled state ####
    @property
    def test_enabled(self):
        return self.ui.comboBox_test.isEnabled()
    @test_enabled.setter
    def test_enabled(self, value):
        self.ui.comboBox_test.setEnabled(value)

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui()
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####
        self.ui.comboBox_test.setModel(self.model.test_model)

        #### connect widget signals to event functions ####
        self.ui.comboBox_test.currentIndexChanged.connect(self.on_test)

    def update_ui_from_model(self):
        print('DEBUG: update_ui_from_model called')
        #### update widget values from model ####
        self.test = self.model.test

    #### widget signal event functions ####
    def on_test(self, index): self.main_ctrl.change_test(index)


###########################
# ctrls\MainController.py #
###########################

class MainController(object):

    def __init__(self, model):
        self.model = model

    #### widget event functions ####
    def change_test(self, index):
        self.model.test = index
        print('DEBUG: change_test called with arg value:', index)


##################
# model\Model.py #
##################
from PyQt5.QtCore import QStringListModel
class Model(object):

    #### properties for value of Qt model contents ####
    @property
    def test_items(self):
        return self.test_model.stringList()
    @test_items.setter
    def test_items(self, value):
        self.test_model.setStringList(value)

    def __init__(self):
        self._update_funcs = []
        self.config_section = 'settings'
        self.config_options = (
            ('test', 'getint'),
        )
        self.string_list = ['Apple', 'Banana', 'Cherry', 'Date']

        #### create Qt models for compatible widget types ####
        self.test_model = QStringListModel()
        self.test_model.setStringList(self.string_list)

        #### model variables ####
        self.test = 5

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            func()


##########
# App.py #
##########
import sys
from PyQt5.QtWidgets import QApplication

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())