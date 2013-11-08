#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_logcensimento import *

class MainWindowLogCensimento(QMainWindow, Ui_LogCensimento):
	
	def __init__(self,db_list,parent=None):
			QMainWindow.__init__(self,parent)
			self.dbs=db_list
			self.w=Ui_LogCensimento()
			self.setupUi(self)	
			for i in self.dbs:
				#self.listCensimenti.addItem(i.getNameDb(), QtCore.QVariant(i))
				#self.listCensimenti.setItemData(n,QtCore.QVariant(i),3)
				item=self.itemBuilder(i)
				self.listCensimenti.addItem(item)
	
	def itemBuilder(self,i):
		"""costruisce l'item per qlistwidget
		@param Db:Db da elencare
		@return QListWidgetItem
		"""
		item=QtGui.QListWidgetItem(i.getNameDb())
		item.setData(3,QtCore.QVariant(i)) 	
		return item		
			
	def writeDescription(self,txt):
		self.descrizione.setText(txt)
	
	def on_OKButton_released(self):
		"""
		slot collegato al pulsante OK
		setta attivo il db selezionato ed emette il segnale logCensimento che viene intercettato da login, che si occupa di completare il processo
		 di logging
		"""
		msg="messaggio di ack censimento"
		#index=self.listCensimenti.currentIndex()
		#data=self.listCensimenti.itemData(index, 3)
		if self.listCensimenti.currentItem() is None:
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"Attenzione", "Seleziona un censimento")
		else:
			itemsel=self.listCensimenti.currentItem()
			data=itemsel.data(3)
			pyobj=data.toPyObject()
			pyobj.setActive(True)		
			self.emit(QtCore.SIGNAL("logCensimento"), msg)
			self.close()
		
	def on_listCensimenti_itemClicked(self,item):
		data=item.data(3)
		pyobj=data.toPyObject()
		description=pyobj.getDescription()
		self.writeDescription( description)
		
	def on_listCensimenti_itemActiveted(self,item):
		data=item.data(3)
		pyobj=data.toPyObject()
		description=pyobj.getDescription()
		self.writeDescription( description)

		
		