# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cercageo.ui'
#
# Created: Wed May  9 12:28:28 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CercaGeo(object):
    def setupUi(self, CercaGeo):
        CercaGeo.setObjectName(_fromUtf8("CercaGeo"))
        CercaGeo.setWindowModality(QtCore.Qt.NonModal)
        CercaGeo.resize(270, 210)
        CercaGeo.setMinimumSize(QtCore.QSize(270, 210))
        CercaGeo.setMaximumSize(QtCore.QSize(270, 210))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CercaGeo.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(CercaGeo)
        self.centralWidget.setStyleSheet(_fromUtf8("/* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
"\n"
"QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
" }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.cercaProv = QtGui.QRadioButton(self.centralWidget)
        self.cercaProv.setGeometry(QtCore.QRect(50, 20, 151, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.cercaProv.setFont(font)
        self.cercaProv.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cercaProv.setObjectName(_fromUtf8("cercaProv"))
        self.cercaCom = QtGui.QRadioButton(self.centralWidget)
        self.cercaCom.setGeometry(QtCore.QRect(50, 50, 131, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.cercaCom.setFont(font)
        self.cercaCom.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cercaCom.setChecked(True)
        self.cercaCom.setObjectName(_fromUtf8("cercaCom"))
        self.cercaCap = QtGui.QRadioButton(self.centralWidget)
        self.cercaCap.setGeometry(QtCore.QRect(50, 80, 141, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.cercaCap.setFont(font)
        self.cercaCap.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cercaCap.setObjectName(_fromUtf8("cercaCap"))
        self.nome_ricerca = QtGui.QLineEdit(self.centralWidget)
        self.nome_ricerca.setGeometry(QtCore.QRect(10, 120, 231, 29))
        self.nome_ricerca.setObjectName(_fromUtf8("nome_ricerca"))
        self.cercaButton = QtGui.QPushButton(self.centralWidget)
        self.cercaButton.setGeometry(QtCore.QRect(140, 170, 98, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.cercaButton.setFont(font)
        self.cercaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.cercaButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
" }\n"
""))
        self.cercaButton.setObjectName(_fromUtf8("cercaButton"))
        CercaGeo.setCentralWidget(self.centralWidget)

        self.retranslateUi(CercaGeo)
        QtCore.QMetaObject.connectSlotsByName(CercaGeo)

    def retranslateUi(self, CercaGeo):
        CercaGeo.setWindowTitle(QtGui.QApplication.translate("CercaGeo", "Cerca Territorio", None, QtGui.QApplication.UnicodeUTF8))
        self.cercaProv.setText(QtGui.QApplication.translate("CercaGeo", "Cerca Provincia", None, QtGui.QApplication.UnicodeUTF8))
        self.cercaCom.setText(QtGui.QApplication.translate("CercaGeo", "Cerca Comune", None, QtGui.QApplication.UnicodeUTF8))
        self.cercaCap.setText(QtGui.QApplication.translate("CercaGeo", "Cerca Cap", None, QtGui.QApplication.UnicodeUTF8))
        self.cercaButton.setText(QtGui.QApplication.translate("CercaGeo", "CERCA", None, QtGui.QApplication.UnicodeUTF8))

import stile_albero_rc
