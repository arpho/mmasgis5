from PyQt4 import QtCore,QtGui
import re 
# Initialize Qt resources from file resources.py
from sessionClasses import *
from sqlalchemy import MetaData, Column, Table, ForeignKey
from sqlalchemy import *
from mmasgisDb_sqlalchemy import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from elixir import *
import sqlalchemy
from sqlalchemy.ext import compiler
from sqlalchemy.sql.expression import Executable, ClauseElement
#from provincia import *
from environment_constants import *
from funzioni import *
import datetime
from mmasgisDb_sqlalchemy import *
from sqlalchemy.engine.url import URL
from Odict import *

		

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
		self.user=utonto
		self.activeDb=utonto.getActiveDb()
		dbfile=self.activeDb.getUserName()+":"+self.activeDb.getPassword()+'@'+self.activeDb.getHost()+":"+self.activeDb.getPort()
		self.dbfile=dbfile
		family=str(self.activeDb.getRDBMS())
		self.family=self.cons.queries[family]
		url = URL(drivername=self.family['family'], username=self.activeDb.getUserName(), password=self.activeDb.getPassword(), host=self.activeDb.getHost(),port=str(self.activeDb.getPort()), database='mmasgisDB')
		print "url",url
		self.engine = create_engine(url)
		#"mysql://"+dbfile
		#print "url","{0}://".format(family['family'])+dbfile
		print "dbfile in datasourceUser __init__",dbfile
		#self.engine = create_engine("{0}://".format(self.family['family'])+dbfile)#+"?charset=utf8&use_unicode=1",convert_unicode=True)
		metadata = MetaData(bind=self.engine)
		#self.engine.execute(self.family['use'])
		#print "connection string","{0}://".format(self.family['family'])+dbfile
		Session = sessionmaker(bind=self.engine)
		self.session=Session()
		
	def __repr__(self):
		return self.dbfile

	def createDb(self,passAdmin,create=True):	
		
		print "creo il db mmasgisDB"
		try:
			print " try create db"
			if create:
				print "drop db"
				self.engine.execute(self.family['drop']) #cancello il vecchio db	
				self.engine.execute(self.family['create']) #create db
			print " db creato"
		except sqlalchemy.exc.ProgrammingError:
			print " il db esiste"
		self.engine.execute(self.family['use']) # select new db
		Base.metadata.create_all(self.engine)
		Session = sessionmaker(bind=self.engine)
		settings = QtCore.QSettings("Metmi", "MMASGIS")
		settings.setValue("familyDb",self.activeDb.getRDBMS())
		#settings
		self.session=Session()
		#self.initDB(dbfile)			
		#creo l'utente metmi
		#self.engine.execute("CREATE USER metmi IDENTIFIED BY  'metmi'")
		users=self.engine.execute(self.family['look4metmi']).first()[0]
		print "users ",users
		if users!=0:
				print "l'utente metmi esiste"
				print "associo a metmi i diritti di amministratore"
				self.engine.execute(self.family['grant%'])
				print "fatto!"				
		else:
				print "l'utente metmi non  esiste"
				print "provvedo a crearlo"
				self.engine.execute("CREATE USER 'metmi'@ IDENTIFIED BY  'metmi'")
				#devo creare lo stesso utente pure su localhost
				self.engine.execute("CREATE USER 'metmi'@'localhost' IDENTIFIED BY  'metmi'")
				print "creato!"
				print "associo a metmi i diritti di amministratore"
				self.engine.execute(self.family['grant*'])
				print "fatto!"
				print "creo l'utente amministratore di mmasgis"	
		user=utente()
		user=utente()
		user.nome_utente='amministratore'
		user.azienda_id=1
		user.password=""
		user.amministratoreAree=1
		user.amministratoreCensimenti=1
		user.amministratoreFunzioni=1
		user.amministratore=1
		user.clruolo_id=1
		self.session.add(user)
		print 	"setto la password di amministratore",passAdmin		
		user.password=passAdmin
		self.session.add(user)
		self.session.flush()
		id_amministratore=user.utente_id
		print "id amministratore",id_amministratore
		print "creo il ruolo amministratore"
		r=ruolo()
		r.nome="amministratore"
		r.clruolo_id=1
		self.session.add(r)
		#aggiungo una riga alla tabella azienda
		az=company()
		az.nome_azienda="home"
		self.session.add(az)
		#rendo l'utente super user per le aree
		area=aree()
		area.amministratore=1
		area.utente_id=id_amministratore
		self.session.add(area)
		#rendo l'utente super user per le funzioni 
		profile=profilo()
		profile.utente_id=id_amministratore
		profile.amministratore=1
		self.session.add(profile)
		dbs=rel_utente_dbmmas()
		dbs.amministratore=1
		dbs.utente_id=id_amministratore
		self.session.add(dbs)
		for f in functions:
			F=funzione()
			F.categoria=f['classe']
			F.nome=f['nome']
			self.session.add(F)
		#rendo l'utente super user per i db
		self.session.commit()
		# rendo metmi amministratore su tutti i db e gli consento di accedere da remoto
		#self.engine.execute("GRANT ALL PRIVILEGES ON *.* TO metmi@'%' IDENTIFIED BY 'metmi' WITH GRANT OPTION")
		#g
		#self.session=Session()	
		
		#self.initDB(dbfile)
		# self.session.query(provincia).count()
		#verifico che la tabella provincia si popolata
		c=self.session.query(provincia).count()
		if c==0:
			print "la tabella 'provincia' non e' ancora popolata"
			print "provvedo a popolare la tabella di servizio provincia"
			n=0
			# create a database connection
			#conn = self.engine.connect()
			#ins=provincia.insert()
			#self.engine.execute("use mmasgisDB")
			for p in province:
				n+=1
				pr=provincia(p[1],p[2])
				self.session.add(pr)
				
				#new_pr=ins.values(sigla=p[1],provincia=p[2])
				#conn.execute(new_pr)
				#self.engine.execute("insert into provincia(sigla,provincia)values({0},{1}".format(p[1],p[2]))
			self.session.commit()
			print "ho inserito {0} province ".format(n)		
			
	def getSession(self):
		return self.session
	
	def writeProfile(self,p,profile_id,company_id=1):
		"""
		crea un profilo standard neldb
		@param Profile_standard: 
		@param int: profilo id
		@param int: company id
		@note: non invoca il commit
		""" 
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
		
		u =self.session.query(utente).filter_by(nome_utente=uname).filter_by(password=pwd).first()

		user=User(u.nome_utente,u.utente_id)
		user.setProfile(self.getUserProfile(u.utente_id))
		user.setId(u.utente_id)
		user.setRuolo(u.clruolo_id)
		user.setAmministratore(u.amministratore)
		user.setCompany(u.azienda_id)
		user.setDbset(self.getUserDbs(u.utente_id))
		user.setZone(self.getUserArea(u.utente_id))
		return user
	
	def getCensusList(self,company_id):
		"""ritorna la lista dei censimenti  registrati sul db per company_id
		@param int:company_id
		@return [Db]
		""" 
		census=[]
		for u in  self.session.query(dbmmas).filter_by(azienda_id=company_id):
			user=self.getDbById(u.db_id)
			census.append(user)
		return census
	
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
	
	def getDbById(self,Id):
		d=self.session.query(dbmmas).filter_by(db_id=Id).first()
		db=Db(d.nome_db,d.db_id)
		db.azienda_id=d.azienda_id
		db.censimento=d.nome_db
		db.versione=d.versione
		db.ins_data=d.ins_data
		db.mod_data=d.mod_data
		db.mod_utente=d.mod_utente
		db.ins_utente=d.ins_utente
		db.setHost(self.activeDb.getHost())
		db.setRDBMS(self.activeDb.getRDBMS())
		return db
		
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
			
	def getStdProfileList(self,company_id=1):
		"""ritorna la lista dei profili_standard per l'azienda
		@param int:company id
		@return: [Profile_standard]
		""" 
		l=[]
		for i in self.session.query(profilo_std).filter_by(azienda_id=company_id).all():
			p=self.getStdProfile(i.Id, company_id)
			l.append(p)
		return l
			
	def getStdProfile(self,profile_id,company_id=1):
		"""
		ritorna il profilo_standard relativo allo id
		@param int:profilo_id
		@param int:company_id opzionale, default 1
		@return:   Profile_standard
		"""
		p=self.session.query(profilo_std).filter_by(Id=profile_id).filter_by(azienda_id=company_id).first()
		if p.amministratore==1:
			pr=Profile_standard(1) # profilo amministratore
			
			pr.setId=profile_id
			return pr 
		else:
			pr=Profile_standard()#no admin
			for i in self.session.query(rel_profilo_funzioni).filter_by(profilo_id=profile_id).all():
				f=self.getFunction(i.funzione_id)
				pr.addElement(f.getId(),f)
		pr.setId(profile_id)
		pr.setName(p.nome_profilo)
		return pr
	
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
		
	def purgesDummyUsers(self):
		"""elimina gli utenti il cui nome e' NULL
		@note: viene invocato ognivolta prima del commitOperation
		"""
		for u in self.session.query(utente).filter_by(nome_utente=None).all():
			self.session.delete(u)
		
	def isAdministrator(self,Id):
		a=self.session.query(utente).filter_by(utente_id=Id).first()
		if a.amministratore!=1:
			return False
		else:
			return True		
		
			
	def isDbAdministrator(self,user_id):
		""" verifica chel'utente sia amministratore per i censimenti
		@param int:user_id
		@return: bool
		"""
		a=self.session.query(utente).filter_by(utente_id=user_id).first()
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
		if a.amministratore!=1:
			return False
		else:
			return True
			

	
	def isDb(self,nome):
		"""verifica che il db sia presente nel server
		@param string:nome db
		@return:  bool
		"""
		connection=self.engine.connect()
		b=connection.execute(self.family['existDb'].format( nome)) 
		if b.fetchone() is None:
			return False
		else:
			print b.fetchone()
			return True
		return b
	
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
			
	def registraCensimento(self,nome,user,versione=0,censimento=0):
		"""
		registra un censimento dul db mmasgis
		@param string:nome del censimento/db
		@param User:utente che registra il db
		@param int:versione del censimento opzionale
		@param int: censimento opzionale
		"""  
		db=dbmmas()  
		try:
			censimento =int(censimento)
		except ValueError:
			censimento =0
		
		try:
			versione =int(versione)
		except ValueError:
			versione =0	
		db.nome_db=nome
		db.censimento=censimento
		db.versione=versione
		db.azienda_id=user.getCompany()
		db.ins_data=datetime.date.today()
		db.ins_utente=user.getId()
		self.session.add(db)
		
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
		self.purgesDummyUsers()#faccio pulizia nel db
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
		print "isregistered ",uname,pwd
		u=self.session.query(utente).filter_by(nome_utente=uname).filter_by(password=pwd).count()
		
		if u!=0:
			print "risultato query diverso 0"
			return True
		else:
			print "risultato query =0"
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
	
			
