# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registrazionecensimento.ui'
#
# Created: Thu Jun 14 15:56:49 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RegistrazioneCensimento(object):
    def setupUi(self, RegistrazioneCensimento):
        RegistrazioneCensimento.setObjectName(_fromUtf8("RegistrazioneCensimento"))
        RegistrazioneCensimento.resize(400, 200)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegistrazioneCensimento.sizePolicy().hasHeightForWidth())
        RegistrazioneCensimento.setSizePolicy(sizePolicy)
        RegistrazioneCensimento.setMinimumSize(QtCore.QSize(400, 200))
        RegistrazioneCensimento.setMaximumSize(QtCore.QSize(400, 200))
        self.centralWidget = QtGui.QWidget(RegistrazioneCensimento)
        self.centralWidget.setStyleSheet(_fromUtf8("/* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
"QToolTip {\n"
"     border: 1px solid rgb(188, 189, 207);\n"
"     padding: 0.1px;\n"
"    border-radius:1px;\n"
"    color: rgb(188, 189, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"   background-origin:padding-box;\n"
"     opacity: 100;\n"
" }\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
" }\n"
"\n"
"\n"
"QLabel{\n"
"       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;\n"
"}\n"
"\n"
"\n"
" QPushButton {\n"
"     border: 2px outset  rgb(188, 198, 207);\n"
"     border-radius: 5px;\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"   \n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"    border: 2px inset  rgb(188, 198, 207);\n"
"     background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                       stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
" }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 15, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 55, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 95, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.OKButton = QtGui.QPushButton(self.centralWidget)
        self.OKButton.setGeometry(QtCore.QRect(300, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.OKButton.setFont(font)
        self.OKButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.AnnullaButton = QtGui.QPushButton(self.centralWidget)
        self.AnnullaButton.setGeometry(QtCore.QRect(187, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.AnnullaButton.setFont(font)
        self.AnnullaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AnnullaButton.setObjectName(_fromUtf8("AnnullaButton"))
        RegistrazioneCensimento.setCentralWidget(self.centralWidget)

        self.retranslateUi(RegistrazioneCensimento)
        QtCore.QMetaObject.connectSlotsByName(RegistrazioneCensimento)

    def retranslateUi(self, RegistrazioneCensimento):
        RegistrazioneCensimento.setWindowTitle(QtGui.QApplication.translate("RegistrazioneCensimento", "RegistrazioneCensimento", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("RegistrazioneCensimento", "Nome Database", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("RegistrazioneCensimento", "Censimento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("RegistrazioneCensimento", "Versione", None, QtGui.QApplication.UnicodeUTF8))
        self.OKButton.setText(QtGui.QApplication.translate("RegistrazioneCensimento", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.AnnullaButton.setText(QtGui.QApplication.translate("RegistrazioneCensimento", "Annulla", None, QtGui.QApplication.UnicodeUTF8))

