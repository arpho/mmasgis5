# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'albero.ui'
#
# Created: Tue Apr 24 12:25:26 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Albero(object):
    def setupUi(self, Albero):
        Albero.setObjectName(_fromUtf8("Albero"))
        Albero.resize(230, 500)
        Albero.setMinimumSize(QtCore.QSize(230, 500))
        Albero.setMaximumSize(QtCore.QSize(230, 500))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Albero.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Albero.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(Albero)
        self.centralWidget.setStyleSheet(_fromUtf8("QWidget{\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
"QToolTip {\n"
"     border: 1px solid rgb(188, 189, 207);\n"
"     padding: 0.1px;\n"
"    border-radius:1px;\n"
"    color: rgb(188, 189, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"   background-origin:padding-box;\n"
"     opacity: 100;\n"
" }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.etichetta = QtGui.QLabel(self.centralWidget)
        self.etichetta.setGeometry(QtCore.QRect(10, 50, 231, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.etichetta.setFont(font)
        self.etichetta.setObjectName(_fromUtf8("etichetta"))
        self.cercaButton = QtGui.QPushButton(self.centralWidget)
        self.cercaButton.setGeometry(QtCore.QRect(120, 10, 98, 29))
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
"\n"
""))
        self.cercaButton.setObjectName(_fromUtf8("cercaButton"))
        self.albero = QtGui.QTreeWidget(self.centralWidget)
        self.albero.setGeometry(QtCore.QRect(10, 70, 211, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.albero.setFont(font)
        self.albero.setStyleSheet(_fromUtf8("QTreeWidget{\n"
"border:2px groove rgb(188, 198, 207);  \n"
"}"))
        self.albero.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.albero.setIndentation(10)
        self.albero.setHeaderHidden(True)
        self.albero.setExpandsOnDoubleClick(False)
        self.albero.setObjectName(_fromUtf8("albero"))
        self.albero.header().setDefaultSectionSize(300)
        self.albero.header().setMinimumSectionSize(300)
        self.albero.header().setStretchLastSection(False)
        self.plusNodes = QtGui.QPushButton(self.centralWidget)
        self.plusNodes.setGeometry(QtCore.QRect(10, 10, 31, 29))
        self.plusNodes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plusNodes.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/ptree.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } "))
        self.plusNodes.setText(_fromUtf8(""))
        self.plusNodes.setObjectName(_fromUtf8("plusNodes"))
        self.minusNodes = QtGui.QPushButton(self.centralWidget)
        self.minusNodes.setGeometry(QtCore.QRect(50, 10, 31, 29))
        self.minusNodes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.minusNodes.setStyleSheet(_fromUtf8("QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/micon.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } "))
        self.minusNodes.setText(_fromUtf8(""))
        self.minusNodes.setObjectName(_fromUtf8("minusNodes"))
        Albero.setCentralWidget(self.centralWidget)

        self.retranslateUi(Albero)
        QtCore.QMetaObject.connectSlotsByName(Albero)

    def retranslateUi(self, Albero):
        Albero.setWindowTitle(QtGui.QApplication.translate("Albero", "Elenco Territori", None, QtGui.QApplication.UnicodeUTF8))
        self.etichetta.setText(QtGui.QApplication.translate("Albero", "Italia", None, QtGui.QApplication.UnicodeUTF8))
        self.cercaButton.setText(QtGui.QApplication.translate("Albero", "CERCA", None, QtGui.QApplication.UnicodeUTF8))
        self.plusNodes.setToolTip(QtGui.QApplication.translate("Albero", "esplodi nodi", None, QtGui.QApplication.UnicodeUTF8))
        self.minusNodes.setToolTip(QtGui.QApplication.translate("Albero", "chiudi nodi", None, QtGui.QApplication.UnicodeUTF8))

import stile_albero_rc
