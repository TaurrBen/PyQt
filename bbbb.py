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
# File       : bbbb.py
# Time       ：2025.2.15 22:28
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
#####################
# views\MainView.py #
#####################
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import pyqtProperty, pyqtSignal
from untitled import Ui_Form


class MainView(QMainWindow):
    # 定义pyqtProperty
    test = pyqtProperty(int, fget=lambda self: self.ui.comboBox_test.currentIndex(),
                        fset=lambda self, v: self.ui.comboBox_test.setCurrentIndex(v))
    test_enabled = pyqtProperty(bool, fget=lambda self: self.ui.comboBox_test.isEnabled(),
                                fset=lambda self, v: self.ui.comboBox_test.setEnabled(v))

    def __init__(self, view_model):
        super().__init__()
        self.view_model = view_model
        self.build_ui()
        self.setup_bindings()
        self.initial_data_load()

    def build_ui(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 新增库存显示控件
        self.inventory_edit = QLineEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.ui.comboBox_test)
        layout.addWidget(self.inventory_edit)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def setup_bindings(self):
        # 绑定组合框变化
        self.ui.comboBox_test.currentIndexChanged.connect(
            lambda: self.view_model.set_selected_index(self.test))

        # 绑定库存输入框变化
        self.inventory_edit.textEdited.connect(
            lambda: self.view_model.set_inventory(int(self.inventory_edit.text()))
        )

        # 监听ViewModel变化
        self.view_model.selected_index_changed.connect(self.update_selection)
        self.view_model.inventory_changed.connect(self.update_inventory)

    def initial_data_load(self):
        self.ui.comboBox_test.setModel(self.view_model.fruit_model)

    def update_selection(self, index):
        self.test = index

    def update_inventory(self, value):
        self.inventory_edit.setText(str(value))


########################
# viewmodels\MainVM.py #
########################
from PyQt5.QtCore import QObject, pyqtSignal


class MainViewModel(QObject):
    selected_index_changed = pyqtSignal(int)
    inventory_changed = pyqtSignal(int)

    def __init__(self, model):
        super().__init__()
        self.model = model

        # 初始化绑定
        model.selected_index_changed.connect(self._on_model_index_changed)
        model.inventory_changed.connect(self._on_model_inventory_changed)

        self._on_model_index_changed(model._selected_index)

    # 新增模型暴露属性
    @property
    def fruit_model(self):
        return self.model.fruit_model

    def set_selected_index(self, index):
        self.model.set_selected_index(index)

    def set_inventory(self, value):
        self.model.set_current_inventory(value)

    def _on_model_index_changed(self, index):
        self.selected_index_changed.emit(index)
        # 更新库存显示
        self.inventory_changed.emit(
            self.model.get_current_inventory()
        )

    def _on_model_inventory_changed(self, value):
        self.inventory_changed.emit(value)


##################
# model\Model.py #
##################
from PyQt5.QtCore import QObject, QStringListModel, pyqtSignal


class Model(QObject):
    selected_index_changed = pyqtSignal(int)
    inventory_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self._selected_index = 3
        self._inventory = {
            "Apple": 10,
            "Banana": 20,
            "Cherry": 15,
            "Date": 5
        }
        self.test_model = QStringListModel(list(self._inventory.keys()))
        self.fruit_model = QStringListModel(list(self._inventory.keys()))

    def get_current_fruit(self):
        return self.test_model.stringList()[self._selected_index]

    def get_current_inventory(self):
        return self._inventory[self.get_current_fruit()]

    def set_selected_index(self, index):
        if self._selected_index != index and 0 <= index < len(self.test_model.stringList()):
            self._selected_index = index
            self.selected_index_changed.emit(index)
            # 同步触发库存更新
            self.inventory_changed.emit(self.get_current_inventory())

    def set_current_inventory(self, value):
        fruit = self.get_current_fruit()
        if self._inventory[fruit] != value:
            self._inventory[fruit] = value
            self.inventory_changed.emit(value)


##########
# App.py #
##########
import sys
from PyQt5.QtWidgets import QApplication


class App(QApplication):
    def __init__(self, sys_argv):
        super().__init__(sys_argv)
        self.model = Model()
        self.view_model = MainViewModel(self.model)
        self.main_view = MainView(self.view_model)
        self.main_view.show()


if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())