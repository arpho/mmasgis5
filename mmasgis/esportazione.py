#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import *
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from PyQt4.QtCore import pyqtSignature
from Ui_esportazione import Ui_MainWindowEsportazione
from Profilo import *
from Entity import Entity2Export
from Profilo import  *
from configurazione import *
import time


class MainWindowEsportazione(QMainWindow, Ui_MainWindowEsportazione):
	"""
	wrapper di Ui_MainWindowEsportazione
	"""
	
	def resetTables(self):
		"""
		resetta le due tabelle
		"""
		self.table_disponibili.clear()
		#self.table_disponibili.setRowCount(0)
		self.table_selezionate.clear()
		#self.table_selezionati.setRowCount(0)
	
	def insertRow(self,table,txt,Id,n):
		"""
		inserisce una riga in una tabella
		@param QTableWidget:table tabella cui si vuole aggiungere una riga
		@param string: testo da inserire nella colonna
		""" 
		item=QtGui.QListWidgetItem(txt)
		item.setData(1,Id)
		table.insertItem(n,item)


	def on_applicaEsp_released(self):
		es=self.getSelectedEntity()
		for e in es:
			self.profile.addEntity(e)
		#print self.profile.getHeaders()
		#setto il profilo  di esportazione in risultati
		self.setter.setProfile(self.profile)
		self.afterSelection()
		self.close()
		
	def isConfigurationNeeded(self):
		"""
		analizza la lista delle entita'  verificando se tra quelle inserite c'e' almeno una che richiede configurazione
		@return: bool
		"""
		#ottengo la lista delle entita'  selezionate
		es=self.getSelectedEntity()
		#instanzio un oggetto Profilo per invocarne il metodo needsConfiguration
		p=Profilo(self.db,self.user,self.activeDb)
		for i in es:
			p.addEntity(i)
		return p.needsConfiguration()
		

	def on_table_disponibili_itemDoubleClicked(self, item):
		
		#print "clicked",item.text(),item.data(1).toInt()[0]
		e= self.lookEntity4Id(item.data(1).toInt()[0])
		#verifico che sia stata trovata l'entita'
		if e!=-1:
			e.setRequired(True)
		self.resetTables()
		self.populateTableSelezionate()
		self.populateTableDisponibili()
		self.configureButton.setVisible(self.isConfigurationNeeded())
		self.applicaEsp.setDisabled(self.isConfigurationNeeded())
		
	def on_configureButton_released(self):
		# ottengo la lista delle entita' selezionate
		es=self.getSelectedEntity()
		# filtro quelle che devono essere configurate
		ec=[]
		for i in es:
			if i.needsConfiguration():
				ec.append(i)
		for i in ec:
			#print i.getHeader()
			c=Configurator(i.getHeader().lower(),self.db)
			self.ui_configurazione[i.getHeader().lower()] =WindowConfigurazione(i.getHeader().lower(),c,i,self.db)
			screen = QtGui.QDesktopWidget().screenGeometry()
			size =  self.ui_configurazione[i.getHeader().lower()].geometry()
			self.ui_configurazione[i.getHeader().lower()].move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.width()/2)
			#self.ui_configurazione[i.getHeader().lower()].setWindowTitle("Configurazione "+i.getHeader())
			self.ui_configurazione[i.getHeader().lower()].show()
		self.configureButton.setVisible(False)
		self.applicaEsp.setDisabled(False)
		#print " configuro",ec
		
	def on_table_selezionate_itemDoubleClicked(self, item):
		
	#	print "clicked",item.text(),item.data(1).toInt()[0]
		e= self.lookEntity4Id(item.data(1).toInt()[0])
		e.setRequired(False)
		e.reset()
		self.resetTables()
		self.populateTableSelezionate()
		self.populateTableDisponibili()
		self.configureButton.setVisible(self.isConfigurationNeeded())
		self.applicaEsp.setDisabled(self.isConfigurationNeeded())
		
	def lookEntity4Id(self,Id):
		"""
		ritorna l'entita' relativa allo id passato
		@param int:
		@return: Entity
		"""
		e=-1
		for i in self.entityList:
			if i.getListId()==Id:
				e=i
		return e
	
	def getSelectedEntity(self):
		"""
		ritorna le entita'selezionate con l'ordine con cui appaiono in lista
		@return: [Entity]
		"""
		l=[]
		n=0
		for i in self.entityList:
			if i.isRequired():
				l.append(i)
			#item= self.table_selezionate.takeItem(i)
			
			#e.setOrder(n)

		return l 
			
	def populateTableSelezionate(self):
		"""
		popola la tabella delle entita' selezionate
		inserendo nella tabella tutti gli elementi 
		di self.entityList che hanno il campo required settato a False
		"""
		for Id,i in enumerate(self.entityList):
			if  i.isRequired():
				n=self.table_selezionate.count()
				self.insertRow(self.table_selezionate,i.getHeader(),Id,n)
				i.setEntityId(Id) 
				
	def setAfterSelection(self,a):
		"""
		setter di self.afterSelection, questo conterra' il riferimento alla funzione da eseguire al termine della selezione delle entita'
		in quanto l'esportazione puo' essere eseguita in file di testo e file excel, in entrambi i casi occorre selezionare le entita', dopodi che si 
		possono seguire strade diverse, questo metodo dovrebbe essere invocato prima di invocare lo show di mainWindowEsportazione
		@param function: e' il metodo che usera' l'oggetto Profilo impostato da esportazione
		cioe' se il metodo viene invocato con self.excelExport in risultati, ad setAfterSelection verra' passato self.excelSelection  
		"""
		self.afterSelection=a 
	
	def populateTableDisponibili(self):
		"""
		popola la tabella delle entita' disponibili
		inserendo nella tabella tutti gli elementi 
		di self.entityList che hanno il campo required settato a False
		"""
		for Id,i in enumerate(self.entityList):
			if not i.isRequired():
				n=self.table_disponibili.count()
				self.insertRow(self.table_disponibili,i.getHeader(),Id,n)
				i.setListId(Id)
	
	def reset(self):
		for i in self.entityList:
			i.reset()
		self.profile=Profilo(self.db,self.user,self.activeDb)
		self.afterSelection=None
		self.resetTables()
		self.populateTableDisponibili()

	def onContextDisp(self,point):
		self.menu = QtGui.QMenu("Menu", self)
		actionSel = QtGui.QAction("Seleziona", self)
		actionSelAll=QtGui.QAction("Seleziona Tutto", self)
		self.menu.addAction(actionSel)
		self.menu.addAction(actionSelAll)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.table_disponibili.mapToGlobal(point))
		if action==actionSel:
			self.actionSel()
		if action==actionSelAll:
			self.actionSelAll()
			
	def actionSel(self):
		listasel=self.table_disponibili.selectedItems()
		for item in listasel:
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			#verifico che sia stata trovata l'entita'
			if e!=-1:
				e.setRequired(True)
		self.resetTables()
		self.populateTableSelezionate()
		self.populateTableDisponibili()
		self.configureButton.setVisible(self.isConfigurationNeeded())
		self.applicaEsp.setDisabled(self.isConfigurationNeeded())
		
	def actionSelAll(self):
		ndisp=self.table_disponibili.count()
		for i in range(0,ndisp):
			item=self.table_disponibili.item(i)
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			#verifico che sia stata trovata l'entita'
			if e!=-1:
				e.setRequired(True)
		self.resetTables()
		self.populateTableSelezionate()
		self.populateTableDisponibili()
		self.configureButton.setVisible(self.isConfigurationNeeded())
		self.applicaEsp.setDisabled(self.isConfigurationNeeded())
		
		
	def onContextSel(self,point):
		self.menu = QtGui.QMenu("Menu", self)
		actionDesel = QtGui.QAction("Deseleziona", self)
		actionDeselAll=QtGui.QAction("Deseleziona Tutto", self)
		self.menu.addAction(actionDesel)
		self.menu.addAction(actionDeselAll)
		action=self.menu.exec_(self.table_selezionate.mapToGlobal(point))
		if action==actionDesel:
			self.actionDesel()
		if action==actionDeselAll:
			self.actionDeselAll()
	
	def actionDesel(self):
		listasel=self.table_selezionate.selectedItems()
		for item in listasel:
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			e.setRequired(False)
			e.reset()
		self.resetTables()
		self.populateTableSelezionate()
		self.populateTableDisponibili()
		self.configureButton.setVisible(self.isConfigurationNeeded())
		self.applicaEsp.setDisabled(self.isConfigurationNeeded())

	def actionDeselAll(self):
		ndisp=self.table_selezionate.count()
		for i in range(0,ndisp):
			item=self.table_selezionate.item(i)
			e= self.lookEntity4Id(item.data(1).toInt()[0])
			e.setRequired(False)
			e.reset()
		self.resetTables()
		self.populateTableSelezionate()
		self.populateTableDisponibili()
		self.configureButton.setVisible(self.isConfigurationNeeded())
		self.applicaEsp.setDisabled(self.isConfigurationNeeded())
				
	def __init__(self,setter,db,user,activeDb,parent=None):
			self.ui_configurazione_marche=None
			self.ui_configurazione_parametri=None
			self.ui_configurazione={}
			self.ui_configurazione['marche']=self.ui_configurazione_marche
			self.ui_configurazione['parametri']=self.ui_configurazione_parametri
			QMainWindow.__init__(self,parent)
			self.setter=setter
			self.w=Ui_MainWindowEsportazione()
			self.setupUi(self)	
			self.db=db
			self.user=user
			self.activeDb=activeDb
			self.configureButton.setVisible(False)
			self.profile=Profilo(self.db,self.user,self.activeDb)
			#instanzio un oggetto che memorizzera' quale tipo di esportazione invocare quando sara' completata la selezione delle entita'
			self.afterSelection=None 
			#print self.profile.getAvailableEntity()
			#instanzio la lista delle entita
			self.entityList=[]
			#popolo la lista
			for i in self.profile.getAvailableEntity():
				#in questo caso uso un Id fittizio
				e=Entity2Export(i,False,271,self.user,self.activeDb,self.db,'anagrafica')#(header, needsConfiguration, Id) 
				self.entityList.append(e)
			#aggiungo l'entita' dei parametri che necessita di essere configurata
			parametri=Entity2Export('PARAMETRI',True,271,self.user,self.activeDb,self.db,'parametri')
			self.entityList.append(parametri)
			marche=Entity2Export('MARCHE',True,271,self.user,self.activeDb,self.db,'marche')
			self.entityList.append(marche)
			#print self.entityList
			self.populateTableDisponibili()
			self.connect(self.table_disponibili,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextDisp)
			self.connect(self.table_selezionate,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextSel)
			#self.connect(self.table_marchi_classe, SIGNAL('cellDoubleClicked(int,int)'),self.doIt)
