# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'separatore.ui'
#
# Created: Tue May  8 11:08:17 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Separatore(object):
    def setupUi(self, Separatore):
        Separatore.setObjectName(_fromUtf8("Separatore"))
        Separatore.setWindowModality(QtCore.Qt.ApplicationModal)
        Separatore.resize(230, 210)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Separatore.sizePolicy().hasHeightForWidth())
        Separatore.setSizePolicy(sizePolicy)
        Separatore.setMinimumSize(QtCore.QSize(230, 210))
        Separatore.setMaximumSize(QtCore.QSize(230, 230))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Separatore.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(Separatore)
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
"QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
"     font: 11pt \"Arial\";\n"
"\n"
" }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.radioButton_tab = QtGui.QRadioButton(self.centralWidget)
        self.radioButton_tab.setGeometry(QtCore.QRect(10, 30, 117, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.radioButton_tab.setFont(font)
        self.radioButton_tab.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_tab.setChecked(True)
        self.radioButton_tab.setObjectName(_fromUtf8("radioButton_tab"))
        self.radioButton_vir = QtGui.QRadioButton(self.centralWidget)
        self.radioButton_vir.setGeometry(QtCore.QRect(10, 60, 117, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.radioButton_vir.setFont(font)
        self.radioButton_vir.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_vir.setObjectName(_fromUtf8("radioButton_vir"))
        self.radioButton_altro = QtGui.QRadioButton(self.centralWidget)
        self.radioButton_altro.setGeometry(QtCore.QRect(10, 90, 117, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.radioButton_altro.setFont(font)
        self.radioButton_altro.setFocusPolicy(QtCore.Qt.NoFocus)
        self.radioButton_altro.setObjectName(_fromUtf8("radioButton_altro"))
        self.line_sep = QtGui.QLineEdit(self.centralWidget)
        self.line_sep.setGeometry(QtCore.QRect(30, 120, 113, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.line_sep.setFont(font)
        self.line_sep.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.line_sep.setObjectName(_fromUtf8("line_sep"))
        self.OKButton = QtGui.QPushButton(self.centralWidget)
        self.OKButton.setGeometry(QtCore.QRect(160, 150, 50, 50))
        self.OKButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OKButton.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/filter_ok_not_hov.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    image: url(:/resources/filter_ok.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } "))
        self.OKButton.setText(_fromUtf8(""))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        Separatore.setCentralWidget(self.centralWidget)

        self.retranslateUi(Separatore)
        QtCore.QMetaObject.connectSlotsByName(Separatore)

    def retranslateUi(self, Separatore):
        Separatore.setWindowTitle(QtGui.QApplication.translate("Separatore", "Separatore", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_tab.setText(QtGui.QApplication.translate("Separatore", "Tabulazione", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_vir.setText(QtGui.QApplication.translate("Separatore", "Virgola", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_altro.setText(QtGui.QApplication.translate("Separatore", "Altro", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
