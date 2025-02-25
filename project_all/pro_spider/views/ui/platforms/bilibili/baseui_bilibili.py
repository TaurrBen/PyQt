# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseui_bilibili.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_base_bilibili(object):
    def setupUi(self, base_bilibili):
        base_bilibili.setObjectName("base_bilibili")
        base_bilibili.resize(1504, 579)
        self.comboBox = QtWidgets.QComboBox(base_bilibili)
        self.comboBox.setGeometry(QtCore.QRect(1410, 30, 50, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.layoutWidget = QtWidgets.QWidget(base_bilibili)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 12, 1385, 476))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_initail_setting = QtWidgets.QHBoxLayout()
        self.horizontalLayout_initail_setting.setObjectName("horizontalLayout_initail_setting")
        self.checkBox_is_playwright = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_is_playwright.setChecked(True)
        self.checkBox_is_playwright.setObjectName("checkBox_is_playwright")
        self.horizontalLayout_initail_setting.addWidget(self.checkBox_is_playwright)
        self.checkBox_headless = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_headless.setObjectName("checkBox_headless")
        self.horizontalLayout_initail_setting.addWidget(self.checkBox_headless)
        self.comboBox_proxy_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_proxy_type.setObjectName("comboBox_proxy_type")
        self.comboBox_proxy_type.addItem("")
        self.comboBox_proxy_type.addItem("")
        self.horizontalLayout_initail_setting.addWidget(self.comboBox_proxy_type)
        self.verticalLayout.addLayout(self.horizontalLayout_initail_setting)
        self.textBrowser_context = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_context.setObjectName("textBrowser_context")
        self.verticalLayout.addWidget(self.textBrowser_context)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.frame_line1 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_line1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_line1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_line1.setObjectName("frame_line1")
        self.verticalLayout_2.addWidget(self.frame_line1)
        self.verticalLayout_type = QtWidgets.QVBoxLayout()
        self.verticalLayout_type.setObjectName("verticalLayout_type")
        self.comboBox_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.verticalLayout_type.addWidget(self.comboBox_type)
        self.horizontalLayout_type = QtWidgets.QHBoxLayout()
        self.horizontalLayout_type.setObjectName("horizontalLayout_type")
        self.verticalLayout_keyword = QtWidgets.QVBoxLayout()
        self.verticalLayout_keyword.setObjectName("verticalLayout_keyword")
        self.horizontalLayout_keyword = QtWidgets.QHBoxLayout()
        self.horizontalLayout_keyword.setObjectName("horizontalLayout_keyword")
        self.label_keyword = QtWidgets.QLabel(self.layoutWidget)
        self.label_keyword.setObjectName("label_keyword")
        self.horizontalLayout_keyword.addWidget(self.label_keyword)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.horizontalLayout_keyword.addWidget(self.lineEdit_keyword)
        self.pushButton_keyword = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_keyword.setObjectName("pushButton_keyword")
        self.horizontalLayout_keyword.addWidget(self.pushButton_keyword)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_keyword)
        self.horizontalLayout_search_type = QtWidgets.QHBoxLayout()
        self.horizontalLayout_search_type.setObjectName("horizontalLayout_search_type")
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.horizontalLayout_search_type.addWidget(self.checkBox_8)
        self.comboBox_search_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_search_type.setObjectName("comboBox_search_type")
        self.comboBox_search_type.addItem("")
        self.comboBox_search_type.addItem("")
        self.comboBox_search_type.addItem("")
        self.comboBox_search_type.addItem("")
        self.comboBox_search_type.addItem("")
        self.comboBox_search_type.addItem("")
        self.comboBox_search_type.addItem("")
        self.horizontalLayout_search_type.addWidget(self.comboBox_search_type)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_search_type)
        self.horizontalLayout_order_type = QtWidgets.QHBoxLayout()
        self.horizontalLayout_order_type.setObjectName("horizontalLayout_order_type")
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.horizontalLayout_order_type.addWidget(self.checkBox_7)
        self.comboBox_order_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_order_type.setObjectName("comboBox_order_type")
        self.comboBox_order_type.addItem("")
        self.comboBox_order_type.addItem("")
        self.comboBox_order_type.addItem("")
        self.comboBox_order_type.addItem("")
        self.comboBox_order_type.addItem("")
        self.horizontalLayout_order_type.addWidget(self.comboBox_order_type)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_order_type)
        self.horizontalLayout_pubtime = QtWidgets.QHBoxLayout()
        self.horizontalLayout_pubtime.setObjectName("horizontalLayout_pubtime")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_pubtime.addWidget(self.checkBox)
        self.dateEdit_pubtime_begin_s = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_pubtime_begin_s.setObjectName("dateEdit_pubtime_begin_s")
        self.horizontalLayout_pubtime.addWidget(self.dateEdit_pubtime_begin_s)
        self.label_pubtime = QtWidgets.QLabel(self.layoutWidget)
        self.label_pubtime.setObjectName("label_pubtime")
        self.horizontalLayout_pubtime.addWidget(self.label_pubtime)
        self.dateEdit_pubtime_end_s = QtWidgets.QDateEdit(self.layoutWidget)
        self.dateEdit_pubtime_end_s.setObjectName("dateEdit_pubtime_end_s")
        self.horizontalLayout_pubtime.addWidget(self.dateEdit_pubtime_end_s)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_pubtime)
        self.horizontalLayout_duration = QtWidgets.QHBoxLayout()
        self.horizontalLayout_duration.setObjectName("horizontalLayout_duration")
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_duration.addWidget(self.checkBox_2)
        self.comboBox_duration = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_duration.setObjectName("comboBox_duration")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.comboBox_duration.addItem("")
        self.horizontalLayout_duration.addWidget(self.comboBox_duration)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_duration)
        self.horizontalLayout_tids = QtWidgets.QHBoxLayout()
        self.horizontalLayout_tids.setObjectName("horizontalLayout_tids")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout_tids.addWidget(self.checkBox_3)
        self.comboBox_tids = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_tids.setObjectName("comboBox_tids")
        self.comboBox_tids.addItem("")
        self.horizontalLayout_tids.addWidget(self.comboBox_tids)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_tids)
        self.horizontalLayout_type.addLayout(self.verticalLayout_keyword)
        self.verticalLayout_bvid = QtWidgets.QVBoxLayout()
        self.verticalLayout_bvid.setObjectName("verticalLayout_bvid")
        self.horizontalLayout_bvid = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bvid.setObjectName("horizontalLayout_bvid")
        self.label_bvid = QtWidgets.QLabel(self.layoutWidget)
        self.label_bvid.setObjectName("label_bvid")
        self.horizontalLayout_bvid.addWidget(self.label_bvid)
        self.lineEdit_bvid = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_bvid.setObjectName("lineEdit_bvid")
        self.horizontalLayout_bvid.addWidget(self.lineEdit_bvid)
        self.pushButton_bvid = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_bvid.setObjectName("pushButton_bvid")
        self.horizontalLayout_bvid.addWidget(self.pushButton_bvid)
        self.verticalLayout_bvid.addLayout(self.horizontalLayout_bvid)
        self.radioButton_other_page = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_other_page.setObjectName("radioButton_other_page")
        self.verticalLayout_bvid.addWidget(self.radioButton_other_page)
        self.horizontalLayout_type.addLayout(self.verticalLayout_bvid)
        self.verticalLayout_upuser = QtWidgets.QVBoxLayout()
        self.verticalLayout_upuser.setObjectName("verticalLayout_upuser")
        self.horizontalLayout_upuser = QtWidgets.QHBoxLayout()
        self.horizontalLayout_upuser.setObjectName("horizontalLayout_upuser")
        self.label_upuser = QtWidgets.QLabel(self.layoutWidget)
        self.label_upuser.setObjectName("label_upuser")
        self.horizontalLayout_upuser.addWidget(self.label_upuser)
        self.lineEdit_upuser = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_upuser.setObjectName("lineEdit_upuser")
        self.horizontalLayout_upuser.addWidget(self.lineEdit_upuser)
        self.pushButton_upuser = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_upuser.setObjectName("pushButton_upuser")
        self.horizontalLayout_upuser.addWidget(self.pushButton_upuser)
        self.verticalLayout_upuser.addLayout(self.horizontalLayout_upuser)
        self.comboBox_upuser_type = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_upuser_type.setObjectName("comboBox_upuser_type")
        self.comboBox_upuser_type.addItem("")
        self.comboBox_upuser_type.addItem("")
        self.comboBox_upuser_type.addItem("")
        self.comboBox_upuser_type.addItem("")
        self.comboBox_upuser_type.addItem("")
        self.verticalLayout_upuser.addWidget(self.comboBox_upuser_type)
        self.horizontalLayout_type.addLayout(self.verticalLayout_upuser)
        self.verticalLayout_type.addLayout(self.horizontalLayout_type)
        self.verticalLayout_2.addLayout(self.verticalLayout_type)
        self.frame_line4 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_line4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_line4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_line4.setObjectName("frame_line4")
        self.verticalLayout_2.addWidget(self.frame_line4)
        self.horizontalLayout_download_video_comment = QtWidgets.QHBoxLayout()
        self.horizontalLayout_download_video_comment.setObjectName("horizontalLayout_download_video_comment")
        self.checkBox_download_video = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_download_video.setObjectName("checkBox_download_video")
        self.horizontalLayout_download_video_comment.addWidget(self.checkBox_download_video)
        self.checkBox_download_comment = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_download_comment.setObjectName("checkBox_download_comment")
        self.horizontalLayout_download_video_comment.addWidget(self.checkBox_download_comment)
        self.checkBox_download_sub_comment = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_download_sub_comment.setObjectName("checkBox_download_sub_comment")
        self.horizontalLayout_download_video_comment.addWidget(self.checkBox_download_sub_comment)
        self.verticalLayout_2.addLayout(self.horizontalLayout_download_video_comment)
        self.horizontalLayout_start_stop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_start_stop.setObjectName("horizontalLayout_start_stop")
        self.pushButton_start_search = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_start_search.setObjectName("pushButton_start_search")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_start_search)
        self.pushButton_stop_search = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_stop_search.setObjectName("pushButton_stop_search")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_stop_search)
        self.verticalLayout_2.addLayout(self.horizontalLayout_start_stop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.frame_line3 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_line3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_line3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_line3.setObjectName("frame_line3")
        self.horizontalLayout_3.addWidget(self.frame_line3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout__video_items = QtWidgets.QVBoxLayout()
        self.verticalLayout__video_items.setObjectName("verticalLayout__video_items")
        self.label_video_items = QtWidgets.QLabel(self.layoutWidget)
        self.label_video_items.setObjectName("label_video_items")
        self.verticalLayout__video_items.addWidget(self.label_video_items)
        self.tableWidget_video_items = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget_video_items.setObjectName("tableWidget_video_items")
        self.tableWidget_video_items.setColumnCount(17)
        self.tableWidget_video_items.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_video_items.setHorizontalHeaderItem(16, item)
        self.verticalLayout__video_items.addWidget(self.tableWidget_video_items)
        self.horizontalLayout_2.addLayout(self.verticalLayout__video_items)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_video_upper_items = QtWidgets.QLabel(self.layoutWidget)
        self.label_video_upper_items.setObjectName("label_video_upper_items")
        self.verticalLayout_4.addWidget(self.label_video_upper_items)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.verticalLayout_4.addWidget(self.tableWidget_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.frame_line2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_line2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_line2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_line2.setObjectName("frame_line2")
        self.verticalLayout_5.addWidget(self.frame_line2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_debug = QtWidgets.QHBoxLayout()
        self.horizontalLayout_debug.setObjectName("horizontalLayout_debug")
        self.label_logs = QtWidgets.QLabel(self.layoutWidget)
        self.label_logs.setObjectName("label_logs")
        self.horizontalLayout_debug.addWidget(self.label_logs)
        self.checkBox_debug = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_debug.setChecked(True)
        self.checkBox_debug.setObjectName("checkBox_debug")
        self.horizontalLayout_debug.addWidget(self.checkBox_debug)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_debug.addWidget(self.pushButton_clear)
        self.verticalLayout_3.addLayout(self.horizontalLayout_debug)
        self.textBrowser_debug = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser_debug.setObjectName("textBrowser_debug")
        self.verticalLayout_3.addWidget(self.textBrowser_debug)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)

        self.retranslateUi(base_bilibili)
        QtCore.QMetaObject.connectSlotsByName(base_bilibili)

    def retranslateUi(self, base_bilibili):
        _translate = QtCore.QCoreApplication.translate
        base_bilibili.setWindowTitle(_translate("base_bilibili", "base_bilibili"))
        self.comboBox.setItemText(0, _translate("base_bilibili", "视频"))
        self.checkBox_is_playwright.setText(_translate("base_bilibili", "playwright"))
        self.checkBox_headless.setText(_translate("base_bilibili", "headless"))
        self.comboBox_proxy_type.setItemText(0, _translate("base_bilibili", "none"))
        self.comboBox_proxy_type.setItemText(1, _translate("base_bilibili", "kuaidaili"))
        self.comboBox_type.setItemText(0, _translate("base_bilibili", "keyword"))
        self.comboBox_type.setItemText(1, _translate("base_bilibili", "bvid"))
        self.comboBox_type.setItemText(2, _translate("base_bilibili", "upuser"))
        self.label_keyword.setText(_translate("base_bilibili", "keyword:"))
        self.pushButton_keyword.setText(_translate("base_bilibili", "open"))
        self.checkBox_8.setText(_translate("base_bilibili", "search_type:"))
        self.comboBox_search_type.setItemText(0, _translate("base_bilibili", "all"))
        self.comboBox_search_type.setItemText(1, _translate("base_bilibili", "video"))
        self.comboBox_search_type.setItemText(2, _translate("base_bilibili", "bangumi"))
        self.comboBox_search_type.setItemText(3, _translate("base_bilibili", "pgc"))
        self.comboBox_search_type.setItemText(4, _translate("base_bilibili", "live"))
        self.comboBox_search_type.setItemText(5, _translate("base_bilibili", "article"))
        self.comboBox_search_type.setItemText(6, _translate("base_bilibili", "upuser"))
        self.checkBox_7.setText(_translate("base_bilibili", "order_type:"))
        self.comboBox_order_type.setItemText(0, _translate("base_bilibili", "all"))
        self.comboBox_order_type.setItemText(1, _translate("base_bilibili", "click"))
        self.comboBox_order_type.setItemText(2, _translate("base_bilibili", "pubdate"))
        self.comboBox_order_type.setItemText(3, _translate("base_bilibili", "dm"))
        self.comboBox_order_type.setItemText(4, _translate("base_bilibili", "stow"))
        self.checkBox.setText(_translate("base_bilibili", "pubtime:from"))
        self.label_pubtime.setText(_translate("base_bilibili", "to"))
        self.checkBox_2.setText(_translate("base_bilibili", "duration:"))
        self.comboBox_duration.setItemText(0, _translate("base_bilibili", "all"))
        self.comboBox_duration.setItemText(1, _translate("base_bilibili", "<10m"))
        self.comboBox_duration.setItemText(2, _translate("base_bilibili", "≥10m&<30m"))
        self.comboBox_duration.setItemText(3, _translate("base_bilibili", "≥30m&<60m"))
        self.comboBox_duration.setItemText(4, _translate("base_bilibili", "≥60m"))
        self.checkBox_3.setText(_translate("base_bilibili", "tids"))
        self.comboBox_tids.setItemText(0, _translate("base_bilibili", "all"))
        self.label_bvid.setText(_translate("base_bilibili", "bvid:"))
        self.pushButton_bvid.setText(_translate("base_bilibili", "open"))
        self.radioButton_other_page.setText(_translate("base_bilibili", "other_page"))
        self.label_upuser.setText(_translate("base_bilibili", "upuser:"))
        self.pushButton_upuser.setText(_translate("base_bilibili", "open"))
        self.comboBox_upuser_type.setItemText(0, _translate("base_bilibili", "home"))
        self.comboBox_upuser_type.setItemText(1, _translate("base_bilibili", "dynamic"))
        self.comboBox_upuser_type.setItemText(2, _translate("base_bilibili", "upload"))
        self.comboBox_upuser_type.setItemText(3, _translate("base_bilibili", "lists"))
        self.comboBox_upuser_type.setItemText(4, _translate("base_bilibili", "favlist"))
        self.checkBox_download_video.setText(_translate("base_bilibili", "download_video"))
        self.checkBox_download_comment.setText(_translate("base_bilibili", "download_comment"))
        self.checkBox_download_sub_comment.setText(_translate("base_bilibili", "sub_comment"))
        self.pushButton_start_search.setText(_translate("base_bilibili", "start_search"))
        self.pushButton_stop_search.setText(_translate("base_bilibili", "stop_search"))
        self.label_video_items.setText(_translate("base_bilibili", "video_items"))
        item = self.tableWidget_video_items.horizontalHeaderItem(0)
        item.setText(_translate("base_bilibili", "keyword"))
        item = self.tableWidget_video_items.horizontalHeaderItem(1)
        item.setText(_translate("base_bilibili", "video_id"))
        item = self.tableWidget_video_items.horizontalHeaderItem(2)
        item.setText(_translate("base_bilibili", "video_type"))
        item = self.tableWidget_video_items.horizontalHeaderItem(3)
        item.setText(_translate("base_bilibili", "title"))
        item = self.tableWidget_video_items.horizontalHeaderItem(4)
        item.setText(_translate("base_bilibili", "desc"))
        item = self.tableWidget_video_items.horizontalHeaderItem(5)
        item.setText(_translate("base_bilibili", "create_time"))
        item = self.tableWidget_video_items.horizontalHeaderItem(6)
        item.setText(_translate("base_bilibili", "user_id"))
        item = self.tableWidget_video_items.horizontalHeaderItem(7)
        item.setText(_translate("base_bilibili", "nickname"))
        item = self.tableWidget_video_items.horizontalHeaderItem(8)
        item.setText(_translate("base_bilibili", "avatar"))
        item = self.tableWidget_video_items.horizontalHeaderItem(9)
        item.setText(_translate("base_bilibili", "liked_count"))
        item = self.tableWidget_video_items.horizontalHeaderItem(10)
        item.setText(_translate("base_bilibili", "video_play_count"))
        item = self.tableWidget_video_items.horizontalHeaderItem(11)
        item.setText(_translate("base_bilibili", "video_danmaku"))
        item = self.tableWidget_video_items.horizontalHeaderItem(12)
        item.setText(_translate("base_bilibili", "video_comment"))
        item = self.tableWidget_video_items.horizontalHeaderItem(13)
        item.setText(_translate("base_bilibili", "last_modify_ts"))
        item = self.tableWidget_video_items.horizontalHeaderItem(14)
        item.setText(_translate("base_bilibili", "video_url"))
        item = self.tableWidget_video_items.horizontalHeaderItem(15)
        item.setText(_translate("base_bilibili", "video_cover_url"))
        item = self.tableWidget_video_items.horizontalHeaderItem(16)
        item.setText(_translate("base_bilibili", "source_keyword"))
        self.label_video_upper_items.setText(_translate("base_bilibili", "video_upper_items"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("base_bilibili", "user_id"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("base_bilibili", "nickname"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("base_bilibili", "avatar"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("base_bilibili", "last_modify_ts"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("base_bilibili", "total_fans"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("base_bilibili", "total_liked"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("base_bilibili", "user_rank"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("base_bilibili", "is_official"))
        self.label_logs.setText(_translate("base_bilibili", "logs"))
        self.checkBox_debug.setText(_translate("base_bilibili", "debug"))
        self.pushButton_clear.setText(_translate("base_bilibili", "clear"))
