#!/usr/bin/python
# -*- coding: latin-1 -*-
import re 
from constants import *


class Relations():
	""" esprime le relazioni n:m esistenti tra utenti e funzioni, utenti e dbs
	utenti e UTB
	trasformando la base dati offerta da Qsettings in una base dati relazionale
	"""
	def __init__(self):
		self.header=""
		self.qName=""
		self.category=""
		#per default non puo' fare nulla 
		self.relations={}
		
	def __repr__(self):
		return "relazione: {0},{1} elementi".format(self.category,len(self.relations))
	def getCategory(self):
		""" ritorna la categoria di Relations
		e' il riferimento al tipo di oggetti che vengono relazionati con gli utenti nella istanza di Relations
		@return: string<'user'><'db'><'function'><'utb'>
		
		"""
		return self.category
		
	def setCategory(self, c):
		""" setta la categoria di Relations
		e' il riferimento al tipo di oggetti che vengono relazionati con gli utenti nella istanza di Relations
		@param: string<'user'><'db'><'function'><'utb'>
		
		"""
		self.category=c	
		
	def getRelations(self,k):
		"""ritorna le relazioni definite per l'utente di cui e' passato il qName
		@return: <int><[string]>::<[Object.Qname]>
		"""
		if self.relations.has_key(k):
			return self.relations[k]
		else:
			return []
		
	def updateRelations(self, k,l):
		""" aggiunge le relazioni di un utente al dict  degli utenti con la lista degli oggetti a lui disponibili
		il formato della struttura dati e' il seguente:
		{string:<[string]>int}::{user.qName:[Object.qName]} se al posto della lista c'e' un intero significa che l'utente ha accesso a tutti gli oggetti di quella categoria
		@param string: chiave del dict User.Qname
		@param <int><[Object.Qname]>:se int l'utente ha accesso a tutti gli oggetti della  categoria descritta da Relations  
		"""
		self.relations[k]=l
		
	def setQName(self,q):
		"""setta la chiave di Qsettings
		@param string:
		""" 
		self.qName=q
		
	def getQName(self):
		""" ritorna la chiave per QSettings
		@return: string
		"""
		return self.qName
		


class Function():
	"""descrive le funzionalita' di mmasgis, cosi' che possano essere
	assegnate ad un utente per definirne il profilo
	"""
	def __init__(self,header,Id):
		self.Id=Id
		self.header=header
		self.category=""
		self.qName=""
		
	def setId(self,Id):
		self.Id=Id
		
	def getId(self):
		return self.Id
		
	def __repr__(self):
		return "Function: {0}, {1} qname:{2}".format(self.category,self.header,self.qName)
	
	def setHeader(self,h):
		self.header=h
		
	def getHeader(self):
		return self.header
	
	def setCategory(self,c):
		self.category=c 
		
	def getCategory(self):
		return self.category
	
	def getQname(self):
		""" ritorna la chiave di Qsettings della funzione
		@return: string
		"""
		return self.qName
	
	def setQname(self,q):
		""" setta la chiave di Qsettings per l'istanza di Function
		@param string: 
		"""
		self.qName=q 

class UTB():
	"""e' un alias di Node per memorizzare le zone agente con QSettings
	 senza  salvare tutto l'oggetto Node, ma solo i parametri sufficienti per identificare lo UTB negli shapefiles
	 """
	def __init__(self,cat,head,Id):
		"""
		@param string: catregoria dello shapefile:<comune>,<provincia>,<cap>,<regione> il valore reale dipende dal nome usato negli shapefiles
		@param string: etichetta dello UTB
		@param int: featureId  		 
		"""
		self.category=cat
		self.header=head
		self.Id=Id
		
	def setCategory(self,c):
		self.category=c
		
	def setHeader(self,h):
		self.header=h
		
	def setId(self,i):
		self.Id=i 
		
	def getCategory(self):
		return self.category
	
	def getHeader(self):
		return self.header
	
	def getId(self):
		return self.Id
	
	def __repr__(self):
		return "UTB: {0} {1} Id: {2}".format(self.category,self.header,self.Id)
	
class Zone():
	"""definisce l'insieme di UTB disponibili per l'utente
	"""
	def __init__(self,area={}):
		"""
		 per default  nessuna funzione e' resa disponibile per l'utente 
		@param opzionale :<int>,<{string:Function}::{cod identificativo funzione:Function}>, se int significa che l'utente puo' fare tutto,
		 se viene passata una lista di funzioni, queste saranno le uniche disponibili per l'utente, che di default non puo' fare nulla
		 """  
		self.area=area
		
	def __repr__(self):
		l=lambda x: "profilo amministratore" if type(x)==type(1) else "profilo standard: {0}".format(x)
		return l(self.area)
		
	def getZone(self):
		"""
		ritorna il set di aree registrate
		@return: <it>,<{string:Nodo}::{cod identificativo funzione:Nodo}>, se int significa che l'utente ha accesso a tutte le aree
		"""
		return self.area
		
		
	def setZone(self,a):
		"""setta le aree di competenza  del profilo
		@param <-1>,<{string:Nodo}::{cod identificativo funzione:Nodo}> se int significa che l'utente puo' fare tutto,
		"""
		self.area=a

		
		
	def isAvailable(self,cod):
		""" verifica se la funzione il cui codice e' passato come argomento e' permessa all'utente
		@param bool:
		"""
		administrator=lambda k,d: True
		ordinaryUser=lambda k,d:d.has_key(k)
		users={}
		users[type(1)]= administrator
		users[type({})]=ordinaryUser
		return users[type(self.area)](cod,self.area)
	
	

class Profile():
	"""definisce l'insieme di funzioni disponibili per l'utente
	"""
	def __repr__(self):
		l=lambda x: "profilo amministratore" if type(x)==type(1) else "profilostandard: {0}".format(x)
		return l(self.profile)
	def __init__(self,role={}):
		"""
		 per default  nessuna funzione e' resa disponibile per l'utente 
		@param opzionale :<int>,<{id:Function}::{funzione_id:Function}>, se int significa che l'utente puo' fare tutto,
		 se viene passata una lista di funzioni, queste saranno le uniche disponibili per l'utente, che di default non puo' fare nulla
		 """  
		self.profile=role
		
	def getProfile(self):
		"""
		ritorna il set di funzioni registrate con il profilo
		@return: <it>,<{string:Function}::{cod identificativo funzione:Function}>, se int significa che l'utente puo' fare tutto
		"""
		return self.profile
		
	def setProfile(self,p):
		"""setta le funzioni registrate per il profilo
		@param <-1>,<{string:Function}::{cod identificativo funzione:Function}> se int significa che l'utente puo' fare tutto.
		"""
		self.profile=p 
		
	def isPermitted(self,cod):
		""" verifica se la funzione il cui codice e' passato come argomento e' permessa all'utente
		@param id: function_id
		"""
		administrator=lambda k,d: True
		ordinaryUser=lambda k,d:d.has_key(k)
		users={}
		users[type(1)]= administrator
		users[type({})]=ordinaryUser
		return users[type(self.profile)](cod,self.profile)

class User():
	""" implementa il concetto di utente  loggato con i db ad esso registrati  e il logo aziendale da usare nell'esprtazione in pdf
	"""
	def __init__(self,uname,Id):
		self.name=uname
		self.Id=Id
		self.amministratore=0
		self.ruolo=-1
		self.qName=""
		self.company_id=-1
		self.loggingTime=""
		self.logo=None
		self.registeredDbs=[]# questa resta per compatibilita' verso il basso io holaversione nuova di User gli altri no
		self.dbs=DbSet({})
		self.logged=False
		self.area=Zone({})
		self.profile=Profile({})
		self.zone=Zone({})	
		#dummy Db
		self.activeDb=	Db('dbName','descrizione','user_name','pwd','host','rdbms','Id')
		self.pwd=""
		
	def setAmministratore(self,a):
		self.amministratore=a 
		
	def getAmministratore(self):
		return self.amministratore
	
	def setCompany(self,c):
		self.company_id=c 
		
	def getCompany(self):
		return self.company_id
		
	def setRuolo(self,r):
		self.ruolo=r 
		
	def getRuolo(self):
		return self.ruolo

	def setLoggingTime(self,t):
		"""
		setta il loggingtime per l'utente
		@param datetime.datetime: tempo attuale come ottenuto da datetime.datetime.now() 
		"""
		self.loggingTime=t
		
	def getLoggingTime(self):
		"""
		ritorna il loggingTime
		@return: datetime.datetime
		"""
		return self.loggingTime			
		
	def setDbset(self,dbs):
		""" setta i dbs registrati con l'utente
		@param DbSet
		"""
		self.dbs=dbs 
		
	def getDbset(self):
		"""ritorna il dict dei dbsregistrati con  l'utente
		@return dbSet
		"""
		#creo una lambda f che ritorna il db relativo alla chiave di self.dbs
		
		return self.dbs
		
	def setProfile(self,p):
		"""setta il profilo utente, cioe' l'insieme di funzioni disponibili per l'utente
		@param Profile::{codice identificativo della funzione:oggetto funzione}
		"""
		self.profile=p 
		
	def getProfile(self):
		"""
		riorna il profilo utente, cioe' l'insieme di funzioni disponibili per l'utente
		@return:  Profile
		"""
		return self.profile		
	
	def setZone(self,p):
		"""setta la zona utente, cioe' l'insieme di aree di competenza dell'utente
		@param {string:Nodo}::{codice identificativo dell'area geografica:Nodo}
		"""
		self.zone=p 
		
	def getZones(self):
		"""
		riorna la zona utente, cioe' l'insieme di aree di competenza dell'utente
		@return:  {string:None}::{Nodo.signature:None}
		"""
		z={}
		if type(self.zone)==type(1):
			#se super-user self.zone e' un intero
			z=self.zone
		else:
			for k in self.zone.itervalues():
				z[k.getSignature()]=None
		return z
	
	def resetProfile(self):
		"""resetta il dict dei profili 
		@note: i profili utente sono registrati  con Qsettings in un oggetto relations con chiave profiles
		"""
		self.profile={}
		
	def resetDbs(self):
		"""resetta il dict dei dbs 
		@note: i dbs utente sono registrati  con Qsettings in un ggetto relations con chiave dbs
		"""
		self.dbs={}
		
	def resetZones(self):
		"""resetta il dict delle zone 
		@note: le zone utente sono registrate  con Qsettings in un oggetto relations con chiave zones
		"""
		self.zone={}
		
	def getLogo(self):
		return self.logo
	
	def setLogo(self,l):
		self.logo=l 
	
	def setName(self,n):
		self.name=n
		
	def getQName(self):
		""" ritorna la chiave di Qsetting per User
			@return: string
		"""
		return self.qName
	
	def setQname(self,q):
		"""setta la chiave di QSettings per User
		"""
		self.qName=q
		
	def setPassword(self,p):
		self.pwd=p 
		
	def getPassword(self):
		return self.pwd
	
	def isLogged(self):
		"""ritorna lo stato dell'utente se loggato e' True
		@return: bool
		"""
		return self.logged
	
	def setLogged(self,b):
		"""setta il parametro logged
		@param bool:
		"""
		self.logged=b
		
	def getName(self):
		"""ritorna lo user name
		@return: string
		"""
		return self.name
	
	def setId(self,Id):
		self.Id=Id
	
	def getId(self):
		"""ritorna lo id utente
		@return: int
		"""
		return self.Id
	
	def getRegisteredDb(self):
		"""converte il dict dei db registrati per l'utente in una lista
		@return: [Db]
		"""
		dbs=[]
		for db in self.registeredDbs.iterValues():
			dbs.append(db)
		return dbs
	
	def setRegisteredDb(self,l):
		""" setta la lista dei db registrati
		@param [DB]:
		"""
		self.registeredDbs=l 
	
	def getActiveDb(self):
		"""ritorna il db attivo dell'utente
		@return: DB
		"""
		return self.activeDb
		"""
		for i in self.registeredDbs:
			if i.isActive():
				db=i 
				"""
		return self.activeDb
	
	def setActiveDb(self,Id):
		"""setta il db attivo,solo un db alla volta puo' essere attivo
		@param int: db_Id
		"""
		#disattivo tutti i dbs
		self.activeDb=Id
				
	def __repr__(self):
		l=lambda x: "autenticato"if x else "non autenticato"
		txt="User: {0}, Id:{1}, {2}, profilo: {3},dbs: {4}, zone: {5}".format(self.name,self.Id,l(self.logged),self.profile,self.dbs,self.zone)
		for i in self.registeredDbs:
			txt+="\d {0}".format(i)
		return txt
			
	
class DbSet():
		"""
		definisce l'insieme di db cui l'utente e' autorizzato
		"""
		
		def __repr__(self):
			l=lambda x:"amministratore censimenti" if type(x)==type(1) else "utente ordinario"
			return "Dbset: {0}".format(l(self.profile))
		
		def __init__(self,dbSet={}):
			"""
			 per default  nessun db e' accessibile per l'utente 
			@param opzionale :<int>,<{id:Db}::{db_id:Db}>, se int significa che l'utente ha accesso a tutti i db del sistema mmasgis,
			 se viene passata una lista di db, questi saranno gli unici disponibili per l'utente, che di default non puo' fare nulla
			 """  
			self.profile=dbSet
		
		def getProfile(self):
			"""
			ritorna il set di funzioni registrate con il profilo
			@return: <it>,<{string:Function}::{cod identificativo funzione:Function}>, se int significa che l'utente puo' fare tutto
			"""
			return self.profile
			
		def setProfile(self,p):
			"""setta le funzioni registrate per il profilo
			@param <-1>,<{string:Function}::{cod identificativo funzione:Function}> se int significa che l'utente puo' fare tutto.
			"""
			self.profile=p 
			
		def isPermitted(self,cod):
			""" verifica se il db il cui id e' passato come argomento e' permessa all'utente
			@param int:db_id
			"""
			administrator=lambda k,d: True
			ordinaryUser=lambda k,d:d.has_key(k)
			users={}
			users[type(1)]= administrator
			users[type({})]=ordinaryUser
			return users[type(self.profile)](cod,self.profile)
		
	
class extendedUser(User):
	
	def __repr__(self):
		l=lambda x: "autenticato"if x else "non autenticato"
		txt="User: {0}, Id:{1} {2} {3}".format(self.name,self.Id,l(self.logged),self.loggingTime)
		for i in self.registeredDbs:
			txt+="\d {0}".format(i)
		return txt
	
	def __init__(self,uname,Id):
		self.name=uname
		self.Id=Id
		self.logo=None
		self.logged=False
		self.loggingTime=""
		self.qsettingsName=""
		self.profile={}
		self.zone={}
		self.pwd=""
		self.registeredDbs=[]
		
	def setProfile(self,p):
		"""setta il profilo utente, cioe' l'insieme di funzioni disponibili per l'utente
		@param {string:Function}::{codice identificativo della funzione:oggetto funzione}
		"""
		self.profile=p 
		
	def getProfile(self):
		"""
		riorna il profilo utente, cioe' l'insieme di funzioni disponibili per l'utente
		@return:  {string:Function}::{codice identificativo della funzione:oggetto funzione}
		"""
		return self.profile		
	
	def setZone(self,p):
		"""setta la zona utente, cioe' l'insieme di aree di competenza dell'utente
		@param {string:Nodo}::{codice identificativo dell'area geografica:Nodo}
		"""
		self.zone=p 
		
	def getZone(self):
		"""
		riorna la zona utente, cioe' l'insieme di aree di competenza dell'utente
		@return:  {string:Nodo}::{codice identificativo della funzione:Nodo}
		"""
		return self.zone
		
	def getLogo(self):
		return self.logo
	
	def setLogo(self,l):
		self.logo=l 
		
	def getPassword(self):
		return self.pwd
		
	def setPassword(self,p):
		self.pwd=p 
		
	def getRegisteredDb(self):
		return self.registeredDbs

	def setRegisteredDb(self,l):
		self.registeredDbs=l 
		
	def isLogged(self):
		return self.logged
	
	def setLogged(self,b):
		self.logged=b 
		
	def getSettingsName(self):
		""" ritorna il nome con cui viene identificato da Datasource nel sistema
		@return: string
		"""
		return self.qsettingsName
	
	def setSettingsName(self,n):
		"""
		setta  il nome che identifica l'utente in DataSource
		@param string:
		"""  
		self.qsettingsName=n		
	
	def setLoggingTime(self,t):
		"""
		setta il loggingtime per l'utente
		@param datetime.datetime: tempo attuale come ottenuto da datetime.datetime.now() 
		"""
		self.loggingTime=t
		
	def getLoggingTime(self):
		"""
		ritorna il loggingTime
		@return: datetime.datetime
		"""
		return self.loggingTime								
			



class USER():
	""" implementa il concetto di utente  loggato con i db ad esso registrati  e il logo aziendale da usare nell'esprtazione in pdf
	"""
	def __init__(self,uname,Id):
		self.name=uname
		self.Id=Id
		self.logo=None
		self.logged=False
		self.loggingTime=""
		self.qsettingsName=""
		self.profile=Profile({})
		self.zone=Zone({})
		self.dbs=DbSet({})
		self.pwd=""
		self.activeDb=None
		self.registeredDbs=[]
		
	def getDbs(self,object=False):
		""" ritorna il dict dei db registrati
		@param bool: facoltativo se True ritorna le istanze deidbs registrati
		@return: <{string:None}::{Db.qName:None}><{string:Db}::{Db.qName:Db}  
		"""
		l=lambda k,b:self.dbs[k] if b==True else None
		db={}
		if type(self.dbs)==type(1):
			#utente root
			db=self.dbs
		else:
			for k in self.dbs.iterkeys():
				db[k]=l(k,object)
		return db
	
	def setName(self,n):
		self.name=n 	
	
	def setPassword(self,p):
		self.pwd=p 
		
	def getPassword(self):
		return self.pwd
		
	def setProfile(self,p):
		"""setta il profilo utente, cioe' l'insieme di funzioni disponibili per l'utente
		@param {string:Function}::{codice identificativo della funzione:oggetto funzione}
		"""
		self.profile=p 
		
	def getProfile(self):
		"""
		riorna il profilo utente, cioe' l'insieme di funzioni disponibili per l'utente
		@return:  {string:Function}::{codice identificativo della funzione:oggetto funzione}
		"""
		return self.profile		
	
	def setZone(self,p):
		"""setta la zona utente, cioe' l'insieme di aree di competenza dell'utente
		@param {string:Nodo}::{codice identificativo dell'area geografica:Nodo}
		"""
		self.zone=p 
		
	def getZone(self):
		"""
		riorna la zona utente, cioe' l'insieme di aree di competenza dell'utente
		@return:  {string:Nodo}::{codice identificativo della funzione:Nodo}
		"""
		return self.zone
		
	def getLogo(self):
		return self.logo
	
	def setLogo(self,l):
		self.logo=l 

	def getSettingsName(self):
		""" ritorna il nome con cui viene identificato da Datasource nel sistema
		@return: string
		"""
		return self.qsettingsName
	
	def setSettingsName(self,n):
		"""
		setta  il nome che identifica l'utente in DataSource
		@param string:
		"""  
		self.qsettingsName=n		
	
	def setLoggingTime(self,t):
		"""
		setta il loggingtime per l'utente
		@param datetime.datetime: tempo attuale come ottenuto da datetime.datetime.now() 
		"""
		self.loggingTime=t
		
	def getLoggingTime(self):
		"""
		ritorna il loggingTime
		@return: datetime.datetime
		"""
		return self.loggingTime								
		
	def isLogged(self):
		"""ritorna lo stato dell'utente se loggato e' True
		@return: bool
		"""
		return self.logged
	
	def setLogged(self,b):
		"""setta il parametro logged
		@param bool:
		"""
		self.logged=b
		
	def getName(self):
		"""ritorna lo user name
		@return: string
		"""
		return self.name
	
	def getId(self):
		"""ritorna lo id utente
		@return: int
		"""
		return self.Id
	
	def getRegisteredDb(self):
		"""ritorna la lista dei db registrati per l'utente
		@return: [Db]
		"""
		return self.registeredDbs
	
	def setRegisteredDb(self,l):
		""" setta la lista dei db registrati
		@param [DB]:
		"""
		self.registeredDbs=l 
	
	def getActiveDb(self):
		"""ritorna il db attivo dell'utente
		@return: DB
		"""
		return self.activeDb
	
	def setActiveDb(self,db):
		"""setta il db attivo,solo un db alla volta puo' essere attivo
		@param Db: db attivo
		"""
		self.activeDb=Db
				
	def __repr__(self):
		l=lambda x: "autenticato"if x else "non autenticato"
		txt="User: {0}, Id:{1} {2}".format(self.name,self.Id,l(self.logged))
		for i in self.registeredDbs:
			txt+="\d {0}".format(i)
		return txt
			
		

		
class Db():
	
	
	def getSettingsName(self):
		""" ritorna il nome con cui viene identificato da Datasource nel sistema
		@return: string
		"""
		return self.qsettingsName
	
	def setSettingsName(self,n):
		"""
		setta  il nome che identifica l'utente in DataSource
		@param string:
		"""  
		self.qsettingsName=n		
	
	
	def getConnectionString(self):
		"""ritorna la stringa di connessione per sqlalchemy
		il formato dela stringa è
		user:pwd@host/db
		@return: string
		"""
		"root:vilu7240@localhost/parafarmacie"
		str="{0}:{1}@{2}/{3}".format(self.user_name,self.password,self.host,self.name)
		return str	
	
	def mysqlConnect(self):
		return self.cons.dbDrivers[self.getRDBMS()].connect(host=self.getHost(), user=self.getUserName(), passwd=self.getPassword(),db=self.getNameDb(),charset="utf8",use_unicode=True)

	def pgConnect(self):
		print "pg connection string","host='{0}' user='{1}' password='{2}' dbname='{3}'".format(self.getHost(),self.getUserName(),self.getPassword(),self.getNameDb())
		return self.cons.dbDrivers[self.getRDBMS()].connect("host='{0}' user='{1}' password='{2}' dbname='{3}'".format(self.getHost(),self.getUserName(),self.getPassword(),self.getNameDb()))
	
	
	def parser(self,txt,pattern):
		#print "text in parser",txt
		match=re.compile(pattern)
		return match.findall(txt)
	
	def __init__(self,dbName,Id,descrizione="",user_name="",pwd="",host="",rdbms=""):
		""""
		@param string: nome del db
		@param string:descrizione
		@param string:user name
		@param string: password
		@param string: host
		@param string: famiglia db<mysql><postgres> ...      
		"""
		self.cons=cons()
		self.qName=""
		self.port=-1
		self.category="db"
		self.name=dbName
		self.descrizione=descrizione
		self.user_name=user_name
		self.host=host
		self.password=pwd
		self.rdbms=""
		self.censimento=""
		self.versione=""
		self.ins_data=""
		self.mod_data=""
		self.ins_utente=""
		self.mod_utente=""
		self.azienda_id=""
		#print "id da parser",lId[0][0]
		self.Id=Id
		self.active=False
		
	def setCensimento(self,c):
		self.censimento=c
		
	def setPort(self,p):
		self.port=p 
		
	def getPort(self):
		return self.port
		
	def getCategory(self):
		""" ritorna lacategoria della classe,
		@note: questometodo e' dummy e' inserito per rendere la classe  Db consistente con Function per CheckFactory in settings.py
		@return: string "db"
		"""
		return self.category
			
	def getCensimento(self):
		return self.censimento
	def setVersione(self,v):
		self.versione=v
	
	def getVersione(self):
		return self.versione
	
	def setIns_data(self,i):
		self.ins_data=i 
		
	def getIns_data(self):
		return self.ins_data
	
	def setMod_data(self,m):
		self.mod_data=m
		
	def getMod_data(self):
		return self.mod_data
	
	def setIns_utente(self,i):
		self.ins_utente=i 
		
	def getIns_utente(self):
		return self.ins_utente
	def getMod_utente(self):
		return self.mod_utente

	def setMod_utente(self,m):
		self.mod_utente=m
		
	def setCompany(self,c):
		self.azienda_id=c 
		
	def getCompany(self):
		return self.azienda_id
		
	def getQname(self):
		return self.qName	
	
	def setQname(self,q):
		self.qName=q
		
	def getConnection(self):
		connectFunctions={}
		connectFunctions['mysql']=self.mysqlConnect
		connectFunctions['postgres']=self.pgConnect	
		return connectFunctions[self.rdbms]()	
	
	def getUserName(self):
		"""ritorna lo user_name del db da usare nella connectionString
		@return: string
		"""
		return self.user_name
	
	def getPassword(self):
		"""ritorna la password di accesso al db
		@return:  string
		"""
		return self.password
		
	def isActive(self):
		"""getter per self.active
		@return: bool
		"""
		return self.active
	
	def setHost(self,h):
		self.host=h
		
	def getHeader(self):
		return self.name
	
	def setRDBMS(self,r):
		self.rdbms=r 

		
	def getRDBMS(self):
		return self.rdbms
		
	def setNameDb(self,db):
		self.name=db
	
	def setUserName(self,u):
		self.user_name=u
		
	def setPassword(self,p):
		self.password=p 
		
	
	def getHost(self):
		return self.host
	
	def setDescrizione(self,d):
		self.descrizione=d 
		
	def getSDescrizione(self):
		return self.descrizione
	
	
	def setId(self,Id):
		self.Id=Id	
	
	def setActive(self,b):
		"""setter per self.active
		@param bool:
		"""
		self.active=b
	
	def getDescription(self):
		""" ritorna la descizione che accompagna il db nella finestra di log-censimento
		@return: string
		"""
		return self.descrizione
	
	def getId(self):
		"""ritorna lo id del db
		@return: int
		"""
		return self.Id
			
	def __repr__(self):
		l=lambda x: "active" if x else 'not active'
		return "DB "+l(self.active)+" : rdbms:{0}, nome:{1}, descrizione:{2}, host:{3},id:{4}".format(self.rdbms,self.name,self.descrizione,self.host,self.Id)
		
