# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selezionegeo.ui'
#
# Created: Tue Apr 24 12:25:25 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelezioneGeo(object):
    def setupUi(self, SelezioneGeo):
        SelezioneGeo.setObjectName(_fromUtf8("SelezioneGeo"))
        SelezioneGeo.resize(230, 500)
        SelezioneGeo.setMinimumSize(QtCore.QSize(230, 500))
        SelezioneGeo.setMaximumSize(QtCore.QSize(230, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelezioneGeo.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(SelezioneGeo)
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
        self.plusNodes = QtGui.QPushButton(self.centralWidget)
        self.plusNodes.setGeometry(QtCore.QRect(10, 10, 31, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.plusNodes.setFont(font)
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
        self.selection_list = QtGui.QListWidget(self.centralWidget)
        self.selection_list.setGeometry(QtCore.QRect(10, 40, 211, 451))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.selection_list.setFont(font)
        self.selection_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selection_list.setStyleSheet(_fromUtf8("QListWidget{\n"
"border:2px groove rgb(188, 198, 207);  \n"
"}"))
        self.selection_list.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.selection_list.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.selection_list.setObjectName(_fromUtf8("selection_list"))
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
        SelezioneGeo.setCentralWidget(self.centralWidget)

        self.retranslateUi(SelezioneGeo)
        QtCore.QMetaObject.connectSlotsByName(SelezioneGeo)

    def retranslateUi(self, SelezioneGeo):
        SelezioneGeo.setWindowTitle(QtGui.QApplication.translate("SelezioneGeo", "Territori Selezionati", None, QtGui.QApplication.UnicodeUTF8))
        self.plusNodes.setToolTip(QtGui.QApplication.translate("SelezioneGeo", "esplodi nodi", None, QtGui.QApplication.UnicodeUTF8))
        self.minusNodes.setToolTip(QtGui.QApplication.translate("SelezioneGeo", "chiudi nodi", None, QtGui.QApplication.UnicodeUTF8))

#import stile_albero_rc
