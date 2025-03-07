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
# File       : ui_xiaohongshu.py
# Time       ：2025.2.20 16:54
# Author     ：Benboy
# Email      : hgq1633923487@gmail.com
# version    ：python 3.9
# Description：
"""
import csv
import sys
from abc import ABC

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QObject
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QFileDialog, QMessageBox

import config
from .baseui_xiaohongshu import Ui_baseui_xiaohongshu
from utils.qEvent import *

class Ui_xiaohongshu(QWidget,Ui_baseui_xiaohongshu):
    signal_write_msg = QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        self.parent = parent
        super(Ui_xiaohongshu, self).__init__()
        self.setupUi(self)
        self.initialUi()

    def initialUi(self):
        self.resize(1280, 720)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.dateEdit_pubtime_begin_s.setDate(QtCore.QDate.currentDate())
        self.dateEdit_pubtime_end_s.setDate((QtCore.QDate.currentDate()))
        self.on_comboBox_type_currentIndexChanged()
        self.pushButton_video_items_export.clicked.connect(self.btn_video_items_export_clicked)
        self.pushButton_video_upuser_items_export.clicked.connect(self.btn_video_upuser_items_export_clicked)
        self.pushButton_keywords.clicked.connect(lambda :self.open_txt_to_lineEdit(self.lineEdit_keywords))
        self.pushButton_bvids.clicked.connect(lambda :self.open_txt_to_lineEdit(self.lineEdit_bvids))
        self.pushButton_upusers.clicked.connect(lambda: self.open_txt_to_lineEdit(self.lineEdit_upusers))

    def open_txt_to_lineEdit(self,lineEdit):
        file_name, _ = QFileDialog.getOpenFileName(self, '打开文件', '', '文本文件 (*.txt);;所有文件 (*)')

        if file_name:
            # 读取文件内容
            with open(file_name, 'r', encoding='utf-8') as file:
                file_content = file.read().replace('，', ',')

            # 将文件内容导入到输入框中
            lineEdit.setText(file_content)

    def export_to_csv(self,table_widget):
        # 打开文件对话框，选择保存位置
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if not file_path:
            return  # 用户取消

        # 导出 QTableWidget 数据到 CSV 文件
        with open(file_path, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # 导出表头
            headers = []
            for column in range(table_widget.model().columnCount()):
                headers.append(table_widget.horizontalHeaderItem(column).text())
            writer.writerow(headers)

            # 导出表格数据
            for row in range(table_widget.rowCount()):
                row_data = []
                for column in range(table_widget.columnCount()):
                    item = table_widget.item(row, column)
                    row_data.append(item.text() if item else '')  # 如果没有数据，默认填入空字符串
                writer.writerow(row_data)

        print(f'Data exported to {file_path}')

    def btn_video_items_export_clicked(self):
        self.export_to_csv(self.tableWidget_video_items)

    def btn_video_upuser_items_export_clicked(self):
        self.export_to_csv(self.tableWidget_upuser_items)

    def btn_load_params_clicked(self, func_name):
        self.pushButton_load_params.clicked.connect(func_name)

    def btn_start_search_clicked(self, func_name):
        self.pushButton_start_search.clicked.connect(func_name)

    def btn_stop_search_clicked(self,func_name):
        self.pushButton_stop_search.clicked.connect(func_name)

    def btn_keyword_clicked(self,func_name):
        self.pushButton_keyword.clicked.connect(func_name)

    def btn_bvid_clicked(self,func_name):
        self.pushButton_bvid.clicked.connect(func_name)

    def btn_upuser_clicked(self, func_name):
        self.pushButton_upuser.clicked.connect(func_name)

    def on_pushButton_clear_clicked(self):
        self.textBrowser_context.clear()
        self.textBrowser_cookies.clear()
        self.textEdit_cookies.clear()
        self.textBrowser_debug.clear()
        self.tableWidget_video_items.setRowCount(0)
        self.tableWidget_upuser_items.setRowCount(0)

    def traverse_layout(self,layout,hide):
        for i in range(layout.count()):  # 遍历当前布局中的每一项
            item = layout.itemAt(i)  # 获取当前项
            if item.widget() is not None:  # 如果是小部件
                widget = item.widget()
                if hide:
                    widget.hide()
                else:
                    widget.show()
            elif item.layout() is not None:  # 如果是嵌套布局
                self.traverse_layout(item.layout(),hide)

    def on_comboBox_type_currentIndexChanged(self):
        type = self.comboBox_type.currentText()
        if type == "keywords":
            self.traverse_layout(self.verticalLayout_keywords, hide=False)
            self.traverse_layout(self.verticalLayout_bvids,hide=True)
            self.traverse_layout(self.verticalLayout_upusers, hide=True)
        elif type == "bvids":
            self.traverse_layout(self.verticalLayout_keywords, hide=True)
            self.traverse_layout(self.verticalLayout_bvids,hide=False)
            self.traverse_layout(self.verticalLayout_upusers, hide=True)
        elif type == "upuser":
            self.traverse_layout(self.verticalLayout_keywords, hide=True)
            self.traverse_layout(self.verticalLayout_bvids,hide=True)
            self.traverse_layout(self.verticalLayout_upusers, hide=False)

    def tableWidget_video_items_addRow(self,data:list):
        current_row_count = self.tableWidget_video_items.rowCount()
        self.tableWidget_video_items.insertRow(current_row_count)
        # 设置每列的默认数据
        for column in range(self.tableWidget_video_items.columnCount()):
            if data and column < len(data):
                item = QTableWidgetItem(data[column])  # 如果有数据则填充
            else:
                item = QTableWidgetItem(f"错误数据")  # 默认填充
                config.logger.error(f"data:{data} error,row:{current_row_count},column{column} ")
            self.tableWidget_video_items.setItem(current_row_count, column, item)
        self.tableWidget_video_items.scrollToBottom()

    def tableWidget_upuser_items_addRow(self,data:list):
        current_row_count = self.tableWidget_upuser_items.rowCount()
        self.tableWidget_upuser_items.insertRow(current_row_count)
        # 设置每列的默认数据
        for column in range(self.tableWidget_upuser_items.columnCount()):
            if data and column < len(data):
                item = QTableWidgetItem(data[column])  # 如果有数据则填充
            else:
                item = QTableWidgetItem("错误数据")  # 默认填充
                config.logger.error(f"data:{data} error,row:{current_row_count},column{column} ")
            self.tableWidget_upuser_items.setItem(current_row_count, column, item)
        self.tableWidget_upuser_items.scrollToBottom()

    def event(self,event):
        if event.type() == ViewDataEvent.idType:
            #根据事件中的数据更新PyQT窗口中的指定组件
            if event.qname == "self":
                exec(event.callback_name)
                return True
            else:
                qwidget = self.findChild(QObject, event.qname)
                if qwidget:
                    exec(event.callback_name)
                return True
        return QWidget.event(self,event)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        # 弹出确认对话框
        reply = QMessageBox.question(
            self,
            "确认关闭",
            "你确定要关闭窗口吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
            # QMessageBox.No
        )
        # 根据用户选择决定是否关闭窗口
        if reply == QMessageBox.Yes:
            event.accept()  # 接受关闭事件，窗口关闭
            # self.parent.ui.show()
        else:
            event.ignore()  # 忽略关闭事件，窗口保持打开

def main():
    app = QApplication(sys.argv)
    ui = Ui_xiaohongshu()
    ui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

