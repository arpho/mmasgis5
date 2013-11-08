# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configurazione.ui'
#
# Created: Wed May  9 12:39:12 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Configurazione(object):
    def setupUi(self, Configurazione):
        Configurazione.setObjectName(_fromUtf8("Configurazione"))
        Configurazione.setWindowModality(QtCore.Qt.ApplicationModal)
        Configurazione.resize(500, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Configurazione.sizePolicy().hasHeightForWidth())
        Configurazione.setSizePolicy(sizePolicy)
        Configurazione.setMinimumSize(QtCore.QSize(500, 500))
        Configurazione.setMaximumSize(QtCore.QSize(500, 500))
        Configurazione.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Configurazione.setWindowIcon(icon)
        Configurazione.setStyleSheet(_fromUtf8("QMenu {\n"
"  background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
"    font: 11pt \"Arial\";\n"
"border: 1px outset rgb(188, 189, 207);\n"
"     border-radius: 1px;\n"
" }\n"
"\n"
" QMenu::item {\n"
"     /* sets background of menu item. set this to something non-transparent\n"
"         if you want menu color and menu item color to be different */\n"
"     background-color: transparent;\n"
"font: 11pt \"Arial\";\n"
" }\n"
"\n"
" QMenu::item:selected { /* when user selects item using mouse or keyboard */\n"
"     background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 226, 229, 255), stop:0.254545 rgba(247, 247, 247, 255), stop:0.722727 rgba(247, 247, 247, 255), stop:1 rgba(220, 226, 229, 255));\n"
"color:black;\n"
"    font: 11pt \"Arial\";\n"
" }"))
        self.centralWidget = QtGui.QWidget(Configurazione)
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
"QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
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
"QListWidget{    \n"
"border: 1px groove rgb(188, 198, 207);\n"
"}\n"
"\n"
"/*table style*/\n"
"QTableView {\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"    background-color: rgba(255, 255, 255,0);\n"
"    alternate-background-color:rgba(210, 233, 241,130);\n"
"    \n"
" }\n"
"\n"
" QHeaderView::section {\n"
"/* background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.00947867 rgba(220, 231, 240, 255), stop:1 rgba(239, 251, 254, 255));\n"
"     border: 0.5px groove rgb(188, 198, 207);\n"
"     height:20px;\n"
"    font: 11pt \"Arial\";\n"
" }\n"
"\n"
"QTableView QTableCornerButton::section {\n"
"     background: rgb(255, 255, 255);\n"
"     border: 0px;\n"
" }\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px groove rgb(188, 198, 207);\n"
" \n"
" }\n"
"\n"
"QSpinBox{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"}\n"
"\n"
"QLabel{   \n"
"    border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;\n"
"}\n"
"\n"
"/* set scrollbar style */\n"
"QScrollBar:horizontal {\n"
" border: 0px solid rgb(168, 172, 204);\n"
" border-radius:7px;\n"
"     background-color:rgba(255,255,255,0);\n"
"     height: 11px;\n"
"     margin: 1px 19px 0px 19px;\n"
" }\n"
"\n"
" QScrollBar::handle:horizontal {    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0272727 rgba(146, 179, 203, 255), stop:1 rgba(228, 240, 248, 255));\n"
"     min-width: 11px;\n"
"   border: 1px solid rgb(168, 172, 204);\n"
"   border-radius:5px;\n"
" }\n"
" QScrollBar::add-line:horizontal {\n"
"  background-color:rgba(255,255,255,0);\n"
"   width: 13px;\n"
"   height:13px;\n"
"     subcontrol-position: right;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
" QScrollBar::sub-line:horizontal {\n"
"  background-color:rgba(255,255,255,0);\n"
"     width: 13px;\n"
"    height:13px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
" }\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"     background-color:rgba(255,255,255,0);\n"
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
"QScrollBar:vertical {\n"
" border: 0px solid rgb(188, 189, 207);\n"
" border-radius:7px;\n"
"    background-color: rgba(255,255,255,0);\n"
"    width: 12px;\n"
"     margin: 19px 0px 19px 1px;\n"
" }\n"
"\n"
" QScrollBar::handle:vertical {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0272727 rgba(146, 179, 203, 255), stop:1 rgba(228, 240, 248, 255));\n"
"     min-height: 13px;\n"
"   border: 1px solid rgb(168, 172, 204);\n"
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
"    background-color:rgba(255,255,255,0);\n"
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
"\n"
"\n"
"\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.apply_conf = QtGui.QPushButton(self.centralWidget)
        self.apply_conf.setGeometry(QtCore.QRect(440, 10, 50, 50))
        self.apply_conf.setFocusPolicy(QtCore.Qt.NoFocus)
        self.apply_conf.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/filter_ok_not_hov.png);\n"
"\n"
"\n"
" }\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/resources/filter_ok.png);\n"
" } \n"
"\n"
"\n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
"\n"
" }\n"
""))
        self.apply_conf.setText(_fromUtf8(""))
        self.apply_conf.setObjectName(_fromUtf8("apply_conf"))
        self.formLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 30, 241, 31))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setMargin(0)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_num = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label_num.setFont(font)
        self.label_num.setObjectName(_fromUtf8("label_num"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_num)
        self.spin_num = QtGui.QSpinBox(self.formLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spin_num.sizePolicy().hasHeightForWidth())
        self.spin_num.setSizePolicy(sizePolicy)
        self.spin_num.setMinimumSize(QtCore.QSize(41, 25))
        self.spin_num.setMaximumSize(QtCore.QSize(41, 25))
        self.spin_num.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.spin_num.setProperty(_fromUtf8("value"), 1)
        self.spin_num.setObjectName(_fromUtf8("spin_num"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spin_num)
        self.table_disp = QtGui.QListWidget(self.centralWidget)
        self.table_disp.setGeometry(QtCore.QRect(10, 90, 241, 401))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_disp.setFont(font)
        self.table_disp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_disp.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_disp.setStyleSheet(_fromUtf8(""))
        self.table_disp.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_disp.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_disp.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_disp.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.table_disp.setObjectName(_fromUtf8("table_disp"))
        self.table_sel = QtGui.QListWidget(self.centralWidget)
        self.table_sel.setGeometry(QtCore.QRect(260, 90, 231, 401))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_sel.setFont(font)
        self.table_sel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_sel.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.table_sel.setStyleSheet(_fromUtf8(""))
        self.table_sel.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_sel.setDragDropMode(QtGui.QAbstractItemView.InternalMove)
        self.table_sel.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.table_sel.setObjectName(_fromUtf8("table_sel"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 241, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(260, 70, 231, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        Configurazione.setCentralWidget(self.centralWidget)

        self.retranslateUi(Configurazione)
        QtCore.QMetaObject.connectSlotsByName(Configurazione)

    def retranslateUi(self, Configurazione):
        Configurazione.setWindowTitle(QtGui.QApplication.translate("Configurazione", "Configurazione", None, QtGui.QApplication.UnicodeUTF8))
        self.apply_conf.setToolTip(QtGui.QApplication.translate("Configurazione", "applica configurazione", None, QtGui.QApplication.UnicodeUTF8))
        self.label_num.setText(QtGui.QApplication.translate("Configurazione", "Num. di elementi per classe", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Configurazione", "CLASSI MARCHE DISPONIBILI", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Configurazione", "CLASSI MARCHE SELEZIONATE", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
