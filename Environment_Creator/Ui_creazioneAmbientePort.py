# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creazioneambienteConPorta.ui'
#
# Created: Wed Jun 13 16:55:31 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CreazioneAmbiente(object):
    def setupUi(self, CreazioneAmbiente):
        CreazioneAmbiente.setObjectName(_fromUtf8("CreazioneAmbiente"))
        CreazioneAmbiente.resize(400, 350)
        CreazioneAmbiente.setMinimumSize(QtCore.QSize(400, 350))
        CreazioneAmbiente.setMaximumSize(QtCore.QSize(400, 350))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        CreazioneAmbiente.setFont(font)
        self.centralWidget = QtGui.QWidget(CreazioneAmbiente)
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
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 15, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(10, 55, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 95, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 175, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(10, 255, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.text_utente = QtGui.QLineEdit(self.centralWidget)
        self.text_utente.setGeometry(QtCore.QRect(190, 9, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.text_utente.setFont(font)
        self.text_utente.setObjectName(_fromUtf8("text_utente"))
        self.text_pass_DB = QtGui.QLineEdit(self.centralWidget)
        self.text_pass_DB.setGeometry(QtCore.QRect(190, 50, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.text_pass_DB.setFont(font)
        self.text_pass_DB.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.text_pass_DB.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_pass_DB.setEchoMode(QtGui.QLineEdit.Password)
        self.text_pass_DB.setObjectName(_fromUtf8("text_pass_DB"))
        self.text_host = QtGui.QLineEdit(self.centralWidget)
        self.text_host.setGeometry(QtCore.QRect(190, 90, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.text_host.setFont(font)
        self.text_host.setObjectName(_fromUtf8("text_host"))
        self.text_pass_utente = QtGui.QLineEdit(self.centralWidget)
        self.text_pass_utente.setGeometry(QtCore.QRect(190, 250, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.text_pass_utente.setFont(font)
        self.text_pass_utente.setEchoMode(QtGui.QLineEdit.Password)
        self.text_pass_utente.setObjectName(_fromUtf8("text_pass_utente"))
        self.box_DB = QtGui.QComboBox(self.centralWidget)
        self.box_DB.setGeometry(QtCore.QRect(190, 170, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.box_DB.setFont(font)
        self.box_DB.setStyleSheet(_fromUtf8("\n"
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
        self.box_DB.setObjectName(_fromUtf8("box_DB"))
        self.OK_Button = QtGui.QPushButton(self.centralWidget)
        self.OK_Button.setGeometry(QtCore.QRect(290, 300, 98, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.OK_Button.setFont(font)
        self.OK_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.OK_Button.setObjectName(_fromUtf8("OK_Button"))
        self.AnnullaButton = QtGui.QPushButton(self.centralWidget)
        self.AnnullaButton.setGeometry(QtCore.QRect(180, 300, 98, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        self.AnnullaButton.setFont(font)
        self.AnnullaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.AnnullaButton.setObjectName(_fromUtf8("AnnullaButton"))
        self.label_6 = QtGui.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(10, 215, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.text_utente_gis = QtGui.QLineEdit(self.centralWidget)
        self.text_utente_gis.setGeometry(QtCore.QRect(190, 210, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        self.text_utente_gis.setFont(font)
        self.text_utente_gis.setObjectName(_fromUtf8("text_utente_gis"))
        self.label_7 = QtGui.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(10, 135, 171, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.text_porta = QtGui.QLineEdit(self.centralWidget)
        self.text_porta.setGeometry(QtCore.QRect(190, 130, 201, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.text_porta.setFont(font)
        self.text_porta.setObjectName(_fromUtf8("text_porta"))
        CreazioneAmbiente.setCentralWidget(self.centralWidget)

        self.retranslateUi(CreazioneAmbiente)
        QtCore.QMetaObject.connectSlotsByName(CreazioneAmbiente)

    def retranslateUi(self, CreazioneAmbiente):
        CreazioneAmbiente.setWindowTitle(QtGui.QApplication.translate("CreazioneAmbiente", "CreazioneAmbiente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Utente Root DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Password DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Famiglia DB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Password Utente GIS", None, QtGui.QApplication.UnicodeUTF8))
        self.OK_Button.setText(QtGui.QApplication.translate("CreazioneAmbiente", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.AnnullaButton.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Annulla", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Utente GIS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("CreazioneAmbiente", "Porta", None, QtGui.QApplication.UnicodeUTF8))

