# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtProjectManager.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QtProjectManager(object):
    def setupUi(self, QtProjectManager):
        QtProjectManager.setObjectName("QtProjectManager")
        QtProjectManager.resize(220, 94)
        self.centralwidget = QtWidgets.QWidget(QtProjectManager)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 140, 30))
        self.comboBox.setStyleSheet("font: 25 14pt \"3ds\";")
        self.comboBox.setEditable(False)
        self.comboBox.setMaxVisibleItems(10)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(160, 10, 40, 30))
        self.pushButton1.setObjectName("pushButton1")
        QtProjectManager.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QtProjectManager)
        self.statusbar.setObjectName("statusbar")
        QtProjectManager.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(QtProjectManager)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 220, 23))
        self.menubar.setTabletTracking(False)
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        QtProjectManager.setMenuBar(self.menubar)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(QtProjectManager)
        QtCore.QMetaObject.connectSlotsByName(QtProjectManager)

    def retranslateUi(self, QtProjectManager):
        _translate = QtCore.QCoreApplication.translate
        QtProjectManager.setWindowTitle(_translate("QtProjectManager", "MainWindow"))
        self.pushButton1.setText(_translate("QtProjectManager", "打开"))
        self.menu.setTitle(_translate("QtProjectManager", "文件"))
        self.menu_2.setTitle(_translate("QtProjectManager", "帮助"))
