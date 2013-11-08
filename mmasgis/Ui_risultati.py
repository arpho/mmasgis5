# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'risultati.ui'
#
# Created: Tue Jun 12 09:35:03 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowResults(object):
    def setupUi(self, MainWindowResults):
        MainWindowResults.setObjectName(_fromUtf8("MainWindowResults"))
        MainWindowResults.setWindowModality(QtCore.Qt.NonModal)
        MainWindowResults.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowResults.sizePolicy().hasHeightForWidth())
        MainWindowResults.setSizePolicy(sizePolicy)
        MainWindowResults.setMinimumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        MainWindowResults.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowResults.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(MainWindowResults)
        self.centralWidget.setStyleSheet(_fromUtf8(" /* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"\n"
"QWidget#centralWidget{\n"
"    /*background-color: qlineargradient(spread:reflect, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(217, 239, 255, 255), stop:0.5 rgba(239, 248, 255, 255), stop:1 rgba(210, 236, 255, 255));\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(223, 246, 255, 255), stop:0.481132 rgba(243, 243, 243, 255), stop:0.995261 rgba(223, 246, 255, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
"\n"
"/* set scrollbar style */\n"
"QScrollBar:horizontal {\n"
" border: 0px solid rgb(168, 172, 204);\n"
" border-radius:7px;\n"
"     background-color:rgba(255,255,255,0);\n"
"     height: 13px;\n"
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
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabella = QtGui.QTableWidget(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabella.sizePolicy().hasHeightForWidth())
        self.tabella.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        font.setStrikeOut(False)
        self.tabella.setFont(font)
        self.tabella.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabella.setStyleSheet(_fromUtf8("\n"
" QTableView {\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"    background-color: rgba(255, 255, 255,0);\n"
"    alternate-background-color:rgba(210, 233, 241,130);\n"
"    selection-color: rgb(59, 66, 90);\n"
"    selection-background-color: rgb(118, 126, 175);\n"
" \n"
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
"QTableWidgetItem{\n"
"    text-align:center;\n"
"}\n"
"\n"
"\n"
""))
        self.tabella.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tabella.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabella.setTabKeyNavigation(True)
        self.tabella.setDragDropOverwriteMode(False)
        self.tabella.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.tabella.setAlternatingRowColors(True)
        self.tabella.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabella.setTextElideMode(QtCore.Qt.ElideRight)
        self.tabella.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tabella.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.tabella.setObjectName(_fromUtf8("tabella"))
        self.tabella.setColumnCount(9)
        self.tabella.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.tabella.setHorizontalHeaderItem(8, item)
        self.tabella.horizontalHeader().setCascadingSectionResizes(False)
        self.tabella.horizontalHeader().setDefaultSectionSize(200)
        self.tabella.horizontalHeader().setHighlightSections(False)
        self.tabella.horizontalHeader().setMinimumSectionSize(80)
        self.tabella.horizontalHeader().setStretchLastSection(True)
        self.tabella.verticalHeader().setCascadingSectionResizes(False)
        self.tabella.verticalHeader().setDefaultSectionSize(45)
        self.tabella.verticalHeader().setMinimumSectionSize(45)
        self.gridLayout.addWidget(self.tabella, 1, 0, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 23))
        self.label.setMaximumSize(QtCore.QSize(16777215, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.text_numero_risultati = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_numero_risultati.sizePolicy().hasHeightForWidth())
        self.text_numero_risultati.setSizePolicy(sizePolicy)
        self.text_numero_risultati.setMinimumSize(QtCore.QSize(91, 23))
        self.text_numero_risultati.setMaximumSize(QtCore.QSize(91, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.text_numero_risultati.setFont(font)
        self.text_numero_risultati.setCursor(QtCore.Qt.ArrowCursor)
        self.text_numero_risultati.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_numero_risultati.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border:2px groove rgb(188,198,207);   \n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(219, 230, 239, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     font: 11pt \"Arial\";\n"
"\n"
" }"))
        self.text_numero_risultati.setMaxLength(200)
        self.text_numero_risultati.setEchoMode(QtGui.QLineEdit.Normal)
        self.text_numero_risultati.setAlignment(QtCore.Qt.AlignCenter)
        self.text_numero_risultati.setObjectName(_fromUtf8("text_numero_risultati"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_numero_risultati)
        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)
        MainWindowResults.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindowResults)
        self.mainToolBar.setMinimumSize(QtCore.QSize(0, 24))
        self.mainToolBar.setMaximumSize(QtCore.QSize(16777215, 27))
        self.mainToolBar.setStyleSheet(_fromUtf8("QToolBar{\n"
"    background-color: rgb(255,255,255);\n"
"    spacing:5px;\n"
"  border: 0.5px inset white;\n"
"}\n"
"\n"
"QToolButton {\n"
"    border:2px groove rgba(255,255,255,0);\n"
"     border-radius: 11px;\n"
"     background-color: rgba(255,255,255,0);\n"
"\n"
" }\n"
"\n"
"QToolButton:hover{\n"
"    border: 1px outset rgb(255, 255, 255);\n"
"}\n"
"\n"
" QToolButton:pressed {\n"
"  /*border: 2px inset rgb(189, 206, 211);*/\n"
"    border:1.5px inset rgb(212, 215, 240);\n"
"    \n"
" }\n"
"\n"
" QToolTip {\n"
"     border: 1px solid rgb(188, 189, 207);\n"
"     padding: 0.1px;\n"
"    border-radius:1px;\n"
"    color: rgb(188, 189, 207);\n"
"    background-color: rgb(255, 255, 255);\n"
"   background-origin:padding-box;\n"
"     opacity: 100;\n"
" }"))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindowResults.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.firstButton = QtGui.QAction(MainWindowResults)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/firs_not_hovt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/first.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/first.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.firstButton.setIcon(icon1)
        self.firstButton.setAutoRepeat(False)
        self.firstButton.setObjectName(_fromUtf8("firstButton"))
        self.previousButton = QtGui.QAction(MainWindowResults)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/back_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/back.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/back.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon2)
        self.previousButton.setAutoRepeat(False)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.nextButton = QtGui.QAction(MainWindowResults)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon3)
        self.nextButton.setAutoRepeat(False)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.lastButton = QtGui.QAction(MainWindowResults)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/last_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/last.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/last.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.lastButton.setIcon(icon4)
        self.lastButton.setAutoRepeat(False)
        self.lastButton.setObjectName(_fromUtf8("lastButton"))
        self.newButton = QtGui.QAction(MainWindowResults)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/new_doc_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/new_doc.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/new_doc.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.newButton.setIcon(icon5)
        self.newButton.setAutoRepeat(False)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.modifyButton = QtGui.QAction(MainWindowResults)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/mod_doc_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/mod_doc.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/mod_doc.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.modifyButton.setIcon(icon6)
        self.modifyButton.setAutoRepeat(False)
        self.modifyButton.setMenuRole(QtGui.QAction.NoRole)
        self.modifyButton.setObjectName(_fromUtf8("modifyButton"))
        self.printButton = QtGui.QAction(MainWindowResults)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_print_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/print.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/print.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.printButton.setIcon(icon7)
        self.printButton.setAutoRepeat(False)
        self.printButton.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.printButton.setObjectName(_fromUtf8("printButton"))
        self.filter = QtGui.QAction(MainWindowResults)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/data_filter-icon_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/filter.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/filter.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.filter.setIcon(icon8)
        self.filter.setAutoRepeat(False)
        self.filter.setObjectName(_fromUtf8("filter"))
        self.eraseButton = QtGui.QAction(MainWindowResults)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/eraser_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/eraser.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/eraser.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.eraseButton.setIcon(icon9)
        self.eraseButton.setAutoRepeat(False)
        self.eraseButton.setObjectName(_fromUtf8("eraseButton"))
        self.findButton = QtGui.QAction(MainWindowResults)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/find_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/find.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/find.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.findButton.setIcon(icon10)
        self.findButton.setAutoRepeat(False)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.openselButton = QtGui.QAction(MainWindowResults)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/open_select_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/open_sel.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/open_sel.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.openselButton.setIcon(icon11)
        self.openselButton.setAutoRepeat(False)
        self.openselButton.setObjectName(_fromUtf8("openselButton"))
        self.cartButton = QtGui.QAction(MainWindowResults)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/ita_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/italia.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/italia.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.cartButton.setIcon(icon12)
        self.cartButton.setAutoRepeat(False)
        self.cartButton.setObjectName(_fromUtf8("cartButton"))
        self.excelButton = QtGui.QAction(MainWindowResults)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/export_excel_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/excel.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/excel.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.excelButton.setIcon(icon13)
        self.excelButton.setAutoRepeat(False)
        self.excelButton.setMenuRole(QtGui.QAction.ApplicationSpecificRole)
        self.excelButton.setObjectName(_fromUtf8("excelButton"))
        self.textButton = QtGui.QAction(MainWindowResults)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/text_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/text.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/text.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.textButton.setIcon(icon14)
        self.textButton.setAutoRepeat(False)
        self.textButton.setMenuRole(QtGui.QAction.NoRole)
        self.textButton.setIconVisibleInMenu(False)
        self.textButton.setObjectName(_fromUtf8("textButton"))
        self.wordButton = QtGui.QAction(MainWindowResults)
        self.wordButton.setEnabled(True)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/export_word_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/word.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/word.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.wordButton.setIcon(icon15)
        self.wordButton.setAutoRepeat(False)
        self.wordButton.setVisible(True)
        self.wordButton.setMenuRole(QtGui.QAction.NoRole)
        self.wordButton.setObjectName(_fromUtf8("wordButton"))
        self.mainToolBar.addAction(self.firstButton)
        self.mainToolBar.addAction(self.previousButton)
        self.mainToolBar.addAction(self.nextButton)
        self.mainToolBar.addAction(self.lastButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.findButton)
        self.mainToolBar.addAction(self.openselButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.filter)
        self.mainToolBar.addAction(self.cartButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.printButton)
        self.mainToolBar.addAction(self.textButton)
        self.mainToolBar.addAction(self.wordButton)
        self.mainToolBar.addAction(self.excelButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.newButton)
        self.mainToolBar.addAction(self.modifyButton)
        self.mainToolBar.addAction(self.eraseButton)

        self.retranslateUi(MainWindowResults)
        QtCore.QMetaObject.connectSlotsByName(MainWindowResults)

    def retranslateUi(self, MainWindowResults):
        MainWindowResults.setWindowTitle(QtGui.QApplication.translate("MainWindowResults", "Elenco Anagrafiche", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setSortingEnabled(True)
        self.tabella.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindowResults", "codice \n"
" MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindowResults", "potenziale \n"
" MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindowResults", "Ragione Sociale", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindowResults", "indirizzo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindowResults", "Cap", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindowResults", "Comune", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(6).setText(QtGui.QApplication.translate("MainWindowResults", "provincia", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(7).setText(QtGui.QApplication.translate("MainWindowResults", "telefono", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.horizontalHeaderItem(8).setText(QtGui.QApplication.translate("MainWindowResults", "fiscale/partita iva", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindowResults", "Numero Anagrafiche", None, QtGui.QApplication.UnicodeUTF8))
        self.text_numero_risultati.setToolTip(QtGui.QApplication.translate("MainWindowResults", "numero risultati", None, QtGui.QApplication.UnicodeUTF8))
        self.mainToolBar.setWindowTitle(QtGui.QApplication.translate("MainWindowResults", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.firstButton.setText(QtGui.QApplication.translate("MainWindowResults", "primo", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("MainWindowResults", "precedente", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindowResults", "successivo", None, QtGui.QApplication.UnicodeUTF8))
        self.lastButton.setText(QtGui.QApplication.translate("MainWindowResults", "ultimo", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("MainWindowResults", "nuovo", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "inserisci nuova anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.modifyButton.setText(QtGui.QApplication.translate("MainWindowResults", "modifica", None, QtGui.QApplication.UnicodeUTF8))
        self.modifyButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "modifica anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.printButton.setText(QtGui.QApplication.translate("MainWindowResults", "stampa", None, QtGui.QApplication.UnicodeUTF8))
        self.filter.setText(QtGui.QApplication.translate("MainWindowResults", "filtro", None, QtGui.QApplication.UnicodeUTF8))
        self.filter.setToolTip(QtGui.QApplication.translate("MainWindowResults", "ulteriore selezione", None, QtGui.QApplication.UnicodeUTF8))
        self.eraseButton.setText(QtGui.QApplication.translate("MainWindowResults", "cancella", None, QtGui.QApplication.UnicodeUTF8))
        self.eraseButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "cancella anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("MainWindowResults", "trova", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "ricerca anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.openselButton.setText(QtGui.QApplication.translate("MainWindowResults", "apri selezionato", None, QtGui.QApplication.UnicodeUTF8))
        self.openselButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "apri anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.cartButton.setText(QtGui.QApplication.translate("MainWindowResults", "cartografia", None, QtGui.QApplication.UnicodeUTF8))
        self.cartButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "torna ai risultati della selezione geografica", None, QtGui.QApplication.UnicodeUTF8))
        self.excelButton.setText(QtGui.QApplication.translate("MainWindowResults", "esporta in excel", None, QtGui.QApplication.UnicodeUTF8))
        self.textButton.setText(QtGui.QApplication.translate("MainWindowResults", "esporta testo", None, QtGui.QApplication.UnicodeUTF8))
        self.textButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "esporta testo", None, QtGui.QApplication.UnicodeUTF8))
        self.wordButton.setText(QtGui.QApplication.translate("MainWindowResults", "esporta in word", None, QtGui.QApplication.UnicodeUTF8))
        self.wordButton.setToolTip(QtGui.QApplication.translate("MainWindowResults", "esporta in word", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
