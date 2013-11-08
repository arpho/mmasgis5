# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created: Thu Jun 14 13:03:23 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Settings(object):
    def setupUi(self, Settings):
        Settings.setObjectName(_fromUtf8("Settings"))
        Settings.resize(700, 500)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Settings.sizePolicy().hasHeightForWidth())
        Settings.setSizePolicy(sizePolicy)
        Settings.setMinimumSize(QtCore.QSize(700, 500))
        Settings.setMaximumSize(QtCore.QSize(700, 500))
        self.centralWidget = QtGui.QWidget(Settings)
        self.centralWidget.setStyleSheet(_fromUtf8("/* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
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
"\n"
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
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 661, 431))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setStyleSheet(_fromUtf8("QTabWidget::pane { /* The tab widget frame */\n"
"     border-top: 2px groove rgb(188, 198, 207);\n"
" \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"\n"
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
"     border-bottom-color: rgb(188, 198, 207); /* same as the pane color */\n"
"     border-top-left-radius: 4px;\n"
"     border-top-right-radius: 4px;\n"
"     min-width: 17ex;\n"
"     padding: 2px;\n"
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
"     margin-top: 2px; /* make non-selected tabs look smaller */\n"
" }\n"
"\n"
""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.user = QtGui.QWidget()
        self.user.setObjectName(_fromUtf8("user"))
        self.label = QtGui.QLabel(self.user)
        self.label.setGeometry(QtCore.QRect(10, 35, 131, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.user)
        self.label_2.setGeometry(QtCore.QRect(10, 85, 141, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.text_user = QtGui.QLineEdit(self.user)
        self.text_user.setGeometry(QtCore.QRect(160, 30, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.text_user.setFont(font)
        self.text_user.setObjectName(_fromUtf8("text_user"))
        self.text_pass = QtGui.QLineEdit(self.user)
        self.text_pass.setGeometry(QtCore.QRect(160, 80, 231, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.text_pass.setFont(font)
        self.text_pass.setEchoMode(QtGui.QLineEdit.PasswordEchoOnEdit)
        self.text_pass.setObjectName(_fromUtf8("text_pass"))
        self.check_amm_DB = QtGui.QCheckBox(self.user)
        self.check_amm_DB.setGeometry(QtCore.QRect(160, 130, 231, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_amm_DB.sizePolicy().hasHeightForWidth())
        self.check_amm_DB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.check_amm_DB.setFont(font)
        self.check_amm_DB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_amm_DB.setObjectName(_fromUtf8("check_amm_DB"))
        self.tabWidget.addTab(self.user, _fromUtf8(""))
        self.databases = QtGui.QWidget()
        self.databases.setObjectName(_fromUtf8("databases"))
        self.Registra = QtGui.QPushButton(self.databases)
        self.Registra.setGeometry(QtCore.QRect(450, 30, 101, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Registra.sizePolicy().hasHeightForWidth())
        self.Registra.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.Registra.setFont(font)
        self.Registra.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Registra.setObjectName(_fromUtf8("Registra"))
        self.EliminaButton = QtGui.QPushButton(self.databases)
        self.EliminaButton.setGeometry(QtCore.QRect(450, 150, 101, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EliminaButton.sizePolicy().hasHeightForWidth())
        self.EliminaButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.EliminaButton.setFont(font)
        self.EliminaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.EliminaButton.setObjectName(_fromUtf8("EliminaButton"))
        self.ModificaButton = QtGui.QPushButton(self.databases)
        self.ModificaButton.setGeometry(QtCore.QRect(450, 90, 101, 51))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ModificaButton.sizePolicy().hasHeightForWidth())
        self.ModificaButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.ModificaButton.setFont(font)
        self.ModificaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ModificaButton.setObjectName(_fromUtf8("ModificaButton"))
        self.list_DB = QtGui.QTreeWidget(self.databases)
        self.list_DB.setGeometry(QtCore.QRect(160, 20, 256, 361))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.list_DB.setFont(font)
        self.list_DB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_DB.setStyleSheet(_fromUtf8("QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}"))
        self.list_DB.setObjectName(_fromUtf8("list_DB"))
        self.list_DB.headerItem().setText(0, _fromUtf8("1"))
        self.list_DB.header().setVisible(False)
        self.list_DB.header().setDefaultSectionSize(250)
        self.list_DB.header().setMinimumSectionSize(250)
        self.tabWidget.addTab(self.databases, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setStyleSheet(_fromUtf8("QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}"))
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 211, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.list_funzioni = QtGui.QTreeWidget(self.groupBox)
        self.list_funzioni.setGeometry(QtCore.QRect(10, 30, 191, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.list_funzioni.setFont(font)
        self.list_funzioni.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_funzioni.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.list_funzioni.setObjectName(_fromUtf8("list_funzioni"))
        self.list_funzioni.headerItem().setText(0, _fromUtf8("1"))
        self.list_funzioni.header().setVisible(False)
        self.list_funzioni.header().setDefaultSectionSize(185)
        self.list_funzioni.header().setMinimumSectionSize(185)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(220, 50, 211, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.list_esp = QtGui.QTreeWidget(self.groupBox_2)
        self.list_esp.setGeometry(QtCore.QRect(10, 30, 191, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.list_esp.setFont(font)
        self.list_esp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_esp.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.list_esp.setObjectName(_fromUtf8("list_esp"))
        self.list_esp.headerItem().setText(0, _fromUtf8("1"))
        self.list_esp.header().setVisible(False)
        self.list_esp.header().setDefaultSectionSize(185)
        self.list_esp.header().setMinimumSectionSize(185)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(430, 50, 211, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.list_amm = QtGui.QTreeWidget(self.groupBox_3)
        self.list_amm.setGeometry(QtCore.QRect(10, 30, 191, 341))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.list_amm.setFont(font)
        self.list_amm.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_amm.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.list_amm.setObjectName(_fromUtf8("list_amm"))
        self.list_amm.headerItem().setText(0, _fromUtf8("1"))
        self.list_amm.header().setVisible(False)
        self.list_amm.header().setDefaultSectionSize(185)
        self.list_amm.header().setMinimumSectionSize(185)
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(120, 10, 241, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox.setStyleSheet(_fromUtf8("\n"
"QFrame{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}\n"
"QComboBox{\n"
" border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
"}\n"
"\n"
" QComboBox:editable {\n"
"    \n"
"    background-color: rgb(222, 232, 245);\n"
" }\n"
"\n"
" QComboBox:!editable, QComboBox::drop-down:editable {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 226, 229, 255), stop:0.254545 rgba(247, 247, 247, 255), stop:0.722727 rgba(247, 247, 247, 255), stop:1 rgba(220, 226, 229, 255));\n"
"color:black;\n"
" }\n"
"\n"
" /* QComboBox gets the \"on\" state when the popup is open */\n"
" QComboBox:!editable:on, QComboBox::drop-down:editable:on {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 226, 229, 255), stop:0.254545 rgba(247, 247, 247, 255), stop:0.722727 rgba(247, 247, 247, 255), stop:1 rgba(220, 226, 229, 255));\n"
"color:black;\n"
" }\n"
"\n"
" QComboBox:on { /* shift the text when the popup opens */\n"
"     padding-top: 3px;\n"
"     padding-left: 4px;\n"
" }\n"
"\n"
"\n"
""))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 101, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Applica = QtGui.QPushButton(self.tab)
        self.Applica.setGeometry(QtCore.QRect(437, 7, 98, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.Applica.setFont(font)
        self.Applica.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Applica.setObjectName(_fromUtf8("Applica"))
        self.CreaNuovo = QtGui.QPushButton(self.tab)
        self.CreaNuovo.setGeometry(QtCore.QRect(540, 7, 98, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.CreaNuovo.setFont(font)
        self.CreaNuovo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.CreaNuovo.setObjectName(_fromUtf8("CreaNuovo"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.AnnullaButton = QtGui.QPushButton(self.centralWidget)
        self.AnnullaButton.setGeometry(QtCore.QRect(467, 450, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.AnnullaButton.setFont(font)
        self.AnnullaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AnnullaButton.setObjectName(_fromUtf8("AnnullaButton"))
        self.OKButton = QtGui.QPushButton(self.centralWidget)
        self.OKButton.setGeometry(QtCore.QRect(587, 450, 101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.OKButton.setFont(font)
        self.OKButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OKButton.setObjectName(_fromUtf8("OKButton"))
        Settings.setCentralWidget(self.centralWidget)

        self.retranslateUi(Settings)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Settings)

    def retranslateUi(self, Settings):
        Settings.setWindowTitle(QtGui.QApplication.translate("Settings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Settings", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Settings", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.check_amm_DB.setText(QtGui.QApplication.translate("Settings", "Amministratore del Sistema", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.user), QtGui.QApplication.translate("Settings", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.Registra.setText(QtGui.QApplication.translate("Settings", "Registra", None, QtGui.QApplication.UnicodeUTF8))
        self.EliminaButton.setText(QtGui.QApplication.translate("Settings", "Elimina", None, QtGui.QApplication.UnicodeUTF8))
        self.ModificaButton.setText(QtGui.QApplication.translate("Settings", "Modifica", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.databases), QtGui.QApplication.translate("Settings", "Databases", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Settings", "Funzionalità", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Settings", "Backoffice", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Settings", "Zone Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Settings", "Profilo", None, QtGui.QApplication.UnicodeUTF8))
        self.Applica.setText(QtGui.QApplication.translate("Settings", "Applica", None, QtGui.QApplication.UnicodeUTF8))
        self.CreaNuovo.setText(QtGui.QApplication.translate("Settings", "Crea Nuovo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Settings", "Profilo", None, QtGui.QApplication.UnicodeUTF8))
        self.AnnullaButton.setText(QtGui.QApplication.translate("Settings", "Annulla", None, QtGui.QApplication.UnicodeUTF8))
        self.OKButton.setText(QtGui.QApplication.translate("Settings", "OK", None, QtGui.QApplication.UnicodeUTF8))

