# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbar.ui'
#
# Created: Mon Apr 16 14:31:23 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ProgressBar(object):
    def setupUi(self, ProgressBar):
        ProgressBar.setObjectName(_fromUtf8("ProgressBar"))
        ProgressBar.setWindowModality(QtCore.Qt.ApplicationModal)
        ProgressBar.resize(250, 150)
        ProgressBar.setMinimumSize(QtCore.QSize(250, 150))
        ProgressBar.setMaximumSize(QtCore.QSize(250, 150))
        ProgressBar.setWindowTitle(QtGui.QApplication.translate("ProgressBar", "Caricamento", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ProgressBar.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(ProgressBar)
        self.centralWidget.setStyleSheet(_fromUtf8("/* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"    /*background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(217, 239, 255, 255), stop:0.5 rgba(239, 248, 255, 255), stop:1 rgba(210, 236, 255, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(223, 246, 255, 255), stop:0.481132 rgba(243, 243, 243, 255), stop:0.995261 rgba(223, 246, 255, 255));*/\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"    \n"
"}\n"
"\n"
" QProgressBar {\n"
"     border: 2px groove rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"    text-align: center;\n"
" }\n"
" QProgressBar::chunk {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0272727 rgba(146, 179, 203, 255), stop:1 rgba(228, 240, 248, 255));\n"
"     width: 10px;\n"
"     margin: 0px;\n"
" }\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.progressBar_1 = QtGui.QProgressBar(self.centralWidget)
        self.progressBar_1.setGeometry(QtCore.QRect(10, 50, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.progressBar_1.setFont(font)
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setTextVisible(True)
        self.progressBar_1.setObjectName(_fromUtf8("progressBar_1"))
        self.progressBar_2 = QtGui.QProgressBar(self.centralWidget)
        self.progressBar_2.setGeometry(QtCore.QRect(10, 90, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.progressBar_2.setFont(font)
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        ProgressBar.setCentralWidget(self.centralWidget)

        self.retranslateUi(ProgressBar)
        QtCore.QMetaObject.connectSlotsByName(ProgressBar)

    def retranslateUi(self, ProgressBar):
        pass

import stile_albero_rc
