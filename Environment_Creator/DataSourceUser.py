#from PyQt4 import QtCore,QtGui
import re
# Initialize Qt resources from file resources.py
from sessionClasses import *
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import *
import sys
from mmasgisDb_sqlalchemy import *
#from sqlAlchemyQueryClass import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from elixir import *
import sqlalchemy
from sqlalchemy.ext import compiler
from sqlalchemy.sql.expression import Executable, ClauseElement
from provincia import *
from environment_constants import *
from funzioni import *
from profilo import *
from createDbMysql import *
from createDbPostgres import *
from createDbMssql import *

#from Odict import *
#sys.path.append("/home/giuseppe/eclipse/plugins/org.python.pydev.debug_2.3.0.2011121518/pysrc/")
#from pydevd import *

class DataSource():
	"""
	gestisce le operazioni di lettura e scrittura sulle tabelle del db mmasgis per la gestione degli utenti dei profili, delle aree utente e dei censimenti
	"""
	def __init__(self,utonto,create=False):
		"""
		@param string: connectionstring
		@note: nellla connection string deve essere omesso il nome del db se si vuole che venga creato in automatico
"root:vilu7240@localhost"
		"""
		self.cons=dbCons
		self.dbs={}
		self.dbs['mysql']='postgres'
		self.dbs['postgresql']='postgres'
		self.dbs['mssql']='master'
		self.activeDb=utonto.getActiveDb()
		self.dbms={}
		self.user=utonto
		self.dbms['mysql']=createDbMysql(self.user,create)
		self.dbms['postgresql']=createDbPostgres(self.user,create)
		self.dbms['mssql']=createDbMssql(self.user,create)
		dbfile=self.activeDb.getUserName()+":"+self.activeDb.getPassword()+'@'+self.activeDb.getHost()+":"+str(self.activeDb.getPort())
		family=self.activeDb.getRDBMS()
		print "dbfile", dbfile
		print "datasourceuser family",family
		self.family=self.cons.queries[family]
		url = URL(drivername=self.family['family'], username=self.activeDb.getUserName(), password=self.activeDb.getPassword(), host=self.activeDb.getHost(),
				port=str(self.activeDb.getPort()), database=self.dbs[self.family['family']])

		#"mysql://"+dbfile
		#print "url","{0}://".format(family['family'])+dbfile
		self.engine = create_engine(url)#+"?charset=utf8&use_unicode=1",convert_unicode=True)
		metadata = MetaData(bind=self.engine)
		try:
			print "query change db",self.family['use']
			self.engine.execute(self.family['use'])
		except:
			print "db non esiste"
		Session = sessionmaker(bind=self.engine)
		self.session=Session()
		
	def writeProfile(self,p,profile_id,company_id=1):
		profilo=profilo_std()
		profilo.nome_profilo=p['nome']
		profilo.azienda_id=company_id
		profilo.amministratore=p['amministratore']
		profilo.profilo_id=profile_id
		self.session.add(profilo)
		self.session.flush()
		self.session.refresh(profilo)
		profilo_Id=profilo.profilo_id
		print "profilo_id",profilo_Id
		for i in  p['funzioni']:
			rpf=rel_profilo_funzioni()
			rpf.profilo_id=profilo_Id
			rpf.funzione_id=i
			self.session.add(rpf)
		self.session.commit()
		

	def createDb(self,data,create=True):
		print "datasourceuser createdb 91 family",self.family['family']
		print "start"
		db=		self.dbms[self.family['family']]
		db.createDb(self.user,data,create)
		print "finito"
		
			#print "ho inserito {0} province ".format(n)		

	def isNametaken(self,name,company_id):
		""" ritorna True se il nome utente e' gia' presente per una certa azienda
		@param string: nome utente
		@param int:company_id
		@return: bool
		"""
		c=self.session.query(utente).filter_by(nome_utente=name).filter_by(azienda_id=company_id).count()
		if c >0:
			return True
		else:
			return False
	def initDB(self,dbfile):
		"""
		@param string:stringa di connessione al db, con il seguente formato di stringa "user:pwd@host/nomedb" esempio root:xxxxx@localhost/parafarmacie
		inizializza il db
		"""
		MetaData.bind = "mysql://%s"%dbfile
		
		setup_all()
		
	def getUserCount(self):
		"""ritorna il valore attuale di UserCounter
		@return: int
		"""
		c= self.ds.value("UserCounter", 0).toInt()[0]
		return c
	
	def updateProfiles(self,userQname,profile):
		""" aggiorna il profilo utente, memorizzato nell'oggetto profiles
		@param User.qSettingsName: identificativo univoco dell'utente nel sistema nel formato user\d+
		@param {classesObject.qName:classesObject}:
		"""
		if self.ds.contains("profiles"):
			#recupero il dizionario dei profili
			profiles=self.ds.value("profiles").toPyObject()
			print profiles
		else:
			#creo un dizionario dei profili
			profiles=Relations()
		profiles.setCategory("profiles")
		profiles.updateRelations(userQname,profile)
		self.ds.setValue(profiles.getCategory(),profiles)
		
	def getUser(self, uname,pwd):
		"""ritorna l'utente identificato da uname e password
		@param string: user-name
		@param string: password
		@return: User
		"""
		for u in self.session.query(utente).filter_by(nome_utente=uname).filter_by(password=pwd):
			pass
		user=User(u.nome_utente,u.utente_id)
		user.setProfile(self.getUserProfile(u.utente_id))
		user.setId(u.utente_id)
		user.setRuolo(u.clruolo_id)
		user.setAmministratore(u.amministratore)
		user.setCompany(u.azienda_id)
		user.setDbs(self.getUserDbs(u.utente_id))
		user.setZone(self.getUserArea(u.utente_id))
		return user
	
	def getUsersList(self,company_id):
		"""ritorna la lista degli utenti registrati sul db per company_id
		@param int:company_id
		@return [User]
		"""
		users=[]
		for u in  self.session.query(utente).filter_by(azienda_id=company_id):
			user=self.getUserById(u.utente_id)
			users.append(user)
		return users
		
	def getUserById(self, Id):
		"""ritorna l'utente identificato da uname e password
		@param int: user_Id
		@return: User
		"""
		u=self.session.query(utente).filter_by(utente_id=Id).first()	
		user=User(u.nome_utente,u.utente_id)
		user.setProfile(self.getUserProfile(u.utente_id))
		user.setId(u.utente_id)
		user.setRuolo(u.clruolo_id)
		user.setCompany(u.azienda_id)
		user.setAmministratore(u.amministratore)
		user.setDbset(self.getUserDbs(u.utente_id))
		user.setZone(self.getUserArea(u.utente_id))
		return user
		
	def getDbs(self,company_id):
		""" ritorna la lista dei db registrati all'azienda
		@param int: company_id
		@return: [Db]
		"""
		l=[]
		for  d in self.session.query(dbmmas).filter_by(azienda_id=company_id):
			db=Db(d.nome_db,d.db_id)
			l.append(db)
		return l
		
	def updateZones(self,userQname,profile):
		""" aggiorna le aree utente, memorizzate nell'oggetto zones
		@param User.qSettingsName: identificativo univoco dell'utente nel sistema nel formato user\d+
		@param {classesObject.qName:classesObject}:
		"""
		
		if self.ds.contains("zones"):
			#recupero il dizionario dei profili
			profiles=self.ds.value("zones").toPyObject()
			print profiles
			#creo un dizionario dei profili
		profiles=Relations()
		profiles.setCategory("zones")
		profiles.updateRelations(userQname,profile)
		self.ds.setValue(profiles.getCategory(),profiles)
		
	def setZones(self,relations):
		"""forza l'oggetto zones di Qsettings
		@param Relations:
		"""
		self.ds.setValue("zones",relations) 	
		
	
	def registerUser(self,user, qName):
		"""
		registra un utente  nel file di sistema con l'etichetta passata come parametro
		@param User:
		@param string: etichetta di identificazione utente
		"""
		#aggiorno il profilo memorizzato in profiles
		self.updateProfiles(qName, user.getProfile())
		#aggiorno i dbs memorizzati in dbs
		self.updateDbs(qName, user.getDbs()) #voglio inserire solo le chiavi in Qsettings
		#aggiorno le aree agente
		self.updateZones(qName, user.getZones)
		#resetto i profili  i db e le zone dell'utente per salvare in Qsettings solo dict vuoti	
		user.resetProfile()
		user.resetDbs()
		user.resetZones()
		self.ds.setValue(qName, user)		
		
		
	def setUserCounter(self,c):
		"""setta il valore di UserCount
		@param int: nuovo valore di userCount
		"""
		self.ds.setValue("userCounter",c)
		
	def setDbCounter(self,c):
		"""setta il valore di DbCounter
		@param int: nuovo valore di userCount
		"""
		self.ds.setValue("dbCounter",c) 		
		
		
	def getDbCount(self):
		"""ritorna il valore attuale di dbCounter
		@return: int
		"""
		c= self.ds.value("dbCounter",0).toInt()[0]
		return c
	
	def insertUser(self,nome,cl,passwd):
		"""
		inserisce un utente nel db
		@param string:nome utente
		@param int: clruolo_id
		@param string: password
		@attention: perche' le modifiche siano permanenti occorre invocare commitOperations
		"""
		user=utente()
		user.nome_utente=nome
		user.password=passwd
		user.clruolo_id=cl
		self.session.add(user)
		
	def countUsers(self):
		"""
		ritorna il numero di utenti registrati nel db
		@return: int
		"""
		c=self.session.query(utente).count()
		return c
	
	def deleteUserDbs(self,user_id):
		for i in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id):
			self.session.delete(i)
			
	def deleteUserZone(self,user_id):
		for i in self.session.query(aree).filter_by(utente_id=user_id):
			self.session.delete(i)	
	

	def getUserDbs(self,user_id,item=False):
		"""ritorna i db regfistrati ad un utente
		@param int:user_id
		@param bool: opzionale, se True ritorna la lista direl_utente_dbmmas
		@return: Dbset
		"""
		profile={}			#self.session.query(Pv).filter_by(pv_id=Id)
		
		#se un utente e' amministratore  per i db tutte le righe di profilo hanno settato amministratore a 1
		if self.isDbAdministrator(user_id):
			profile=DbSet(-1)
		else:
			for p in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id):	
				profile[p.db_id]=self.getDbMMas(p.db_id)
			profile=DbSet(profile)
		return profile
	def getUserDbRelations(self,user_id):
		return self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id)
	
	def getItemUtente(self,Id):
		"""ritorna il mapper di sqlalchemy per utente
		@param int:utente_id
		@return: mmasgisDb_sqlalchemy.utente
		"""
		return self.session.query(utente).filter_by(utente_id=Id).first()
	
	def createNewProfile(self):
		"""ritorna il mapper di sqlalchemy per un nuovo utente
		@return: mmasgisDb_sqlalchemy.utente
		"""
		return profilo()
	
	def createNewUser(self):
		"""ritorna il mapper di sqlalchemy per un nuovo utente
		@return: mmasgisDb_sqlalchemy.utente
		"""
		return utente()
	
	
	def getAllRDU(self,user_id,db_Id):
		"""
		ritorna le relazioni utente db
		@return: mmasgisDb_sqlalchemy.rel_utente_dbmmas
		"""
		return self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id).filter_by(db_id=db_Id).all()
	def getRDU(self,user_id,db_Id):
		"""
		ritorna la relazione utente db
		@return: mmasgisDb_sqlalchemy.rel_utente_dbmmas
		"""
		return self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id).filter_by(db_id=db_Id).first()
	
	def createNewRDU(self):
		"""ritorna il mapper di sqlalchemy per una nuova relazione utente_db
		@return: mmasgisDb_sqlalchemy.rel_utente_dbmmas
		"""		
		return rel_utente_dbmmas()
	
	def getAllProfile(self,user_id):
		"""
		ritorna le relazioni utente funzione
		@return: mmasgisDb_sqlalchemy.profilo
		"""
		return self.session.query(profilo).filter_by(utente_id=user_id).all()
	
	def deleteProfile(self,user_id):
		for i in self.session.query(profilo).filter_by(utente_id=user_id).all():
			self.session.delete(i)
	def getProfile(self,user_id,function_id):
		"""
		ritorna la relazione utente funzione
		@return: mmasgisDb_sqlalchemy.profilo
		"""
		return self.session.query(profilo).filter_by(utente_id=user_id).filter_by(funzione_id=function_id).first()
	
	def deleteObject(self,obj):
		"""cancella un oggetto dalla sessione
		@param mmasgisDb_sqlalchemy:
		"""
		self.session.delete(obj)
	
	def getFunctions(self):
		"""ritorna la lista delle funzioni definite nel sistema
		@return: [Functions]
		"""
		l=[]
		for f in self.session.query(funzione).all():
			F=Function(f.nome,f.funzione_id)
			F.setCategory(f.categoria)
			l.append(F)
		return l
	
	def getUserArea(self,user_id):
		"""ritorna le aree di pertinenza  di un utente
		@return: <[string]> per l'utenteordinario<int> per l'utente root
		"""
		#se un utente e' amministratore tutte le righe di profilo hanno settato amministratore a 1
		profile={}
		if self.isAreaAdministrator(user_id):
				profile=Zone(-1)
		else:
			for p in self.session.query(aree).filter_by(utente_id=user_id):
				profile[p.UTB_id]=self.getUTB(p.UTB_id)
			profile=Zone(profile)
		return profile
	
	def getUserProfile(self,user_id):
		"""ritorna il profilo di un utente
		@return: <[int]> per l'utenteordinario<int> per l'utente root
		"""
		profile={}			#self.session.query(Pv).filter_by(pv_id=Id)
		
			
		#se un utente e' amministratore tutte le righe di profilo hanno settato amministratore a 1
		if self.isFunctionAdministrator(user_id):
			profile=Profile(-1)
		else:
			for p in self.session.query(profilo).filter_by(utente_id=user_id):
						if p is not None:
							profile[p.funzione_id]=self.getFunction(p.funzione_id)
			profile=Profile(profile)
		return profile
	
	def deleteUser(self,user_id):
		"""elimina un utente e tutte le sue  relazioni dal db
		@param int:user_id
		"""
		user=self.getItemUtente(user_id)
		self.session.delete(user)
		self.deleteProfile(user_id)
		self.deleteUserDbs(user_id)
		self.deleteUserZone(user_id)
	
	def getDbMMas(self,db_Id):
		"""
		ritorna il censimento relativo allo id passato
		@param int:db_id
		@return: Db
		"""
		DBMMAS=self.session.query(dbmmas).filter_by(db_id=db_Id).one()
		url=str(self.engine.url)
		#estraggo lo  host dallo url
		url=url[url.find('@')+1:]
		host=url[0:url.find('/')]
		db=Db('metmi','metmi',host,self.engine.name)
		db.setId(DBMMAS.db_id)
		db.setNameDb(DBMMAS.nome_db)
		return db
	
	def getFunction(self,function_id):
		"""
		ritorna la funzione con  id function_id
		@param int:function_id
		@return: Function
		"""
		f=self.session.query(funzione).filter_by(funzione_id=function_id).first()
		function=Function(f.nome,f.funzione_id)
		function.setCategory(f.categoria)
		return function
	
	def setAreaAdministrator(self,user_id,amministratore):
		"""
		rende l'utente amministratore per le aree
		@param int:utente_id
		@param bool:se True setta l'utente come amministratore
		@note: invocare commitOperations per rendere permanenti le modifiche
		"""
		l=lambda y:1 if y==True else 0
		for p in self.session.query(aree).filter_by(utente_id=user_id): 	
			p.amministratore=l(amministratore)	
	
	def setProfileAdministrator(self,user_id,amministratore):
		"""
		rende l'utente amministratore per le funzioni
		@param int:utente_id
		@param bool:se True setta l'utente come amministratore
		@note: invocare commitOperations per rendere permanenti le modifiche
		"""
		l=lambda y:1 if y==True else 0
		for p in self.session.query(profilo).filter_by(utente_id=user_id): 	
			p.amministratore=l(amministratore)	
			
	def setDbsAdministrator(self,user_id,amministratore):
		"""
		rende l'utente amministratore per i db
		@param int:utente_id
		@param bool:se True setta l'utente come amministratore
		@note: invocare commitOperations per rendere permanenti le modifiche
		"""
		l=lambda y:1 if y==True else 0
		for p in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id): 	
			p.amministratore=l(amministratore)	
			
	def addObject(self,obj):
		"""aggiunge un elemento alla sessione
		@param SQLalchemy.Element: riga daaggiungere
		"""
		self.session.add(obj)
			
	def isDbAdministrator(self,user_id):
		""" verifica chel'utente sia amministratore per i censimenti
		@param int:user_id
		@return: bool
		"""
		a=self.session.query(utente).filter_by(utente_id=user_id).first()
		if a is None:
			return False
		if a.amministratore!=1:
			return False
		else:
			return True
			
	def isAreaAdministrator(self,user_id):
		""" verifica chel'utente sia amministratore per le aree
		@param int:user_id
		@return: bool
		"""
		a=self.session.query(utente).filter_by(utente_id=user_id).first()
		if a is None:
			return False
		if a.amministratore!=1:
			return False
		else:
			return True
			
	def isFunctionAdministrator(self,user_id):
		""" verifica chel'utente sia amministratore per le funzioni
		@param int:user_id
		@return: bool
		"""
		a=self.session.query(utente).filter_by(utente_id=user_id).first()
		if a is None:
			return False
		if a.amministratore!=1:
			return False
		else:
			return True
			
	"""def addCensimento(self,name,censimento,versione, ins_utente):
			nome_db=Column(String(10))
	censimento=Column(Integer)
	versione=Column(Integer)
	ins_data=Column(DateTime)
	mod_data=Column(DateTime)
	ins_utente=Column(Integer)
	mod_utente=Column(Integer)"""
	
	def addArea(self,utente_id,area_id,administrator=False):
			"""
			aggiunge una funzione/abilita al profilo dell'utente
			@param int:utente_id
			@param string:signature della UTB
			@param bool opzionale:  se True setta a uno il campo amministratore della riga inserita in rel_utente_funzione
			@note: il campo amminisatratore della tabella profilo e' settato a 0 di default, cioe' come se fosse un utente ordinario
			@note: il parametro amministratore dovrebbe avere ilvalore ottenuto invocando isAdministrator
			@attention: perche' le modifiche siano permanenti occorre invocare commitOperations
			"""
			p=aree()
			p.utente_id=utente_id
			p.UTB_id=area_id
			if administrator:
				p.amministratore=1
			p.amministratore=0 #0 e' il valore di default per l'utente ordinario
			self.session.add(p)
	
	def addFunction(self,utente_id,funzione_id,administrator=False):
			"""
			aggiunge una funzione/abilita al profilo dell'utente
			@param int:utente_id
			@param int:function_id
			@param bool opzionale:  se True setta a uno il campo amministratore della riga inserita in rel_utente_funzione
			@note: il campo amminisatratore della tabella profilo e' settato a 0 di default, cioe' come se fosse un utente ordinario
			@note: il parametro amministratore dovrebbe avere ilvalore ottenuto invocando isAdministrator
			@attention: perche' le modifiche siano permanenti occorre invocare commitOperations
			"""
			p=profilo()
			p.utente_id=utente_id
			p.funzione_id=funzione_id
			if administrator:
				p.amministratore=1
			p.amministratore=0 #0 e' il valore di default per l'utente ordinario
			self.session.add(p)
			
	def addDb(self,user_id,db_id,administrator=False):
			"""
			aggiunge una funzione/abilita al profilo dell'utente
			@param int:utente_id
			@param int:function_id
			@param bool opzionale:  se True setta a uno il campo amministratore della riga inserita in rel_utente_funzione
			@note: il campo amminisatratore della tabella profilo e' settato a 0 di default, cioe' come se fosse un utente ordinario
			@note: il parametro amministratore dovrebbe avere ilvalore ottenuto invocando isAdministrator
			@attention: perche' le modifiche siano permanenti occorre invocare commitOperations
			"""
			p=rel_utente_dbmmas()
			p.utente_id=user_id
			p.db_id=db_id
			if administrator:
				p.amministratore=1
			p.amministratore=0 #0 e' il valore di default per l'utente ordinario
			self.session.add(p)
			
	def removeFunction(self,user_id,function_id):
		"""rimuove una funzione dal profilo utente
		@param int: utente_id
		@param int:funzione_id
		@attention: rimuovere una funzione non ha effetto se l'utente e' amministratore
		"""
		for f in self.session.query(profilo).filter_by(utente_id=user_id).filter_by(funzione_id=function_id):
			self.session.delete(f)
			
	def removeDb(self,user_id,db_Id):
		"""rimuove un db  da i dbs a sua disposizione
		@param int: utente_id
		@param int:funzione_id
		@attention: rimuovere una funzione non ha effetto se l'utente e' amministratore
		"""
		for f in self.session.query(rel_utente_dbmmas).filter_by(utente_id=user_id).filter_by(db_id=db_Id):
			self.session.delete(f)
			
	def removeArea(self,user_id,area_id):
		"""rimuove un'area dalle zone utente
		@param int: utente_id
		@param string:UTB_signature
		@attention: rimuovere una funzione non ha effetto se l'utente e' amministratore
		"""
		for f in self.session.query(aree).filter_by(utente_id=user_id).filter_by(UTB_id=area_id):
			self.session.delete(f)
			
	def deleteElement(self,row):
		"""
		invoca il delete di un oggetto nella sessione
		@param sqlalchemy.entity: oggetto da rimuovere
		"""
		self.session.delete(row)
	
	def commitOperations(self):
		"""
		esegue il commit della sessione
		"""
		self.session.commit()
		
	def flushOperations(self):
		"""
		esegue il flush della sessione
		"""
		self.session.commit()
		
	def isRegistered(self, uname,pwd):
		""" verifica che le credenziali siano corrette
		@param string: nome utente
		@param string:password
		@return: bool: True se le credenziali coincidono con quelle di un utente registrato
		"""
		u=self.session.query(utente).filter_by(nome_utente=uname).filter_by(password=pwd).count()
		if u!=0:
			return True
		else:
			return False
		
		
	def parser(self,txt,pattern):
		""" ritorna la lista di tutte le occorrenze del pattern nella stringa passata
		@param string:  stringa da esaminare
		@param string:  pattern da applicare
		@return: [string]
		"""
		match=re.compile(pattern)
		return match.findall(txt)	
	
	def getObject(self,uname):	
		"""ritorna l'oggetto registrato con uname
		@param string: username come appare nella lista  di QSettings
		@return User
		"""
		return self.ds.value(uname).toPyObject()
		
	def getUserList(self):
		""" ritorna la lista degli utenti registrati
		@return  [User]
		"""
		self.chiavi=self.ds.allKeys()	
		userNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "\user\d+")]
		users=[]
		for i in userNames:
			users.append(self.getObject(i))
		return users
	
	def removeDBs(self):
		"""rimuove i db registrati nel sistema
		"""
		self.chiavi=self.ds.allKeys()	
		dbNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "db\d+")]
		for db in dbNames:
			self.ds.remove(db)	
			

	def getDbList(self):
		""" ritorna la lista degli utenti registrati
		@return  [extendedDb]
		"""
		self.chiavi=self.ds.allKeys()	
		dbNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "db\d+")]
		dbs=[]
		for i in dbNames:
			dbs.append(self.getObject(i))
		return dbs	
	
	def registerDb(self,db):
		"""registra un db nel sistema
			e incrementa dbCounter
		@param extendedDb:
		"""
		self.chiavi=self.ds.allKeys()
		Id=self.ds.value("dbCounter", 0).toInt()[0]
		#registro il db
		#db.setSettingsName("db{0}".format(Id))
		print "registro il db:db{0}".format(Id)
		self.ds.setValue("db{0}".format(Id),db)
		# incremento il contatore
		Id+=1
		self.ds.setValue("dbCounter",Id)
		print "dbCounter",Id
	
			
