# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ricercaanagrafica.ui'
#
# Created: Sun Jun 17 16:35:27 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowRicercaAnagrafica(object):
    def setupUi(self, MainWindowRicercaAnagrafica):
        MainWindowRicercaAnagrafica.setObjectName(_fromUtf8("MainWindowRicercaAnagrafica"))
        MainWindowRicercaAnagrafica.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindowRicercaAnagrafica.resize(500, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowRicercaAnagrafica.sizePolicy().hasHeightForWidth())
        MainWindowRicercaAnagrafica.setSizePolicy(sizePolicy)
        MainWindowRicercaAnagrafica.setMinimumSize(QtCore.QSize(500, 300))
        MainWindowRicercaAnagrafica.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/World.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowRicercaAnagrafica.setWindowIcon(icon)
        MainWindowRicercaAnagrafica.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(MainWindowRicercaAnagrafica)
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
"QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(220, 232, 243, 255), stop:0.35545 rgba(247, 247, 247, 255), stop:0.635071 rgba(247, 247, 247, 255), stop:0.933649 rgba(220, 232, 243, 255));\n"
"     font: 11pt \"Arial\";\n"
"\n"
" }"))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 121, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(250, 80, 121, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.text_codiceMMAS = QtGui.QLineEdit(self.centralWidget)
        self.text_codiceMMAS.setGeometry(QtCore.QRect(10, 100, 231, 27))
        self.text_codiceMMAS.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_codiceMMAS.setObjectName(_fromUtf8("text_codiceMMAS"))
        self.text_codcliente = QtGui.QLineEdit(self.centralWidget)
        self.text_codcliente.setGeometry(QtCore.QRect(250, 100, 231, 27))
        self.text_codcliente.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_codcliente.setObjectName(_fromUtf8("text_codcliente"))
        self.label_3 = QtGui.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 131, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.text_ragionesociale = QtGui.QLineEdit(self.centralWidget)
        self.text_ragionesociale.setGeometry(QtCore.QRect(10, 160, 471, 27))
        self.text_ragionesociale.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_ragionesociale.setObjectName(_fromUtf8("text_ragionesociale"))
        self.label_4 = QtGui.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(10, 200, 91, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.text_comune = QtGui.QLineEdit(self.centralWidget)
        self.text_comune.setGeometry(QtCore.QRect(10, 220, 471, 27))
        self.text_comune.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.text_comune.setObjectName(_fromUtf8("text_comune"))
        self.check_minma = QtGui.QCheckBox(self.centralWidget)
        self.check_minma.setGeometry(QtCore.QRect(10, 260, 161, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.check_minma.setFont(font)
        self.check_minma.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_minma.setStyleSheet(_fromUtf8("QCheckBox {\n"
"     spacing: 2px;\n"
"     border:2px groove rgb(188,198,207);   \n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(219, 230, 239, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
" }\n"
"QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    image: url(:/resources/checkbox_off_en.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/resources/checkbox_on_enabled.png);\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked:!enabled {\n"
"    \n"
"    image: url(:/resources/checkbox_off_dis.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:!enabled {\n"
"    \n"
"    image: url(:/resources/checkbox_on_disabled.png);\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    \n"
"    image: url(:/resources/checkbox_off_enabled_hover.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"    \n"
"    image: url(:/resources/checkbox_on_enabled_hover.png);\n"
" }\n"
"\n"
"\n"
" \n"
"\n"
""))
        self.check_minma.setObjectName(_fromUtf8("check_minma"))
        self.check_int = QtGui.QCheckBox(self.centralWidget)
        self.check_int.setGeometry(QtCore.QRect(250, 260, 151, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.check_int.setFont(font)
        self.check_int.setFocusPolicy(QtCore.Qt.NoFocus)
        self.check_int.setStyleSheet(_fromUtf8("QCheckBox {\n"
"     spacing: 2px;\n"
"     border:2px groove rgb(188,198,207);   \n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(219, 230, 239, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
" }\n"
"QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    \n"
"    image: url(:/resources/checkbox_off_en.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    \n"
"    image: url(:/resources/checkbox_on_enabled.png);\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked:!enabled {\n"
"    \n"
"    image: url(:/resources/checkbox_off_dis.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked:!enabled {\n"
"    \n"
"    image: url(:/resources/checkbox_on_disabled.png);\n"
" }\n"
"\n"
"QCheckBox::indicator:unchecked:hover {\n"
"    \n"
"    image: url(:/resources/checkbox_off_enabled_hover.png);\n"
" }\n"
"\n"
"\n"
" QCheckBox::indicator:checked:hover {\n"
"    \n"
"    image: url(:/resources/checkbox_on_enabled_hover.png);\n"
" }\n"
"\n"
"\n"
" \n"
"\n"
""))
        self.check_int.setObjectName(_fromUtf8("check_int"))
        self.trovaButton = QtGui.QPushButton(self.centralWidget)
        self.trovaButton.setGeometry(QtCore.QRect(440, 10, 50, 50))
        self.trovaButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.trovaButton.setStyleSheet(_fromUtf8("/* pushbutton style */\n"
"QPushButton {\n"
"     border: 1px groove rgba(255,255,255,0);\n"
"     border-radius: 5px;\n"
"    background-color: rgba(255, 255, 255,0);\n"
"    \n"
"    image: url(:/resources/filter_ok_not_hov.png);\n"
"\n"
" }\n"
"\n"
" QPushButton:hover {\n"
"     border: 1px outset rgb(188, 189, 207);\n"
"border-radius:3px;\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"    \n"
"    image: url(:/resources/filter_ok.png);\n"
" } \n"
"QPushButton:pressed {\n"
"     border: 3px inset rgb(188, 189, 207);\n"
"    border-radius:3px;\n"
" } \n"
""))
        self.trovaButton.setText(_fromUtf8(""))
        self.trovaButton.setObjectName(_fromUtf8("trovaButton"))
        MainWindowRicercaAnagrafica.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindowRicercaAnagrafica)
        QtCore.QMetaObject.connectSlotsByName(MainWindowRicercaAnagrafica)

    def retranslateUi(self, MainWindowRicercaAnagrafica):
        MainWindowRicercaAnagrafica.setWindowTitle(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "Ricerca Anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "Codice MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "Codice Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "Ragione Sociale", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "Comune", None, QtGui.QApplication.UnicodeUTF8))
        self.check_minma.setText(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "maiuscole/minuscole", None, QtGui.QApplication.UnicodeUTF8))
        self.check_int.setText(QtGui.QApplication.translate("MainWindowRicercaAnagrafica", "Solo parole intere", None, QtGui.QApplication.UnicodeUTF8))

