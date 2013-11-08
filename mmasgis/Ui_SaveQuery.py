# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'savequerywindow.ui'
#
# Created: Tue May  8 10:48:00 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SaveQueryWindow(object):
    def setupUi(self, SaveQueryWindow):
        SaveQueryWindow.setObjectName(_fromUtf8("SaveQueryWindow"))
        SaveQueryWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        SaveQueryWindow.resize(550, 230)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SaveQueryWindow.sizePolicy().hasHeightForWidth())
        SaveQueryWindow.setSizePolicy(sizePolicy)
        SaveQueryWindow.setMinimumSize(QtCore.QSize(550, 230))
        SaveQueryWindow.setMaximumSize(QtCore.QSize(550, 230))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SaveQueryWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(SaveQueryWindow)
        self.centralWidget.setStyleSheet(_fromUtf8("QWidget {\n"
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
"/* set scrollbar style */\n"
"QScrollBar:horizontal {\n"
" border: 1px solid rgb(188, 189, 207);\n"
" border-radius:7px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"     height: 15px;\n"
"     margin: 0px 19px 0px 19px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(140, 159, 171, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     min-width: 13px;\n"
"   border: 2px groove rgb(188, 189, 207);\n"
"   border-radius:5px;\n"
" }\n"
" QScrollBar::add-line:horizontal {\n"
" /*border:2px groove rgb(188, 198, 207);  \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 7px;*/\n"
"  background-color:rgba(255,255,255,0);\n"
"   width: 13px;\n"
"   height:13px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"   /*border:2px groove rgb(188, 198, 207);  \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 7px;*/\n"
"  background-color:rgba(255,255,255,0);\n"
"     width: 13px;\n"
"    height:13px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.00947867 rgba(232, 237, 240, 255), stop:1 rgba(239, 251, 254, 255));\n"
" }\n"
"\n"
"  QScrollBar:left-arrow:horizontal{\n"
"    image: url(:/resources/back_not_hov.png);\n"
"   width:13px;\n"
"   height:13px;\n"
"     }\n"
"   QScrollBar:left-arrow:horizontal:hover{\n"
"    image: url(:/resources/back_not_hov.png);\n"
"   width:15px;\n"
"   height:15px;\n"
"     }\n"
"  QScrollBar:left-arrow:horizontal:pressed{\n"
"    image: url(:/resources/back_not_hov.png);\n"
"   width:11px;\n"
"   height:11px;\n"
"     }\n"
" QScrollBar:right-arrow:horizontal{\n"
"    image: url(:/resources/next_not_hov.png);\n"
"   width:13px;\n"
"   height:13px;\n"
"     }\n"
"  QScrollBar:right-arrow:horizontal:hover{\n"
"    image: url(:/resources/next_not_hov.png);\n"
"   width:15px;\n"
"   height:15px;\n"
"     }\n"
"  QScrollBar:right-arrow:horizontal:pressed{\n"
"    image: url(:/resources/next_not_hov.png);\n"
"   width:11px;\n"
"   height:11px;\n"
"     }\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QScrollBar:vertical {\n"
" border: 1px solid rgb(188, 189, 207);\n"
" border-radius:7px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"    width: 15px;\n"
"     margin: 19px 0px 19px 0px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(140, 159, 171, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     min-height: 13px;\n"
"   border: 2px groove rgb(188, 189, 207);\n"
"   border-radius:5px;\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
" background-color:rgba(255,255,255,0);\n"
"   width: 13px;\n"
"   height:13px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:vertical {\n"
"     background-color:rgba(255,255,255,0);\n"
"     width: 13px;\n"
"    height:13px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.00947867 rgba(232, 237, 240, 255), stop:1 rgba(239, 251, 254, 255));\n"
" }\n"
"\n"
"  QScrollBar:up-arrow:vertical{\n"
"    image: url(:/resources/up_arrow.png);\n"
"   width:13px;\n"
"   height:13px;\n"
"     }\n"
"  QScrollBar:up-arrow:vertical:hover{\n"
"    image: url(:/resources/up_arrow.png);\n"
"   width:15px;\n"
"   height:15px;\n"
"     }\n"
"  QScrollBar:up-arrow:vertical:pressed{\n"
"    image: url(:/resources/up_arrow.png);\n"
"   width:11px;\n"
"   height:11px;\n"
"     }\n"
" QScrollBar:down-arrow:vertical{\n"
"    image: url(:/resources/down_arrow.png);\n"
"   width:13px;\n"
"   height:13px;\n"
"     }\n"
" QScrollBar:down-arrow:vertical:hover{\n"
"    image: url(:/resources/down_arrow.png);\n"
"   width:15px;\n"
"   height:15px;\n"
"     }\n"
" QScrollBar:down-arrow:vertical:pressed{\n"
"    image: url(:/resources/down_arrow.png);\n"
"   width:11px;\n"
"   height:11px;\n"
"     }\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.Salva = QtGui.QPushButton(self.centralWidget)
        self.Salva.setGeometry(QtCore.QRect(490, 10, 50, 50))
        self.Salva.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Salva.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/icon_save_not_hov.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/resources/icon_save.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } \n"
""))
        self.Salva.setText(_fromUtf8(""))
        self.Salva.setObjectName(_fromUtf8("Salva"))
        self.NomeQuery = QtGui.QLineEdit(self.centralWidget)
        self.NomeQuery.setGeometry(QtCore.QRect(160, 70, 371, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.NomeQuery.setFont(font)
        self.NomeQuery.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
"     font: 11pt \"Arial\";\n"
"\n"
" }"))
        self.NomeQuery.setMaxLength(44)
        self.NomeQuery.setObjectName(_fromUtf8("NomeQuery"))
        self.DescrizioneQuery = QtGui.QTextEdit(self.centralWidget)
        self.DescrizioneQuery.setGeometry(QtCore.QRect(160, 100, 371, 121))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DescrizioneQuery.sizePolicy().hasHeightForWidth())
        self.DescrizioneQuery.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.DescrizioneQuery.setFont(font)
        self.DescrizioneQuery.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255,0);\n"
" border:2px groove rgb(188, 198, 207);   "))
        self.DescrizioneQuery.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DescrizioneQuery.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.DescrizioneQuery.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.DescrizioneQuery.setLineWrapColumnOrWidth(0)
        self.DescrizioneQuery.setObjectName(_fromUtf8("DescrizioneQuery"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setWeight(50)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        SaveQueryWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SaveQueryWindow)
        QtCore.QMetaObject.connectSlotsByName(SaveQueryWindow)

    def retranslateUi(self, SaveQueryWindow):
        SaveQueryWindow.setWindowTitle(QtGui.QApplication.translate("SaveQueryWindow", "Salvataggio Query", None, QtGui.QApplication.UnicodeUTF8))
        self.Salva.setToolTip(QtGui.QApplication.translate("SaveQueryWindow", "salva query", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SaveQueryWindow", "Nome Query", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SaveQueryWindow", "Descrizione", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
