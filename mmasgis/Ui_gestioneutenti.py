# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestioneutenti.ui'
#
# Created: Mon Jun 11 14:43:16 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GestioneUtenti(object):
    def setupUi(self, GestioneUtenti):
        GestioneUtenti.setObjectName(_fromUtf8("GestioneUtenti"))
        GestioneUtenti.resize(400, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GestioneUtenti.sizePolicy().hasHeightForWidth())
        GestioneUtenti.setSizePolicy(sizePolicy)
        GestioneUtenti.setMinimumSize(QtCore.QSize(400, 500))
        GestioneUtenti.setMaximumSize(QtCore.QSize(400, 500))
        self.centralWidget = QtGui.QWidget(GestioneUtenti)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMinimumSize(QtCore.QSize(400, 500))
        self.centralWidget.setMaximumSize(QtCore.QSize(400, 500))
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
" }\n"
"\n"
"QGroupBox {\n"
"     border-radius: 5px;\n"
"    border:2px groove rgb(188, 198, 207);\n"
"     background-color:  rgba(255, 255, 255, 0);\n"
"        margin: 6px;\n"
"\n"
"}\n"
"QGroupBox::title {\n"
"     subcontrol-origin: margin;\n"
"     subcontrol-position: top left; /* position at the top center */\n"
"     padding: 0 3px;\n"
"     border:2px groove rgb(188, 198, 207);\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"        font: 11pt \"Arial\";\n"
"     border-radius: 5px;\n"
"}\n"
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
" }\n"
"\n"
"QListWidget{\n"
"border: 1px groove rgb(188, 198, 207);\n"
"}"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.list_utenti = QtGui.QListWidget(self.centralWidget)
        self.list_utenti.setGeometry(QtCore.QRect(10, 30, 251, 431))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.list_utenti.setFont(font)
        self.list_utenti.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_utenti.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.list_utenti.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.list_utenti.setObjectName(_fromUtf8("list_utenti"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QLabel{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px outset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.CreaUtente = QtGui.QPushButton(self.centralWidget)
        self.CreaUtente.setGeometry(QtCore.QRect(280, 30, 101, 52))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.CreaUtente.setFont(font)
        self.CreaUtente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CreaUtente.setObjectName(_fromUtf8("CreaUtente"))
        self.ModificaUtente = QtGui.QPushButton(self.centralWidget)
        self.ModificaUtente.setGeometry(QtCore.QRect(280, 100, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.ModificaUtente.setFont(font)
        self.ModificaUtente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ModificaUtente.setObjectName(_fromUtf8("ModificaUtente"))
        self.EliminaUtente = QtGui.QPushButton(self.centralWidget)
        self.EliminaUtente.setGeometry(QtCore.QRect(280, 170, 101, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.EliminaUtente.setFont(font)
        self.EliminaUtente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EliminaUtente.setObjectName(_fromUtf8("EliminaUtente"))
        GestioneUtenti.setCentralWidget(self.centralWidget)

        self.retranslateUi(GestioneUtenti)
        QtCore.QMetaObject.connectSlotsByName(GestioneUtenti)

    def retranslateUi(self, GestioneUtenti):
        GestioneUtenti.setWindowTitle(QtGui.QApplication.translate("GestioneUtenti", "GestioneUtenti", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GestioneUtenti", "Utenti", None, QtGui.QApplication.UnicodeUTF8))
        self.CreaUtente.setText(QtGui.QApplication.translate("GestioneUtenti", "Crea", None, QtGui.QApplication.UnicodeUTF8))
        self.ModificaUtente.setText(QtGui.QApplication.translate("GestioneUtenti", "Modifica", None, QtGui.QApplication.UnicodeUTF8))
        self.EliminaUtente.setText(QtGui.QApplication.translate("GestioneUtenti", "Elimina", None, QtGui.QApplication.UnicodeUTF8))

