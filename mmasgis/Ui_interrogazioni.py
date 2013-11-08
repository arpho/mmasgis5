# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interrogazioni.ui'
#
# Created: Tue May  8 15:06:04 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowInterrogazioni(object):
    def setupUi(self, MainWindowInterrogazioni):
        MainWindowInterrogazioni.setObjectName(_fromUtf8("MainWindowInterrogazioni"))
        MainWindowInterrogazioni.resize(800, 555)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowInterrogazioni.sizePolicy().hasHeightForWidth())
        MainWindowInterrogazioni.setSizePolicy(sizePolicy)
        MainWindowInterrogazioni.setMinimumSize(QtCore.QSize(800, 555))
        MainWindowInterrogazioni.setMaximumSize(QtCore.QSize(800, 555))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        MainWindowInterrogazioni.setFont(font)
        MainWindowInterrogazioni.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowInterrogazioni.setWindowIcon(icon)
        MainWindowInterrogazioni.setStyleSheet(_fromUtf8(" QMenu {\n"
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
" }\n"
"\n"
"\n"
""))
        self.centralWidget = QtGui.QWidget(MainWindowInterrogazioni)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 555))
        self.centralWidget.setStyleSheet(_fromUtf8(" /* sets background color  */\n"
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
"QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"/* set scrollbar style */\n"
"QScrollBar:horizontal {\n"
" border: 0px solid rgb(168, 172, 204);\n"
" border-radius:7px;\n"
"     background-color:rgba(255,255,255,0);\n"
"     height: 11px;\n"
"     margin: 0px 19px 0px 19px;\n"
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
"\n"
"QScrollBar:vertical {\n"
" border: 0px solid rgb(188, 189, 207);\n"
" border-radius:7px;\n"
"    background-color: rgba(255,255,255,0);\n"
"    width: 13px;\n"
"     margin: 19px 0px 19px 0px;\n"
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
"\n"
"/* checkbox style*/\n"
"\n"
"QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
"\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"\n"
"    image: url(:/resources/checkbox_off_en.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked {\n"
"\n"
"    image: url(:/resources/checkbox_on_enabled.png);\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked:!enabled {\n"
"\n"
"    image: url(:/resources/checkbox_off_dis.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:!enabled {\n"
"\n"
"    image: url(:/resources/checkbox_on_disabled.png);\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"\n"
"    image: url(:/resources/checkbox_off_enabled_hover.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"\n"
"    image: url(:/resources/checkbox_on_enabled_hover.png);\n"
" }\n"
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 30, 781, 521))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet(_fromUtf8("QTableView {\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"    background-color: rgb(255, 255, 255);\n"
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
" QTabWidget::tab-bar {\n"
"     left: 5px; /* move to the right by 5px */\n"
" }\n"
"\n"
" /* Style the tab using the tab sub-control. Note that\n"
"     it reads QTabBar _not_ QTabWidget */\n"
" QTabBar::tab {\n"
"     \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(199, 209, 217, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(118, 212, 230, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"     border: 2px groove rgb(188, 198, 207);\n"
"    border-bottom:0.5px;\n"
"     border-bottom-color: rgb(188, 198, 207); /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     width: 119px;\n"
"    height:29px;\n"
"     padding: 3px;\n"
" }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
" }\n"
"\n"
" QTabBar::tab:selected {\n"
"     border-color: rgb(188, 198, 207);\n"
"     border-bottom-color: rgb(188, 198, 207); /* same as pane color */\n"
" }\n"
"\n"
" QTabBar::tab:!selected {\n"
"     margin-top: 1px; /* make non-selected tabs look smaller */\n"
" }"))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_parametri = QtGui.QWidget()
        self.tab_parametri.setObjectName(_fromUtf8("tab_parametri"))
        self.label_4 = QtGui.QLabel(self.tab_parametri)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 231, 19))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.attributeList_parametri = QtGui.QTreeWidget(self.tab_parametri)
        self.attributeList_parametri.setGeometry(QtCore.QRect(10, 30, 231, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.attributeList_parametri.setFont(font)
        self.attributeList_parametri.setFocusPolicy(QtCore.Qt.NoFocus)
        self.attributeList_parametri.setStyleSheet(_fromUtf8(""))
        self.attributeList_parametri.setMidLineWidth(1)
        self.attributeList_parametri.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.attributeList_parametri.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.attributeList_parametri.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.attributeList_parametri.setIndentation(0)
        self.attributeList_parametri.setObjectName(_fromUtf8("attributeList_parametri"))
        self.attributeList_parametri.header().setVisible(False)
        self.attributeList_parametri.header().setCascadingSectionResizes(False)
        self.attributeList_parametri.header().setDefaultSectionSize(310)
        self.attributeList_parametri.header().setMinimumSectionSize(300)
        self.attributeList_parametri.header().setStretchLastSection(False)
        self.label_5 = QtGui.QLabel(self.tab_parametri)
        self.label_5.setGeometry(QtCore.QRect(250, 10, 256, 19))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.availableValueList_parametri = QtGui.QListWidget(self.tab_parametri)
        self.availableValueList_parametri.setGeometry(QtCore.QRect(250, 30, 256, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.availableValueList_parametri.setFont(font)
        self.availableValueList_parametri.setFocusPolicy(QtCore.Qt.NoFocus)
        self.availableValueList_parametri.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.availableValueList_parametri.setStyleSheet(_fromUtf8("border: 1px groove rgb(188, 198, 207);"))
        self.availableValueList_parametri.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.availableValueList_parametri.setObjectName(_fromUtf8("availableValueList_parametri"))
        self.label_6 = QtGui.QLabel(self.tab_parametri)
        self.label_6.setGeometry(QtCore.QRect(520, 10, 256, 19))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.selectedValueList_parametri = QtGui.QListWidget(self.tab_parametri)
        self.selectedValueList_parametri.setGeometry(QtCore.QRect(520, 30, 256, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.selectedValueList_parametri.setFont(font)
        self.selectedValueList_parametri.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectedValueList_parametri.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.selectedValueList_parametri.setStyleSheet(_fromUtf8("border: 1px groove rgb(188, 198, 207);"))
        self.selectedValueList_parametri.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.selectedValueList_parametri.setObjectName(_fromUtf8("selectedValueList_parametri"))
        self.tabWidget.addTab(self.tab_parametri, _fromUtf8(""))
        self.tab_marchi = QtGui.QWidget()
        self.tab_marchi.setObjectName(_fromUtf8("tab_marchi"))
        self.attributesList_marchi = QtGui.QTreeWidget(self.tab_marchi)
        self.attributesList_marchi.setGeometry(QtCore.QRect(10, 30, 231, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.attributesList_marchi.setFont(font)
        self.attributesList_marchi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.attributesList_marchi.setStyleSheet(_fromUtf8(""))
        self.attributesList_marchi.setMidLineWidth(1)
        self.attributesList_marchi.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.attributesList_marchi.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.attributesList_marchi.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.attributesList_marchi.setIndentation(0)
        self.attributesList_marchi.setRootIsDecorated(True)
        self.attributesList_marchi.setObjectName(_fromUtf8("attributesList_marchi"))
        self.attributesList_marchi.header().setVisible(False)
        self.attributesList_marchi.header().setCascadingSectionResizes(False)
        self.attributesList_marchi.header().setDefaultSectionSize(310)
        self.attributesList_marchi.header().setMinimumSectionSize(310)
        self.availableValueList_marchi = QtGui.QListWidget(self.tab_marchi)
        self.availableValueList_marchi.setGeometry(QtCore.QRect(250, 30, 256, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setItalic(False)
        self.availableValueList_marchi.setFont(font)
        self.availableValueList_marchi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.availableValueList_marchi.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.availableValueList_marchi.setStyleSheet(_fromUtf8("border: 1px groove rgb(188, 198, 207);"))
        self.availableValueList_marchi.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.availableValueList_marchi.setObjectName(_fromUtf8("availableValueList_marchi"))
        self.selectedValueList_marchi = QtGui.QListWidget(self.tab_marchi)
        self.selectedValueList_marchi.setGeometry(QtCore.QRect(520, 30, 256, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setItalic(False)
        self.selectedValueList_marchi.setFont(font)
        self.selectedValueList_marchi.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectedValueList_marchi.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.selectedValueList_marchi.setStyleSheet(_fromUtf8("border: 1px groove rgb(188, 198, 207);"))
        self.selectedValueList_marchi.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.selectedValueList_marchi.setObjectName(_fromUtf8("selectedValueList_marchi"))
        self.label = QtGui.QLabel(self.tab_marchi)
        self.label.setGeometry(QtCore.QRect(10, 10, 231, 19))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab_marchi)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 256, 19))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab_marchi)
        self.label_3.setGeometry(QtCore.QRect(520, 10, 256, 19))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab_marchi, _fromUtf8(""))
        self.tab_potenziali = QtGui.QWidget()
        self.tab_potenziali.setObjectName(_fromUtf8("tab_potenziali"))
        self.label_7 = QtGui.QLabel(self.tab_potenziali)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 231, 19))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tab_potenziali)
        self.label_8.setGeometry(QtCore.QRect(250, 10, 256, 19))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.attributeList_potenziali = QtGui.QTreeWidget(self.tab_potenziali)
        self.attributeList_potenziali.setGeometry(QtCore.QRect(10, 30, 231, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.attributeList_potenziali.setFont(font)
        self.attributeList_potenziali.setFocusPolicy(QtCore.Qt.NoFocus)
        self.attributeList_potenziali.setAutoFillBackground(False)
        self.attributeList_potenziali.setStyleSheet(_fromUtf8(""))
        self.attributeList_potenziali.setFrameShape(QtGui.QFrame.StyledPanel)
        self.attributeList_potenziali.setFrameShadow(QtGui.QFrame.Sunken)
        self.attributeList_potenziali.setMidLineWidth(1)
        self.attributeList_potenziali.setIndentation(0)
        self.attributeList_potenziali.setObjectName(_fromUtf8("attributeList_potenziali"))
        self.attributeList_potenziali.header().setVisible(False)
        self.attributeList_potenziali.header().setDefaultSectionSize(300)
        self.attributeList_potenziali.header().setMinimumSectionSize(50)
        self.availableValueList_potenziali = QtGui.QListWidget(self.tab_potenziali)
        self.availableValueList_potenziali.setGeometry(QtCore.QRect(250, 30, 256, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.availableValueList_potenziali.setFont(font)
        self.availableValueList_potenziali.setFocusPolicy(QtCore.Qt.NoFocus)
        self.availableValueList_potenziali.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.availableValueList_potenziali.setStyleSheet(_fromUtf8("border: 1px groove rgb(188, 198, 207);"))
        self.availableValueList_potenziali.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.availableValueList_potenziali.setObjectName(_fromUtf8("availableValueList_potenziali"))
        self.selectedValueList_potenziali = QtGui.QListWidget(self.tab_potenziali)
        self.selectedValueList_potenziali.setGeometry(QtCore.QRect(520, 30, 256, 441))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.selectedValueList_potenziali.setFont(font)
        self.selectedValueList_potenziali.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectedValueList_potenziali.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.selectedValueList_potenziali.setStyleSheet(_fromUtf8("border: 1px groove rgb(188, 198, 207);"))
        self.selectedValueList_potenziali.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.selectedValueList_potenziali.setObjectName(_fromUtf8("selectedValueList_potenziali"))
        self.label_9 = QtGui.QLabel(self.tab_potenziali)
        self.label_9.setGeometry(QtCore.QRect(520, 10, 256, 19))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.tab_potenziali, _fromUtf8(""))
        self.resetButton = QtGui.QPushButton(self.centralWidget)
        self.resetButton.setGeometry(QtCore.QRect(680, 10, 50, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy)
        self.resetButton.setMinimumSize(QtCore.QSize(50, 50))
        self.resetButton.setMaximumSize(QtCore.QSize(50, 50))
        self.resetButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resetButton.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    image: url(:/resources/refresh_filter.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    image: url(:/resources/refresh.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } \n"
""))
        self.resetButton.setText(_fromUtf8(""))
        self.resetButton.setIconSize(QtCore.QSize(45, 45))
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.applyButton = QtGui.QPushButton(self.centralWidget)
        self.applyButton.setGeometry(QtCore.QRect(740, 10, 50, 50))
        self.applyButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        self.applyButton.setFont(font)
        self.applyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.applyButton.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
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
        self.applyButton.setText(_fromUtf8(""))
        self.applyButton.setIconSize(QtCore.QSize(45, 45))
        self.applyButton.setObjectName(_fromUtf8("applyButton"))
        self.saveButton = QtGui.QPushButton(self.centralWidget)
        self.saveButton.setGeometry(QtCore.QRect(620, 10, 50, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setMinimumSize(QtCore.QSize(50, 50))
        self.saveButton.setMaximumSize(QtCore.QSize(50, 50))
        self.saveButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.saveButton.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
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
        self.saveButton.setText(_fromUtf8(""))
        self.saveButton.setIconSize(QtCore.QSize(40, 40))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.loadButton = QtGui.QPushButton(self.centralWidget)
        self.loadButton.setGeometry(QtCore.QRect(560, 10, 50, 50))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadButton.sizePolicy().hasHeightForWidth())
        self.loadButton.setSizePolicy(sizePolicy)
        self.loadButton.setMinimumSize(QtCore.QSize(50, 50))
        self.loadButton.setMaximumSize(QtCore.QSize(50, 50))
        self.loadButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.loadButton.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/open_folder.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    image: url(:/resources/open_folder_hov.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } \n"
""))
        self.loadButton.setText(_fromUtf8(""))
        self.loadButton.setIconSize(QtCore.QSize(45, 45))
        self.loadButton.setObjectName(_fromUtf8("loadButton"))
        MainWindowInterrogazioni.setCentralWidget(self.centralWidget)
        self.actionProva = QtGui.QAction(MainWindowInterrogazioni)
        self.actionProva.setObjectName(_fromUtf8("actionProva"))
        self.actionProva_2 = QtGui.QAction(MainWindowInterrogazioni)
        self.actionProva_2.setObjectName(_fromUtf8("actionProva_2"))
        self.actionProva_3 = QtGui.QAction(MainWindowInterrogazioni)
        self.actionProva_3.setObjectName(_fromUtf8("actionProva_3"))
        self.actionProva_4 = QtGui.QAction(MainWindowInterrogazioni)
        self.actionProva_4.setObjectName(_fromUtf8("actionProva_4"))

        self.retranslateUi(MainWindowInterrogazioni)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowInterrogazioni)

    def retranslateUi(self, MainWindowInterrogazioni):
        MainWindowInterrogazioni.setWindowTitle(QtGui.QApplication.translate("MainWindowInterrogazioni", "Filtri", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "filtra per", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "valori", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "selezionati", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_parametri), QtGui.QApplication.translate("MainWindowInterrogazioni", "PARAMETRI", None, QtGui.QApplication.UnicodeUTF8))
        self.attributesList_marchi.headerItem().setText(0, QtGui.QApplication.translate("MainWindowInterrogazioni", "select", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "filtra per", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "valori", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "selezionati", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_marchi), QtGui.QApplication.translate("MainWindowInterrogazioni", "MARCHE", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "filtra per", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "valori", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "selezionati", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_potenziali), QtGui.QApplication.translate("MainWindowInterrogazioni", "POTENZIALI", None, QtGui.QApplication.UnicodeUTF8))
        self.resetButton.setToolTip(QtGui.QApplication.translate("MainWindowInterrogazioni", "refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.applyButton.setToolTip(QtGui.QApplication.translate("MainWindowInterrogazioni", "applica filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setToolTip(QtGui.QApplication.translate("MainWindowInterrogazioni", "salva query", None, QtGui.QApplication.UnicodeUTF8))
        self.loadButton.setToolTip(QtGui.QApplication.translate("MainWindowInterrogazioni", "carica query", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProva.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "Prova", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProva_2.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "Prova", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProva_3.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "Prova", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProva_4.setText(QtGui.QApplication.translate("MainWindowInterrogazioni", "Prova", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
