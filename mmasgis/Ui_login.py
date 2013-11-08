# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Thu Jun 14 16:07:11 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(400, 420)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(400, 420))
        Login.setMaximumSize(QtCore.QSize(400, 420))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Login.setWindowIcon(icon)
        self.centralWidget = QtGui.QWidget(Login)
        self.centralWidget.setStyleSheet(_fromUtf8("/* sets background color  */\n"
"QWidget {\n"
"background-color:rgba(255,255,255,0);\n"
"}\n"
"QWidget#centralWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"}\n"
"\n"
"QLabel{\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
" border: 1px outset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.0545455 rgba(237, 240, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(237, 240, 243, 255));\n"
" }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.text_user = QtGui.QLineEdit(self.centralWidget)
        self.text_user.setGeometry(QtCore.QRect(10, 107, 381, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_user.sizePolicy().hasHeightForWidth())
        self.text_user.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.text_user.setFont(font)
        self.text_user.setObjectName(_fromUtf8("text_user"))
        self.text_pass = QtGui.QLineEdit(self.centralWidget)
        self.text_pass.setGeometry(QtCore.QRect(10, 177, 381, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_pass.sizePolicy().hasHeightForWidth())
        self.text_pass.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.text_pass.setFont(font)
        self.text_pass.setEchoMode(QtGui.QLineEdit.Password)
        self.text_pass.setObjectName(_fromUtf8("text_pass"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 381, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8(""))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 149, 381, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.LoginButton = QtGui.QPushButton(self.centralWidget)
        self.LoginButton.setGeometry(QtCore.QRect(10, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.LoginButton.setFont(font)
        self.LoginButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.LoginButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
""))
        self.LoginButton.setObjectName(_fromUtf8("LoginButton"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 271, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(290, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.check_conn = QtGui.QCheckBox(self.centralWidget)
        self.check_conn.setGeometry(QtCore.QRect(10, 340, 201, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.check_conn.setFont(font)
        self.check_conn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_conn.setObjectName(_fromUtf8("check_conn"))
        self.text_host = QtGui.QLineEdit(self.centralWidget)
        self.text_host.setGeometry(QtCore.QRect(10, 35, 271, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.text_host.setFont(font)
        self.text_host.setObjectName(_fromUtf8("text_host"))
        self.text_porta = QtGui.QLineEdit(self.centralWidget)
        self.text_porta.setGeometry(QtCore.QRect(290, 35, 101, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.text_porta.setFont(font)
        self.text_porta.setObjectName(_fromUtf8("text_porta"))
        self.ResetButton = QtGui.QPushButton(self.centralWidget)
        self.ResetButton.setGeometry(QtCore.QRect(145, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.ResetButton.setFont(font)
        self.ResetButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ResetButton.setStyleSheet(_fromUtf8(" QPushButton {\n"
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
" }"))
        self.ResetButton.setObjectName(_fromUtf8("ResetButton"))
        self.AnnullaButton = QtGui.QPushButton(self.centralWidget)
        self.AnnullaButton.setGeometry(QtCore.QRect(280, 370, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.AnnullaButton.setFont(font)
        self.AnnullaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AnnullaButton.setStyleSheet(_fromUtf8("QPushButton {\n"
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
" }"))
        self.AnnullaButton.setObjectName(_fromUtf8("AnnullaButton"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 381, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Box_DB = QtGui.QComboBox(self.centralWidget)
        self.Box_DB.setGeometry(QtCore.QRect(10, 307, 381, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.Box_DB.setFont(font)
        self.Box_DB.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Box_DB.setStyleSheet(_fromUtf8("\n"
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
        self.Box_DB.setObjectName(_fromUtf8("Box_DB"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 215, 381, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit = QtGui.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 241, 381, 29))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        Login.setCentralWidget(self.centralWidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.text_host, self.text_porta)
        Login.setTabOrder(self.text_porta, self.text_user)
        Login.setTabOrder(self.text_user, self.text_pass)
        Login.setTabOrder(self.text_pass, self.lineEdit)

    def retranslateUi(self, Login):
        Login.setWindowTitle(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Login", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Login", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.LoginButton.setText(QtGui.QApplication.translate("Login", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Login", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Login", "Porta", None, QtGui.QApplication.UnicodeUTF8))
        self.check_conn.setText(QtGui.QApplication.translate("Login", "Connessione Locale", None, QtGui.QApplication.UnicodeUTF8))
        self.ResetButton.setText(QtGui.QApplication.translate("Login", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.AnnullaButton.setText(QtGui.QApplication.translate("Login", "Annulla", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Login", "Famiglia DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Login", "Azienda", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
