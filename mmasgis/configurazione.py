#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_configurazione import *
from Configurator import *
from EntityElements import *

class WindowConfigurazione(QMainWindow, Ui_Configurazione):
	
	def insertRow(self,table,txt,Id,n):
			"""
			inserisce una riga in una tabella
			@param QTableWidget:table tabella cui si vuole aggiungere una riga
			@param string: testo da inserire nella colonna
			@param int: n posizione nella riga in cui inserire lo item 
			""" 
			item=QtGui.QListWidgetItem(txt)
			item.setData(1,Id)
			table.insertItem(n,item)
			
	def resetList(self):
		"""
		resetta le due liste
		"""
		self.table_disp.clear()
		#self.table_disponibili.setRowCount(0)
		self.table_sel.clear()
		#self.table_selezionati.setRowCount(0)
		
	def lookEntity4Id(self,Id):
		"""
		ritorna l'entita' relativa allo id passato
		@param int:
		@return: Entity
		"""
		e=-1
		for i in self.elementsList:
			if i.getId()==Id:
				e=i
		return e
		
	def updateLists(self):
		"""
		aggiorna l'elenco delle due liste
		scorre self.elementsList gli elementi in cui  il campo required e' settato a False sono  visualizzati nella prima lista
		gli altri nella seconda
		"""
		self.resetList()
		for i in self.elementsList:
			if i.isRequired():
				self.insertRow(self.table_sel, i.getHeader(), i.getId(),self.table_sel.count())
			else:
				self.insertRow(self.table_disp, i.getHeader(), i.getId(),self.table_disp.count())
				
	def on_table_disp_itemDoubleClicked(self, item):
		
		e= self.lookEntity4Id(item.data(1).toInt()[0])
		e.setRequired(True)
		self.updateLists()
		
	def on_table_sel_itemDoubleClicked(self, item):
		e= self.lookEntity4Id(item.data(1).toInt()[0])
		e.setRequired(False)
		self.updateLists()
		
	def on_apply_conf_released(self):
		#aggiungo le entita' selezionate a self.configurator
		for i in self.elementsList:
			if i.isRequired():
				if self.tab=='marche':
					i.setMax(self.spin_num.value())
				self.configurator.addElement(i,self.db)
		self.entity.setConfigurator(self.configurator)
		self.entity.setConfigured(True)
		self.close()
		#print "applico configurazione a"
	
	def onContextDisp(self, point):
		self.menu = QtGui.QMenu("Menu", self)
		actionSel = QtGui.QAction("Seleziona", self)
		actionSelAll=QtGui.QAction("Seleziona Tutto", self)
		self.menu.addAction(actionSel)
		self.menu.addAction(actionSelAll)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.table_disp.mapToGlobal(point))
		if action==actionSel:
			self.actionSel()
		if action==actionSelAll:
			self.actionSelAll()
	
	def actionSel(self):
		listasel=self.table_disp.selectedItems()
		for item in listasel:
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			e.setRequired(True)
		self.updateLists()
	
	def actionSelAll(self):
		ndisp=self.table_disp.count()
		for i in range(0,ndisp):
			item=self.table_disp.item(i)
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			e.setRequired(True)
		self.updateLists()
	
	
	def onContextSel(self, point):
		self.menu = QtGui.QMenu("Menu", self)
		actionDesel = QtGui.QAction("Deseleziona", self)
		actionDeselAll=QtGui.QAction("Deseleziona Tutto", self)
		self.menu.addAction(actionDesel)
		self.menu.addAction(actionDeselAll)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.table_sel.mapToGlobal(point))
		if action==actionDesel:
			self.actionDesel()
		if action==actionDeselAll:
			self.actionDeselAll()
	
	def actionDesel(self):
		listasel=self.table_sel.selectedItems()
		for item in listasel:
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			e.setRequired(False)
		self.updateLists()
	
	def actionDeselAll(self):
		ndisp=self.table_sel.count()
		for i in range(0,ndisp):
			item=self.table_sel.item(i)
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			e.setRequired(False)
		self.updateLists()
	
		
	def __init__(self,tab,c,e,db):
		"""
		inizializza la gui di configurazione delle entita'
		@param string: classe o tab di appartenenza dell'entita' <'MARCHE'><'PARAMETRI'>
		@param Configurator:i
		@note: il valore del tab fa si che il testo delle entichette sopra le due liste sia adeguato all'entita'  
		inoltre la casella per la selezione del numero max di marche e' visibile esclusivamente se tab ='marche'
		"""
		label={}
		self.entity=e
		self.configurator=c 
		label['marche']=["CLASSI MARCHE DISPONIBILI","CLASSI MARCHE SELEZIONATE"]
		label['parametri']=["PARAMETRI DISPONIBILI","PARAMETRI SELEZIONATI"]
		visible={}
		visible['marche']=True
		visible['parametri']=False
		self.tab=tab.lower()
		QMainWindow.__init__(self,parent=None)
		self.w=Ui_Configurazione()
		self.setupUi(self)
		self.label.setText(label[self.tab][0])
		self.label_2.setText(label[self.tab][1])
		self.label_num.setVisible(visible[self.tab])
		self.spin_num.setVisible(visible[self.tab])
		#self.setWindowTitle("Configurazione "+self.tab.lower()+nomeDb.capitalize())
		self.db=db
		c=Configurator(self.tab,self.db)
		#genero la lista degli elementi selezionabili
		self.elementsList=[]
		l=c.getAvailableElements(self.tab)
		for i in l:
			#print i
			e=EntityElement(i['Id'],self.tab,self.db)# il costruttore richiede class_id e tab
			self.elementsList.append(e)
			#c.addElement()
		self.updateLists()
		self.connect(self.table_disp,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextDisp)
		self.connect(self.table_sel,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextSel)	
		
		