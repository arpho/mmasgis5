#!/usr/bin/python
# -*- coding: latin-1 -
from sqlalchemy import Column, Integer, Unicode,Unicode, ForeignKey, DateTime,Float,Boolean,String
from sqlalchemy import create_engine
from sqlalchemy import  Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import *
from sqlalchemy.schema import UniqueConstraint

echo=False
#engine = create_engine('mysql://'+'root:vilu7240@localhost',echo=True)

#metadata = #metadata(bind=engine)

#def __init__(self):

Base = declarative_base()
class Istat(Base):
	__tablename__="tc_istat"
	id=Column(Integer,primary_key=True,autoincrement=True)
	tc_comune_id=Column(Integer)
	tc_provincia_id=Column(Integer)
	tc_regione_id=Column(Integer)
	tc_istat_id=Column(Integer)
	#comuni = relationship("comuniIstat", backref="Istat")
	def __init__(self,istat,regione,provincia,comune):
		self.tc_istat_id=istat
		self.tc_comune_id=comune
		self.tc_provincia_id=provincia
		self.tc_regione_id=regione
		
class comuniIstat(Base):
	__tablename__="comuni"
	id=Column(Integer,primary_key=True,autoincrement=True)
	codice_provincia=Column(Integer)
	codice=Column(Integer)
	nome=Column(Unicode(70))
	tc_comune_id=Column(Integer)
	#tc_comune_id=Column(Integer,ForeignKey('Istat.tc_comune_id'))
	def __init__(self,provincia,codice,nome,comune):
		self.codice=codice
		self.nome=nome.decode('latin-1').encode("utf-8")
		self.tc_comune_id=comune
		self.codice_provincia=provincia

class provinciaIstat(Base):
	__tablename__="province"
	id=Column(Integer,primary_key=True,autoincrement=True)
	codice_regione=Column(Integer)
	codice=Column(Integer)
	tc_provincia_id=Column(Integer)
	nome=Column(Unicode(30))
	sigla= Column(String(2))
	
	"""
		@param codice_regione:integer
		@param codice_shapefile:Integer
		@param nome:Unicode
		@param sigla:String 
	"""
	def __init__(self,regione,codice,nome,sigla,tc_provincia):
		self.codice_regione=regione
		self.codice=codice
		self.sigla=sigla
		self.nome=nome.decode('latin-1').encode("utf-8")
		self.tc_provincia_id=tc_provincia

class regioniIstat(Base):
	__tablename__="regioni"
	id=Column(Integer,primary_key=True,autoincrement=True)
	codice=Column(Integer)
	nome=Column(String(30))
	tc_regione_id=Column(Integer)
	def __init__(self,codice,nome,istat):
		self.codice=codice
		self.nome=nome
		self.tc_regione_id=istat

		
class company(Base):
	__tablename__="azienda"
	azienda_id=Column(Integer,primary_key=True,autoincrement=True)
	nome_azienda=Column(Unicode(20))
	

class ruolo(Base):
	__tablename__="tc_clruolo"
	clruolo_id=Column(Integer,primary_key=True,autoincrement=True)
	nome=Column(String(20))
	#metadata.create_all()

class utente(Base):
	__tablename__="utente"
	utente_id=Column(Integer,primary_key=True,autoincrement=True)
	azienda_id=Column(Integer)
	nome_utente=Column(Unicode(20))
	password=Column(Unicode(10))
	clruolo_id=Column(Integer)
	amministratore=Column(Integer)
	amministratoreFunzioni=Column(Integer)
	amministratoreCensimenti=Column(Integer)
	amministratoreAree=Column(Integer)
	#metadata.create_all()

	def __repr(self):
		return "utente: {0}, {1}, id: {2}".format(self.ruolo,self.nome_utente,self.utente_id)
	
	
class dbmmas(Base):
	
	__tablename__="dbmmas"
	db_id=Column(Integer,primary_key=True,autoincrement=True)
	nome_db=Column(String(20))
	censimento=Column(Integer)
	versione=Column(Integer)
	ins_data=Column(DateTime)
	mod_data=Column(DateTime)
	ins_utente=Column(Integer)
	mod_utente=Column(Integer)
	azienda_id=Column(Integer)
	#metadata.create_all()

	def __repr(self):
		return "dbmmas: {0}, censimento {1}, versione {2}".format(self.nome_db,self.censimento,self.versione)	
	
class funzione(Base):
	__tablename__="funzione"
	funzione_id=Column(Integer,primary_key=True,autoincrement=True)
	categoria=Column(String(10))
	nome=Column(String(20))
	
	def __repr__(self):
		return "funzione:{0},categoria:{1},id:{2} ".format(self.nome,self.categoria,self.funzione_id)
	
class profilo_std(Base):
	__tablename__="profilo_std"
	Id=Column(Integer,primary_key=True,autoincrement=True) 
	nome_profilo=Column(String(20))
	amministratore=Column(Boolean)
	profilo_id=Column(Integer)
	azienda_id=Column(Integer)
	
class rel_profilo_funzioni(Base):
	__tablename__="rel_profilo_funzioni"
	Id=Column(Integer,primary_key=True,autoincrement=True)
	profilo_id=Column(Integer)
	funzione_id=Column(Integer)
	
class profilo(Base):
	__tablename__="rel_utente_funzione" 
	id=Column(Integer,primary_key=True,autoincrement=True)
	utente_id=Column(Integer,autoincrement=False)
	funzione_id=Column(Integer,autoincrement=False)
	#metadata.create_all()
	
	def __repr(self):
		l=lambda x: "amministratore" if x==1 else "generico"
		return "profilo per utente_id:{0}, tipo: {1}, funzione_id: {2}".format(self.utente_id,l(self.amministratore),self.funzione_id)
	
class provincia(Base):
	
	def __init__(self,pr,nome):
		self.sigla=pr 
		self.provincia=nome
		
	__tablename__="provincia"  
	id=Column(Integer,primary_key=True)
	sigla= Column(String(2))
	provincia=Column(Unicode(25))
		
		
class aree(Base):
	__tablename__="rel_utente_zona"
	id=Column(Integer,primary_key=True,autoincrement=True)
	UTB_id=Column(String(10),autoincrement=False)#in realta' si tratta della featureSignature della feature sullo shapefile
	utente_id=Column(Integer,autoincrement=False)
	#metadata.create_all()
	def __repr(self):
		l=lambda x: "amministratore" if x==1 else "generico"
		return "zona: {0}, pe utente_id:{1}, {2}".format(self.UTB_id,self.utente_id,l(self.amministratore))
	
class rel_utente_dbmmas(Base):
	__tablename__="rel_utente_dbmmas"
	id=Column(Integer,primary_key=True,autoincrement=True)
	utente_id=Column(Integer,autoincrement=False)
	db_id=Column(Integer,autoincrement=False)
	#metadata.create_all()
	def __repr(self):
		l=lambda x: "amministratore" if x==1 else "generico"
		return "dbregistrato: {0} per l'utente{1} {2}".format(self.db_id,self.utente_id,l(self.amministratore))
	
class Query(Base):
	""""""
	__tablename__ = "queries"
 
	id = Column(Integer, primary_key=True)
	nome = Column(String(50))
	descrizione = Column(String(50))
 
	#----------------------------------------------------------------------
	def __init__(self, nome, descrizione):
		"""Constructor"""
		self.nome = nome
		self.descrizione = descrizione
 
	def __repr__(self):
		return "Query('%s','%s', '%s')" % (self.nome, self.descrizione,self.id)
 
class Parametro(Base):
	"""
	Address Class
 
	Create some class properties before initilization
	"""
	__tablename__ = "parametri_mmas"
	id = Column(Integer, primary_key=True)
	parametro_id=Column(Integer)
	category = Column(Integer)
	query_id = Column(Integer, ForeignKey('queries.id'))
 
	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	user = relation(Query, backref=backref('parametri_mmas', order_by=id))
 
	#----------------------------------------------------------------------
	def __init__(self,query, category,parametro_id):
		"""Constructor"""
		self.category=category
		self.parametro_id=parametro_id
		self.query_id=query
 
	def __repr__(self):
		return "<parametro({0}-{1})>".format(self.category,self.parametro_id)
	

	

	
class Marchi(Base):
	"""
	Address Class
 
	Create some class properties before initilization
	"""
	__tablename__ = "marchi" 

	id = Column(Integer, primary_key=True,autoincrement=True)
	marchio_id=Column(Integer, nullable=False)
	category = Column(Integer, nullable=False)
	query_id = Column(Integer, ForeignKey('queries.id'))
 
	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	user = relation(Query, backref=backref('marchi', order_by=id))
 
	#----------------------------------------------------------------------
	def __init__(self,query, category,marchio_id):
		"""Constructor"""
		self.category=category
		self.query_id=query
		self.marchio_id=marchio_id
 
	def __repr__(self):
		return "<marchio(%d-%d)>" % (self.category,self.marchio_id)
 
 
class Potenziale(Base):
	"""
	Address Class
 
	Create some class properties before initilization
	"""
	__tablename__ = "potenziali"
	id = Column(Integer, primary_key=True,autoincrement=True)
	potenziale_id=Column(Integer, nullable=False)
	category = Column(Integer, nullable=False)
	query_id = Column(Integer, ForeignKey('queries.id'))
 
	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	user = relation(Query, backref=backref('potenziali', order_by=id))
 
	#----------------------------------------------------------------------
	def __init__(self,query, category,potenziale_id):
		"""Constructor"""
		self.category=category
		self.potenziale_id=potenziale_id
		self.query_id=query
 
	def __repr__(self):
		return "<potenziale({0}-{1})>".format(self.category,self.potenziale_id)

	

	
	
