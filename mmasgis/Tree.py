from PyQt4 import QtCore,QtGui
from tree_sqlalchemy_class import  treeNode 

import MySQLdb
#import sys

class Nodo():
	"""rappresenta i nodi che comporranno l'albero, cioe' tutti gli elementi feature che mmasgis rileva negli shapefiles durante la fase di caricamento del plugin
	"""
	def __init__(self,header,Id,category,father,featId):
		"""
		@param string:testo che accompagna lo item
		@param int: id che distingue l'elemento
		@param string: categoria di appartenenza dello item: <'cap'><'comune'><'provincia'><'regione'>
		@param int:      father_id
		@param int: featureId 
		"""
		#font=QtGui.QFont("" , 9 , QtGui.QFont::Bold )
		self.layers={}
		self.id=Id
		self.cathegory=category		
		self.header=header
		self.visible=False
		self.feat_id=featId
		self.signature=category.lower()+str(featId)
		item=QtGui.QTreeWidgetItem(header)
		self.subHeader=True
		self.selected=False
		self.children=[]
		#setto il subHeader di default e' una stringa vuota
		item.setData(0,5,QtCore.QVariant(""))		
		item.setText(0,unicode(self.header))
		item.setData(0,1,QtCore.QVariant(self.feat_id))
		item.setData(0,3,QtCore.QVariant(category[0:3]))
		# memorizzo il nodo nel campo 4 dello item
		item.setData(0,4,QtCore.QVariant(self))
		#item.setFont( 0,  font )
		self.father_id=father
		self.QItem=item
		
	def export(self,f):
		"""esporta il nodo in una variabile js
		@param file:file aperto in output su cui estrarre il nodo
		@note: e'una funzione ricorsiva,esporta il nodo e tutti i suoi figli
		"""
		#apro la descrizione di un nodo
		f.write("{")
		f.write("text:'{0}',".format((self.header.replace("'","`").encode('utf8'))))
		f.write("subheader:'{0}',".format(self.getSubHeader()))
		f.write("id: {0},".format(self.feat_id))
		f.write("layer:'{0}',".format(self.cathegory))
		if self.hasChildren():
			f.write("expanded:false,children:[")
			for i in self.getChildren():
				i.export(f)
			#chiudo la lista dei nodi figli
			f.write("]")
		else:
			f.write("leaf:true")
			#chiudo il nodo
		f.write("},")
		
	def exportDb(self,session,father_id):
		text=self.getHeader().encode("utf8").replace("'","`")
		codice=int(self.getFeatId())
		layer=self.getCathegory()
		sigla=self.getSubHeader()
		#father_id=self.getFather()
		query="insert into tree(text,codice,layer,sigla,parent_id) values('{0}','{1}','{2}','{3}','{4}')".format(text,codice,layer,sigla,father_id)
		print query
#		cur.execute(query)
		#con.commit()
		node=treeNode(text,sigla,codice,layer,father_id)
		session.add(node)
		session.commit()
		last_id=session.execute("SELECT LAST_INSERT_ID()").fetchall()[0][0]

		#rs=cur.fetchall()
		#last_id=rs[0][0]
		
		#esporto i nodi figli
		for c in self.getChildren():
			c.exportDb(session,last_id)
		
	def exportJson(self,f):
		"""esporta il nodo in una variabile js
		@param file:file aperto in output su cui estrarre il nodo
		@note: e'una funzione ricorsiva,esporta il nodo e tutti i suoi figli
		"""
		#apro la descrizione di un nodo
		f.write("{")
		f.write('"text":"{0}",'.format((self.header.replace("'","`").encode('utf8'))))
		f.write('"subheader:"{0}",'.format(self.getSubHeader()))
		f.write('"id": "{0}",'.format(self.feat_id))
		f.write('"layer":"{0}",'.format(self.cathegory))
		if self.hasChildren():
			f.write('"expanded":"false","children":[')
			for i in self.getChildren():
				i.exportJson(f)
			#chiudo la lista dei nodi figli
			f.write("]")
		else:
			f.write('"leaf":"true"')
			#chiudo il nodo
		f.write("},")
		
	def getSignature(self):
		"""ritorna la signature del nodo
		@return: string
		@note: la signature e' formata da category.lower()+str(featId) e' usata come identificativo del nodo 
		"""
		return self.signature
	def isSelected(self):
		""" getter per self.selected
		@return: bool
		"""
		return self.selected		

	def setSelected(self,v, recursive=False):
		"""
		setter per self.selected
		@param bool: 
		@param bool: opzionale se True il metodo opera ricorsivamente
		"""  			
		self.selected=v
		#print "seleziono {0} a {1}".format(self.cathegory, v)
		#print "setto {0} a {1}".format(unicode(self), v)
		if recursive:
			for i in self.getChildren():
				i.setSelected(v,True)

	def sameFeature(self,n): 
		return  (self.cathegory==n.getCathegory().lower()) and (self.feat_id==n.getFeatId())
				
		
	def isVisible(self):
		"""getter per self.visible
		@return: bool
		"""
		return self.visible
		
	def getFeatId(self):
		return self.feat_id
			
	def explode(self):
		"""setta viswible a True in tutti i nodi figli, presenti in self.children
		rendendoli di fatto visibili nella finestra delle selezioni
		"""
		for i in self.children:
			i.setVisible(True)
		#nascondo il nodo esploso
		#self.visible=False
			
	def collapse(self):
		"""setta visible a False in tutti i nodi figli, presenti in self.children
		rendendoli di fatto invisibili nella finestra delle selezioni
		"""
		for i in self.children:
			i.setVisible(False,True)
			
	def hasChildren(self):
		""" ritorna True se il nodo possiede nodi figli cioe' se len(self.children)>0
		@return: bool
		"""
		if len(self.children)>0:
			return True
		else:
			return False 
			
	def getChildren(self):
		"""getter di self.children
		"""
		return self.children
	
	def appendChild(self,c):
		""" aggiunge un elemento alla lista dei nodi figli self.children
		"""
		self.children.append(c)
		
	def setVisible(self,v,recursive=False):
		""" setter di self.visible, quando e' True il nodo e' visibile nella finestra delle selezioni
		@param bool:
		@param bool:opzionale se True il metodo opera ricorsivamente, settando allo stesso modo il campo visible di tutti i nodi figli della gerarchia 
		"""
		self.visible=v
		if recursive:
			for i in self.getChildren():
				i.setVisible(v,True)
				
	def setLayers(self,l):
		self.layers=l 

		
	def translateProvincia(self,pr,crs):
		query="select sigla from provincia where provincia like '{0}'".format(pr.replace("'","`"))
		crs.execute(query)
		sigla=crs.fetchone()[0]
		return sigla	
		
	def setSubHeader(self,crs,*father):
		""" setter per il subHeader, il subheader e' il testo che segue lo header del nodo nella finestra delle selezioni
		tutti i nodi eccetto le regioni ne hanno uno
		@param Nodo: nodo padre
		@note: il subHeader e' memorizato nel campo Data di QItem con ruolo 5
		""" 
		subHeaderMaker={}
		subHeaderMaker['regione']=lambda f,c: ""
		subHeaderMaker['provincia']=lambda f,c:"("+self.translateProvincia(c.getHeader(), crs)+"/"+f.getHeader()[0:3]+")"
		subHeaderMaker['comune']=lambda f,c: f.getSubHeader()
		subHeaderMaker['Cap']=lambda f,c:f.getSubHeader()
		subHeaderMaker['cap']=subHeaderMaker['Cap']
		if len(father)>0:
			h= subHeaderMaker[self.cathegory](father[0],self)
		else:
			h=""
		self.QItem.setData(0,5,QtCore.QVariant(h))
		self.subHeader=True
		
	def hasSubHeader(self):
		""" getter per self.subHeader
			@return:  bool
		"""
		return self.subHeader
		
	def getSubHeader(self):
		""" getter per il valore del subHeader
		ritorna il valore memorizzato nel campo data di QItem al ruolo 5
		@return: string
		"""
		h= str(self.QItem.data(0,5).toString())
		return h 
	
	def __repr__(self):
		return "Nodo-%s:%s,father: %s,selected:%s"%(self.cathegory,self.header,self.father_id,self.selected)
		
	def getLayer(self,k):
		return self.layers[k]
		
	def getId(self):
		""" getter di Id
		@return: int
		"""
		return self.id
	
	def getNode(self):
		"""getter per il nodo dell'albero
		@return QTreeWidgetItem
		"""
		return self.QItem
	
	def getFather(self):
		""" getter dell'identificativo del fATHER 	 del nodo
		@return: object <string><int>
		"""
		return self.father_id
	
	def getCathegory(self):
		""" getter per self.cathegory
		@return: string
		"""
		return self.cathegory
	
	def getHeader(self):
		return self.header 
	
	def setNode(self,q):
		"""setter per il nodo dell'albero
		@param QTreeWidgetItem:
		""" 
		self.QItem=q

class SelectionList():
	"""
	questa classe implementa la lista delle features
	selezionate e ne gestisce l'aggiunta di elementi
	in modo tale che questi possano essere esplosi nella
	finestra delle selezioni
	"""	
	
	def __init__(self):
		self.selectionlist=Odict()
		
	def __repr__(self):
		return "{0} elementi in lista".format(len(self.selectionlist))	
		
	def printList(self):
		txt="\n"
		for i in self.selectionlist.iterkeys():
			txt+=str(i)+"\n"
		return txt  
		
	def isPresent(self,n):
		"""verifica la presenza del nodo in lista
		@return: bool
		@param Nodo:
		"""
		return self.selectionlist.has_key(n)
		
	def isSelected(self,n):
		""" ritorna True se il nodo e' presente in lista e selezionato
		@param Nodo:nodo in esame
		@return: bool
		"""
		b=False
		for i in self.selectionlist:
			if (i==n) and (i.isSelected()):
				b=True
		return b			
		
	def reset(self):
		"azzera self.selectionList "
		self.selectionlist.clear()
	
	def getList(self):
		"""ritorna self.selectionList
		@return: iterator over keys 
		"""
		#print "asked list "#,self.selectionlist.iterkeys()
		print "getlist in Selectionlist in Tree  324 "+str(len(self.selectionlist.iterkeys()))
		#settrace()
		return self.selectionlist.iterkeys() #iterkeys in Odict nonritorna un iteratore ma la lista delle chiavi, che in questo caso coincide con la lista dei nodi
	
	def addElement(self,n):
		""" aggiunge un nodo n a selectionList
			e ricorsivamente aggiunge tutti i nodi figli di n alla lista di seguito
			@param Nodo:
			@note: e' importante settare il nodo  con il metodo Nodo.setSelected(True,True) dopo averlo aggiunto alla lista
		"""
		#print "LLL elementi attualmente in lista {0}".format(len(self.getList()))
		#print "AAA aggiungo nodo {0}"
		self.selectionlist[n]=None
		##settrace()
		for child in n.getChildren():
			self.addElement(child)
			
	def removeElement(self,n):
		""" rimuove dalla lista l'elemento passato e tutti i suoi discendenti
		@param Node:
		""" 
		self.selectionlist.pop(n)
		for i in n.getChildren():
			self.removeElement(i)
			
			
class Tree():
	""" implementa la struttura dell'albero dei territori, viene  popolato da mmasgis.py che ne invoca i metodi adder
	inoltre viene usata per popolare i dati predefiniti per la modifica dell'anagrafica
	"""
	def __repr__(self):
		return "Tree: #cap: %d,#comuni: %d, #regioni:%d,#provincie:%d"%(len(self.cap),len(self.comuni),len(self.regioni),len(self.provincie))
	
	def fetchNode(self,cat, featId):
		"""recupera il nodo  corrispondente alla feature cliccata sul layer
		@param string: sigla del layer:<'cap>',<'reg'>,<'com'>,<'pro'>
		@return: Nodo 
		"""
		#creo un dict che contiene  le liste usate da tree indicizzate dallasigla del layer
		dicts={}
		dicts['cap']=self.cap
		dicts['regione']=self.regioni
		dicts['comune']=self.comuni
		dicts['provincia']=self.provincie
		#instanzio un nodo dummy con featId e cat richieste	
		dummy=Nodo(0,0,cat,0,featId)
		##settrace()	
		for n in dicts[cat]:
			if dummy.sameFeature(n):
				return n
	
	"""
	@param User: e' loggetto creato nella sequenza di login che possiede le informazioni relative al db attivo 
	"""
	def __init__(self,user):
		self.user=user
		self.cap=[]
		self.comuni=[]
		self.provincie=[]
		self.regioni=[]
	def cerca(self,name,cat):
		"""
		ritorna il nodo  dato il suo  header e la sua categoria
		e' usato per ottenere il nodo dell'albero da espandere
		@param string: nome del nodo da ricercare
		@param string: nome del layer<'cap'><'comune'><'provincia'>
		@return: Nodo
		"""   
		category={}
		category['cap']=self.cap
		category['comune']=self.comuni
		category['provincia']=self.provincie
		#category['province']=self.province
		found=None
		for n in category[cat.lower()]:
			if n.getHeader().lower()==unicode(name).lower():
				found=n
		return found		
		
	def resetTree(self):
		"""resetta l'istanza dell'albero
		svuotando le liste degli elementi
		self.cap, self.comuni,self.provincie
		self.regioni
		"""
		del self.cap[:]
		del self.comuni[:]
		del self.provincie[:]
		del self.regioni[:]
				
	def addComune(self,c):
		""" aggiunge un elemento alla lista self.comuni
		@param Nodo:
		self.comuni.append(c)
		"""
		self.comuni.append(c)
		
	def export(self,f):
		"""esporta il nodo in una variabile js
		@param file:file aperto in output su cui estrarre il nodo
		@note: e'una funzione ricorsiva,esporta il nodo e tutti i suoi figli
		"""
		#apro la descrizione di un nodo
		f.write("{")
		f.write("text:'{0}',".format(self.header))
		f.write("subheader:'{0}',".format(self.getSubHeader()))
		f.write("featureId: {0},".format(self.feat_id))
		f.write("layer:'{0}',".format(self.cathegory))
		if self.hasChildren():
			f.write("expanded:true,children:[")
			for i in self.getChildren():
				i.export(f)
			#chiudo la lista dei nodi figli
			f.write("]")
		else:
			f.write("leaf:true")
			#chiudo il nodo
		f.write("},")
		
	def treeBuilder(self):
		"""
		combina i nodi  delle quattro liste in un unico albero
		ritorna i nodi delle regioni a cui sono stati aggiunti nodi delle provincie, dei comuni e dei cap
		@return: [Nodo]
		@precondition: fare attenzione che id e father_id siano consistenti tra le varie categorie
		"""							
		self.childrenAdder(self.regioni,self.provincie)
		#aggrego i comuni alle provincie
		self.childrenAdder(self.provincie,self.comuni)
		#aggrego i cap ai relativi comuni
		self.childrenAdder(self.comuni, self.cap)
		return self.regioni
	
	def addCap(self,c):
		""" aggiunge un elemento alla lista self.cap
		@param Nodo:
		self.comuni.append(c)
		"""
		self.cap.append(c)
		
	def addProvincia(self,c):
		""" aggiunge un elemento alla lista self.provincia
		@param Nodo:
		self.comuni.append(c)
		"""
		self.provincie.append(c)
		
	def addRegione(self,c):
		""" aggiunge un elemento alla lista self.cap
		@param Nodo:
		self.comuni.append(c)
		"""
		c.setSubHeader(2)#e' un valore dummy perche' in questo caso voglio settate un subHeader ""
		self.regioni.append(c)
		
	def getComune(self):
		""" aggiunge un elemento alla lista self.comuni
		@param Nodo:
		self.comuni.append(c)
		"""
		return self.comuni

	def getCap(self):
		""" aggiunge un elemento alla lista self.cap
		@param Nodo:
		self.comuni.append(c)
		"""
		return self.cap
		
	def getProvincia(self):
		""" aggiunge un elemento alla lista self.provincia
		@param Nodo:
		self.comuni.append(c)
		"""
		return self.provincie
		
	def getRegione(self):
		""" aggiunge un elemento alla lista self.cap
		@param Nodo:
		self.comuni.append(c)
		"""
		return self.regioni
	
	def childrenAdder(self,lf,lc):
		"""aggiunge father nodi figli della seconda lista lc ai rispettivi nodi padre nella prima lista
		@param [Nodo]: lista contenente father nodi padre
		@param [Nodo]: lista contenente father nodi figli
		@return: [Nodo] lista dei nodi padre a cui sono stati aggiunti father figli  
		""" 
		db = self.user.getActiveDb().getConnectionMMASGISDB()#MySQLdb.connect(host="localhost", user="metmi", passwd="metmi",db="mmasgisDB")
		crs=db.cursor()
		for father in lf:
			for child in lc:
				if father.getId()==child.getFather():
					# aggiungo il nodo all'albero
					father.getNode().addChild(child.getNode())
					#aggiungo il nodo alla lista dei nodi figli di father
					father.appendChild(child)
					#setto lo subHeader del figlio
					child.setSubHeader(crs,father)
					#print "ho aggiunto ",child,"a",father
		db.close
		return lf

	def collapseAll(self):
		"""collassa i nodi dell'albero relativi a province e comuni"""
		for i in self.comuni:
			i.getNode().setExpanded(False)
		for i in self.provincie:
			i.getNode().setExpanded(False)
from Odict import *