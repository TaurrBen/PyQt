# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'baseui_spider.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_baseui_spider(object):
    def setupUi(self, baseui_spider):
        baseui_spider.setObjectName("baseui_spider")
        baseui_spider.resize(559, 597)
        self.centralwidget = QtWidgets.QWidget(baseui_spider)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 551, 551))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(self.layoutWidget)
        self.treeWidget.setObjectName("treeWidget")
        self.horizontalLayout.addWidget(self.treeWidget)
        self.frame = QtWidgets.QFrame(self.layoutWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout.addWidget(self.frame)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.frame_2 = QtWidgets.QFrame(self.layoutWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        baseui_spider.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(baseui_spider)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 559, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        baseui_spider.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(baseui_spider)
        self.statusbar.setObjectName("statusbar")
        baseui_spider.setStatusBar(self.statusbar)
        self.action1 = QtWidgets.QAction(baseui_spider)
        self.action1.setObjectName("action1")
        self.menu.addAction(self.action1)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(baseui_spider)
        QtCore.QMetaObject.connectSlotsByName(baseui_spider)

    def retranslateUi(self, baseui_spider):
        _translate = QtCore.QCoreApplication.translate
        baseui_spider.setWindowTitle(_translate("baseui_spider", "baseui_spider"))
        self.treeWidget.headerItem().setText(0, _translate("baseui_spider", "分类"))
        self.pushButton.setText(_translate("baseui_spider", "打开"))
        self.comboBox.setItemText(0, _translate("baseui_spider", "视频"))
        self.menu.setTitle(_translate("baseui_spider", "帮助"))
        self.action1.setText(_translate("baseui_spider", "关于"))
