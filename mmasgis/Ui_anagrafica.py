# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anagrafica.ui'
#
# Created: Thu Jun 14 20:43:58 2012
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindowAnagrafica(object):
    def setupUi(self, MainWindowAnagrafica):
        MainWindowAnagrafica.setObjectName(_fromUtf8("MainWindowAnagrafica"))
        MainWindowAnagrafica.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindowAnagrafica.resize(819, 635)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindowAnagrafica.sizePolicy().hasHeightForWidth())
        MainWindowAnagrafica.setSizePolicy(sizePolicy)
        MainWindowAnagrafica.setBaseSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        MainWindowAnagrafica.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/icon_mmas.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindowAnagrafica.setWindowIcon(icon)
        MainWindowAnagrafica.setStyleSheet(_fromUtf8(""))
        self.centralWidget = QtGui.QWidget(MainWindowAnagrafica)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy)
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
"    width: 11px;\n"
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
""))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout_6 = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.text_codice_mmas = QtGui.QLineEdit(self.centralWidget)
        self.text_codice_mmas.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_codice_mmas.sizePolicy().hasHeightForWidth())
        self.text_codice_mmas.setSizePolicy(sizePolicy)
        self.text_codice_mmas.setMinimumSize(QtCore.QSize(110, 20))
        self.text_codice_mmas.setSizeIncrement(QtCore.QSize(0, 0))
        self.text_codice_mmas.setCursor(QtCore.Qt.ArrowCursor)
        self.text_codice_mmas.setMouseTracking(False)
        self.text_codice_mmas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_codice_mmas.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.text_codice_mmas.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_codice_mmas.setEchoMode(QtGui.QLineEdit.Normal)
        self.text_codice_mmas.setReadOnly(True)
        self.text_codice_mmas.setObjectName(_fromUtf8("text_codice_mmas"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_codice_mmas)
        self.codiceMMAS = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.codiceMMAS.sizePolicy().hasHeightForWidth())
        self.codiceMMAS.setSizePolicy(sizePolicy)
        self.codiceMMAS.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.codiceMMAS.setFont(font)
        self.codiceMMAS.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.codiceMMAS.setObjectName(_fromUtf8("codiceMMAS"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.codiceMMAS)
        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)
        self.checkBox_cliente = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_cliente.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_cliente.sizePolicy().hasHeightForWidth())
        self.checkBox_cliente.setSizePolicy(sizePolicy)
        self.checkBox_cliente.setMinimumSize(QtCore.QSize(85, 20))
        self.checkBox_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_cliente.setStyleSheet(_fromUtf8("QCheckBox {\n"
"     spacing: 2px;\n"
"     border:2px groove rgb(188,198,207);   \n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(219, 230, 239, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"         font: 10pt \"Arial\";\n"
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
"\n"
"\n"
""))
        self.checkBox_cliente.setIconSize(QtCore.QSize(15, 15))
        self.checkBox_cliente.setCheckable(False)
        self.checkBox_cliente.setObjectName(_fromUtf8("checkBox_cliente"))
        self.gridLayout_2.addWidget(self.checkBox_cliente, 0, 1, 1, 1)
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_2.setHorizontalSpacing(3)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.CodiceCliente = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CodiceCliente.sizePolicy().hasHeightForWidth())
        self.CodiceCliente.setSizePolicy(sizePolicy)
        self.CodiceCliente.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.CodiceCliente.setFont(font)
        self.CodiceCliente.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.CodiceCliente.setObjectName(_fromUtf8("CodiceCliente"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.CodiceCliente)
        self.text_codice_cliente = QtGui.QLineEdit(self.centralWidget)
        self.text_codice_cliente.setMinimumSize(QtCore.QSize(110, 20))
        self.text_codice_cliente.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_codice_cliente.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_codice_cliente.setReadOnly(True)
        self.text_codice_cliente.setObjectName(_fromUtf8("text_codice_cliente"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_codice_cliente)
        self.gridLayout_2.addLayout(self.formLayout_2, 0, 2, 1, 1)
        self.formLayout_3 = QtGui.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_3.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setHorizontalSpacing(3)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.text_potenziale = QtGui.QLineEdit(self.centralWidget)
        self.text_potenziale.setMinimumSize(QtCore.QSize(110, 20))
        self.text_potenziale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_potenziale.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_potenziale.setReadOnly(True)
        self.text_potenziale.setObjectName(_fromUtf8("text_potenziale"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_potenziale)
        self.PotenzialeMMAS = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PotenzialeMMAS.sizePolicy().hasHeightForWidth())
        self.PotenzialeMMAS.setSizePolicy(sizePolicy)
        self.PotenzialeMMAS.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.PotenzialeMMAS.setFont(font)
        self.PotenzialeMMAS.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.PotenzialeMMAS.setObjectName(_fromUtf8("PotenzialeMMAS"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.PotenzialeMMAS)
        self.gridLayout_2.addLayout(self.formLayout_3, 0, 3, 1, 1)
        self.formLayout_4 = QtGui.QFormLayout()
        self.formLayout_4.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_4.setHorizontalSpacing(3)
        self.formLayout_4.setObjectName(_fromUtf8("formLayout_4"))
        self.RagioneSociale = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RagioneSociale.sizePolicy().hasHeightForWidth())
        self.RagioneSociale.setSizePolicy(sizePolicy)
        self.RagioneSociale.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.RagioneSociale.setFont(font)
        self.RagioneSociale.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.RagioneSociale.setObjectName(_fromUtf8("RagioneSociale"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.LabelRole, self.RagioneSociale)
        self.text_ragione_sociale = QtGui.QLineEdit(self.centralWidget)
        self.text_ragione_sociale.setEnabled(True)
        self.text_ragione_sociale.setMinimumSize(QtCore.QSize(665, 20))
        self.text_ragione_sociale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_ragione_sociale.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_ragione_sociale.setReadOnly(True)
        self.text_ragione_sociale.setObjectName(_fromUtf8("text_ragione_sociale"))
        self.formLayout_4.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_ragione_sociale)
        self.gridLayout_2.addLayout(self.formLayout_4, 1, 0, 1, 4)
        self.formLayout_5 = QtGui.QFormLayout()
        self.formLayout_5.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_5.setHorizontalSpacing(3)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.Titolare = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Titolare.sizePolicy().hasHeightForWidth())
        self.Titolare.setSizePolicy(sizePolicy)
        self.Titolare.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Titolare.setFont(font)
        self.Titolare.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Titolare.setObjectName(_fromUtf8("Titolare"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.Titolare)
        self.text_titolare = QtGui.QLineEdit(self.centralWidget)
        self.text_titolare.setEnabled(True)
        self.text_titolare.setMinimumSize(QtCore.QSize(435, 20))
        self.text_titolare.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_titolare.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_titolare.setReadOnly(True)
        self.text_titolare.setObjectName(_fromUtf8("text_titolare"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_titolare)
        self.gridLayout_2.addLayout(self.formLayout_5, 2, 0, 1, 3)
        self.formLayout_6 = QtGui.QFormLayout()
        self.formLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_6.setHorizontalSpacing(3)
        self.formLayout_6.setObjectName(_fromUtf8("formLayout_6"))
        self.CodFiscale = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CodFiscale.sizePolicy().hasHeightForWidth())
        self.CodFiscale.setSizePolicy(sizePolicy)
        self.CodFiscale.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.CodFiscale.setFont(font)
        self.CodFiscale.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.CodFiscale.setObjectName(_fromUtf8("CodFiscale"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.LabelRole, self.CodFiscale)
        self.text_codice_fiscale = QtGui.QLineEdit(self.centralWidget)
        self.text_codice_fiscale.setMinimumSize(QtCore.QSize(110, 20))
        self.text_codice_fiscale.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_codice_fiscale.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_codice_fiscale.setReadOnly(True)
        self.text_codice_fiscale.setObjectName(_fromUtf8("text_codice_fiscale"))
        self.formLayout_6.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_codice_fiscale)
        self.gridLayout_2.addLayout(self.formLayout_6, 2, 3, 1, 1)
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_7.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_7.setHorizontalSpacing(3)
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.Indirizzo = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Indirizzo.sizePolicy().hasHeightForWidth())
        self.Indirizzo.setSizePolicy(sizePolicy)
        self.Indirizzo.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Indirizzo.setFont(font)
        self.Indirizzo.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Indirizzo.setObjectName(_fromUtf8("Indirizzo"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.Indirizzo)
        self.text_indirizzo = QtGui.QLineEdit(self.centralWidget)
        self.text_indirizzo.setEnabled(True)
        self.text_indirizzo.setMinimumSize(QtCore.QSize(665, 20))
        self.text_indirizzo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_indirizzo.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_indirizzo.setReadOnly(True)
        self.text_indirizzo.setObjectName(_fromUtf8("text_indirizzo"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_indirizzo)
        self.gridLayout_2.addLayout(self.formLayout_7, 3, 0, 1, 4)
        self.formLayout_8 = QtGui.QFormLayout()
        self.formLayout_8.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_8.setHorizontalSpacing(3)
        self.formLayout_8.setObjectName(_fromUtf8("formLayout_8"))
        self.Comune = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Comune.sizePolicy().hasHeightForWidth())
        self.Comune.setSizePolicy(sizePolicy)
        self.Comune.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Comune.setFont(font)
        self.Comune.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Comune.setObjectName(_fromUtf8("Comune"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.LabelRole, self.Comune)
        self.text_comune = QtGui.QLineEdit(self.centralWidget)
        self.text_comune.setMinimumSize(QtCore.QSize(200, 20))
        self.text_comune.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_comune.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_comune.setReadOnly(True)
        self.text_comune.setObjectName(_fromUtf8("text_comune"))
        self.formLayout_8.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_comune)
        self.gridLayout_2.addLayout(self.formLayout_8, 4, 0, 1, 2)
        self.formLayout_9 = QtGui.QFormLayout()
        self.formLayout_9.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_9.setHorizontalSpacing(3)
        self.formLayout_9.setObjectName(_fromUtf8("formLayout_9"))
        self.Provincia = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Provincia.sizePolicy().hasHeightForWidth())
        self.Provincia.setSizePolicy(sizePolicy)
        self.Provincia.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Provincia.setFont(font)
        self.Provincia.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Provincia.setObjectName(_fromUtf8("Provincia"))
        self.formLayout_9.setWidget(0, QtGui.QFormLayout.LabelRole, self.Provincia)
        self.text_provincia = QtGui.QLineEdit(self.centralWidget)
        self.text_provincia.setMinimumSize(QtCore.QSize(110, 20))
        self.text_provincia.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_provincia.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_provincia.setReadOnly(True)
        self.text_provincia.setObjectName(_fromUtf8("text_provincia"))
        self.formLayout_9.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_provincia)
        self.gridLayout_2.addLayout(self.formLayout_9, 4, 2, 1, 1)
        self.formLayout_10 = QtGui.QFormLayout()
        self.formLayout_10.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_10.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_10.setHorizontalSpacing(3)
        self.formLayout_10.setObjectName(_fromUtf8("formLayout_10"))
        self.text_cap = QtGui.QLineEdit(self.centralWidget)
        self.text_cap.setMinimumSize(QtCore.QSize(110, 20))
        self.text_cap.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_cap.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_cap.setReadOnly(True)
        self.text_cap.setObjectName(_fromUtf8("text_cap"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_cap)
        self.CAP = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CAP.sizePolicy().hasHeightForWidth())
        self.CAP.setSizePolicy(sizePolicy)
        self.CAP.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.CAP.setFont(font)
        self.CAP.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.CAP.setObjectName(_fromUtf8("CAP"))
        self.formLayout_10.setWidget(0, QtGui.QFormLayout.LabelRole, self.CAP)
        self.gridLayout_2.addLayout(self.formLayout_10, 4, 3, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.formLayout_14 = QtGui.QFormLayout()
        self.formLayout_14.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_14.setHorizontalSpacing(3)
        self.formLayout_14.setObjectName(_fromUtf8("formLayout_14"))
        self.Telefono = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Telefono.sizePolicy().hasHeightForWidth())
        self.Telefono.setSizePolicy(sizePolicy)
        self.Telefono.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Telefono.setFont(font)
        self.Telefono.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Telefono.setObjectName(_fromUtf8("Telefono"))
        self.formLayout_14.setWidget(0, QtGui.QFormLayout.LabelRole, self.Telefono)
        self.text_telefono = QtGui.QLineEdit(self.centralWidget)
        self.text_telefono.setMinimumSize(QtCore.QSize(110, 20))
        self.text_telefono.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_telefono.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_telefono.setReadOnly(True)
        self.text_telefono.setObjectName(_fromUtf8("text_telefono"))
        self.formLayout_14.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_telefono)
        self.gridLayout.addLayout(self.formLayout_14, 0, 0, 1, 1)
        self.formLayout_15 = QtGui.QFormLayout()
        self.formLayout_15.setHorizontalSpacing(3)
        self.formLayout_15.setObjectName(_fromUtf8("formLayout_15"))
        self.Telefono2 = QtGui.QLabel(self.centralWidget)
        self.Telefono2.setMaximumSize(QtCore.QSize(0, 0))
        self.Telefono2.setObjectName(_fromUtf8("Telefono2"))
        self.formLayout_15.setWidget(0, QtGui.QFormLayout.LabelRole, self.Telefono2)
        self.text_telefono_2 = QtGui.QLineEdit(self.centralWidget)
        self.text_telefono_2.setMinimumSize(QtCore.QSize(110, 20))
        self.text_telefono_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_telefono_2.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_telefono_2.setReadOnly(True)
        self.text_telefono_2.setObjectName(_fromUtf8("text_telefono_2"))
        self.formLayout_15.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_telefono_2)
        self.gridLayout.addLayout(self.formLayout_15, 0, 1, 1, 1)
        self.formLayout_16 = QtGui.QFormLayout()
        self.formLayout_16.setHorizontalSpacing(3)
        self.formLayout_16.setObjectName(_fromUtf8("formLayout_16"))
        self.Telefono3 = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Telefono3.sizePolicy().hasHeightForWidth())
        self.Telefono3.setSizePolicy(sizePolicy)
        self.Telefono3.setMaximumSize(QtCore.QSize(0, 0))
        self.Telefono3.setObjectName(_fromUtf8("Telefono3"))
        self.formLayout_16.setWidget(0, QtGui.QFormLayout.LabelRole, self.Telefono3)
        self.text_telefono_3 = QtGui.QLineEdit(self.centralWidget)
        self.text_telefono_3.setMinimumSize(QtCore.QSize(110, 20))
        self.text_telefono_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_telefono_3.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_telefono_3.setReadOnly(True)
        self.text_telefono_3.setObjectName(_fromUtf8("text_telefono_3"))
        self.formLayout_16.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_telefono_3)
        self.gridLayout.addLayout(self.formLayout_16, 0, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 3)
        self.formLayout_17 = QtGui.QFormLayout()
        self.formLayout_17.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_17.setHorizontalSpacing(3)
        self.formLayout_17.setObjectName(_fromUtf8("formLayout_17"))
        self.Fax = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Fax.sizePolicy().hasHeightForWidth())
        self.Fax.setSizePolicy(sizePolicy)
        self.Fax.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Fax.setFont(font)
        self.Fax.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Fax.setObjectName(_fromUtf8("Fax"))
        self.formLayout_17.setWidget(0, QtGui.QFormLayout.LabelRole, self.Fax)
        self.text_fax = QtGui.QLineEdit(self.centralWidget)
        self.text_fax.setMinimumSize(QtCore.QSize(110, 20))
        self.text_fax.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_fax.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_fax.setReadOnly(True)
        self.text_fax.setObjectName(_fromUtf8("text_fax"))
        self.formLayout_17.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_fax)
        self.gridLayout_2.addLayout(self.formLayout_17, 5, 3, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.formLayout_13 = QtGui.QFormLayout()
        self.formLayout_13.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_13.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_13.setHorizontalSpacing(3)
        self.formLayout_13.setObjectName(_fromUtf8("formLayout_13"))
        self.Email = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Email.sizePolicy().hasHeightForWidth())
        self.Email.setSizePolicy(sizePolicy)
        self.Email.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.Email.setFont(font)
        self.Email.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.Email.setObjectName(_fromUtf8("Email"))
        self.formLayout_13.setWidget(0, QtGui.QFormLayout.LabelRole, self.Email)
        self.text_mail = QtGui.QLineEdit(self.centralWidget)
        self.text_mail.setMinimumSize(QtCore.QSize(285, 0))
        self.text_mail.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_mail.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_mail.setReadOnly(True)
        self.text_mail.setObjectName(_fromUtf8("text_mail"))
        self.formLayout_13.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_mail)
        self.gridLayout_3.addLayout(self.formLayout_13, 0, 0, 1, 1)
        self.formLayout_12 = QtGui.QFormLayout()
        self.formLayout_12.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.formLayout_12.setHorizontalSpacing(3)
        self.formLayout_12.setObjectName(_fromUtf8("formLayout_12"))
        self.SitoInternet = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SitoInternet.sizePolicy().hasHeightForWidth())
        self.SitoInternet.setSizePolicy(sizePolicy)
        self.SitoInternet.setMinimumSize(QtCore.QSize(110, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.SitoInternet.setFont(font)
        self.SitoInternet.setStyleSheet(_fromUtf8("       border-bottom:1px solid;\n"
"     border-bottom-color: rgb(188, 198, 207);\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"     border-radius: 5px;\n"
"     padding: 0 0px;"))
        self.SitoInternet.setObjectName(_fromUtf8("SitoInternet"))
        self.formLayout_12.setWidget(0, QtGui.QFormLayout.LabelRole, self.SitoInternet)
        self.text_sito = QtGui.QLineEdit(self.centralWidget)
        self.text_sito.setMinimumSize(QtCore.QSize(250, 20))
        self.text_sito.setSizeIncrement(QtCore.QSize(321, 0))
        self.text_sito.setFocusPolicy(QtCore.Qt.NoFocus)
        self.text_sito.setStyleSheet(_fromUtf8("QLineEdit {\n"
"     border: 1px inset rgb(188, 189, 207);\n"
"     border-radius: 5px;\n"
"     padding: 0 3px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.127962 rgba(239, 251, 254, 255), stop:0.862559 rgba(219, 230, 239, 255));\n"
"     font: 9pt \"Arial\";\n"
"\n"
" }"))
        self.text_sito.setReadOnly(True)
        self.text_sito.setObjectName(_fromUtf8("text_sito"))
        self.formLayout_12.setWidget(0, QtGui.QFormLayout.FieldRole, self.text_sito)
        self.gridLayout_3.addLayout(self.formLayout_12, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 6, 0, 1, 4)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(801, 39))
        self.groupBox.setMaximumSize(QtCore.QSize(801, 39))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("QGroupBox {\n"
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
""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.checkBox_anagrafica = QtGui.QCheckBox(self.groupBox)
        self.checkBox_anagrafica.setEnabled(True)
        self.checkBox_anagrafica.setGeometry(QtCore.QRect(116, 9, 151, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.checkBox_anagrafica.setFont(font)
        self.checkBox_anagrafica.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkBox_anagrafica.setStyleSheet(_fromUtf8("QCheckBox {\n"
"    spacing: 0px;\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"        /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 5px;\n"
"     padding:0 px;\n"
"         font: 9pt \"Arial\";\n"
" }\n"
"\n"
"QCheckBox::indicator {\n"
"   padding:2px;\n"
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
""))
        self.checkBox_anagrafica.setCheckable(False)
        self.checkBox_anagrafica.setObjectName(_fromUtf8("checkBox_anagrafica"))
        self.date_aggiornamento = QtGui.QDateEdit(self.groupBox)
        self.date_aggiornamento.setEnabled(True)
        self.date_aggiornamento.setGeometry(QtCore.QRect(401, 10, 81, 20))
        self.date_aggiornamento.setFocusPolicy(QtCore.Qt.NoFocus)
        self.date_aggiornamento.setStyleSheet(_fromUtf8("QWidget {\n"
"    /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"}\n"
"QDateEdit{\n"
"    spacing: 0px;\n"
"    border:2px groove rgb(188, 198, 207);   \n"
"      /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));*/\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"     border-radius: 5px;\n"
"     padding: 0 px;\n"
"     font: 9pt \"Arial\";\n"
"}\n"
"\n"
"QTableView {\n"
"    border:2px groove rgb(188, 198, 207);   \n"
"      background-color: rgb(255,255,255);\n"
"alternate-background-color:rgba(210, 233, 241,130);\n"
"    font: 10pt \"Arial\";\n"
" }\n"
"  \n"
"\n"
"\n"
"QMenu { \n"
"   font-size:16px; \n"
"   width: 150px; \n"
"   left: 90px; \n"
"   background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"   color:black;\n"
"}\n"
"\n"
"QToolButton {\n"
"\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"  height: 70px; \n"
"  width: 75px;\n"
"  color:black;\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"    selection-background-color: rgb(188, 198, 207);\n"
"   selection-color:black;\n"
"}\n"
"\n"
"QListView {\n"
"  background-color:white;\n"
"  width:70px;\n"
"}\n"
"QSpinBox {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));\n"
"}\n"
""))
        self.date_aggiornamento.setWrapping(False)
        self.date_aggiornamento.setAlignment(QtCore.Qt.AlignCenter)
        self.date_aggiornamento.setReadOnly(True)
        self.date_aggiornamento.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.date_aggiornamento.setCalendarPopup(False)
        self.date_aggiornamento.setObjectName(_fromUtf8("date_aggiornamento"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(279, 10, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("  spacing: 0px;\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"        /*background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(169, 228, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.208531 rgba(212, 223, 232, 255), stop:0.905213 rgba(239, 251, 254, 255));*/\n"
"     border-radius: 5px;\n"
"     padding: 0 px;\n"
"  \n"
""))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tabWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(_fromUtf8("QTableView {\n"
"     border:2px groove rgb(188, 198, 207);   \n"
"    background-color: rgba(255, 255, 255,0);\n"
"    alternate-background-color:rgba(210, 233, 241,130);\n"
"    \n"
" }\n"
"QTableWidget{\n"
"    gridline-color:  rgb(188, 198, 207);\n"
"}\n"
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
""))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_parametri_m = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.tab_parametri_m.setFont(font)
        self.tab_parametri_m.setAutoFillBackground(False)
        self.tab_parametri_m.setStyleSheet(_fromUtf8(""))
        self.tab_parametri_m.setObjectName(_fromUtf8("tab_parametri_m"))
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_parametri_m)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.table_parametri_mmas = QtGui.QTableWidget(self.tab_parametri_m)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_parametri_mmas.setFont(font)
        self.table_parametri_mmas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_parametri_mmas.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.table_parametri_mmas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_parametri_mmas.setAlternatingRowColors(True)
        self.table_parametri_mmas.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_parametri_mmas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_parametri_mmas.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_parametri_mmas.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_parametri_mmas.setObjectName(_fromUtf8("table_parametri_mmas"))
        self.table_parametri_mmas.setColumnCount(0)
        self.table_parametri_mmas.setRowCount(0)
        self.table_parametri_mmas.horizontalHeader().setDefaultSectionSize(380)
        self.table_parametri_mmas.horizontalHeader().setMinimumSectionSize(380)
        self.table_parametri_mmas.horizontalHeader().setStretchLastSection(True)
        self.table_parametri_mmas.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout_4.addWidget(self.table_parametri_mmas, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_parametri_m, _fromUtf8(""))
        self.tab_marchi_m = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.tab_marchi_m.setFont(font)
        self.tab_marchi_m.setObjectName(_fromUtf8("tab_marchi_m"))
        self.gridLayout_5 = QtGui.QGridLayout(self.tab_marchi_m)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.table_marchi_classe = QtGui.QTableWidget(self.tab_marchi_m)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_marchi_classe.setFont(font)
        self.table_marchi_classe.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_marchi_classe.setStyleSheet(_fromUtf8("QTableWidget{    \n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
"}"))
        self.table_marchi_classe.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_marchi_classe.setDragDropOverwriteMode(False)
        self.table_marchi_classe.setAlternatingRowColors(True)
        self.table_marchi_classe.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_marchi_classe.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_marchi_classe.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_marchi_classe.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_marchi_classe.setObjectName(_fromUtf8("table_marchi_classe"))
        self.table_marchi_classe.setColumnCount(0)
        self.table_marchi_classe.setRowCount(0)
        self.table_marchi_classe.horizontalHeader().setDefaultSectionSize(250)
        self.table_marchi_classe.horizontalHeader().setMinimumSectionSize(250)
        self.table_marchi_classe.horizontalHeader().setStretchLastSection(True)
        self.table_marchi_classe.verticalHeader().setMinimumSectionSize(30)
        self.table_marchi_classe.verticalHeader().setStretchLastSection(False)
        self.gridLayout_5.addWidget(self.table_marchi_classe, 0, 0, 1, 1)
        self.table_marchi = QtGui.QTableWidget(self.tab_marchi_m)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_marchi.setFont(font)
        self.table_marchi.setStyleSheet(_fromUtf8("QTableWidget{    \n"
"background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.0181818 rgba(233, 240, 243, 255), stop:0.372727 rgba(247, 247, 247, 255), stop:0.659091 rgba(247, 247, 247, 255), stop:1 rgba(233, 240, 243, 255));\n"
"}"))
        self.table_marchi.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_marchi.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_marchi.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_marchi.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_marchi.setObjectName(_fromUtf8("table_marchi"))
        self.table_marchi.setColumnCount(0)
        self.table_marchi.setRowCount(0)
        self.table_marchi.horizontalHeader().setDefaultSectionSize(250)
        self.table_marchi.horizontalHeader().setMinimumSectionSize(250)
        self.table_marchi.horizontalHeader().setStretchLastSection(True)
        self.table_marchi.verticalHeader().setMinimumSectionSize(30)
        self.table_marchi.verticalHeader().setStretchLastSection(False)
        self.gridLayout_5.addWidget(self.table_marchi, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab_marchi_m, _fromUtf8(""))
        self.tab_potenziali_m = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.tab_potenziali_m.setFont(font)
        self.tab_potenziali_m.setObjectName(_fromUtf8("tab_potenziali_m"))
        self.gridLayout_7 = QtGui.QGridLayout(self.tab_potenziali_m)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.table_potenziali_mmas = QtGui.QTableWidget(self.tab_potenziali_m)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_potenziali_mmas.setFont(font)
        self.table_potenziali_mmas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table_potenziali_mmas.setStyleSheet(_fromUtf8(""))
        self.table_potenziali_mmas.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_potenziali_mmas.setAlternatingRowColors(True)
        self.table_potenziali_mmas.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_potenziali_mmas.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_potenziali_mmas.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_potenziali_mmas.setObjectName(_fromUtf8("table_potenziali_mmas"))
        self.table_potenziali_mmas.setColumnCount(0)
        self.table_potenziali_mmas.setRowCount(0)
        self.table_potenziali_mmas.horizontalHeader().setDefaultSectionSize(385)
        self.table_potenziali_mmas.horizontalHeader().setMinimumSectionSize(385)
        self.table_potenziali_mmas.horizontalHeader().setStretchLastSection(True)
        self.table_potenziali_mmas.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout_7.addWidget(self.table_potenziali_mmas, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_potenziali_m, _fromUtf8(""))
        self.tab_parametri_t = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.tab_parametri_t.setFont(font)
        self.tab_parametri_t.setObjectName(_fromUtf8("tab_parametri_t"))
        self.gridLayout_8 = QtGui.QGridLayout(self.tab_parametri_t)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.table_parametri_territoriali = QtGui.QTableWidget(self.tab_parametri_t)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.table_parametri_territoriali.setFont(font)
        self.table_parametri_territoriali.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_parametri_territoriali.setAlternatingRowColors(True)
        self.table_parametri_territoriali.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_parametri_territoriali.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_parametri_territoriali.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.table_parametri_territoriali.setObjectName(_fromUtf8("table_parametri_territoriali"))
        self.table_parametri_territoriali.setColumnCount(0)
        self.table_parametri_territoriali.setRowCount(0)
        self.table_parametri_territoriali.horizontalHeader().setDefaultSectionSize(250)
        self.table_parametri_territoriali.horizontalHeader().setMinimumSectionSize(250)
        self.table_parametri_territoriali.horizontalHeader().setStretchLastSection(True)
        self.table_parametri_territoriali.verticalHeader().setMinimumSectionSize(30)
        self.gridLayout_8.addWidget(self.table_parametri_territoriali, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_parametri_t, _fromUtf8(""))
        self.tab_note = QtGui.QWidget()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.tab_note.setFont(font)
        self.tab_note.setObjectName(_fromUtf8("tab_note"))
        self.gridLayout_9 = QtGui.QGridLayout(self.tab_note)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.text_note = QtGui.QTextEdit(self.tab_note)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(10)
        self.text_note.setFont(font)
        self.text_note.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255,0);\n"
" border:2px groove rgb(188, 198, 207);   "))
        self.text_note.setObjectName(_fromUtf8("text_note"))
        self.gridLayout_9.addWidget(self.text_note, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_note, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.tabWidget, 2, 0, 1, 1)
        MainWindowAnagrafica.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtGui.QToolBar(MainWindowAnagrafica)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainToolBar.sizePolicy().hasHeightForWidth())
        self.mainToolBar.setSizePolicy(sizePolicy)
        self.mainToolBar.setMinimumSize(QtCore.QSize(0, 24))
        self.mainToolBar.setMaximumSize(QtCore.QSize(16777215, 24))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(9)
        self.mainToolBar.setFont(font)
        self.mainToolBar.setAutoFillBackground(False)
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
        MainWindowAnagrafica.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.savemodButton = QtGui.QAction(MainWindowAnagrafica)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/ok_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/ok.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/ok.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.savemodButton.setIcon(icon1)
        self.savemodButton.setObjectName(_fromUtf8("savemodButton"))
        self.deletemodButton = QtGui.QAction(MainWindowAnagrafica)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/del_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/del.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/del.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.deletemodButton.setIcon(icon2)
        self.deletemodButton.setObjectName(_fromUtf8("deletemodButton"))
        self.firstButton = QtGui.QAction(MainWindowAnagrafica)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/firs_not_hovt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/first.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/first.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.firstButton.setIcon(icon3)
        self.firstButton.setObjectName(_fromUtf8("firstButton"))
        self.previousButton = QtGui.QAction(MainWindowAnagrafica)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/back_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/back.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/back.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.previousButton.setIcon(icon4)
        self.previousButton.setObjectName(_fromUtf8("previousButton"))
        self.nextButton = QtGui.QAction(MainWindowAnagrafica)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/next.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.nextButton.setIcon(icon5)
        self.nextButton.setObjectName(_fromUtf8("nextButton"))
        self.lastButton = QtGui.QAction(MainWindowAnagrafica)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/last_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/last.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/last.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.lastButton.setIcon(icon6)
        self.lastButton.setObjectName(_fromUtf8("lastButton"))
        self.newButton = QtGui.QAction(MainWindowAnagrafica)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/new_doc_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/new_doc.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/new_doc.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.newButton.setIcon(icon7)
        self.newButton.setObjectName(_fromUtf8("newButton"))
        self.modifyButton = QtGui.QAction(MainWindowAnagrafica)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/mod_doc_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/mod_doc.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/mod_doc.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.modifyButton.setIcon(icon8)
        self.modifyButton.setObjectName(_fromUtf8("modifyButton"))
        self.eraseButton = QtGui.QAction(MainWindowAnagrafica)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/eraser_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/eraser.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/eraser.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.eraseButton.setIcon(icon9)
        self.eraseButton.setObjectName(_fromUtf8("eraseButton"))
        self.pdfButton = QtGui.QAction(MainWindowAnagrafica)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/pdf_not_hov.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/pdf.png")), QtGui.QIcon.Active, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/resources/pdf.png")), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        self.pdfButton.setIcon(icon10)
        self.pdfButton.setObjectName(_fromUtf8("pdfButton"))
        self.mainToolBar.addAction(self.firstButton)
        self.mainToolBar.addAction(self.previousButton)
        self.mainToolBar.addAction(self.nextButton)
        self.mainToolBar.addAction(self.lastButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.pdfButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.newButton)
        self.mainToolBar.addAction(self.modifyButton)
        self.mainToolBar.addAction(self.eraseButton)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(self.savemodButton)
        self.mainToolBar.addAction(self.deletemodButton)
        self.mainToolBar.addSeparator()

        self.retranslateUi(MainWindowAnagrafica)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindowAnagrafica)

    def retranslateUi(self, MainWindowAnagrafica):
        MainWindowAnagrafica.setWindowTitle(QtGui.QApplication.translate("MainWindowAnagrafica", "Scheda Anagrafica", None, QtGui.QApplication.UnicodeUTF8))
        self.codiceMMAS.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Codice MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_cliente.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.CodiceCliente.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Codice Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.PotenzialeMMAS.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Potenziale MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.RagioneSociale.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Ragione Sociale", None, QtGui.QApplication.UnicodeUTF8))
        self.Titolare.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Titolare", None, QtGui.QApplication.UnicodeUTF8))
        self.CodFiscale.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Cod. Fis. / P. IVA", None, QtGui.QApplication.UnicodeUTF8))
        self.Indirizzo.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Indirizzo", None, QtGui.QApplication.UnicodeUTF8))
        self.Comune.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Comune", None, QtGui.QApplication.UnicodeUTF8))
        self.Provincia.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Provincia", None, QtGui.QApplication.UnicodeUTF8))
        self.CAP.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "CAP", None, QtGui.QApplication.UnicodeUTF8))
        self.Telefono.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Telefono", None, QtGui.QApplication.UnicodeUTF8))
        self.Telefono2.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Telefono2", None, QtGui.QApplication.UnicodeUTF8))
        self.Telefono3.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Telefono3", None, QtGui.QApplication.UnicodeUTF8))
        self.Fax.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Fax", None, QtGui.QApplication.UnicodeUTF8))
        self.Email.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Email", None, QtGui.QApplication.UnicodeUTF8))
        self.SitoInternet.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Sito Internet", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindowAnagrafica", "Certificazione", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_anagrafica.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Anagrafica Certificata", None, QtGui.QApplication.UnicodeUTF8))
        self.date_aggiornamento.setDisplayFormat(QtGui.QApplication.translate("MainWindowAnagrafica", "dd/MM/yyyy", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "Data Aggiornamento", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_parametri_m), QtGui.QApplication.translate("MainWindowAnagrafica", "Parametri MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_marchi_m), QtGui.QApplication.translate("MainWindowAnagrafica", "Marche MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_potenziali_m), QtGui.QApplication.translate("MainWindowAnagrafica", "Potenziali MMAS", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_parametri_t), QtGui.QApplication.translate("MainWindowAnagrafica", "Parametri Territoriali", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_note), QtGui.QApplication.translate("MainWindowAnagrafica", "Note", None, QtGui.QApplication.UnicodeUTF8))
        self.savemodButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "salva_modifica", None, QtGui.QApplication.UnicodeUTF8))
        self.deletemodButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "annulla_modifica", None, QtGui.QApplication.UnicodeUTF8))
        self.firstButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "primo", None, QtGui.QApplication.UnicodeUTF8))
        self.previousButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "precedente", None, QtGui.QApplication.UnicodeUTF8))
        self.nextButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "successivo", None, QtGui.QApplication.UnicodeUTF8))
        self.lastButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "ultimo", None, QtGui.QApplication.UnicodeUTF8))
        self.newButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "nuovo", None, QtGui.QApplication.UnicodeUTF8))
        self.modifyButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "modifica", None, QtGui.QApplication.UnicodeUTF8))
        self.eraseButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "cancella", None, QtGui.QApplication.UnicodeUTF8))
        self.pdfButton.setText(QtGui.QApplication.translate("MainWindowAnagrafica", "esporta in pdf", None, QtGui.QApplication.UnicodeUTF8))
        self.pdfButton.setToolTip(QtGui.QApplication.translate("MainWindowAnagrafica", "esporta in pdf", None, QtGui.QApplication.UnicodeUTF8))

import risorse_rc
