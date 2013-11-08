#!/usr/bin/python
# -*- coding: latin-1 -*-
"""
/***************************************************************************
 mmasgis
								 A QGIS plugin
 mmasgis
							  -------------------
		begin				: 2011-11-09
		copyright			: (C) 2011 by mmasgis
		email				: mmasgis@iol.it
 ***************************************************************************/

/***************************************************************************
 *																		 *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or	 *
 *   (at your option) any later version.								   *
 *																		 *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from lista import Lista
from dbSwitcher import MainWindowDbSwitcher
from LoginRefactored import *
from albero import *

from Ui_selezionegeo import *
from alberodialog import MainWindowAlbero
#import logging
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from risultati import testDialog
import time
from constants import cons
from utility import *
import re
import os
import sys
from albero import *
from Tree import *
from login import *
from gestioneUtenti import *
from sessionClasses import *
from alberodialog import *


class mmasgis:

	def converter(self,attr,key):
		"""
		converte l' attributo ricevuto
		da provincia a sigla se key e' pro
		da regione a lista di provincie se
		key e' regione
		ritorna lo stesso attributo se key=com
		"""
		result=attr
		if self.cons.attributes2convert[key]:
			#e' una provicia==> converto
			result= self.util.translateProvincia(attr)
		if  self.cons.attributes2expand[key]:
			##self.log("expanding {0}".format(attr),"test.py 50")
			print "mmasgis.py 69 regione da esplodere",str(attr)
			result =self.cons.regione[str(attr)]
			#converto le provincie inserite nella loro sigla
			pr=[self.util.translateProvincia(i) for i in result]
			##self.log("province nella regione {0}".format(attr),"test.py 55")
			##self.log("sigle province test.py 55",pr)
			##self.log("{0} espansa".format(attr),"{0} test.py 52".format(result))
		return pr
	
	def getTime(self):
		year=time.localtime()[0]
		month=time.localtime()[1]
		day=time.localtime()[2]
		hour=time.localtime()[3]
		min=time.localtime()[4]
		sec=time.localtime()[5]
		return"{0}:{1}:{2}:{3}/{4}/{5}".format(hour,min,sec,day,month,year)

	def undo(self):
		self.ui.close()
		infoString=" login non effettuato: sarà possibile usare QGIS, ma  MMASGIS 5.0 non sarà fruibile"
		d=QtGui.QMainWindow()
		QtGui.QMessageBox.warning(d,"LOGIN ANNULLATO!", infoString)

	def logged(self,user):
			self.user=user
			self.user.setLogged(True)
			#print "utente loggato in mmasgis.logged",user
			infoString="benvenuto {0} database di lavoro: {1}".format(self.user.getName(),self.user.getActiveDb().getRDBMS())
			print "Logged",infoString
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"logged user", infoString)  
			self.ds=self.ui.getDataSource()
			self.ui.close()
			
	def showTree(self):
		self.albero=Albero(self.iface,self.user)
		self.tree=Tree(self.user)
		self.albero.run()
		
	def userManager(self):
		profilo=self.user.getProfile()
		print "profilo",profilo
		####settrace()
		if profilo.isPermitted(4):
			print "funzione ammessa"
			self.gestioneUtenti_ui=MainWindowUserManager(self.user)
			self.gestioneUtenti_ui.show()
		else:
			infoString="non godi dei diritti sufficienti per questa funzione, contatta il tuo amministratore!"
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.warning(d,"NON AUTORIZZATO!!", infoString)
			

	def __init__(self, iface):
		self.dbSwitcher_ui=None
		self.censimentoSelected=False
		self.ui =LoginRefactored(True)
		self.ds=None
		self.gestioneUtenti_ui=None
		self.user=None
		QtCore.QObject.connect(self.ui,QtCore.SIGNAL("undo"),self.undo)
		QtCore.QObject.connect(self.ui,QtCore.SIGNAL("logged"),self.logged)
		self.ui.show()#comincia il login
		# Save reference to the QGIS interface
		#logging.basicConfig(filename='/home/giuseppe/.qgis/log/mmasgis.log',level=logging.DEBUG)
		self.nLayers=0
		self.iface = iface
		self.albero=Albero(iface,None)
		self.tree=Tree(None)
		self.ui_tree=MainWindowAlbero(iface,self.tree)
		self.textArea=None
		self.dlg=None
		self.selectionList=None
		self.cons=cons()
		self.util=None#non  popolera' le tabelle
		self.login=None
		self.cons=cons()
		
	def log(self, title, txt):
		logging.debug(self.getTime()+" "+title+" "+str(txt))
		
	def test(self):
			infoString="Nessuna anagrafica selezionata"
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"Attenzione", infoString)	

	def initGui(self):
		#logging.basicConfig(filename='/home/giuseppe/.qgis/log/mmasgis.log',level=logging.DEBUG)
		# Create action that will start plugin configuration
		self.action = QAction(QIcon(":/plugins/mmasgis/icon.png"), \
			"mmasgis", self.iface.mainWindow())
		# connect the action to the run method
		QObject.connect(self.action, SIGNAL("triggered()"), self.run)


		self.actionTree=QAction(QIcon(":/plugins/mmasgis/resources/tree.png"),"albero delle utb",self.iface.mainWindow())
		self.actionTree.setWhatsThis("fornisce una visualizzazione gerarchica delle utb")
		self.actionManager = QAction(QIcon(":/plugins/mmasgis/iconx.png"), "gestione utenti mmasgis", self.iface.mainWindow())
		self.actionManager.setWhatsThis("gestisce gli utenti mmasgis")
		self.iface.registerMainWindowAction(self.actionManager, "F8")   # The function should also be triggered by the F8 key
		self.iface.registerMainWindowAction(self.actionTree, "F7")   # The function should also be triggered by the F7 key
		QObject.connect(self.actionManager, SIGNAL("triggered()"), self.userManager)
		QObject.connect(self.actionTree, SIGNAL("triggered()"), self.showTree)
		
		
		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu("&mmasgis", self.action)
		self.iface.addPluginToMenu("&mmasgis", self.actionManager)
		self.iface.addPluginToMenu("&mmasgis", self.actionTree)
		self.toolBar = self.iface.addToolBar("MMASGIS")
		self.toolBar.addAction(self.actionManager)
		self.toolBar.addAction(self.actionTree)
		
	def printComune(self,feat):
		attr=feat.attributeMap()
		####settrace()
		
		s="comune: {0}, id: {1}, identificativo comune: {3}, cod: {2}".format(attr[3],feat.id(),attr[0].toString(),attr[1].toString())
		return s
		
	def getSelections(self,curLayer,key):
		####settrace()
		
		#recupero gli id degli items selezionati
		featids=curLayer.selectedFeaturesIds()
		###self.log( "chiave in getselections={0}".format(key),"test.py 102")
		  #featids = range(curLayer.featureCount())		 
		fProvider = curLayer.dataProvider()
		feat = QgsFeature()
		allAttrs = fProvider.attributeIndexes()
		fProvider.select(allAttrs)
		
		##self.log("numero campi: {0}".format(fProvider.fieldCount()),"test.py 112")
#		##self.log()
#recupero gli attributi della feature selezionata
		
		attrmap=QgsFeature().attributeMap()
		####settrace()
		####settrace()
		
		c={}
		c['pro']="provincia"
		c['com']='comune'
		c['cap']='cap'
		c['reg']='regione'
		adder={}
		adder['pro']=self.tree.addProvincia
		adder['com']=self.tree.addComune
		adder['cap']=self.tree.addCap
		adder['reg']=self.tree.addRegione
		fields={}
		fields['pro']={'header':lambda x:str(x[2][1]),'father':lambda x:x[0][1].toInt()[0],'Id':lambda x:x[1][1].toInt()[0]}
		fields['com']={'header':lambda x: unicode(x[3][1]),'father':lambda x : x[1][1].toInt()[0],'Id':lambda x: unicode( x[3][1])}# la lambda function per lo id dovrebbe essere x[2][1].toInt()[0] ma il father_id del cap e' il nome del comune, quindi lo header del comune e' pure il suo id
		fields['cap']={'header':lambda x: unicode(x[1][1]),'father':lambda x: unicode(x[6][1]),'Id':lambda x: x[0][1].toInt()[0]}
		fields['reg']={'header':lambda x:str(x[1][1]),'father':lambda x:0,'Id':lambda x:x[0][1].toInt()[0]}
		while fProvider.nextFeature(feat):
			#esploro gli attributi di feat, non sono uguali tra i vari layer
			d=[(key1,feat.attributeMap()[key1].toString()) for key1 in feat.attributeMap().iterkeys()]
			cat=str(feat.typeName())[0:3].lower()
			header=fields[cat]['header'](d)
			father=fields[cat]['father'](d)
			Id=fields[cat]['Id'](d)
			nodo=Nodo(header,Id,c[cat],father,feat.id())#(header,Id,cathegory,father,featureId)
			
			#print "sto aggiungendo ",nodo
			adder[cat](nodo)
			if key=="com":
				pass###self.log("campi del comune: {0}".format(self.printComune(feat)),"mmasgis.py 131")
		myFields = fProvider.fields()
		allFieldsNames= [f.name() for f in myFields.values()]
		myFieldsNames=[]
		for f in myFields.values():
			print 'for', f.name()
			##self.log("myFields.type {0}".format(f.typeName()),"test.py 127")
			if f.typeName() == "Real":
				##self.log("casting real {0}".format(f),"test.py 129")				
				myFieldsNames.append(f.name())
			if f.typeName() == "String":
				##self.log("casting string ok {0}".format(f),"test.py 116")
				myFieldsNames.append(f.name())
		if len(myFieldsNames) == 0:
		  # QMessageBox.information(self.iface.mainWindow(),"Warning","No string field names. Exiting")
		   return
		elif len(myFieldsNames) == 1:
			#se c'e' un solo nome seleziono il primo
			
			rfield = myFieldsNames[0]
		   ##self.log("attrfield test.py 127",attrfield)
		else:
		  attrfield=myFieldsNames[0]

		  attrindex = allFieldsNames.index(attrfield)
		  ##self.log("attrindex test.py 109", attrindex)
		  ##self.log("featids test.py 110",featids)
		  #return attrindex
	   # adumpfile = QFileDialog.getSaveFileName(None, "save file dialog", attrfield +'.txt', "Text (*.txt)")
#		selectionList =[]
		
		for fid in featids:
			features={}
			result={}
			features[fid]=QgsFeature()
		   ###self.log("fid  test.py 119",fid)
		   ###self.log("features[fid] test.py 120",features[fid])
			curLayer.featureAtId(fid,features[fid])
		   ####settrace()
		   #prendo la tabella degli attributi
			attrmap=features[fid].attributeMap()
#		   ##self.log("attrmap test.py 124",attrmap)
		   ##self.log("comune {0}, indice {1}, provincia {2}".format(len(attrmap.values()),attrmap.values(),attrmap.values()),"mmasgis.py 177")

			attr=attrmap.values()[self.cons.attributes[key]]#in ogni layer la colonna degli attributi utile cambia
			attr=attr.toString()
			getId={}
			getId['pro']=lambda x: int(str(x[1].toString()))
			getId['reg']=lambda x: int(str(x[0].toString()))
			getId['com']=lambda x: int(str(x[2].toString()))
			getId['cap']=lambda x: str(x[1].toString())
			Id=getId[key](attrmap)
			#Id=fields[key]['Id'](attrmap)
		   ##self.log("attr inviato a lista={0}".format(attr),"test.py 175")
			self.selectionList.appendItem([key,unicode(attr),Id])
		   
		   ##self.log("selectionLIst test.py 178",self.selectionList.getList())
#		   ##self.log("selectionList test.py 131 ",self.selectionList)
		####settrace()
		print "utb selezionate",self.selectionList.getList()
		#settrace()
		return self.selectionList

	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu("&mmasgis",self.action)
		self.iface.removeToolBarIcon(self.action)
	def addList(self,a,b):
		pass #return a+b
	def search(self,string,pattern):
		match=re.compile(pattern)
		b=False
		if match.search(string):
			b=True
		return b
	def match(self,string,pattern):
		match=re.compile(pattern)
		b=False
		if match.match(string):
			b=True
		return b
		
	
	def makeList(self):
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		
		curLayer = self.iface.mapCanvas().currentLayer()
		mc=self.iface.mapCanvas() 
		self.nLayers=mc.layerCount() 
		self
		##self.log("nLayers test.py 194",self.nLayers)
		
		# rimuovo  il layer aggiunto dal plugin openLayers
		#non posso cambiare il dict mentre sono in un ciclo 
		#quindi creo un dict con i soli layers che mi interessano
		dummymap={}
		for key in layersmap.iterkeys():
			if (self.search(str(key),"_g"))or(self.match(str(key),'Cap')):
				dummymap[key]=layersmap[key]
		##self.log("dummymap={0}".format(dummymap),"203 test.py")
		##self.log("layersmap={0}".format(layersmap),"204 test.py")
		##self.log("lunghezza dummy={0}".format(len(dummymap)),"lunghezza original={0}".format(len(layersmap)))
		for key in dummymap.iterkeys():
			##self.log("esamino layers {0}".format(key),"test.py 212")
			##self.log("type(key {0}".format(type(key))," ###")
			curLayer=layersmap[key]
			fProvider = curLayer.dataProvider()
			myFields = fProvider.fields()
			####settrace()
			##self.log("attributi nel layer {0}: {1}".format(curLayer.name(),[f.name() for f in myFields.values()]),"mmasgis.py 245")
			# verificato cicla una volta
			#aggiungo la lista dei campi selezionati  sul layer
			chiave=str(key[0:3])
			##self.log("full key {0}".format(key),"test.py 214")
			##self.log("key  troncata test.py 215",key[0:3])
			##self.log("chiave convertita test.py 216",self.cons.typeItem[chiave.lower()])
			self.ui_tree.addLayer(str(key).lower()[0:3], curLayer)
			self.getSelections(curLayer,chiave.lower())
			####settrace()
			###self.log("nome layer for key={0}  in selectionList test.py 161".format(key),self.selectionListget[0])
			
			
			##self.log("selectionList test.py 248",self.selectionList.getList())
		
		
	def censusSelected(self,db):
		self.dbSwitcher_ui.close()
		db.setUserName("metmi")
		db.setPassword("metmi")
		#e' stato selezionato il censimento ma manca la porta e la famiglia del server che sono presenti nel db attivo passato da loginrefactored
		db.setPort(self.user.getActiveDb().getPort())
		db.setRDBMS(str(self.user.getActiveDb().getRDBMS()))
		self.user.setActiveDb(db)
		print "utente loggato",self.user
		self.analyze(self.user)
		
	# run method that performs all the real work
	def run(self):
		if not self.censimentoSelected:
			self.dbSwitcher_ui=MainWindowDbSwitcher(self.user,self.ds)
			self.dbSwitcher_ui.show()
			QtCore.QObject.connect(self.dbSwitcher_ui,QtCore.SIGNAL("dbSelected"),self.censusSelected)
	

			
		
			screen = QtGui.QDesktopWidget().screenGeometry()
			#size =  self.login.geometry()
			#self.login.move((screen.width()/2)-(size.width()/2),(screen.height()/2)-size.height())
			#self.login.show()
		else:
			self.mmasgis(self.user)
		
	"""
	analizza i layers cercando le selezioni effettuate
	"""
	def analyze(self,user):
		print "***selezioni su finestra "+str(self.ui_tree.getList()) 
		self.selectionList=Lista(user,user.getActiveDb())
		self.util=utility([],0,user,user.getActiveDb())#non  potra' popolare' le tabelle
		# create and show the dialog
		curLayer = self.iface.mapCanvas().currentLayer()
		#elenco tutti gli elementi del layer corrente
		featids = range(curLayer.featureCount())
		#creo la lista della selezioni

		self.makeList()
		print("SSScomuni selezionati mmasgis.py 430",self.selectionList.getList())
		self.dlg = testDialog(self.selectionList.getList(),user,user.getActiveDb())
		NomeDb=user.getActiveDb().getNameDb()
		self.dlg.setWindowTitle("Elenco Anagrafiche "+NomeDb.capitalize())
		# show the dialog
		self.dlg.show()
		#app=QtGui.QApplication(["show",""],True)
		#resetto la lista
		self.selectionList.resetList()
		#sys.exit(app.exec_())
		result=1
		#dlg.traccheggio()
		# See if OK was pressed
		if result == 1:
			# do something useful (delete the line containing pass and
			# substitute with your code
			pass


	def mmasgis(self,user):
		self.util=utility([],0,user,user.getActiveDb())#non  potra' popolare' le tabelle
		self.selectionList=Lista(user,user.getActiveDb())
		# create and show the dialog
		#####settrace()
		curLayer = self.iface.mapCanvas().currentLayer()
		#elenco tutti gli elementi del layer corrente
		featids = range(curLayer.featureCount())
		#creo la lista della selezioni
		self.makeList()
		self.log("comuni selezionati mmasgis.py 297",self.selectionList.getList())
		self.log("lista inviata a testDialog {0} ".format(self.selectionList.getList()),"test.py 212")
		self.dlg = testDialog(self.selectionList.getList(),user,user.getActiveDb())
		# show the dialog
		self.dlg.show()
		#app=QtGui.QApplication(["show",""],True)
		#resetto la lista
		self.selectionList.resetList()
		#sys.exit(app.exec_())
		result=1
		#dlg.traccheggio()
		# See if OK was pressed
		if result == 1:
			# do something useful (delete the line containing pass and
			# substitute with your code
			pass	
from Odict import *
