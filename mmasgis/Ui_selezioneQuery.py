# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectionquerywindow.ui'
#
# Created: Tue May  8 10:47:10 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SelectionQueryWindow(object):
    def setupUi(self, SelectionQueryWindow):
        SelectionQueryWindow.setObjectName(_fromUtf8("SelectionQueryWindow"))
        SelectionQueryWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        SelectionQueryWindow.resize(500, 370)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SelectionQueryWindow.sizePolicy().hasHeightForWidth())
        SelectionQueryWindow.setSizePolicy(sizePolicy)
        SelectionQueryWindow.setMinimumSize(QtCore.QSize(500, 370))
        SelectionQueryWindow.setMaximumSize(QtCore.QSize(500, 370))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SelectionQueryWindow.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(SelectionQueryWindow)
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
"     }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tableQuery = QtGui.QTableWidget(self.centralWidget)
        self.tableQuery.setGeometry(QtCore.QRect(10, 70, 471, 281))
        self.tableQuery.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableQuery.setStyleSheet(_fromUtf8("QTableView {\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"    background-color: rgba(255, 255, 255,0);\n"
"    alternate-background-color:rgba(210, 233, 241,130);\n"
"    \n"
" }\n"
"QTableView::resizeColumnToContents{\n"
"}\n"
"\n"
" QHeaderView::section {\n"
"/* background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.00947867 rgba(220, 231, 240, 255), stop:1 rgba(239, 251, 254, 255));\n"
"     border: 0.5px groove rgb(188, 198, 207);\n"
"     height:30px;\n"
"    font: 11pt \"Arial\";\n"
" }\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"     background: rgb(255, 255, 255);\n"
"     border: 0px;\n"
" }\n"
"QTableWidget{\n"
"    gridline-color:  rgb(188, 198, 207);\n"
"}\n"
""))
        self.tableQuery.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableQuery.setDragDropOverwriteMode(False)
        self.tableQuery.setAlternatingRowColors(True)
        self.tableQuery.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableQuery.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableQuery.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableQuery.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tableQuery.setObjectName(_fromUtf8("tableQuery"))
        self.tableQuery.setColumnCount(2)
        self.tableQuery.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableQuery.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableQuery.setHorizontalHeaderItem(1, item)
        self.tableQuery.horizontalHeader().setDefaultSectionSize(230)
        self.tableQuery.horizontalHeader().setMinimumSectionSize(210)
        self.tableQuery.horizontalHeader().setStretchLastSection(True)
        self.Selezione = QtGui.QPushButton(self.centralWidget)
        self.Selezione.setGeometry(QtCore.QRect(430, 10, 50, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Selezione.sizePolicy().hasHeightForWidth())
        self.Selezione.setSizePolicy(sizePolicy)
        self.Selezione.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Selezione.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/icon_load_not_hov.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    image: url(:/resources/icon_load.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } \n"
""))
        self.Selezione.setText(_fromUtf8(""))
        self.Selezione.setObjectName(_fromUtf8("Selezione"))
        self.Eliminazione = QtGui.QPushButton(self.centralWidget)
        self.Eliminazione.setGeometry(QtCore.QRect(370, 10, 50, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Eliminazione.sizePolicy().hasHeightForWidth())
        self.Eliminazione.setSizePolicy(sizePolicy)
        self.Eliminazione.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Eliminazione.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/no_filter_not_hov.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    image: url(:/resources/no_filter.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } \n"
""))
        self.Eliminazione.setText(_fromUtf8(""))
        self.Eliminazione.setObjectName(_fromUtf8("Eliminazione"))
        SelectionQueryWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(SelectionQueryWindow)
        QtCore.QMetaObject.connectSlotsByName(SelectionQueryWindow)

    def retranslateUi(self, SelectionQueryWindow):
        SelectionQueryWindow.setWindowTitle(QtGui.QApplication.translate("SelectionQueryWindow", "Caricamento Query", None, QtGui.QApplication.UnicodeUTF8))
        self.tableQuery.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("SelectionQueryWindow", "Query", None, QtGui.QApplication.UnicodeUTF8))
        self.tableQuery.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("SelectionQueryWindow", "Descrizione", None, QtGui.QApplication.UnicodeUTF8))
        self.Selezione.setToolTip(QtGui.QApplication.translate("SelectionQueryWindow", "carica query", None, QtGui.QApplication.UnicodeUTF8))
        self.Eliminazione.setToolTip(QtGui.QApplication.translate("SelectionQueryWindow", "elimina query", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
