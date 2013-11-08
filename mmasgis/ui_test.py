# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Fri Nov 11 18:21:08 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_test(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1124, 331)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "COMUNE SELEZIONATO", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.textArea = QtGui.QLineEdit(self.centralwidget)
        self.textArea.setMinimumSize(QtCore.QSize(400, 0))
        self.textArea.setObjectName(_fromUtf8("textArea"))
        self.gridLayout.addWidget(self.textArea, 1, 0, 1, 1)
        self.tabella = QtGui.QTableWidget(self.centralwidget)
        self.tabella.setMinimumSize(QtCore.QSize(1100, 0))
        self.tabella.setDragEnabled(False)
        self.tabella.setObjectName(_fromUtf8("tabella"))
        self.tabella.setColumnCount(13)
        self.tabella.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "ragione sociale", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "indirizzo", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Codice cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Cap", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "comune", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "provincia", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "telefono1", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "telefono2", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "telefono3", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "cod. fiscale/partita iva", None, QtGui.QApplication.UnicodeUTF8))
        self.tabella.setHorizontalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("MainWindow", "Potenziale MMAS", None, QtGui.QApplication.UnicodeUTF8))
        
        self.tabella.setHorizontalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        
        self.tabella.setHorizontalHeaderItem(12, item)
        self.gridLayout.addWidget(self.tabella, 3, 0, 1, 2)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "parafarmacie", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)
        #self.menubar = QtGui.QMenuBar(MainWindow)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 27))
        #self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        #self.statusbar = QtGui.QStatusBar(MainWindow)
        #self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        item = self.tabella.horizontalHeaderItem(0)
        item = self.tabella.horizontalHeaderItem(1)
        item = self.tabella.horizontalHeaderItem(2)
        item = self.tabella.horizontalHeaderItem(3)
        item = self.tabella.horizontalHeaderItem(4)
        item = self.tabella.horizontalHeaderItem(5)
        item = self.tabella.horizontalHeaderItem(6)
        item = self.tabella.horizontalHeaderItem(7)
        item = self.tabella.horizontalHeaderItem(8)
        item = self.tabella.horizontalHeaderItem(9)
        item = self.tabella.horizontalHeaderItem(10)
        item = self.tabella.horizontalHeaderItem(11)
        item = self.tabella.horizontalHeaderItem(12)
        

