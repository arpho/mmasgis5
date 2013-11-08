#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_cercageo import *

class MainWindowCercaGeo(QMainWindow, Ui_CercaGeo):
	"""wrapper di Ui_MainWindowAnagrafica
	"""
	
	def __init__(self,tree,parent=None):
			self.tree=tree
			QMainWindow.__init__(self,parent)
			#self.w=Ui_ProgressBar()
			self.setupUi(self)		
			#QMainWindow.__init__(self,parent)
			self.w=Ui_CercaGeo()
			#self.setupUi(self)					
	
	def on_nome_ricerca_returnPressed(self):
		name=self.nome_ricerca.text()
		radio={}
		radio['cap']=self.cercaCap
		radio['comune']=self.cercaCom
		radio['provincia']=self.cercaProv
		cat=""
		for k in radio.iterkeys():
			if radio[k].isChecked():
				cat=k
		msg=[name,cat]
		self.emit(QtCore.SIGNAL("myExplode"), msg)
		#self.close()

	
	def on_cercaButton_released(self):
		name=self.nome_ricerca.text()
		radio={}
		radio['cap']=self.cercaCap
		radio['comune']=self.cercaCom
		radio['provincia']=self.cercaProv
		cat=""
		for k in radio.iterkeys():
			if radio[k].isChecked():
				cat=k
		msg=[name,cat]
		self.emit(QtCore.SIGNAL("myExplode"), msg)
		#self.close()