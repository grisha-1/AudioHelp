# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(937, 519)
        MainWindow.setMinimumSize(QtCore.QSize(937, 519))
        MainWindow.setMaximumSize(QtCore.QSize(937, 519))
        font = QtGui.QFont()
        font.setKerning(False)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #22222e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 440, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 15%;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:#54547d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:#4545ed;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 440, 300, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: #22222e;\n"
"border: 2px solid #f66867;\n"
"border-radius: 15%;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:#54547d;\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"background-color:#4545ed;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 40, 941, 381))
        self.textEdit.setStyleSheet("background-color:white;\n"
"border: 2px solid #f66867;\n"
"border-radius:25%;\n"
"color: black;\n"
"font-size:16px;")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 10, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ГОВОРИ"))
        self.pushButton_2.setText(_translate("MainWindow", "ПОКА"))
        self.label.setText(_translate("MainWindow", "МУСОР"))
