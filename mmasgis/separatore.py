#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_separatore import Ui_Separatore

class MainWindowSeparazione(QMainWindow, Ui_Separatore):
	
	def __init__(self,risultati,parent=None):
			self.risultati=risultati
			QMainWindow.__init__(self,parent)
			self.separator=None
			self.w=Ui_Separatore()
			self.setupUi(self)	
			
	def setSeparator(self):
		if self.radioButton_tab.isChecked():
			self.separator="\t"
		elif self.radioButton_vir.isChecked():
			self.separator=","
		else:
			self.separator=self.line_sep.text()
			
	def on_OKButton_released(self):
		self.setSeparator()
		#imposto il separatore in risultati
		self.risultati.setSeparator(self.separator)
		self.close()
		self.risultati.esportazione.setAfterSelection(self.risultati.tsvExport)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.risultati.esportazione.geometry()
		self.risultati.esportazione.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.width()/2)
		self.risultati.esportazione.setWindowTitle("Esportazione "+self.risultati.nomeDb.capitalize())
		self.risultati.esportazione.show()
		
