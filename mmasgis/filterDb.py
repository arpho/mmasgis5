#!/usr/bin/env python
# -*- coding: latin-1 -*-
from mysql_sqlalchemy_class import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from collections import OrderedDict
#from mysqlEntities import *
from elixir import *
from sqlalchemy import *

class filterDb():
	
	def checkParameter(self,Id,(class_id,parameter_id)):
		"""
		verifica che il parametro (class_id,parameter_id) sia presente per il pv Id
		@param Id::int pv_id
		@param (class_id,parameter_id)::(int,int) rispettivamente  id della claasse e del parametro
		@return: boolean  
		"""
		for p in self.session.query(rel_pv_par).filter_by(pv_id=Id).filter_by(tc_clpar_id=class_id).filter_by(tc_par_id=parameter_id):
			#se entro il parametro esiste
			return True
		return False
	
	def checkPotential(self,Id,(class_id,potential_id)):
		"""
		verifica che il potenziale (class_id,potential_id) sia presente per il pv Id
		@param Id::int pv_id
		@param (class_id,parameter_id)::(int,int) rispettivamente  id della claasse e del parametro
		@return: boolean  
		"""
		for p in self.session.query(rel_pv_pot).filter_by(pv_id=Id).filter_by(tc_clpot_id=class_id).filter_by(tc_pot_id=potential_id):
			#se entro il potenziale esiste
			return True
		return False

	def checkBrand(self,Id,(class_id,brand_id)):
		"""
		verifica che il potenziale (class_id,potential_id) sia presente per il pv Id
		@param Id::int pv_id
		@param (class_id,parameter_id)::(int,int) rispettivamente  id della claasse e del parametro
		@return: boolean  
		"""
		b=False
		for p in self.session.query(rel_pv_mar).filter_by(pv_id=Id).filter_by(tc_clmar_id=class_id).filter_by(tc_mar_id=brand_id):
			#se entro il potenziale esiste
			return True
		return False
	
	def checkClassParameter(self,Id,class_id,l):
		"""
		verifica che se almeno uno dei parametri della classe class_id contenuti nella lista l appartenga al pv
		facendo uso di checkParameter
		@param Id::int pv_id
		@param class_id::int id della classe parametro
		@param [int]:: [parameter_id] lista di parametri da analizzare
		@return: boolean 
		""" 
		b=False
		for i in l:
			c=self.checkParameter(Id, (class_id, i)) 
			if c:
				"""
				questo metodo ritorna la somma logica  di tutte le operazioni che esegue
				quindi se solo uno e' True il risultato sara' True
				"""
				return True
			else:
				b=b or c 
		return b

	def checkClassPotential(self,Id,class_id,l):
		"""
		verifica che se almeno uno dei potenziali della classe class_id contenuti nella lista l appartenga al pv
		facendo uso di checkPotential
		@param Id::int pv_id
		@param class_id::int id della classe potenziale
		@param [int]:: [parameter_id] lista di potenziali da analizzare
		@return: boolean 
		""" 
		b=False
		for i in l:
			c= self.checkPotential(Id, (class_id, i))
			if c:
				"""
				questo metodo ritorna la somma logica  di tutte le operazioni che esegue
				quindi se solo uno e' True il risultato sara' True
				"""
				return True
			else:
				b=b or c  
		return b
	
	def checkClassBrand(self,Id,class_id,l):
		"""
		verifica che se almeno uno dei brands della classe class_id contenuti nella lista l appartenga al pv
		facendo uso di checkBrand
		@param Id::int pv_id
		@param class_id::int id della classe potenziale
		@param [int]:: [brand_id] lista di potenziali da analizzare
		@return: boolean 
		""" 
		b=False
		for i in l:
			c= self.checkBrand(Id, (class_id, i))
			if c:
				"""
				questo metodo ritorna la somma logica  di tutte le operazioni che esegue
				quindi se solo uno e' True il risultato sara' True
				"""
				return True
			else:
				b=b or c 
		return b
	

	def initDB(self,dbfile):
		"""
		@param string:stringa di connessione al db, con il seguente formato di stringa "user:pwd@host/nomedb" esempio root:xxxxx@localhost/parafarmacie
		inizializza il db
		"""
		metadata.bind = "mysql://%s"%dbfile
		metadata.bind.echo = False
		setup_all()   

	def __init__(self,user,db):
		#mysql://username:password@localhost/mydb
		self.user=user
		self.activeDb=db
		dbfile=db.getConnectionString()
		
		engine = create_engine("mysql+mysqldb://"+dbfile+"?charset=utf8&use_unicode=1",convert_unicode=True)
		Session = sessionmaker(bind=engine)
		self.session=Session()
		self.initDB(dbfile)
