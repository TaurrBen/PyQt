# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseui_weibo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_baseui_weibo(object):
    def setupUi(self, baseui_weibo):
        baseui_weibo.setObjectName("baseui_weibo")
        baseui_weibo.resize(1368, 621)
        self.widget = QtWidgets.QWidget(baseui_weibo)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1364, 574))
        self.widget.setObjectName("widget")
        self.centralWidget = QtWidgets.QHBoxLayout(self.widget)
        self.centralWidget.setContentsMargins(5, 5, 5, 5)
        self.centralWidget.setSpacing(10)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_initail_setting = QtWidgets.QHBoxLayout()
        self.horizontalLayout_initail_setting.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_initail_setting.setSpacing(6)
        self.horizontalLayout_initail_setting.setObjectName("horizontalLayout_initail_setting")
        self.checkBox_is_playwright = QtWidgets.QCheckBox(self.widget)
        self.checkBox_is_playwright.setChecked(True)
        self.checkBox_is_playwright.setObjectName("checkBox_is_playwright")
        self.horizontalLayout_initail_setting.addWidget(self.checkBox_is_playwright)
        self.checkBox_headless = QtWidgets.QCheckBox(self.widget)
        self.checkBox_headless.setChecked(False)
        self.checkBox_headless.setObjectName("checkBox_headless")
        self.horizontalLayout_initail_setting.addWidget(self.checkBox_headless)
        self.horizontalLayout_proxy_type = QtWidgets.QHBoxLayout()
        self.horizontalLayout_proxy_type.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_proxy_type.setSpacing(6)
        self.horizontalLayout_proxy_type.setObjectName("horizontalLayout_proxy_type")
        self.label_proxy_type = QtWidgets.QLabel(self.widget)
        self.label_proxy_type.setObjectName("label_proxy_type")
        self.horizontalLayout_proxy_type.addWidget(self.label_proxy_type)
        self.comboBox_proxy_type = QtWidgets.QComboBox(self.widget)
        self.comboBox_proxy_type.setObjectName("comboBox_proxy_type")
        self.comboBox_proxy_type.addItem("")
        self.comboBox_proxy_type.addItem("")
        self.horizontalLayout_proxy_type.addWidget(self.comboBox_proxy_type)
        self.horizontalLayout_initail_setting.addLayout(self.horizontalLayout_proxy_type)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_concurrency_num = QtWidgets.QLabel(self.widget)
        self.label_concurrency_num.setObjectName("label_concurrency_num")
        self.horizontalLayout_8.addWidget(self.label_concurrency_num)
        self.lineEdit_concurrency_num = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_concurrency_num.setObjectName("lineEdit_concurrency_num")
        self.horizontalLayout_8.addWidget(self.lineEdit_concurrency_num)
        self.horizontalLayout_initail_setting.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_initail_setting.setStretch(0, 1)
        self.horizontalLayout_initail_setting.setStretch(1, 1)
        self.horizontalLayout_initail_setting.setStretch(2, 1)
        self.horizontalLayout_initail_setting.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_initail_setting)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.textBrowser_context = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_context.setObjectName("textBrowser_context")
        self.verticalLayout_7.addWidget(self.textBrowser_context)
        self.textBrowser_cookies = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_cookies.setObjectName("textBrowser_cookies")
        self.verticalLayout_7.addWidget(self.textBrowser_cookies)
        self.verticalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_type = QtWidgets.QVBoxLayout()
        self.verticalLayout_type.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_type.setSpacing(6)
        self.verticalLayout_type.setObjectName("verticalLayout_type")
        self.comboBox_type = QtWidgets.QComboBox(self.widget)
        self.comboBox_type.setObjectName("comboBox_type")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.comboBox_type.addItem("")
        self.verticalLayout_type.addWidget(self.comboBox_type)
        self.horizontalLayout_type = QtWidgets.QHBoxLayout()
        self.horizontalLayout_type.setSpacing(0)
        self.horizontalLayout_type.setObjectName("horizontalLayout_type")
        self.verticalLayout_keyword = QtWidgets.QVBoxLayout()
        self.verticalLayout_keyword.setSpacing(6)
        self.verticalLayout_keyword.setObjectName("verticalLayout_keyword")
        self.horizontalLayout_keyword = QtWidgets.QHBoxLayout()
        self.horizontalLayout_keyword.setObjectName("horizontalLayout_keyword")
        self.label_keyword = QtWidgets.QLabel(self.widget)
        self.label_keyword.setObjectName("label_keyword")
        self.horizontalLayout_keyword.addWidget(self.label_keyword)
        self.lineEdit_keyword = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_keyword.setObjectName("lineEdit_keyword")
        self.horizontalLayout_keyword.addWidget(self.lineEdit_keyword)
        self.pushButton_keyword = QtWidgets.QPushButton(self.widget)
        self.pushButton_keyword.setObjectName("pushButton_keyword")
        self.horizontalLayout_keyword.addWidget(self.pushButton_keyword)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_keyword)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_start_page = QtWidgets.QCheckBox(self.widget)
        self.checkBox_start_page.setObjectName("checkBox_start_page")
        self.horizontalLayout_4.addWidget(self.checkBox_start_page)
        self.lineEdit_start_page = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_start_page.setObjectName("lineEdit_start_page")
        self.horizontalLayout_4.addWidget(self.lineEdit_start_page)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_search_type = QtWidgets.QHBoxLayout()
        self.horizontalLayout_search_type.setObjectName("horizontalLayout_search_type")
        self.checkBox_search_type = QtWidgets.QCheckBox(self.widget)
        self.checkBox_search_type.setObjectName("checkBox_search_type")
        self.horizontalLayout_search_type.addWidget(self.checkBox_search_type)
        self.comboBox_search_type = QtWidgets.QComboBox(self.widget)
        self.comboBox_search_type.setObjectName("comboBox_search_type")
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
        self.checkBox_order_type = QtWidgets.QCheckBox(self.widget)
        self.checkBox_order_type.setObjectName("checkBox_order_type")
        self.horizontalLayout_order_type.addWidget(self.checkBox_order_type)
        self.comboBox_order_type = QtWidgets.QComboBox(self.widget)
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
        self.checkBox_pubtime = QtWidgets.QCheckBox(self.widget)
        self.checkBox_pubtime.setChecked(False)
        self.checkBox_pubtime.setObjectName("checkBox_pubtime")
        self.horizontalLayout_pubtime.addWidget(self.checkBox_pubtime)
        self.dateEdit_pubtime_begin_s = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_pubtime_begin_s.setCalendarPopup(True)
        self.dateEdit_pubtime_begin_s.setObjectName("dateEdit_pubtime_begin_s")
        self.horizontalLayout_pubtime.addWidget(self.dateEdit_pubtime_begin_s)
        self.label_pubtime = QtWidgets.QLabel(self.widget)
        self.label_pubtime.setObjectName("label_pubtime")
        self.horizontalLayout_pubtime.addWidget(self.label_pubtime)
        self.dateEdit_pubtime_end_s = QtWidgets.QDateEdit(self.widget)
        self.dateEdit_pubtime_end_s.setCalendarPopup(True)
        self.dateEdit_pubtime_end_s.setObjectName("dateEdit_pubtime_end_s")
        self.horizontalLayout_pubtime.addWidget(self.dateEdit_pubtime_end_s)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_pubtime)
        self.horizontalLayout_duration = QtWidgets.QHBoxLayout()
        self.horizontalLayout_duration.setObjectName("horizontalLayout_duration")
        self.checkBox_duration = QtWidgets.QCheckBox(self.widget)
        self.checkBox_duration.setObjectName("checkBox_duration")
        self.horizontalLayout_duration.addWidget(self.checkBox_duration)
        self.comboBox_duration = QtWidgets.QComboBox(self.widget)
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
        self.checkBox_tids = QtWidgets.QCheckBox(self.widget)
        self.checkBox_tids.setObjectName("checkBox_tids")
        self.horizontalLayout_tids.addWidget(self.checkBox_tids)
        self.comboBox_tids = QtWidgets.QComboBox(self.widget)
        self.comboBox_tids.setObjectName("comboBox_tids")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.comboBox_tids.addItem("")
        self.horizontalLayout_tids.addWidget(self.comboBox_tids)
        self.verticalLayout_keyword.addLayout(self.horizontalLayout_tids)
        self.horizontalLayout_type.addLayout(self.verticalLayout_keyword)
        self.verticalLayout_bvid = QtWidgets.QVBoxLayout()
        self.verticalLayout_bvid.setSpacing(6)
        self.verticalLayout_bvid.setObjectName("verticalLayout_bvid")
        self.horizontalLayout_bvid = QtWidgets.QHBoxLayout()
        self.horizontalLayout_bvid.setObjectName("horizontalLayout_bvid")
        self.label_bvid = QtWidgets.QLabel(self.widget)
        self.label_bvid.setObjectName("label_bvid")
        self.horizontalLayout_bvid.addWidget(self.label_bvid)
        self.lineEdit_bvid = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_bvid.setObjectName("lineEdit_bvid")
        self.horizontalLayout_bvid.addWidget(self.lineEdit_bvid)
        self.pushButton_bvid = QtWidgets.QPushButton(self.widget)
        self.pushButton_bvid.setObjectName("pushButton_bvid")
        self.horizontalLayout_bvid.addWidget(self.pushButton_bvid)
        self.verticalLayout_bvid.addLayout(self.horizontalLayout_bvid)
        self.radioButton_other_page = QtWidgets.QRadioButton(self.widget)
        self.radioButton_other_page.setObjectName("radioButton_other_page")
        self.verticalLayout_bvid.addWidget(self.radioButton_other_page)
        self.horizontalLayout_type.addLayout(self.verticalLayout_bvid)
        self.verticalLayout_upuser = QtWidgets.QVBoxLayout()
        self.verticalLayout_upuser.setSpacing(6)
        self.verticalLayout_upuser.setObjectName("verticalLayout_upuser")
        self.horizontalLayout_upuser = QtWidgets.QHBoxLayout()
        self.horizontalLayout_upuser.setObjectName("horizontalLayout_upuser")
        self.label_upuser = QtWidgets.QLabel(self.widget)
        self.label_upuser.setObjectName("label_upuser")
        self.horizontalLayout_upuser.addWidget(self.label_upuser)
        self.lineEdit_upuser = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_upuser.setObjectName("lineEdit_upuser")
        self.horizontalLayout_upuser.addWidget(self.lineEdit_upuser)
        self.pushButton_upuser = QtWidgets.QPushButton(self.widget)
        self.pushButton_upuser.setObjectName("pushButton_upuser")
        self.horizontalLayout_upuser.addWidget(self.pushButton_upuser)
        self.verticalLayout_upuser.addLayout(self.horizontalLayout_upuser)
        self.comboBox_upuser_type = QtWidgets.QComboBox(self.widget)
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
        self.horizontalLayout_download_video_comment = QtWidgets.QHBoxLayout()
        self.horizontalLayout_download_video_comment.setSpacing(6)
        self.horizontalLayout_download_video_comment.setObjectName("horizontalLayout_download_video_comment")
        self.checkBox_download_video = QtWidgets.QCheckBox(self.widget)
        self.checkBox_download_video.setCheckable(True)
        self.checkBox_download_video.setChecked(False)
        self.checkBox_download_video.setObjectName("checkBox_download_video")
        self.horizontalLayout_download_video_comment.addWidget(self.checkBox_download_video)
        self.checkBox_download_comment = QtWidgets.QCheckBox(self.widget)
        self.checkBox_download_comment.setCheckable(True)
        self.checkBox_download_comment.setChecked(False)
        self.checkBox_download_comment.setObjectName("checkBox_download_comment")
        self.horizontalLayout_download_video_comment.addWidget(self.checkBox_download_comment)
        self.checkBox_download_sub_comment = QtWidgets.QCheckBox(self.widget)
        self.checkBox_download_sub_comment.setObjectName("checkBox_download_sub_comment")
        self.horizontalLayout_download_video_comment.addWidget(self.checkBox_download_sub_comment)
        self.verticalLayout_2.addLayout(self.horizontalLayout_download_video_comment)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_video_count = QtWidgets.QLabel(self.widget)
        self.label_video_count.setObjectName("label_video_count")
        self.horizontalLayout.addWidget(self.label_video_count)
        self.lineEdit_video_count = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_video_count.setObjectName("lineEdit_video_count")
        self.horizontalLayout.addWidget(self.lineEdit_video_count)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_comment_count = QtWidgets.QLabel(self.widget)
        self.label_comment_count.setObjectName("label_comment_count")
        self.horizontalLayout_6.addWidget(self.label_comment_count)
        self.lineEdit_conment_count = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_conment_count.setObjectName("lineEdit_conment_count")
        self.horizontalLayout_6.addWidget(self.lineEdit_conment_count)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_start_stop = QtWidgets.QHBoxLayout()
        self.horizontalLayout_start_stop.setObjectName("horizontalLayout_start_stop")
        self.pushButton_load_params = QtWidgets.QPushButton(self.widget)
        self.pushButton_load_params.setObjectName("pushButton_load_params")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_load_params)
        self.pushButton_start_search = QtWidgets.QPushButton(self.widget)
        self.pushButton_start_search.setEnabled(False)
        self.pushButton_start_search.setCheckable(False)
        self.pushButton_start_search.setChecked(False)
        self.pushButton_start_search.setObjectName("pushButton_start_search")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_start_search)
        self.pushButton_stop_search = QtWidgets.QPushButton(self.widget)
        self.pushButton_stop_search.setEnabled(False)
        self.pushButton_stop_search.setCheckable(False)
        self.pushButton_stop_search.setChecked(False)
        self.pushButton_stop_search.setObjectName("pushButton_stop_search")
        self.horizontalLayout_start_stop.addWidget(self.pushButton_stop_search)
        self.verticalLayout_2.addLayout(self.horizontalLayout_start_stop)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 12)
        self.centralWidget.addLayout(self.verticalLayout_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout__video_items = QtWidgets.QVBoxLayout()
        self.verticalLayout__video_items.setObjectName("verticalLayout__video_items")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_video_items = QtWidgets.QLabel(self.widget)
        self.label_video_items.setObjectName("label_video_items")
        self.horizontalLayout_3.addWidget(self.label_video_items)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_video_items_is_save = QtWidgets.QCheckBox(self.widget)
        self.checkBox_video_items_is_save.setObjectName("checkBox_video_items_is_save")
        self.verticalLayout_4.addWidget(self.checkBox_video_items_is_save)
        self.pushButton_video_items_export = QtWidgets.QPushButton(self.widget)
        self.pushButton_video_items_export.setObjectName("pushButton_video_items_export")
        self.verticalLayout_4.addWidget(self.pushButton_video_items_export)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout__video_items.addLayout(self.horizontalLayout_3)
        self.tableWidget_video_items = QtWidgets.QTableWidget(self.widget)
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
        self.verticalLayout_upper_items = QtWidgets.QVBoxLayout()
        self.verticalLayout_upper_items.setObjectName("verticalLayout_upper_items")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_video_upuser_items = QtWidgets.QLabel(self.widget)
        self.label_video_upuser_items.setObjectName("label_video_upuser_items")
        self.horizontalLayout_5.addWidget(self.label_video_upuser_items)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_video_upuser_items_is_save = QtWidgets.QCheckBox(self.widget)
        self.checkBox_video_upuser_items_is_save.setObjectName("checkBox_video_upuser_items_is_save")
        self.verticalLayout_6.addWidget(self.checkBox_video_upuser_items_is_save)
        self.pushButton_video_upuser_items_export = QtWidgets.QPushButton(self.widget)
        self.pushButton_video_upuser_items_export.setObjectName("pushButton_video_upuser_items_export")
        self.verticalLayout_6.addWidget(self.pushButton_video_upuser_items_export)
        self.horizontalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_upper_items.addLayout(self.horizontalLayout_5)
        self.tableWidget_upuser_items = QtWidgets.QTableWidget(self.widget)
        self.tableWidget_upuser_items.setObjectName("tableWidget_upuser_items")
        self.tableWidget_upuser_items.setColumnCount(8)
        self.tableWidget_upuser_items.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_upuser_items.setHorizontalHeaderItem(7, item)
        self.verticalLayout_upper_items.addWidget(self.tableWidget_upuser_items)
        self.horizontalLayout_2.addLayout(self.verticalLayout_upper_items)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_debug = QtWidgets.QHBoxLayout()
        self.horizontalLayout_debug.setObjectName("horizontalLayout_debug")
        self.label_logs = QtWidgets.QLabel(self.widget)
        self.label_logs.setObjectName("label_logs")
        self.horizontalLayout_debug.addWidget(self.label_logs)
        self.checkBox_debug = QtWidgets.QCheckBox(self.widget)
        self.checkBox_debug.setChecked(True)
        self.checkBox_debug.setObjectName("checkBox_debug")
        self.horizontalLayout_debug.addWidget(self.checkBox_debug)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout_debug.addWidget(self.pushButton_clear)
        self.verticalLayout_3.addLayout(self.horizontalLayout_debug)
        self.textBrowser_debug = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_debug.setObjectName("textBrowser_debug")
        self.verticalLayout_3.addWidget(self.textBrowser_debug)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_5.setStretch(0, 3)
        self.verticalLayout_5.setStretch(1, 1)
        self.centralWidget.addLayout(self.verticalLayout_5)
        self.centralWidget.setStretch(0, 1)
        self.centralWidget.setStretch(1, 1)

        self.retranslateUi(baseui_weibo)
        QtCore.QMetaObject.connectSlotsByName(baseui_weibo)

    def retranslateUi(self, baseui_weibo):
        _translate = QtCore.QCoreApplication.translate
        baseui_weibo.setWindowTitle(_translate("baseui_weibo", "baseui_weibo"))
        self.checkBox_is_playwright.setText(_translate("baseui_weibo", "playwright"))
        self.checkBox_headless.setText(_translate("baseui_weibo", "headless"))
        self.label_proxy_type.setText(_translate("baseui_weibo", "proxy:"))
        self.comboBox_proxy_type.setItemText(0, _translate("baseui_weibo", "none"))
        self.comboBox_proxy_type.setItemText(1, _translate("baseui_weibo", "kuaidaili"))
        self.label_concurrency_num.setText(_translate("baseui_weibo", "concurrency_num:"))
        self.lineEdit_concurrency_num.setText(_translate("baseui_weibo", "3"))
        self.comboBox_type.setItemText(0, _translate("baseui_weibo", "keyword"))
        self.comboBox_type.setItemText(1, _translate("baseui_weibo", "bvid"))
        self.comboBox_type.setItemText(2, _translate("baseui_weibo", "upuser"))
        self.label_keyword.setText(_translate("baseui_weibo", "keyword:"))
        self.lineEdit_keyword.setText(_translate("baseui_weibo", "神经网络,深度学习"))
        self.pushButton_keyword.setText(_translate("baseui_weibo", "open"))
        self.checkBox_start_page.setText(_translate("baseui_weibo", "start_page:"))
        self.lineEdit_start_page.setText(_translate("baseui_weibo", "1"))
        self.checkBox_search_type.setText(_translate("baseui_weibo", "search_type:"))
        self.comboBox_search_type.setItemText(0, _translate("baseui_weibo", "video"))
        self.comboBox_search_type.setItemText(1, _translate("baseui_weibo", "media_bangumi"))
        self.comboBox_search_type.setItemText(2, _translate("baseui_weibo", "media_ft"))
        self.comboBox_search_type.setItemText(3, _translate("baseui_weibo", "live"))
        self.comboBox_search_type.setItemText(4, _translate("baseui_weibo", "article"))
        self.comboBox_search_type.setItemText(5, _translate("baseui_weibo", "bili_user"))
        self.checkBox_order_type.setText(_translate("baseui_weibo", "order_type:"))
        self.comboBox_order_type.setItemText(0, _translate("baseui_weibo", "综合排序"))
        self.comboBox_order_type.setItemText(1, _translate("baseui_weibo", "最多播放"))
        self.comboBox_order_type.setItemText(2, _translate("baseui_weibo", "最新发布"))
        self.comboBox_order_type.setItemText(3, _translate("baseui_weibo", "最多弹幕"))
        self.comboBox_order_type.setItemText(4, _translate("baseui_weibo", "最多收藏"))
        self.checkBox_pubtime.setText(_translate("baseui_weibo", "pubtime:from"))
        self.label_pubtime.setText(_translate("baseui_weibo", "to"))
        self.checkBox_duration.setText(_translate("baseui_weibo", "duration:"))
        self.comboBox_duration.setItemText(0, _translate("baseui_weibo", "all"))
        self.comboBox_duration.setItemText(1, _translate("baseui_weibo", "<10m"))
        self.comboBox_duration.setItemText(2, _translate("baseui_weibo", "≥10m&<30m"))
        self.comboBox_duration.setItemText(3, _translate("baseui_weibo", "≥30m&<60m"))
        self.comboBox_duration.setItemText(4, _translate("baseui_weibo", "≥60m"))
        self.checkBox_tids.setText(_translate("baseui_weibo", "tids"))
        self.comboBox_tids.setItemText(0, _translate("baseui_weibo", "综合分区"))
        self.comboBox_tids.setItemText(1, _translate("baseui_weibo", "动画"))
        self.comboBox_tids.setItemText(2, _translate("baseui_weibo", "番剧"))
        self.comboBox_tids.setItemText(3, _translate("baseui_weibo", "国创"))
        self.comboBox_tids.setItemText(4, _translate("baseui_weibo", "音乐"))
        self.comboBox_tids.setItemText(5, _translate("baseui_weibo", "舞蹈"))
        self.comboBox_tids.setItemText(6, _translate("baseui_weibo", "游戏"))
        self.comboBox_tids.setItemText(7, _translate("baseui_weibo", "知识"))
        self.comboBox_tids.setItemText(8, _translate("baseui_weibo", "科技"))
        self.comboBox_tids.setItemText(9, _translate("baseui_weibo", "运动"))
        self.comboBox_tids.setItemText(10, _translate("baseui_weibo", "汽车"))
        self.comboBox_tids.setItemText(11, _translate("baseui_weibo", "生活"))
        self.comboBox_tids.setItemText(12, _translate("baseui_weibo", "美食"))
        self.comboBox_tids.setItemText(13, _translate("baseui_weibo", "动物圈"))
        self.comboBox_tids.setItemText(14, _translate("baseui_weibo", "鬼畜"))
        self.comboBox_tids.setItemText(15, _translate("baseui_weibo", "时尚"))
        self.comboBox_tids.setItemText(16, _translate("baseui_weibo", "咨询"))
        self.comboBox_tids.setItemText(17, _translate("baseui_weibo", "娱乐"))
        self.comboBox_tids.setItemText(18, _translate("baseui_weibo", "影视"))
        self.comboBox_tids.setItemText(19, _translate("baseui_weibo", "纪录片"))
        self.comboBox_tids.setItemText(20, _translate("baseui_weibo", "电影"))
        self.comboBox_tids.setItemText(21, _translate("baseui_weibo", "电视剧"))
        self.label_bvid.setText(_translate("baseui_weibo", "bvid:"))
        self.pushButton_bvid.setText(_translate("baseui_weibo", "open"))
        self.radioButton_other_page.setText(_translate("baseui_weibo", "other_page"))
        self.label_upuser.setText(_translate("baseui_weibo", "upuser:"))
        self.pushButton_upuser.setText(_translate("baseui_weibo", "open"))
        self.comboBox_upuser_type.setItemText(0, _translate("baseui_weibo", "home"))
        self.comboBox_upuser_type.setItemText(1, _translate("baseui_weibo", "dynamic"))
        self.comboBox_upuser_type.setItemText(2, _translate("baseui_weibo", "upload"))
        self.comboBox_upuser_type.setItemText(3, _translate("baseui_weibo", "lists"))
        self.comboBox_upuser_type.setItemText(4, _translate("baseui_weibo", "favlist"))
        self.checkBox_download_video.setText(_translate("baseui_weibo", "download_video"))
        self.checkBox_download_comment.setText(_translate("baseui_weibo", "download_comment"))
        self.checkBox_download_sub_comment.setText(_translate("baseui_weibo", "sub_comment"))
        self.label_video_count.setText(_translate("baseui_weibo", "video_count:"))
        self.lineEdit_video_count.setText(_translate("baseui_weibo", "20"))
        self.label_comment_count.setText(_translate("baseui_weibo", "comment_count:"))
        self.lineEdit_conment_count.setText(_translate("baseui_weibo", "20"))
        self.pushButton_load_params.setText(_translate("baseui_weibo", "load_params"))
        self.pushButton_start_search.setText(_translate("baseui_weibo", "start_search"))
        self.pushButton_stop_search.setText(_translate("baseui_weibo", "stop_search"))
        self.label_video_items.setText(_translate("baseui_weibo", "video_items"))
        self.checkBox_video_items_is_save.setText(_translate("baseui_weibo", "is_save"))
        self.pushButton_video_items_export.setText(_translate("baseui_weibo", "export"))
        item = self.tableWidget_video_items.horizontalHeaderItem(0)
        item.setText(_translate("baseui_weibo", "keyword"))
        item = self.tableWidget_video_items.horizontalHeaderItem(1)
        item.setText(_translate("baseui_weibo", "video_id"))
        item = self.tableWidget_video_items.horizontalHeaderItem(2)
        item.setText(_translate("baseui_weibo", "video_type"))
        item = self.tableWidget_video_items.horizontalHeaderItem(3)
        item.setText(_translate("baseui_weibo", "title"))
        item = self.tableWidget_video_items.horizontalHeaderItem(4)
        item.setText(_translate("baseui_weibo", "desc"))
        item = self.tableWidget_video_items.horizontalHeaderItem(5)
        item.setText(_translate("baseui_weibo", "create_time"))
        item = self.tableWidget_video_items.horizontalHeaderItem(6)
        item.setText(_translate("baseui_weibo", "user_id"))
        item = self.tableWidget_video_items.horizontalHeaderItem(7)
        item.setText(_translate("baseui_weibo", "nickname"))
        item = self.tableWidget_video_items.horizontalHeaderItem(8)
        item.setText(_translate("baseui_weibo", "avatar"))
        item = self.tableWidget_video_items.horizontalHeaderItem(9)
        item.setText(_translate("baseui_weibo", "liked_count"))
        item = self.tableWidget_video_items.horizontalHeaderItem(10)
        item.setText(_translate("baseui_weibo", "video_play_count"))
        item = self.tableWidget_video_items.horizontalHeaderItem(11)
        item.setText(_translate("baseui_weibo", "video_danmaku"))
        item = self.tableWidget_video_items.horizontalHeaderItem(12)
        item.setText(_translate("baseui_weibo", "video_comment"))
        item = self.tableWidget_video_items.horizontalHeaderItem(13)
        item.setText(_translate("baseui_weibo", "last_modify_ts"))
        item = self.tableWidget_video_items.horizontalHeaderItem(14)
        item.setText(_translate("baseui_weibo", "video_url"))
        item = self.tableWidget_video_items.horizontalHeaderItem(15)
        item.setText(_translate("baseui_weibo", "video_cover_url"))
        item = self.tableWidget_video_items.horizontalHeaderItem(16)
        item.setText(_translate("baseui_weibo", "source_keyword"))
        self.label_video_upuser_items.setText(_translate("baseui_weibo", "video_upuser_items"))
        self.checkBox_video_upuser_items_is_save.setText(_translate("baseui_weibo", "is_save"))
        self.pushButton_video_upuser_items_export.setText(_translate("baseui_weibo", "export"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(0)
        item.setText(_translate("baseui_weibo", "user_id"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(1)
        item.setText(_translate("baseui_weibo", "nickname"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(2)
        item.setText(_translate("baseui_weibo", "avatar"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(3)
        item.setText(_translate("baseui_weibo", "last_modify_ts"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(4)
        item.setText(_translate("baseui_weibo", "total_fans"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(5)
        item.setText(_translate("baseui_weibo", "total_liked"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(6)
        item.setText(_translate("baseui_weibo", "user_rank"))
        item = self.tableWidget_upuser_items.horizontalHeaderItem(7)
        item.setText(_translate("baseui_weibo", "is_official"))
        self.label_logs.setText(_translate("baseui_weibo", "logs"))
        self.checkBox_debug.setText(_translate("baseui_weibo", "debug"))
        self.pushButton_clear.setText(_translate("baseui_weibo", "clear"))
