#!/usr/bin/env python
# -*- coding: latin-1 -*-
from mysql_sqlalchemy_class import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from elixir import *
from sqlalchemy import *
from AnagraficaDb import *


class Odict(dict):
	"""
	implementa un' ordered dict estendendo la classe dict
	crea una lista che memorizza le chiavi inserite nel dict  con lo stesso ordine di inserimento
	"""
	def __init__(self):
		self.order=[]
		
	def clear(self):
		"""
		override del metodo clear
		"""
		dict.clear(self)
		self.order=[]
	
	def __setitem__(self, key, value):
		"""
		override di __setitem__
		oltre alle normali operazioni di __setitem__ inserisce le chiavi in self.order
		@param key: come in dict 
		@param value:come in dict
		"""
		#aggiungo le chiavi nell'ordine di inserimento
		self.order.append(key)
		dict.__setitem__(self, key, value)
	def iterkeys(self):
		"""
		override del metodo iterkeys invece dell'iteratore di dict ritorna la lista delle chiavi
		"""
		return self.order


class Entity2Export():
	"""
	rappresenta le entita' che possono essere selezionate 
	per l'estrazione dell'anagrafica
	"""
	
	def initDB(self,dbfile):
		"""
		@param string:stringa di connessione al db, con il seguente formato di stringa "user:pwd@host/nomedb" esempio root:xxxxx@localhost/parafarmacie
		inizializza il db
		"""
		metadata.bind = "mysql://%s"%dbfile
		metadata.bind.echo = False
		setup_all()  
		
	def fetchPv(self,Id):
		"""
		recupera il pv relativo allo Id memorizzato in self.pv_id
		@param int:
		@return   
		"""

		return self.db.fetchPv(Id)
	
	def setDb(self,db):
		self.db=db
	
	def populateFetchers(self,populate):
		"""
		popola il dict dei fetchers dei dati
		"""
# instanzio una funzione lambda che ritorna l'attributo valore dell'oggetto sqlalchemy, se per il pv esiste il potenziale MMAS piuttosto che una stringa vuota se non esiste		
		l=lambda x:x.valore if type(x)!=type("") else ""
		l1=lambda x,y:x if y==True else None
		self.fetchers['codice MMAS']=l1(self.pv.codice,populate)
		self.fetchers['potenziale MMAS']=l1(l(self.db.getPotentialValueById4Extraction(self.pv_id)),populate)
		self.fetchers['ragione sociale']=l1(self.pv.ragione_sociale,populate)
		self.fetchers['titolare']=l1(self.pv.titolare,populate)
		self.fetchers['codFisc_P.IVA']=l1(self.pv.cf_pi,populate)
		self.fetchers['cod cliente']=l1(self.pv.cod_cliente,populate)
		self.fetchers['indirizzo']=l1(self.pv.indirizzo,populate)
		self.fetchers['comune']=l1(self.pv.comune,populate)
		self.fetchers['provincia']=l1(self.pv.provincia,populate)
		self.fetchers['cap']=l1(self.pv.cap,populate)
		self.fetchers['telefono']=l1(self.pv.tel1,populate)
		self.fetchers['fax']=l1(self.pv.fax,populate)
		self.fetchers['sito']=l1(self.pv.sito,populate)
		self.fetchers['email']=l1(self.pv.email,populate)
		self.fetchers['cliente']=l1(self.pv.cliente,populate)
		self.fetchers['certificato']=l1(self.pv.certificato,populate)
		self.fetchers['codice istat']=l1(self.pv.tc_istat_id,populate)


		
	def setId(self,Id,populate=True):
		"""
		setter di self.pv_id
		contestualmente allo id deve essere aggiornato  self.pv e self.fetchers
		"""
		self.pv_id=Id
		#aggiorno self.pv
		self.pv=self.fetchPv(Id)
		self.populateFetchers(populate)
		
		
		
	def getAvailableEntity(self):
		"""
		ritorna la lista delle entità referenziabili
		in pratica è la lista delle chiavi di self.fetchers
		@return: [string]
		"""
		l=[]
		for i in self.fetchers.iterkeys():
			l.append(i)
		return l 
	

	def setHeader(self, h):
		"""
		setter di self.header, questo attributo setta la classe, nel senso che
		getValue ritorna il valore relativo all attributo di Pv che nel dict self.fetcher
		è distinto dalla chiave corrispondente a self.header
		@param string:uno degli attributi della tabella pv 
		"""
		self.header=h
		
	def getHeaders(self,subfix=True):
		"""
		ritorna gli headers per l'estrazione delle enagrafiche
		@note: se l'entita' non necessita di configurazione ritorna self.header, valore che viene impostato dal costruttore, altrimenti ritorna gli header ottenuti invocando il metodo 
		getHeaders di Configurator
		@return: [string]
		"""
		d=self.getHeader()
		if self.Configurator is not  None:
			d=self.Configurator.getHeaders(subfix)
		return d 
		
	def getValue(self,Id,fetcher,set=False):
		"""
		ritorna il valore relativo al campo desiderato, specificato dal parametro fetcher
		@param string: header del fetcher dell'entita'
		@param bool: specifica se e' un'entita' configurabile o meno, se configurabile deve invocare il metodo getData di configurator
		@param int:Id del pv in esame 
		altrimenti ritorna il fetcher 
		return string 
		"""
		if set:
			self.setId(Id,set)
		#self.setId(Id)
		#d=[False]=self.fetchers[fetcher]
		#d[True]=self.configurator.getData(self.getEntityId())
		if  self.Configurator is None:
			d=self.fetchers[fetcher]
		else:
			d=self.Configurator.getData(Id)
		return d 
	
	def setRequired(self,b):
		""" setter di self.required
		@param boolean:
		"""
		self.required=b 
		
	def isRequired(self):
		"""
		getter di self.required
		@return: boolean
		"""
		return self.required
	
	def setConfigurator(self,c):
		"""
		setter di self.configurator, questo è l'oggetto che si occupa di configurare le entità delle marche e  dei parametri
		@param Configurator: 
		"""
		self.Configurator=c 

	def needsConfiguration(self):
		"""
	 	getter di self.toBeConfigured
	 	@return: boolean
	 	"""
	 	l=lambda a,b:a and not b 
	 	a=self.toBeConfigured
	 	b=self.configured
		return l(a,b) 
	
	def getData(self,Id):
		"""
		ritorna i dati forniti dalle entita' configurabili
		dovrebbe essere invocato solo se needsConfiguration e' settato a True e il configuratore dell'entita' impostato
		@param int: pv_id del pv investigato
		@return: [string]
		""" 
		return self.configurator.getData(Id)
	
	def isConfigured(self):
		"""
		getter di self.configured
		@return: boolean
		"""
		return self.configured
	
	def setConfigured(self,b):
		"""
		setter di self.configured
		@param boolean: 
		"""
		self.configured=b 
	
	def setListId(self,Id):
		"""
		setter di self.list_id
		"""
		self.list_id=Id
		
	def getListId(self):
		"""
		getter di self.list_id
		"""
		return self.list_id
	
	def setEntityId(self,Id):
		"""
		setter di entityId
		@param Id:int 
		"""
		#print "ww"*1000
		#print Id
		if not self.toBeConfigured:
			self.entityId=Id
		
	def getEntityId(self):
		"""getter di self.entityId
		@return: boolean
		"""
		return self.entityId
	
	def getHeader(self):
		"""
		getter di self.header
		@return: string
		"""
		return self.header
	
	def __repr__(self):
		return "Entity-%s: required:%s| toconfigure:%s,Id%d"%(self.header,self.required,self.toBeConfigured,self.Id)
	
	def setOrder(self,order):
		"""
		 setter di self.order
		 @param int: ordine con cui deve essere visualizzata l'entita' 
		"""
		self.order=order
		
	def getorder(self):
		"""
		getter di self.order, questo rappresenta l'ordine con cui verra' visualizzata l'entita'
		@return: int
		"""
		return self.order
	
	def reset(self):
		self.configured=False
		self.required=False
		self.Configurator=None
		print "reset"
	
	def setType(self,t):
		self.type=t
		
	def getType(self):
		return self.type
	
	def __init__(self,header,toBeConfigured,entityId,user,activeDb,db,tipo,populate=True):
		"""
		@param header:string: rappresenta lo header della colonna  
		del campo quando viene esportato, e' importante che corrisponda alla chiave usata per il campo in self.fetchers
		@param toBeConfigured:boolean  indica se l'entita' deve essere configurata o meno, sempre False tranne che per marche e parametri
		@param entityId:int: identifica l'entita' nella lista entityList di Profilo
		"""	
		self.user=user
		self.activeDb=activeDb
		self.order=-1
		self.type=tipo
		self.header=header
		self.pv_id=None
		self.entityId=-1
		self.db=db
		self.Id=entityId
		self.toBeConfigured=toBeConfigured
		self.Configurator=None
		self.required=False
		self.configured=False
		self.list_id=-1# distingue l'entita' in entityList in esportazione
		# acquisisco un' istanza di mysql_sqlalchemy_class.Pv 
		self.pv=self.db.fetchPv(self.Id)
		#instanzio il dict dei fetchers
		self.fetchers=Odict()
		#popolo il dict dei fetchers
		self.populateFetchers(populate)
		
		
