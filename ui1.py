# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(758, 558)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 60, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 250, 721, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 100, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 180, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(580, 20, 161, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.college_name = QtWidgets.QTextBrowser(self.centralwidget)
        self.college_name.setEnabled(True)
        self.college_name.setGeometry(QtCore.QRect(290, 140, 0, 0))
        self.college_name.setObjectName("college_name")
        self.label_grade2choose = QtWidgets.QLabel(self.centralwidget)
        self.label_grade2choose.setGeometry(QtCore.QRect(20, 110, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_grade2choose.setFont(font)
        self.label_grade2choose.setObjectName("label_grade2choose")
        self.comboBox_grade = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_grade.setGeometry(QtCore.QRect(20, 180, 341, 41))
        self.comboBox_grade.setObjectName("comboBox_grade")
        self.if_ingore_grade_filter = QtWidgets.QCheckBox(self.centralwidget)
        self.if_ingore_grade_filter.setGeometry(QtCore.QRect(210, 100, 201, 81))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.if_ingore_grade_filter.setFont(font)
        self.if_ingore_grade_filter.setObjectName("if_ingore_grade_filter")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 758, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "??????????????????"))
        self.comboBox.setItemText(1, _translate("MainWindow", "2"))
        self.label.setText(_translate("MainWindow", "???????????????:"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">???????????????</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "????????????"))
        self.pushButton_2.setText(_translate("MainWindow", "??????Excel??????"))
        self.pushButton_3.setText(_translate("MainWindow", "???????????????"))
        self.label_grade2choose.setText(_translate("MainWindow", "???????????????:"))
        self.if_ingore_grade_filter.setText(_translate("MainWindow", "???????????????"))
