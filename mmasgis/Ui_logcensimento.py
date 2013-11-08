# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logcensimento.ui'
#
# Created: Thu Jun 14 16:30:26 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LogCensimento(object):
    def setupUi(self, LogCensimento):
        LogCensimento.setObjectName(_fromUtf8("LogCensimento"))
        LogCensimento.setWindowModality(QtCore.Qt.ApplicationModal)
        LogCensimento.resize(300, 290)
        LogCensimento.setMinimumSize(QtCore.QSize(300, 290))
        LogCensimento.setMaximumSize(QtCore.QSize(300, 290))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogCensimento.setWindowIcon(icon)
        LogCensimento.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(LogCensimento)
        self.centralWidget.setStyleSheet(_fromUtf8("/* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
"\n"
"QListWidget{\n"
"border: 1px groove rgb(188, 198, 207);\n"
"}\n"
"\n"
"QLabel{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px outset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}\n"
"QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
" }\n"
"\n"
"QTextEdit{\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
"}\n"
"\n"
"QListWidget{\n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
"border: 1px groove rgb(188, 198, 207);\n"
"border-radius:3px;\n"
"}\n"
"\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(13, 10, 271, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.OKButton = QtGui.QPushButton(self.centralWidget)
        self.OKButton.setGeometry(QtCore.QRect(210, 250, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.OKButton.setFont(font)
        self.OKButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OKButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
"     border: 2px outset  rgb(188, 198, 207);\n"
"     border-radius: 5px;\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"   \n"
" }\n"
"\n"
" QPushButton:pressed {\n"
"    border: 2px inset  rgb(188, 198, 207);\n"
"     \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 226, 229, 255), stop:0.254545 rgba(247, 247, 247, 255), stop:0.722727 rgba(247, 247, 247, 255), stop:1 rgba(220, 226, 229, 255));\n"
" }\n"
""))
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        self.listCensimenti = QtGui.QListWidget(self.centralWidget)
        self.listCensimenti.setGeometry(QtCore.QRect(13, 30, 271, 141))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.listCensimenti.setFont(font)
        self.listCensimenti.setFocusPolicy(QtCore.Qt.NoFocus)
        self.listCensimenti.setStyleSheet(_fromUtf8(""))
        self.listCensimenti.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listCensimenti.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.listCensimenti.setObjectName(_fromUtf8("listCensimenti"))
        self.check_certMMAS = QtGui.QCheckBox(self.centralWidget)
        self.check_certMMAS.setGeometry(QtCore.QRect(10, 175, 201, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.check_certMMAS.setFont(font)
        self.check_certMMAS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_certMMAS.setObjectName(_fromUtf8("check_certMMAS"))
        self.check_nonMMAS = QtGui.QCheckBox(self.centralWidget)
        self.check_nonMMAS.setGeometry(QtCore.QRect(10, 200, 221, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.check_nonMMAS.setFont(font)
        self.check_nonMMAS.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_nonMMAS.setObjectName(_fromUtf8("check_nonMMAS"))
        self.check_nonCert = QtGui.QCheckBox(self.centralWidget)
        self.check_nonCert.setGeometry(QtCore.QRect(10, 225, 191, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.check_nonCert.setFont(font)
        self.check_nonCert.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_nonCert.setObjectName(_fromUtf8("check_nonCert"))
        LogCensimento.setCentralWidget(self.centralWidget)

        self.retranslateUi(LogCensimento)
        QtCore.QMetaObject.connectSlotsByName(LogCensimento)

    def retranslateUi(self, LogCensimento):
        LogCensimento.setWindowTitle(QtGui.QApplication.translate("LogCensimento", "Scelta Censimento", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LogCensimento", "Censimento", None, QtGui.QApplication.UnicodeUTF8))
        self.OKButton.setText(QtGui.QApplication.translate("LogCensimento", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.check_certMMAS.setText(QtGui.QApplication.translate("LogCensimento", "Certificate MMASGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.check_nonMMAS.setText(QtGui.QApplication.translate("LogCensimento", "Non Certificate MMASGIS", None, QtGui.QApplication.UnicodeUTF8))
        self.check_nonCert.setText(QtGui.QApplication.translate("LogCensimento", "Altre non certificate", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
