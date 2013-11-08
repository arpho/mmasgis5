# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progress.ui'
#
# Created: Fri Jun  8 15:15:31 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Progress(object):
    def setupUi(self, Progress):
        Progress.setObjectName(_fromUtf8("Progress"))
        Progress.resize(250, 110)
        Progress.setMinimumSize(QtCore.QSize(250, 110))
        Progress.setMaximumSize(QtCore.QSize(250, 110))
        self.centralWidget = QtGui.QWidget(Progress)
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
        self.progressBar = QtGui.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 40, 231, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.progressBar.setFont(font)
        self.progressBar.setProperty(_fromUtf8("value"), 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        Progress.setCentralWidget(self.centralWidget)

        self.retranslateUi(Progress)
        QtCore.QMetaObject.connectSlotsByName(Progress)

    def retranslateUi(self, Progress):
        Progress.setWindowTitle(QtGui.QApplication.translate("Progress", "Caricamento", None, QtGui.QApplication.UnicodeUTF8))

