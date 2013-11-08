# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""



#from Ui_interrogazioni import Ui_MainWindow
#from risultati import MainWindowResults
#from PyQt4.QtGui import QMainWindow
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from sqlAlchemyQueryClass import *
from Filter import  *
from PyQt4.QtCore import pyqtSignature
from PyQt4 import QtCore,QtGui
from dbQuery import *
from risultati import *
from Ui_interrogazioni import Ui_MainWindowInterrogazioni
from SaveQuery import *
from selezioneQuery import *
#import logging
#import time
from queriesDb import *
from AnagraficaDb import *




class Pv_item():
	"""
	rappresenta i pv nella lista dei pv  su cui eseguire i filtri
	"""
	def __repr__(self):
		return "pv_id:{0}".format(self.id)
	def __init__(self,Id):
		"""
		@param Id::(int,) ipv_id del pv e' contenuto in una lista per compatibilita' verso il basso
		@note: il parametro self.visible e' settato di default a True, cioe' il pv viene mostrato su
		 schermo, non e' filtrato
		"""
		  
		self.id=Id
		self.visible=True
	def getId(self):
		"""
		getter per self.id
		"""
		return self.id
	
	def isVisible(self):
		"""
		getter di visible
		@return: boolean
		"""
		return self.visible
	
	def setVisible(self,h):
		"""
		seter di visible
		@param hyded: boolean, il parametro hyded e' settato di default  a True
		""" 
		self.visible= h

class ListManager():
	"""
	contiene la struttura dati che gestisce la selezaione dei parametri del filtro
	usata  da interrogazioni per ogni operazione  di IN/OUT sulla lista, destinata a contenere tutti i parametri di tutti i ceckBox selezionati
	"""

	def write(self,t):
		if self.debug:
			pass

	def has_element(self, l, e,tab):
		"""
		verifica che nella lista l sia presente lo item con stessa signature di e; in caso positivo ritorna True
		@param l:[item] lista da analizzare
		@param e:signature dello item  da cercare nella lista
		@return: boolean  
		"""
		if type(l)==type([]):
			for i in l:
				if (i.getSignature()==e and i.getTab()==tab):
					return True
		else:
			if l.isSame(e):
				return True
		return False
	
	def findKey4List(self,val,tab):
		"""return the key of dictionary dic, given a value inside a list, il dict  su cui opera e' self.elementsList
		@return: ceckBox 
		"""
		return [k for k, v in self.elementsList.iteritems() if self.has_element(v,val,tab) ][0]
	
	def look4cBoxByItemSignature(self,signature,tab):
		""" ritorna il checkBox cui fa riferimento lo item con la signature passata
		@param signature:  (class_id,param_id):(int,int)
		@return: ceckBox
		"""
		return self.findKey4List(signature,tab)
	
	def __init__(self):
		self.debug=True
		self.elementsList={}
		
	def getDigest(self):
		"""
		ritorna una descrizione del contenuto del dict nella forma [(key:len(value))]
		per debug
		@return: [(ceckBox,int)]
		"""
		d={}
		for k in self.elementsList.iterkeys():
			d[k]=len(self.elementsList[k])
		return d
	def getFullList(self):
		"""
		ritorna l'intera lista contenuta in ListManager
		"""
		return self.elementsList

	def getUnusedByKey(self,k):
		"""
		@param k: ceckBox
		@return: [Item]
		recupera i parametri non selezionati del ceckBox, dal momento che i checkBox contengono l'informazione sul tab in cui si trovano e' possibile ricostruire le tre liste di parametri usate per 
		lanciare il filtro
		"""
		selections=[]
		for i in self.elementsList[k]:
			if not i.isSelected():
				selections.append(i)
		return selections
	
	def GetUnusedBoxes(self):
		"""
		@return: {ceckBox:""} se la chiave e' presente nel dict allora e' usata  e il relativo checkBox deve essere segnato
		ritorna la lista dei ceckBox di cui e' stato selezionato almenmo un parametro
		ritorna un dict per ragioni di efficienza, in quanto non vogliamo che un checBox sia presente piu' di una volta, il controllo di presenza su un dict
		e' piu' efficiente e semplice che nelle altre strutture dati 
		
		"""
		unusedBoxes={}
		#esploro elementsList alla ricerca di 
		for key in self.elementsList.iterkeys():
			if not self.hasUsed(self.elementsList[key]):
				unusedBoxes[key]=""# se l'oggetto 
		return unusedBoxes
		
	
	def setSelectedItem(self,param,b):
		"""
		@param ceckBox:  identifica a quale ceckBox afferisce la lista dei parametri
		@param param: Item lo param da deselezionare/selezionare
		@param b:valore da settare in Item.selected 
		@note: la chiave  e' sempre disponibile quando si seleziona un parametro
		setta un parametro  della lista a settato e viceversa
		
		"""
		#scorro la lista di elementi di cBox cercandone uno con la stessa signature
		#print "parametro da settare: {0}".format(param)
		for i in self.elementsList[param.getCeckBox()]:
		#	print "item in setSelectedItem: {0}".format(i)
			if param.isSame(i):
				i.setSelected(b)
				self.write("ITEM TROVATO")


	def resetLists(self):
		"""
		resetta tutte le liste azzerando self.elementsList
		ponendo selected a False
		"""
		for k in self.elementsList.iterkeys():
			for i in self.elementsList[k]:
				i.setSelected(False)
				
	def addItem(self,k,item):
		"""
		@param ceckBox: potrebbe essere un oggetto qualsiasi, in interrogazioni viene usato ceckBox; identifica a quale ceckBox afferisce la lista dei parametri
		@param item: Item
		aggiunge un elemento alla lista relativa alla chiave key
		da notare che in interrogazioni quando si seleziona un  parametro, il ceckBox che ne rappresenta la chiave e' sempre selezionato, quindi disponibile
		"""
		#controllo che la chiave sia gia' presente nella lista
		if not self.elementsList.has_key(k):
			#creo la  nuova lista
			self.elementsList[k]=[]
			#aggiungo lo item alla lista
		self.elementsList[k].append(item)
	def getSingleItem(self,signature):
		"""
		ritorna l'oggetto della lista che ha la stessa coppia classe_id,parametro_id
		@param parametro: Item parametro ricercato 
		@note: nel parametro passato e' sufficiente definire il campo signature del costruttore cioe' classe_id e parametro_id, gli altri campi non servono e possono essere inizializzati a valori qualsiasi, non conosco ceckbox, devo iterare su tutte le chiavi presenti in elementsList
 		@return: Item
		"""
		#settrace()
		p=None
		#print "sto cercando: %s"%(parametro)
		#print "lista completa:%s"%(self.getFullList())
		for key in self.elementsList.iterkeys():
			#print "getSingleItem key: {0}".format(key)
			# tutti gli elementi cliccabili sulla avaibleValueList sono gia' presenti in elementsList e la signature e' univoca
			# quindi mi aspetto un risultato non None in ogni caso, ma quando in ElementsList sono presenti piu' chiavi getelements
			# ritornera' None
			# se cerco il parametro in una lista cui non appartiene, quindi uso una variabile di comodo e solo quando ottengo un p non nullo lo ritorno
			p1=self.getElement(self.elementsList[key],signature)
			if p1 is not None:
				p=p1
		return p
			
	def getElement(self,l,i):
		"""
		ritorna l' elemento della lista l che ha la stessa signature e stesso tab di i
		@param l: [Item]
		"""
		n=0
		#print "item cercato da getElement: {0}".format(i)
		#print "lista in getElement:{0}".format(l)
		for j in l:
			if j.isSame(i):
				#print "item trovato in posizione {0}".format(n)
				return j
				n=n+1
	def hasUsed(self,l):
		"""
		@param l:[Item]	
		@return: bool
		verifica che almeno un elemento della lista sia usato 
		"""
		b=False
		#scorro la lista l
		for i in l:
			if i.isSelected():
				b=True
		return b
	def GetUsedBoxes(self):
		"""
		@return: {ceckBox:""} se la chiave e' presente nel dict allora e' usata  e il relativo checkBox deve essere segnato
		ritorna la lista dei ceckBox di cui e' stato selezionato almenmo un parametro
		ritorna un dict per ragioni di efficienza, in quanto non vogliamo che un checBox sia presente piu' di una volta, il controllo di presenza su un dict
		e' piu' efficiente e semplice che nelle altre strutture dati 
		
		"""
		usedBoxes={}
		#esploro elementsList alla ricerca di 
		for key in self.elementsList.iterkeys():
			if self.hasUsed(self.elementsList[key]):
				usedBoxes[key]=""# se l'oggetto 
		return usedBoxes
	def filterByTab(self,l,tab):
		"""
		ritorna gli elementi della lista che appartengono al tab
		@param l: [Item]
		@param tab: string <-('marchi','prodotti','parametri')
		"""
		fl=[]
		for i in l:
			if i.belongsTo(tab):
				fl.append(i.getSignature())
		return fl
	
	def getSelectionsByTab(self):
		"""
		genera la lista dei parametri selezionati in ogni tab in forma di dizionario come in Retrieve.getAllValues()
		@note: scorre i tabs elencati in  una lista, questa puo' essere modificata per adattare il metodo  ad altri tabs
		@return: {key:[signature]}
		@note: in precedenti releases di questo interrogazioni e' possibilie che signature fosse implementata come coppia,invece che lista funzionalmente non cambia nulla, ma poteva essere origine di un baco
		quando si calcola l'intersezione delle liste prodotte da interrogazioni, perche' l'intersezione lavora con liste non con tuple 
		"""
		sl={}
		#prendo la lista di tutte le selezioni
		tabs=['potenziali','marchi','parametri']
		l=self.getRawSelected()
		for tab in tabs:
			if len(self.filterByTab(l,tab))>0:
				#inserisco il tab  solo se presenta selezioni
				sl[tab]=self.filterByTab(l,tab)
		return sl

	def getSelectionsByKey(self,k):
		"""
		@param k: ceckBox
		@return: [Item]
		recupera i parametri selezionati del ceckBox, dal momento che i checkBox contengono l'informazione sul tab in cui si trovano e' possibile ricostruire le tre liste di parametri usate per 
		lanciare il filtro
		"""
		selections=[]
		for i in self.elementsList[k]:
			if i.isSelected():
				selections.append(i)
		return selections
	
	def getRawSelected(self):
		"""
		ritorna la lista di tutti i parametri selezionati, serve per flaggare i ceckBox, senza distinzione tra i tab
		@return: [Item]
		"""
		#instanzio la lista in cui memorizzero' i parametri 
		selectedList=[]
		#scorro elementsList per chiave
		for l in self.elementsList.iterkeys():
			#esploro le singole liste
			for i in self.elementsList[l]:
				if i.isSelected():
					selectedList.append(i)
		return selectedList
		
				
		
class Item():
	"""
	questa classe  gestisce la struttura dati che rappresenta le selezioni dei parametri per il filtro
	si tratta di coppie ordinate di interi [int,int]:[class_id,param_id]
	gli oggetti Item vengono memorizzati da Listmanager
	@note: in precedenti releases di questo interrogazioni e' possibili che signature
	 fosse implementata come coppia,invece che lista funzionalmente non cambia nulla,
	  ma poteva essere origine di un baco
	 @note: la signature  non e' univoca, lo diventa congiuntamente al tab
	quando si calcola l'intersezione delle liste prodotte da interrogazioni, perche' l'intersezione lavora con liste non con tuple
	@todo: sarebbe bello convertire tutte le signature ancora espresse come tuple () in liste [], ma e' piu' un vezzo che qualcosa di serioperche' signature e' instanziata come lista dal costruttore di Item 
		
	"""
	
	def __init__(self,signature,cBox):
		"""
		@param item:[int,int] coppia ordinata di interi [class_id,param_id]
		@param cBox: ceckBox:e' il riferimento al ceckbox della categoria
		"""
		self.signature=[signature[0],signature[1]]
		self.cBox=cBox
		self.tab=cBox.getTab()
		if type(cBox)==type("ww"):
			self.repr=cBox
		else:
			self.repr=cBox.getTab()
		self.text=""
		self.selected=False
		
	def getTab(self):
		"""
		getter del tab e' un wrapper di checkBox.getTab
		@return: string
		"""
		return self.tab
	
	def getCeckBox(self):
		return self.cBox
	def __repr__(self):
		return "ITEM:,selected:%s,firma_parametro:%s, tab:%s"%(self.selected,self.signature,self.repr)
	
	def belongsTo(self,tab):
		"""
		verifica se il parametro appartiene al tab
		@param tab:string <- ('parametri','marchi','potenziali') 
		@return: bool
		"""
		return tab==self.cBox.getTab()
	def getSignature(self):
		"""
		getter di signature
		@return: (class_id,param_id):(int,int)
		"""
		return self.signature
	def isSelected(self):
		"""
		@return bool
		getter di self.selected, True se il parametro e' presente nella lista dei selezionati
		"""
		return self.selected
	def setText(self,txt):
		"""
		@param txt: String
		setter di self.text, self.text e' il testo mostrato accanto allo item nella lista 
		"""
		self.text=txt
	def getText(self):
		return self.text
	def setSelected(self,b):
		"""
		@param b: bool
		setter di self.selected, True se il parametro e' presente nella lista dei selezionati
		"""
		self.selected=b
	def isSameClass(self,cl):
		"""
		@param cl:int
		@return: bool 
		controlla che lo item appartenga alla classe passata come parametro
		"""
		
		b= False
		if self.signature[0]==cl:
			b=True
		else:
			b=False
		return b
	def has_SameSignature(self, signature):
		"""
		@param signature:[int,int][class_id,parameter_id]
		@return boolean 
		verifica che la signature dello item sia uguale a signature
		"""
		return self.signature==signature 
	def sameTab(self,i):
		"""
		confronta il campo tab di due Item
		@param i:Item di confronto
		@return boolean
		"""
		return i.getTab()==self.tab
	
	def isSame(self,i):
		"""
		@param i: Item
		@return: bool
		controlla l'uguaglianza tra lo item corrente e un altro mediante
		 confronto tra gli elementi di self.item
		serve per selezionare l'elemento da deselezionare
		"""
		return ((i.signature[0]==self.signature[0]) and (i.signature[1]==self.signature[1]) and (i.tab==self.tab))



class Retrieve():
	"""
	questa classe e' una comodity, nel senso che esplora la gui elencando i parametri che sono stati selezionati
	"""
	def __init__(self, List):
		"""
		@param List:	dict dei QwidgetList di interesse, formato: {'parametri'/'marchi'/'potenziali':QListWidget} 
		"""
		#logging.basicConfig(filename='/home/giuseppe/.qgis/log/mmasgis.log',level=logging.DEBUG)
		self.selectedValue=List
	def getValues(self,  listwidget):
		"""
		ritorna tutti i valori presenti nel QListWidget passatO
		@param listwidget:	 QListWidget
		@return: [(category_id,parameter_id)]
		"""
		l=[]
		#"category {0}, item id {1}".format(item.data(1).toString(), item.data(5).toString())
		for i in range( listwidget.count()):
			l.append([int(listwidget.item(i).data(1).toString()),int( listwidget.item(i).data(5).toString())])
		return l
	def getAllValues(self):
		"""
		recupera tutti i valori presenti in tutte le liste
		@return: {'parametri'/'marchi'/'potenziali':[(category,id)]} 
		"""
		l={}
		for key in self.selectedValue.iterkeys():
			#print key
			if self.selectedValue[key].count()>0:
				l[key]=	self.getValues(self.selectedValue[key])
		return l



class ceckBox(QtGui.QCheckBox):
	"""
	estende QCheckBox con un segnale (mySignal) per poter interagire con il resto della gui  
	"""
	def __init__(self, testo, Id, tab):
		"""
		@param testo:	String
		@param Id:	Integer
		@param category:	Integer  
		"""
		QtGui.QCheckBox.__init__(self, testo)
		self.text=testo
		self.tab=tab
		self.id=Id
		self.inhibit=False
		QtCore.QObject.connect(self, QtCore.SIGNAL("stateChanged(int)"), self.on_checkChanged)
		QtCore.QObject.connect(self, QtCore.SIGNAL("reset"), self.reset)
	
	def setFlag(self,b):
		"""
		setta il ceckBox a True o False
		@param b: bool valore assegnato al ceckBox
		@note: e' necessario inibire il segnale  my_signal
		@note: quindi poniamo momentaneamente self.inhibit a True. 
		"""
		self.inhibit=True
		self.setCheckState(b)
		#riabilito il segnale
		self.inhibit=False 
	
	def getTab(self):
		return self.tab
	
	def getId(self):
		"""
		getter di self.id
		"""
		return self.id
	
	def __repr__(self):
		return "ceckbox:%s,id:%d,cat:%s"%(self.text,self.id,self.tab)
	def reset(self):
		"""
		resetta il checkBox
		@note: e' invocato da groupReset, al momento quindi non viene usato
		"""
		
		self.setCheckState(False)
		
	def groupReset(self, *sms):
		"""
		rende i checkbox mutualmente esclusivi
		@note: al momento e' disabilitata
		@todo: cambiare la logica dei checkBox: devono essere flaggati solo se almeno uno dei loro campi e' selezionato
		"""
		pass
		# rimuovo il codice per i checkBox mutualmente esclusivi
		#id=sms[0][0]
		#category=sms[0][1]

		#if (self.category==category) and (int(self.id)!=int(id)):

		#	self.setCheckState(False)



	def on_checkChanged(self):
		"""
		@note: formato del messaggio msg=[self.id,self.text,self.tab,self]<[int,string,string,ceckBox>
		@note: self.text è il testo che accompagna il boxpyqt contextmenu last selection
		emette il segnale mySignal se il checkbox passa a true
		"""
		msg=[self.id,self.text,self.tab,self]
		if (self.checkState() and (not self.inhibit)):
			self.emit(QtCore.SIGNAL("mySignal"), msg)


class MainWindowQuery(QMainWindow,  Ui_MainWindowInterrogazioni):
	"""
	wrapper di Ui_MainWindowQuery gestisce tutte le funzioni della gui interrogazioni
	@requires:  invocare addGeographicList dopo aver instanziato  la classe,perche' il tasto reset funzioni, senza errori e perche' il filtro non lavori su tutto il db, ma sull'insieme di pv presenti nella selezione geografica
	@requires: setRisultati per settare la finestra su cui stampare la lista filtrata
	@note: effettua una query per ogni tab: cioe' una per marchi, potenziali e parametri e infine calcola l'intersezione tra il risultato di ogni query e la lista iniziale inserita con addGeographicList, per fare cio' usa la funzionalita' set.intersection di python che ritorna un set 
	"""
	


	def __init__(self, user, db, parent=None):
		self.debug=True
		echo=False
		"""
		Constructor
		"""
		#questo dizionario contiene i campi che vengono rimossi
		#a ogni click su i checkbox
		self.user=user
		self.activeDb=db
		self.nomeDb=user.getActiveDb().getNameDb()
		self.selections={}
		self.queryDb=DbQueries(db)
		self.pv=[] # lista da visualizzare
		self.filters=[] #inizializzo la lista dei filtri da usare va inizializzata ogni volta prima di generare i nuovi filtri
		self.elementsList=ListManager()
		#self.log("partenza interrogazioni","risultati.py 95")
		self.dlg=None
		self.loadWindow=None
		#setto i campi del dict
		self.selections['marchi']=[]
		self.selections['parametri']=[]
		self.selections['potenziali']=[]
		self.signals={'marchi':'resetMarchi', 'parametri':'resetParametri', 'marchi':'resetMarchi', 'potenziali':'resetPotenziali'}
		self.w=None
		self.Wsq=None# window saveQuery
		self.c=0
		self.filteredList={}
		self.intersectedList={}
		self.lista={}
		self.elements={}
		QMainWindow.__init__(self, parent)
		self.setupUi(self)
		#sistemo il testo nella gui
		#subito i tab cosi' Fra e' tranquillo
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3),"marchi")
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4),"potenziali")
		#self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5),"parametri")
		#nelle liste
		self.attributeList_potenziali.headerItem().setText(0, "")
		self.attributesList_marchi.headerItem().setText(0, "")
		self.attributeList_parametri.headerItem().setText(0, "")
		self.attributeList_parametri.headerItem().setText(1, QtGui.QApplication.translate("MainWindowQuery", "", None, QtGui.QApplication.UnicodeUTF8))
		self.attributesList_marchi.headerItem().setText(1, QtGui.QApplication.translate("MainWindowQuery", "", None, QtGui.QApplication.UnicodeUTF8))
		self.db=dbQuery(self.user,self.activeDb)
		self.tabs={'parametri':self.attributeList_parametri, 'marchi':self.attributesList_marchi, 'potenziali':self.attributeList_potenziali}
		self.availableValue={'parametri':self.availableValueList_parametri, 'marchi':self.availableValueList_marchi, 'potenziali':self.availableValueList_potenziali}
		self.selectedValue={'parametri':self.selectedValueList_parametri, 'marchi':self.selectedValueList_marchi, 'potenziali':self.selectedValueList_potenziali}
		self.populateTabs()
		self.r=Retrieve(self.selectedValue)
		self.connect(self.availableValueList_parametri,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextPar)
		self.connect(self.availableValueList_marchi,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextMar)
		self.connect(self.availableValueList_potenziali,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextPot)
		self.connect(self.selectedValueList_parametri,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextParSel)
		self.connect(self.selectedValueList_marchi,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextMarSel)
		self.connect(self.selectedValueList_potenziali,QtCore.SIGNAL("customContextMenuRequested(QPoint)"),self.onContextPotSel)
		self.connect(self,QtCore.SIGNAL('triggered()'),self.closeEvent)
		#self.availableValueList.dropEvent = self.lbDropEvent
		#self.availableValueList_1.dropEvent = self.lbDropEvent_1
	#	self.availableValueList_2.dropEvent = self.lbDropEvent_2
	
	def onContextPar(self,point):
		"""
		Gestisce il menu di selezione nella lista dei parametri disponibili
		"""
		self.menu = QtGui.QMenu("Menu", self)
		actionSelPar = QtGui.QAction("Seleziona", self)
		actionSelAllPar=QtGui.QAction("Seleziona Tutto", self)
		self.menu.addAction(actionSelPar)
		self.menu.addAction(actionSelAllPar)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.availableValueList_parametri.mapToGlobal(point))
		if action==actionSelPar:
			self.actionSelPar()
		if action==actionSelAllPar:
			self.actionSelAllPar()
			
	def cerca(self,p):
		cl=p[0]
		db=tableDb(self.user,self.activeDb)
		l=db.ricercaAnd(cl,wholeWord=p[1])
		for i in self.pv:
			i.setVisible(l.has_key(i.getId()[0]))
		self.openResults(self.pvList2dict())
			
	def actionSelPar(self):
		"""
		Gestisce la selezione degli item selezionati nella lista dei parametri disponibili
		"""
		listapar=self.availableValueList_parametri.selectedItems()
		for i in listapar:
			par=self.selectionsPerformer(i,'parametri')
			self.selectBox(par)
			self.selectCeckBoxes()
	
	def actionSelAllPar(self):
		"""
		Gestisce la selezione di tutti item presenti nella lista dei parametri disponibili
		"""
		nitems=self.availableValueList_parametri.count()
		for i in range(0,nitems):
			item=self.availableValueList_parametri.item(i)
			par=self.selectionsPerformer(item,'parametri')
			self.selectBox(par)
			self.selectCeckBoxes()
	
	def onContextMar(self,point):
		"""
		Gestisce il menu di selezione nella lista delle marche disponibili
		"""
		self.menu = QtGui.QMenu("Menu", self)
		actionSelMar = QtGui.QAction("Seleziona", self)
		actionSelAllMar=QtGui.QAction("Seleziona Tutto", self)
		self.menu.addAction(actionSelMar)
		self.menu.addAction(actionSelAllMar)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.availableValueList_marchi.mapToGlobal(point))
		if action==actionSelMar:
			self.actionSelMar()
		if action==actionSelAllMar:
			self.actionSelAllMar()
			
	def actionSelMar(self):
		"""
		Gestisce la selezione degli item selezionati nella lista delle marche disponibili
		"""
		listamar=self.availableValueList_marchi.selectedItems()
		for i in listamar:
			mar=self.selectionsPerformer(i,'marchi')
			self.selectBox(mar)
			self.selectCeckBoxes()
	
	def actionSelAllMar(self):
		"""
		Gestisce la selezione di tutti item presenti nella lista delle marche disponibili
		"""
		nitems=self.availableValueList_marchi.count()
		for i in range(0,nitems):
			item=self.availableValueList_marchi.item(i)
			mar=self.selectionsPerformer(item,'marchi')
			self.selectBox(mar)
			self.selectCeckBoxes()
		
	def onContextPot(self,point):
		"""
		Gestisce il menu di selezione nella lista dei potenziali disponibili
		"""
		self.menu = QtGui.QMenu("Menu", self)
		actionSelPot = QtGui.QAction("Seleziona", self)
		actionSelAllPot=QtGui.QAction("Seleziona Tutto", self)
		self.menu.addAction(actionSelPot)
		self.menu.addAction(actionSelAllPot)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.availableValueList_potenziali.mapToGlobal(point))
		if action==actionSelPot:
			self.actionSelPot()
		if action==actionSelAllPot:
			self.actionSelAllPot()
			
	def actionSelPot(self):
		"""
		Gestisce la selezione degli item selezionati nella lista dei potenziali disponibili
		"""
		listapot=self.availableValueList_potenziali.selectedItems()
		for i in listapot:
			pot=self.selectionsPerformer(i,'potenziali')
			self.selectBox(pot)
			self.selectCeckBoxes()
	
	def actionSelAllPot(self):
		"""
		Gestisce la selezione di tutti item presenti nella lista dei potenziali disponibili
		"""
		nitems=self.availableValueList_potenziali.count()
		for i in range(0,nitems):
			item=self.availableValueList_potenziali.item(i)
			pot=self.selectionsPerformer(item,'potenziali')
			self.selectBox(pot)
			self.selectCeckBoxes()

	
	def closeEvent(self, event):
		# rendiamo visibili tutti gli elementi della lista iniziale
		for p in self.pv:
			p.setVisible(True)
		self.dlg.setOriginalList(self.pvList2dict())
	
	def filterRunner(self,Id):
		"""
		applica i filtri definiti in self.filters al pv con pv_id Id, invocandoil metodo test di Filter
		@param Id:int:
		@return: boolean 
		"""
		b=True
		for f in self.filters:
			c=f.test(Id)
			if c:
				pass
			else:
				"""dal momento che deve ritornare il prodotto logico del risultato di ogni filtro
				se uno solo di essi ritorna false non serve  esseguire gli altri test
				quindi posso uscire dal metodo ritornando False
				"""
				return False	
		return b


	def showSelectedParameters(self,cBox):
		"""
		popola la lista dei valori selezionati relativa al tab in cui si trova cBox prelevando i valori dalla lista elementsList secondo il java pattern delle liste
		@param cBox: ceckBox
		@return: None
		"""
		#ricavo la lista dei parametri del cBox selezionati
		l=self.elementsList.getSelectionsByKey(cBox)
		self.write( "parametri selezionati: {0}".format(l))
#		print "numero parametri selezionati={0}".format(len(l))
	#	print "lista dei selezionati:{0}".format(l)
		#ricavo il tab di lavoro
		tab=cBox.getTab()
		for item in l:
			#signature=item.getSignature()
			#instanzio il QWidgetListItem
			item2insert=self.itemBuilderFromList(item)
			# aggiorno il numero di righe in self.selectedValue[tab]
			#self.selectedValue[tab].setRowCount(self.selectedValue[tab].count()+1)
			
			#inserisco l'elemento nella lista
			
			self.selectedValue[tab].addItem(item2insert)#self.selectedValue[tab].count(),
			self.write( "mostro item: {0} su  tab: {1}".format(item,tab))

		



	def getTime(self):
		"""
		usata dal log
		per recuperare l'ora di sistema
		@return: String
		"""
		year=time.localtime()[0]
		month=time.localtime()[1]
		day=time.localtime()[2]
		hour=time.localtime()[3]
		minu=time.localtime()[4]
		sec=time.localtime()[5]
		return"%d:%d:%d-%d/%d/%d"%(hour,minu,sec,day,month,year)
	
	def log(self,title, txt):
		"""
		produce  log di debug
		@param title: String
		@param txt: String
		@note: non c'e' una relae differenza tra title e txt
		"""
		logging.debug(self.getTime()+" "+title+" "+str(txt))


		
	def populateList(self,tab,param):
		"""
		@param tab: <'marchi','parametri','potenziali'>
		@param param: [( classe,item_id)]
		@note: popola la selectedList indicata da tab con gli items prodotti  da param
		"""
	#	print "param in populateList: {0}".format(param)
		for i in param:
			self.write("elemento inpopulateList:{0}".format(i))
			item=self.itemBuilder((i[0],i[1]),tab)
			self.selectionsPerformer(item,tab)
		self.write("selezioni:{0}".format(self.elementsList.getRawSelected()))
			#self.selectedValue[key].insertItem(self.availableValue[key].count(), item)
			
		
	def loadQuery(self, fields):
		"""
		@note: legge  i campi della query selezionata e popola le selectedLists
		@param : {'potenziali':[(category,potenziale_id)],'marchi':[(category,marchio_id)],'parametri':[(category,parametro_id)]}
		@return: None
		"""
		for tab in fields.iterkeys():
			#rimuovo le vecchie selezioni
			self.clearList(tab)
			self.populateList(tab,fields[tab])
	#	print "loadQuery in interrogazioni got fields:{0}".format(fields)	
		



	def pvList2dict(self):
		"""
		converte la lista dei pv in un dizionario di pv per compatibilità con risultati e testdialog
		@return:{(int):""}::{(pv_id):""}
		"""
		d={}
		for p in self.pv: 
			if p.isVisible():
				d[(p.getId())]=""
		return d
	def resetFilter(self):
		"""
		resetta la lista delle anagrafiche 
		"""
		for p in self.pv:
			p.setVisible(True)
		self.openResults(self.pvList2dict())
		self.filters=[]
		for key in self.selectedValue.iterkeys():
			self.selectedValue[key].clear()
			self.availableValue[key].clear()
			self.emit(QtCore.SIGNAL("reset"))
		#rimuovo le selezioni nascoste
		for k in self.selections.iterkeys():
			self.selections[k]=[]
		#rimuovo le selezioni nel patternList
		self.elementsList.resetLists()
		#mostro la lista iniziale



		
	def list2dict(self, l):
		"""
		converte una lista di elementi in un dizionario
	le cui chiavi sono sono gli elementi della lista i valori una stringa vuota
	serve per garantire la compatibilita' con la lista degli item che viene dalla
	lista delle selezioni geografiche
	"""
		d={}
		for i in l:
			d[i]=""
		return d
	
	def filterList(self):
		"""
		filtra la lista di pv self.pv settando in ogni elemento il valore visible uguale al valore ritornato da filterRunner eseguito sul pv_id  
		"""
		for p in self.pv:
			b=self.filterRunner(p.getId()[0])
			p.setVisible(b)
			
	def addGeographicList(self,l):
		"""
		@param l:{(int,):""}::{(pv_id,:"")} la lista dei pv e' in forma di dizionario perche' cosi' viene generata in mmasgis e passata a testdialog e a risultati;
		il dict e' usato al posto di una semplice lista, perche' il dict risulta piu' efficiente nel controllo di pv gia' in lista 
		aggiungeva la lista ottenuta dalla selezione geografica a self.filteredList con la chiave 'first'
		nella nuova release popola la lista dei pv self.pv
		"""
		self.filteredList['first']=l# resta per compatibilita'
		for k in l.iterkeys():
			p=Pv_item(k)
			self.pv.append(p)

		#popo
		#print " lista iniziale {0}".format(self.filteredList)

		
	def setRisultati(self,dlg):
		"""
		setta la finestra dove stampare l'esito della query
		@param dlg: risultati
		@note: e' stata inserita per ragioni di compatibilita' verso le versioni precedenti, per non modificare il costruttore
		"""
		self.dlg=dlg
		self.dlg.setOriginalList(self.pvList2dict())
		
	def intersectionWithAccumulator(self, rs):
		"""
		@param rs: {'key':{pv_id:""}}
		esegue l'intersezione delle liste passetegli in rs
		@attention: se le liste non sono dello stesso tipo
		ritorna un insieme vuoto
		e' implementato con un accumulatore, cioe' procede per intersezioni successive 
		con una lista che e' l'accumulatore che e' settato inizialmente uguale a una delle liste in rs, poi e' posto uguale alle intersezioni tra accumulatore e un' altra lista 
		"""
		first=True
		accunulatore=[]
		for key in rs.iterkeys():
		#	print "lista per {0}:{1}".format(key,rs[key])
			if first:
	#			print "lista da intersecare in intersection {0}".format(rs[key])
				accumulatore=rs[key]
				first=False
			else:
			#	print "lista da intersecare in intersection {0}".format(rs[key])
				accumulatore=set(accumulatore).intersection(rs[key])
	#	print "accumulatore: {0}".format(accumulatore)
		return accumulatore
	def set2Dict(self, s):
		"""
		converte un oggetto di tipo set in un dizionario
		rende compatibili le liste su cui si lavora
		"""
		d={}
		for j in s:
			d[j]=""
		return d
	def itemBuilderFromList(self,param):
		text=param.getText()
		listItem=QtGui.QListWidgetItem(text)

		#setto il class_id
		listItem.setData(1, param.getSignature()[0])
		#setto param_id
		listItem.setData(5, param.getSignature()[1])
		return listItem
	
	def itemBuilder(self,item,key):
		"""
		genera un item da inserire in una lista
		@param item: la coppia di valori che specifica lo item (item_id,classe_id) signature nella classe Item
		@param key:la chiave del tab <'marchi','parametri','potenziali'>
		@return: 	QListWidgetItem
		"""
		# recupero il testo dello item
		text=self.db.getAllText(key,item[0],item[1])
		#print "testo: {0}".format(text)
		#print item
		listItem=QtGui.QListWidgetItem(text)
		#setto class_id
		listItem.setData(1, item[0])
		#setto param_id
		listItem.setData(5, item[1])
		return listItem
	
	def loadParametersByBox(self,box):
		"""
		@param box: ceckBox box è il ceckBox di cui caricare i parametri in lista
		@return: None
		"""
		valori= self.db.getValues(box.getTab(), box.getId())#(tab,id) conosco il checkBox
		for row in valori:
			#setto il testo dell 'attributo
			#item=QtGui.QListWidgetItem(row[1])
			#instanzio l'elemento di self.elementslist, passando il class_id alias category_id e il suo ceckBox
			parametro=Item((box.getId(),row[0]),box)
			#setto il campo testo del parametro
			parametro.setText(unicode(row[1]))
			#aggiungo il parametro alla lista
			self.elementsList.addItem(box,parametro)
			
	
	def populateValues(self, values, key, category_id,cBox):
		"""
		@note: popola la lista dei valori disponibili
		@note: values e' nel formato [(classe_id,testo)]
		@param values:[(classe_id,testo)]
		@param cBox: ceckBox oggetto ceckBox usato come chiave in self.elementsList 
		"""
		#svuoto la lista
		self.availableValue[key].clear()
		for row in values:
			self.write( "row in values:{0} on tab:{1}, cBox.tab:{2}".format(row,key,cBox.getTab()))
			#setto il testo dell attributo
			item=QtGui.QListWidgetItem(row[1])
			#instanzio l'elemento di self.elementslist, passando il class_id alias category_id e il suo ceckBox
			parametro=Item((category_id,row[0]),cBox)
			#setto il campo testo del parametro
			parametro.setText(unicode(row[1]))
			#aggiungo il parametro alla lista
			#self.elementsList.addItem(cBox,parametro)
		#	print "categoria {0}: attributo {1}: testo: {2}".format(category_id, row[0], row[1])
			#setto lo id della classe
			item.setData(1, category_id)
			#setto il parameter_id
			item.setData(5, row[0])
			#print " attributo id  originale{0} riga 64".format(row[0])
			#print " item.id={0}  prima di setext riga 65".format(item.data(5).toString())
			self.availableValue[key].insertItem(self.availableValue[key].count(), item)
			item.setText(row[1])
			#print " item.id={0}  dopo di setext riga 67".format(item.data(5).toString())
	#	print self.elementsList.getFullList()

	def clearList(self,key):
		"""
		rimuove le selezioni 
		@param key:'marchi'/'prodotti'/'parametri' 
		"""
		self.selectedValue[key].clear()
		
	def clearSelectedList(self,tab):
		"""
		svuota la lista dei parametri selezionati relativa  al tab
		"""
		self.selectedValue[tab].clear()
		
	def recoverSelections(self,key):
		"""
		salva le selezioni inserite in self.selections
		@param key:	'marchi'/'prodotti'/'parametri'
		@return: None 
		"""
		self.selections[key]=self.selections[key]+self.r.getValues(self.selectedValue[key])
		
	def selectionsFilter(self,lista,classe_id):
		"""
		esamina la lista passata come parametro e ne estrae gli elementi che appartengono all stessa classe
		serve a recuperare  i parametri nascosti che appartengono al checkbox selezionato
		@param classe_id: Integer
		@param lista: [(classe_id, param_id)]
		"""
		filteredList=[]
		for item in lista:
			if item[0]==classe_id:
				filteredList.append(item)
		return filteredList
		
	def setCheck(self,cBox,b):
		"""
		@param b: bool setta il ceckBox del parametro a b 
		"""	
		#tab=cBox.getTab()
		
		#print self.tabs[tab].topLevelItemCount()
		#print "itemTreeChild:{0}".format(self.tabs[tab].itemAt(0,0).data)
		if b:
			cBox.setFlag(b)
		else:
			if len(self.elementsList.getSelectionsByKey(cBox))==0:
				cBox.setFlag(b)
		
	def refreshSelections(self,key,classe_id):
		"""
		@note: ripristina le selezioni fatte per un dato checkbox, se questo viene cliccato nuovamente
		@param key: String <'marchi','potenziali','parametri'>
		@param classe_id:	Integer  
		"""
		list2Refresh=[]
		if self.selections.has_key(key):
			list2Refresh=self.selectionsFilter(self.selections[key],classe_id)
		#print "list2refresh:{0}".format(list2Refresh)
		for item in list2Refresh:
		#	print "item to refresh: {0}".format(item)
			#i=(item[1],item[0])# devo invertire l'ordine dei termini per compatibilita' con le funzioni che recuperano il testo
			item2insert=self.itemBuilder(item,key)
			self.selectedValue[key].insertItem(self.availableValue[key].count(), item2insert)
		#print self.r.getValues(self.selectedValue[key])
	
	def on_mySignal(self, *msg):
		"""
		esegue tutte le operazioni pertinenti a un cambio di categoria, cioe' ad un click su un checkbox
		@param *msg:	messaggio del segnale mySignal msg=[self.id,self.text,self.tab,ceckBox]
		"""
		#print " digest in mySignal: {0}".format(self.elementsList.getDigest())
		#recupero i parametri afferenti al ceckBox
		valori= self.db.getValues(msg[0][2], msg[0][0])#(tab,id) conosco il checkBox
		#print "VALORI : {0}".format(valori)
		self.populateValues(valori, msg[0][2], msg[0][0],msg[0][3])
		sms=[msg[0][0], msg[0][2]]#id,key
		#recupero le selezioni relative al vecchio checkbox
		self.recoverSelections(sms[1])
		#rimuovo le vecchie selezioni
		self.clearList(sms[1])
		self.refreshSelections(sms[1],sms[0])#key,classe_id
		self.write( self.selections[sms[1]])
		self.write( "messaggio inviato dal cBox: {0}".format(sms))
		#self.refreshSelections()
		self.emit(QtCore.SIGNAL(self.signals[msg[0][2]]), sms)


	def write(self,t):
		if self.debug:
			pass
			#print t
			 
	def populateParameters(self, List, tab ):
		"""
		popola la lista dei parametri disponibili
		@param List: QListWidget
		@param tab: viene passata a checkboxBuilder per inizializzare i checkbox
		"""
		parametri=self.db.getParameters(tab)
		for p in parametri:#p:(id,testo,enabled)
			check=self.checkBoxBuilder(p[1], p[0], tab)
			#self.write("genero check per {0} su {1}".format(p[1],tab))
			#print "signature del ceck: ({0},{1}), tab: {2}".format(p[1],p[0],tab)
			nodo=QtGui.QTreeWidgetItem("dummy")
			nodo.setText (1, "")
			nodo.setData(0,1,check)
			if p[2]==1:
				List.insertTopLevelItem (0, nodo)
				List.setItemWidget(  nodo,0,  check)
			#carico i parametri per i checkBox
			self.loadParametersByBox(check)



	def populateTabs(self):
		"""

		popola l'albero dei parametri nei tab disponibili
		"""
		for key in self.tabs.iterkeys():
			self.populateParameters(self.tabs[key], key)

	def openResults(self, l1):
		"""
		gestisce la finestra di output:
		1) svuta la tabella
		2) invoca il metodo populateTableByDb
		"""
		#print " mostro i seguenti risultati {0}".format(l)
		l={}
		for p in self.pv:
			if p.isVisible():
				l[(p.getId())]=""
		#  #ui =MainWindow(QtGui.QMainWindow)
		#ui.populateTable(l)
		#  #ui.show()
	#ui2=Ui_MainWindowResults()
		#QtGui.QMainWindow.__init__(self)
		#mainWindow=QtGui.QMainWindow(self)
		#self.w = MainWindowResults(l)
		#cancello i vecchi valori
		#print "lista da stampare:{0}".format(l)
		self.dlg.cleanTable()
		self.dlg.populateTableByDb(l)
		#self.w.show()

	def openSaveQuery(self):
		"""
		apre la finestra per il salvataggio della query
		"""
		#mainWindow=QtGui.QMainWindow(self)
		# se la lista dei filtri e' vuota  devo rigenerare i filtri 
		if len(self.filters)==0:
			self.filtersFactory(self.elementsList.getSelectionsByTab())
		self.Wsq = SaveQueryWindow(self.filters,self.queryDb,self.nomeDb.capitalize())
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.Wsq.geometry()
		self.Wsq.move((screen.width()/2)-size.height(),(screen.height()/2)-size.height())
		self.Wsq.setWindowTitle("Salva Query " +self.nomeDb.capitalize())
		self.Wsq.show()
		



	def on_checkChanged(self, s):
		pass
	def checkBoxBuilder(self, testo, Id, category):
		"""
		instanzia un singolo checkbox, curandosi di  allacciarlo con tutti i signals necessari al suo corretto funzionamento
		@param testo: String
		@param Id: Integer param_id
		@param category: Integer class_id
		@return:  ceckBox
		"""
		check=   ceckBox(testo, Id, category)
		check.setFocusPolicy(0)
		QtCore.QObject.connect(self, QtCore.SIGNAL("reset"), check.reset)
		QtCore.QObject.connect(check, QtCore.SIGNAL("stateChanged(int)"), self.on_checkChanged)
		QtCore.QObject.connect(check, QtCore.SIGNAL("mySignal"), self.on_mySignal)
		QtCore.QObject.connect(self, QtCore.SIGNAL(self.signals[category]), check.groupReset)
		return check
	def joinSelections(self,selections):
		"""
		unisce le selezioni che sono state nascoste con quelle visibili
		@param selections:	{'marchi'/'Potenziali'/'parametri':[(classe,id)]} 
		"""
		for key in self.selections.iterkeys():
			if selections.has_key(key):
				selections[key]=selections[key]+self.selections[key]
		return selections
	
	def groupList(self,l):
		"""
		produce le liste di parametri separati per class_id  
		genera un dict le cui chiavi sono il class_id, mentre i valori sono le liste dei parameters_id che afferiscono alla classe
		@param l: [[int,int]] con il seguente significato [class_id,parameter_id]
		@return: {int:[int]}{class_id:[parameter_id]}: la chiave e' il class_id degli elementi in l, 
		"""
		groups={}
		for k in l:
			if not (groups.has_key(k[0])):
				groups[k[0]]=[]
				groups[k[0]].append(k[1])
			else:
				groups[k[0]].append(k[1])
		return groups
	
	def filtersFactory(self,selections):
		"""
		genera gli oggetti Filter sulla base delle selezioni effettuate per tab
		@param selections::{key:[signature]}
		@note gli oggetti Filter sono aggiunti alla variabile globale self.filters
		@todo: refactory: rimpiazzare variabile globale self.filters 
		"""
		for k in selections.iterkeys():
			filter=Filter(self.groupList(selections[k]),k,self.queryDb,self.user,self.activeDb)
			#print filter
			#aggiungo il Filter alla lista
			self.filters.append(filter)
			#applico i filtri
		
	def on_applyButton_released(self):
		"""
		invoca le funzioni di Retrieve
		per recuperare le selezioni effettuate sulla gui, 
		 effettua il join con le selezioni nascoste
		 ed infine invoca openResults
		"""

		selections= self.elementsList.getSelectionsByTab()#self.r.getAllValues()
		for k in selections.iterkeys():
			filter=Filter(self.groupList(selections[k]),k,self.queryDb,self.user,self.activeDb)
			self.filters.append(filter)
			self.filterList()
		self.write( "SELECTIONS: %s"%selections)
		for key in selections.iterkeys():
			query=self.db.queryBuilder(key, selections)
			#rs=self.db.getResultSet(query)
			#self.filteredList[key]=self.list2dict(rs)
			self.intersectedList=self.intersectionWithAccumulator(self.filteredList)
			
			if type(self.intersectedList)==type(set('a')):
				self.intersectedList= self.set2Dict(self.intersectedList)

		self.openResults(self.pvList2dict())
		mx=QtGui.QMainWindow()
		QtGui.QMessageBox.information(mx,"Info", "Selezione applicata correttamente")

	def on_saveButton_released(self): 
		"""
		apre la finestra pere il salvataggio della query
		"""
		self.openSaveQuery()
		
	def on_loadButton_released(self):
		"""
		apre la finestra per il caricamento di una query
		"""
		self.loadWindow=SelectionQueryWindow(self,self.queryDb,self.nomeDb.capitalize())
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.loadWindow.geometry()
		self.loadWindow.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.height()/2)
		self.loadWindow.setWindowTitle("Carica Query " +self.nomeDb.capitalize())
		self.loadWindow.show()


	@pyqtSignature("")
	def on_resetButton_released(self):
		"""
		chiama il metodo resetFilter quando viene clickato il bottone reset 
		"""
		self.resetFilter()



	@pyqtSignature("QListWidgetItem*")
	def on_selectedValueList_parametri_itemDoubleClicked(self, item):
		"""
		gestisce la selezione tramite doppio click sulla lista dei parametri selezionati
		"""
		#settrace()
		signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
		c=self.elementsList.look4cBoxByItemSignature(signature,'parametri')
		dummy=Item(signature,c)

		parametro=self.elementsList.getSingleItem(dummy)
		#self.write( "parametro xxx {0} su tab {1}".format(parametro,parametro.getTab()))
		self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())

	def onContextParSel(self,point):
		"""
		Gestisce il menu di deselezione nella lista dei parametri selezionati
		"""
		self.menu = QtGui.QMenu("Menu", self)
		actionDeselPar = QtGui.QAction("Deseleziona", self)
		actionDeselAllPar=QtGui.QAction("Deseleziona Tutto", self)
		self.menu.addAction(actionDeselPar)
		self.menu.addAction(actionDeselAllPar)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.selectedValueList_parametri.mapToGlobal(point))
		if action==actionDeselPar:
			self.actionDeselPar()
		if action==actionDeselAllPar:
			self.actionDeselAllPar()
			
	def actionDeselPar(self):
		"""
		Gestisce la deselezione degli item selezionati nella lista dei parametri selezionati
		"""
		listapar=self.selectedValueList_parametri.selectedItems()
		parametro=None
		for i in listapar:
			signature=[i.data(1).toInt()[0],i.data(5).toInt()[0]]
			c=self.elementsList.look4cBoxByItemSignature(signature,'parametri')
			dummy=Item(signature,c)
			parametro=self.elementsList.getSingleItem(dummy)
			self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	
	def actionDeselAllPar(self):
		"""
		Gestisce la deselezione di tutti item presenti nella lista dei parametri selezionati
		"""
		nitems=self.selectedValueList_parametri.count()
		parametro=None
		for i in range(0,nitems):
			item=self.selectedValueList_parametri.item(i)
			signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
			c=self.elementsList.look4cBoxByItemSignature(signature,'parametri')
			dummy=Item(signature,c)
			parametro=self.elementsList.getSingleItem(dummy)
			self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	
	
	

	@pyqtSignature("QListWidgetItem*")
	def on_selectedValueList_marchi_itemDoubleClicked(self, item):
		"""
		gestisce la selezione tramite doppio click sulla lista dei marchi selezionati
		"""
		signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
		#creo un item dummy con la stessa signature di quello cliccato
		signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
		c=self.elementsList.look4cBoxByItemSignature(signature,'marchi')
		dummy=Item(signature,c)
		parametro=self.elementsList.getSingleItem(dummy)
		self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	
	def onContextMarSel(self,point):
		"""
		Gestisce il menu di deselezione nella lista delle marche selezionate
		"""
		self.menu = QtGui.QMenu("Menu", self)
		actionDeselMar = QtGui.QAction("Deseleziona", self)
		actionDeselAllMar=QtGui.QAction("Deseleziona Tutto", self)
		self.menu.addAction(actionDeselMar)
		self.menu.addAction(actionDeselAllMar)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.selectedValueList_marchi.mapToGlobal(point))
		if action==actionDeselMar:
			self.actionDeselMar()
		if action==actionDeselAllMar:
			self.actionDeselAllMar()
			
	def actionDeselMar(self):
		"""
		Gestisce la deselezione degli item selezionati nella lista delle marche selezionate
		"""
		listamar=self.selectedValueList_marchi.selectedItems()
		parametro=None
		for i in listamar:
			signature=[i.data(1).toInt()[0],i.data(5).toInt()[0]]
			signature=[i.data(1).toInt()[0],i.data(5).toInt()[0]]
			c=self.elementsList.look4cBoxByItemSignature(signature,'marchi')
			dummy=Item(signature,c)
			parametro=self.elementsList.getSingleItem(dummy)
			self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	
	def actionDeselAllMar(self):
		"""
		Gestisce la deselezione di tutti item presenti nella lista delle marche selezionate
		"""
		nitems=self.selectedValueList_marchi.count()
		parametro=None
		for i in range(0,nitems):
			item=self.selectedValueList_marchi.item(i)
			signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
			signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
			c=self.elementsList.look4cBoxByItemSignature(signature,'marchi')
			dummy=Item(signature,c)
			parametro=self.elementsList.getSingleItem(dummy)
			self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	
	
	
	def on_selectedValueList_potenziali_itemDoubleClicked(self,item):
		"""
		gestisce la selezione tramite doppio click sulla lista dei potenziali selezionati
		"""
		#settrace()
		signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
		#creo un item dummy con la stessa signature di quello cliccato
		signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
		c=self.elementsList.look4cBoxByItemSignature(signature,'potenziali')
		dummy=Item(signature,c)
		parametro=self.elementsList.getSingleItem(dummy)
		# deseleziono lo item nella lista
		self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())

	def onContextPotSel(self,point):
		"""
		Gestisce il menu di deselezione nella lista dei potenziali selezionati
		"""
		self.menu = QtGui.QMenu("Menu", self)
		actionDeselPot = QtGui.QAction("Deseleziona", self)
		actionDeselAllPot=QtGui.QAction("Deseleziona Tutto", self)
		self.menu.addAction(actionDeselPot)
		self.menu.addAction(actionDeselAllPot)
		#actionSelPar.triggered.connect(self.actionSelPar())
		action=self.menu.exec_(self.selectedValueList_potenziali.mapToGlobal(point))
		if action==actionDeselPot:
			self.actionDeselPot()
		if action==actionDeselAllPot:
			self.actionDeselAllPot()
			
	def actionDeselPot(self):
		"""
		Gestisce la deselezione degli item selezionati nella lista dei potenziali selezionati
		"""
		listapot=self.selectedValueList_potenziali.selectedItems()
		parametro=None
		for i in listapot:
			signature=[i.data(1).toInt()[0],i.data(5).toInt()[0]]
			signature=[i.data(1).toInt()[0],i.data(5).toInt()[0]]
			c=self.elementsList.look4cBoxByItemSignature(signature,'potenziali')
			dummy=Item(signature,c)
			parametro=self.elementsList.getSingleItem(dummy)
			self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	
	def actionDeselAllPot(self):
		"""
		Gestisce la deselezione di tutti item presenti nella lista dei potenziali selezionati
		"""
		nitems=self.selectedValueList_potenziali.count()
		parametro=None
		for i in range(0,nitems):
			item=self.selectedValueList_potenziali.item(i)
			signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
			signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
			c=self.elementsList.look4cBoxByItemSignature(signature,'potenziali')
			dummy=Item(signature,c)
			parametro=self.elementsList.getSingleItem(dummy)
			self.elementsList.setSelectedItem(parametro,False)
		self.clearSelectedList(parametro.getCeckBox().getTab())
		self.showSelectedParameters(parametro.getCeckBox())
	



	@pyqtSignature("QListWidgetItem*")
	def selectionsPerformer(self,item,tab):
		"""
		esegue le operazioni di selezione item 
		genera un parametro dummy  che contiene solo la signature per individuare il parametro 
		reale in elementsList e settarlo a selected
		@param item: QListWidgetItem item cliccato sulla lista
		@return: Item parametro reale da usare per flaggare il ceckBox di riferimento 
		"""
		#genero la signature che ricerco
#		self.write( "PARAMETRO SELEZIONATO  performer %s"%item)
		signature=[item.data(1).toInt()[0],item.data(5).toInt()[0]]
		c=self.elementsList.look4cBoxByItemSignature(signature,tab)
		c.setFlag(True)
		#print "signature in selectionsPerformer: {0}".format(signature)
		#instanzio il parametro dummy
		dummy=Item(signature,c)
		#recupero il parametro reale
		parametro=self.elementsList.getSingleItem(dummy)
		#setto il parametro a selezionato
		self.elementsList.setSelectedItem(parametro,True)
		#reset lista parametri selezionati
		self.clearSelectedList(parametro.getCeckBox().getTab())
		#print " fullList: {0}".format(self.elementsList.getFullList())
		#popolo la lista parametri selezionati
		self.showSelectedParameters(parametro.getCeckBox())
		return parametro
	
	def selectBox(self,parametro):
		"""
		@param parametro: Item di cui occorre settare il ceckBox 
		setta il ceckBox di parametro
		"""
		parametro.getCeckBox().setFlag(True)
	def selectCeckBoxes(self):
		"""
		put the flag  in every ceckBox that has a selected parameter
		"""
		# ottengo la lista di tutti i parametri selezionati
		l=self.elementsList.getRawSelected()
		#setto il flag dei rispettivi ceckBox
		for c in l:
			self.selectBox(c)
		
	def on_availableValueList_marchi_itemDoubleClicked(self, item):
		"""
		gestisce la selezione tramite doppio click sulla lista dei marchi disponibili
		"""
		#settrace()#seleziono il parametro nella lista 
		parametro=self.selectionsPerformer(item,'marchi')
		self.selectBox(parametro)
		# setto i ceckBox
		self.selectCeckBoxes()	
		
	def on_availableValueList_parametri_itemDoubleClicked(self, item):
		"""
		gestisce la selezione tramite doppio click sulla lista dei parametri disponibili
		"""	
		#seleziono il parametro nella lista 
		parametro=self.selectionsPerformer(item,'parametri')
		self.selectBox(parametro)
		# setto i ceckBox
		self.selectCeckBoxes()
		
	def on_availableValueList_potenziali_itemDoubleClicked(self, item):
		"""
		gestisce la selezione tramite doppio click sulla lista dei potenziali disponibili
		"""	
		#seleziono il parametro nella lista 
		parametro=self.selectionsPerformer(item,'potenziali')
		self.selectBox(parametro)
		# setto i ceckBox
		self.selectCeckBoxes()
		

