"""
/***************************************************************************
 Albero
								 A QGIS plugin
 permette di selezionare rapidamente gli elementi di un progetto qgis tramite una struttura ad albero
							  -------------------
		begin				: 2012-04-06
		author			: (C) 2012 by Giuseppe D'Amico
		email				: damicogiuseppe77@gmail.com
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
from tree_sqlalchemy_class import  *
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from tree_sqlalchemy_class import *
import PyQt4 
import re
from qgis.core import *
from Tree import *
from progressBar import *
from functools import partial
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from alberodialog import *
import MySQLdb

class Albero:
	
		
	def makeList(self):
		""""
		genera la lista delle selezioni e' invocato direttamente dal metodo run
		"""
		#ottengo l'elenco dei layers caricati nel progetto
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		
		curLayer = self.iface.mapCanvas().currentLayer()
		mc=self.iface.mapCanvas() 
		#self.log("nLayers test.py 194",self.nLayers)
		
		# rimuovo  il layer aggiunto dal plugin openLayers
		#non posso cambiare il dict mentre sono in un ciclo 
		#quindi creo un dict con i soli layers che mi interessano
		dummymap={}
		print "inizio generazione albero"		
		for key in layersmap.iterkeys():
			if (self.search(str(key),"_g"))or(self.match(str(key),'Cap')):
				dummymap[key]=layersmap[key]
		#self.log("dummymap={0}".format(dummymap),"203 test.py")
		#self.log("layersmap={0}".format(layersmap),"204 test.py")
		#self.log("lunghezza dummy={0}".format(len(dummymap)),"lunghezza original={0}".format(len(layersmap)))
		for key in dummymap.iterkeys():
		#	self.log("esamino layers {0}".format(key),"test.py 212")
		#	self.log("type(key {0}".format(type(key))," ###")
			curLayer=layersmap[key]
			#print "curLayer {0} for key {1}".format(curLayer,key)
			fProvider = curLayer.dataProvider()
			myFields = fProvider.fields()
			####settrace()()
			#self.log("attributi nel layer {0}: {1}".format(curLayer.name(),[f.name() for f in myFields.values()]),"mmasgis.py 245")
			# verificato cicla una volta
			#aggiungo la lista dei campi selezionati  sul layer
			chiave=str(key[0:3])
			#self.log("full key {0}".format(key),"test.py 214")
			#self.log("key  troncata test.py 215",key[0:3])
			#self.log("chiave convertita test.py 216",self.cons.typeItem[chiave.lower()])
			self.ui_tree.addLayer(str(key)[0:3], curLayer)
			self.analizeLayers(curLayer,chiave.lower())
			####settrace()()
			#self.log("nome layer for key={0}  in selectionList test.py 161".format(key),self.selectionListget[0])
			
			
	#		self.log("selectionList mmasgist.py 283",self.selectionList.getList())
		
		
		

	
	def analizeLayers(self,curLayer,key,nameLayer):
		"""
		interroga il layer passato come parametro e ritorna la lista delle selezioni sul layer
		@param curLayer: oggetto Layer di Qgis
		@param key: String tipo di selezione'reg'/'com'/'pro'   
		"""
		layersName={}
		layersName['reg']="delle regioni"
		layersName['com']=" dei comuni"
		layersName['cap']=" dei cap"
		layersName['pro']="delle province"	
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.progressBar.geometry()
		self.progressBar.setValueLabel("analisi del  layer"+layersName[key] +" in corso")
		#print "XXXlayer",key
		self.progressBar.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.height())
		self.progressBar.show()
		
		#recupero gli id degli items selezionati
		featids=curLayer.selectedFeaturesIds()
		#self.log( "chiave in getselections={0}".format(key),"test.py 102")
		#featids = range(curLayer.featureCount())		 
		fProvider = curLayer.dataProvider()
		self.progressBar.setMaximumPartial(fProvider.featureCount())
		feat = QgsFeature()
		allAttrs = fProvider.attributeIndexes()
		fProvider.select(allAttrs)
		attrmap=QgsFeature().attributeMap()

		c={}# dict delle  categorie da settare nel Nodo
		c['pro']="provincia"
		c['com']='comune'
		c['Cap']='Cap'
		c['reg']='regione'
		adder={}
		adder['pro']=self.tree.addProvincia
		adder['com']=self.tree.addComune
		adder['Cap']=self.tree.addCap
		adder['reg']=self.tree.addRegione
		fields={}
		fields['pro']={'header':lambda x:str(x[2][1]),'father':lambda x:x[0][1].toInt()[0],'Id':lambda x:x[1][1].toInt()[0]}
		fields['com']={'header':lambda x: unicode(x[3][1]),'father':lambda x : x[1][1].toInt()[0],'Id':lambda x: unicode( x[3][1])}# la lambda function per lo id dovrebbe essere x[2][1].toInt()[0] ma il father_id del cap e' il nome del comune, quindi lo header del comune e' pure il suo id
		fields['Cap']={'header':lambda x: unicode(x[1][1]),'father':lambda x: unicode(x[6][1]),'Id':lambda x: x[0][1].toInt()[0]}
		fields['reg']={'header':lambda x:str(x[1][1]),'father':lambda x:0,'Id':lambda x:x[0][1].toInt()[0]}
		###settrace()()
		n=0
		while fProvider.nextFeature(feat):
			
			#esploro gli attributi di feat non sono uguali tra i vari layer
			d=[(key1,feat.attributeMap()[key1].toString()) for key1 in feat.attributeMap().iterkeys()]
			#print d 
			cat=str(feat.typeName())[0:3]
			header=fields[cat]['header'](d)
			father=fields[cat]['father'](d)
			Id=fields[cat]['Id'](d)
			#self.log("header",header)
			#self.log('father',father)
			#self.log("id",Id)
			
			nodo=Nodo(header,Id,c[cat],father,feat.id())#(header,Id,cathegory,father)
			adder[cat](nodo)
			#print "aggiunto nodo per",cat
			n=n+1
			#print "analisi layer {1} eseguita al {0}% ".format((n/fProvider.featureCount())*100,nameLayer)
			self.progressBar.setValueParticular(n)					
			
		
	def match(self,string,pattern):
		match=re.compile(pattern)
		b=False
		if match.match(string):
			b=True
		return b
	"""
	@param iface: e' l'oggetto richiesto da qgis per avviare il plugin dell'albero
	@param user: oggetto user creato dalla procedura di login contiene le informazioni relative al db attivo
	@note: con l'introduzione del secondo parametro la classe  Albero non puo' esssere usata per il plugin albero
	"""
	def __init__(self, iface,user):
		# Save reference to the QGIS interface
		self.iface = iface
		self.message=None
		self.tree=Tree(user)
		self.message="selected"
		self.progressBar=ProgressBarWindow(True,True)# apro la progress bar con due barre
		self.progressBar.setMaximumOverall(4)
		self.ui_tree=MainWindowAlbero(iface,self.tree)
		#self.tree
		
	def testExport(self,L):
		f=open("/home/giuseppe/Scrivania/treeNodes.json","w")
		#self.t.childrenAdder(self.t.getProvincia(), self.t.getComune())
		#f.write("var treeNodes={text:'root','expanded':true,'children'"+":[") #file js
		f.write('{"text":"root","expanded":"true","children"'+":[")
		l=L[0:1]#prendo  un sottoinsieme di regioni
		#l.export(f)
		for p in l:
			p.exportJson(f)
		f.write("]}")
		
	def exportDb(self,L):
		dbfile='root'+":"+'mmasgisDB'+'@'+'localhost'+":"+'3306'
		engine = create_engine('mysql://root:vilu7240@localhost/mmasgisDB?charset=utf8&use_unicode=0', pool_recycle=3600)
		
		connection =MySQLdb.connect(user='root',passwd='vilu7240',db='mmasgisDB',host='localhost')# engine.connect()
		cur=connection.cursor()
		metadata = MetaData(bind=engine)
		Session = sessionmaker(bind=engine)
		session=Session()
		c=0
		for p in L:
			print " nodo ",c
			c+=1
			p.exportDb(session,-1)
		session.commit()
	def treeMaker(self):
		self.tree.resetTree()
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		
		curLayer = self.iface.mapCanvas().currentLayer()
		mc=self.iface.mapCanvas() 
		#self.log("nLayers test.py 194",self.nLayers)
		
		# rimuovo  il layer aggiunto dal plugin openLayers
		#non posso cambiare il dict mentre sono in un ciclo 
		#quindi creo un dict con i soli layers che mi interessano
		dummymap={}
		for key in layersmap.iterkeys():
			if (self.search(str(key),"_g"))or(self.match(str(key),'Cap')):
				dummymap[key]=layersmap[key]
		#self.log("dummymap={0}".format(dummymap),"203 test.py")
		#self.log("layersmap={0}".format(layersmap),"204 test.py")
		#self.log("lunghezza dummy={0}".format(len(dummymap)),"lunghezza original={0}".format(len(layersmap)))
		n=0
		for key in dummymap.iterkeys():

			self.progressBar.setValueOverall(n)
		#	self.log("esamino layers {0}".format(key),"test.py 212")
		#	self.log("type(key {0}".format(type(key))," ###")
			curLayer=layersmap[key]
			chiave=str(key[0:3])
			#aggiungo il layer che verra' usato per selezionare le features sulla mappa
			self.ui_tree.addLayer(str(key)[0:3], curLayer)
			self.analizeLayers(curLayer,chiave.lower(),str(key))
			n+=1
		lista_nodi=self.tree.treeBuilder()
		#self.testExport(lista_nodi)
		#self.exportDb(lista_nodi)
		#creo il file javascript per l'albero
		for i  in lista_nodi:
			if self.ui_tree.albero.topLevelItemCount()<20:
				self.ui_tree.albero.addTopLevelItem(i.getNode())
		#print " nodi dell'albero",self.ui_tree.albero.topLevelItemCount()
		self.ui_tree.etichetta.setText("Italia")
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.ui_tree.geometry()
		self.ui_tree.move((screen.width()/2)-size.width()*2,(screen.height()/2)-size.width())
		self.ui_tree.show()
			
		self.progressBar.close()

	def initGui(self):
		# Create action that will start plugin configuration
		self.action = QAction(QIcon(":/plugins/Albero/icon.png"), \
			"visualizzazione ad albero", self.iface.mainWindow())
		# connect the action to the run method
		QObject.connect(self.action, SIGNAL("triggered()"), self.run)

		# Add toolbar button and menu item
		self.iface.addToolBarIcon(self.action)
		self.iface.addPluginToMenu("&visualizzazione ad albero", self.action)
		
	def search(self,string,pattern):
		"""
		esegue il metodo search su una stringa:
		@param string: stringa da analizzare
		@param string: pattern dell' espressione regolare
		@return: boolean  
		"""
		match=re.compile(pattern)
		b=False
		if match.search(string):
			b=True
		return b
	def putNode(self,nodo):
		"""inserisce un nodo nella lista di selezionegeo
		@param Nodo:
		"""
		self.ui_tree.selectNode(nodo) 
		
	def getSelectedNodes(self,selections):
		"""
		ritorna la lista dei nodi relativiu alla lista dei feat_id passata
		@param [long,string:  [(feat_id,layer_alias<'cap'>,<'regione'>,<'comune'>,<'provincia'>)] 
		@return: [Nodo]
		"""
		selectedNodes=[]
		for i in selections:
			print "selezioni",i
			nodo=self.tree.fetchNode(i[1], i[0])
			selectedNodes.append(nodo)
		return selectedNodes
	
	def showNodes(self,selectedNodes):
		""" inserisce  i nodi presenti nella lista passata in selezionegeo
		@param [Nodo]:
		"""  
		for nodo in selectedNodes:
			#seleziono il nodo e tutti i suoi discendenti  
			nodo.setSelected(True,True)
			#e rendo visibile  il nodo
			nodo.setVisible(True)
			# visualizzo la finestra delle selezioni geografiche
			self.ui_tree.showSelectionGui()
			# aggiungo il nodo alla finestra
			self.putNode(nodo)		
	
	def slotSelectionChanged(self,*a):
		""" slot connesso al segnale selectionChanged di qgis
		"""
		selections=self.getSelectionsByMetadataLayer(a[0],a[1])
		selectedNodes=self.getSelectedNodes(selections)
		if len(selectedNodes)==0:
			self.ui_tree.reset()
		self.showNodes(selectedNodes)
	
	def getSelectionsByMetadataLayer(self, *a):
		"""ritorna la lista delle features selezionate sul layer di cui vengono passati i metadata
		@param *string:(string,qgsVectorLayer): self.message, QGSVectorLayer
		@return: [(long,string)]: [(feat_id,layer_alias<'cap'>,<'regione'>,<'comune'>,<'provincia'>)] 
		"""
		#####settrace()()
		#print "argomenti"+str(a)
		#print "metadata"#+()
		#print self.retrieveLayer(a[1].metadata())
		#print "selected Ids",
		#print self.message+str(self.n)
		metadata=a[1].name()
		layer=self.retrieveLayer(metadata)
		selectedFeatures=a[1].selectedFeaturesIds()	
		selectedNodes=[]
		for i in selectedFeatures:
			#nodo=self.tree.fetchNode(layer, i)
			#nodo.setSelected(True,True)
			#nodo.setVisible(True)
			#print "e' stata cliccato",str(nodo)
			selectedNodes.append((i,layer))
		return selectedNodes
		"""			
		for n in selectedNodes:
			#print "selezione "+str(n)+"\n"
			#aggiungo il nodo a selectionGui
			self.ui_tree.selectNode(n)
		"""
		#self.dlg.listWidget.addItem(item)	
	
	def retrieveLayer(self,metadata):
		"""
		determina il nome del layer dai suoi metadata
		@param string:metadata del layer
		@return: string sigla layer:<'cap',<'pro'>,<'reg'>,<'com'>
		"""
		layersTest=[]
		layersTest.append(('regione','reg'))
		layersTest.append(('provincia','prov'))
		layersTest.append(('comune','comuni'))
		layersTest.append(('cap','CAP'))
		for i in layersTest:
			if self.search(metadata, i[1]):
				return i[0]					
			
		
	
	def selectedChanged(self,t):
		#self.ui_tree.etichetta.setText(self.getLayer())
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		curLayer = curLayer=layersmap[layersmap.keys()[0]]#self.iface.mapCanvas().currentLayer()
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		fProvider = curLayer.dataProvider()		
		myFields = fProvider.fields()
		featids=curLayer.selectedFeaturesIds()
		#self.log( "chiave in getselections={0}".format(key),"test.py 102")
		#featids = range(curLayer.featureCount())		 

		feat = QgsFeature()		

	def unload(self):
		# Remove the plugin menu item and icon
		self.iface.removePluginMenu("&visualizzazione ad albero",self.action)
		self.iface.removeToolBarIcon(self.action)

	# run method that performs all the real work

		
		#if map 
	def getLayer(self):
		""" ritorna la sigla del layer corrente
		@return: string <'reg'>,<'pro'>,<'cap'>,<'com'>
		"""
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		curLayer= self.iface.mapCanvas().currentLayer()#layersmap[layersmap.keys()[0]]
		if curLayer is None:
			curLayer=layersmap[layersmap.keys()[0]]
		fProvider = curLayer.dataProvider()
		fProvider = curLayer.dataProvider()
		fieldMap=fProvider.fieldNameMap()		
		layers={}
		regione=PyQt4.QtCore.QString(unicode('NOME_REG'))#1
		provincia= PyQt4.QtCore.QString(unicode('SIGLA_PRO'))#5
		comune=PyQt4.QtCore.QString(unicode('NOME_COM'))# 6
		cap=PyQt4.QtCore.QString(unicode('nome1'))#2
		layers[regione]=(1,"reg")#(valore della chiave nella maplist del layer,sigla del layer
		layers[provincia]=(5,"pro")
		layers[comune]=(3,"com")
		layers[cap]=(2,"Cap")
		for k in layers.iterkeys():
			if fieldMap.has_key(k):
				print "chiave presente {0}".format(k)
				if layers[k][0]==fieldMap[k]:
					return layers[k][1] 
				
	def findAllSelections(self):
		""" ritorna le selezioni effettuate su ogni layer
		@param  [(long,string)]: [(feat_id,layer_alias<'cap'>,<'regione'>,<'comune'>,<'provincia'>)]
		"""
		selections=[]
		#ottengo l'elenco dei layers caricati nel progetto
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		for key in layersmap.iterkeys():
			curLayer=layersmap[key] 
			#settrace()()
			selections+=self.getSelectionsByMetadataLayer("",curLayer)
		return selections
				
			
	def run(self):

		#self.message="selected"+" "+self.getLayer()
		#wrapped_slot = partial(self.selectedChanged, self.message)
		#self.iface.mapCanvas().getSelectionsByMetadataLayer.connect(wrapped_slot)
		self.ui_tree.reset()
		self.treeMaker()
		# create and show the dialog 
		wrapped_slot = partial(self.slotSelectionChanged, self.message)
		self.iface.mapCanvas().selectionChanged.connect(wrapped_slot)
		# cerco le selezioni su tutti i layers
		selections= self.findAllSelections()
		# visualizzo e selziono i nodi
		nodes=self.getSelectedNodes(selections)
		self.showNodes(nodes)	 	
		#self.makeList()
		# show the dialog

		#dlg.show()
		#result = dlg.exec_()
		# See if OK was pressed
		#if result == 1:
			# do something useful (delete the line containing pass and
			# substitute with your code
			
		#	pass
