#!/usr/bin/python
# -*- coding: latin-1 -
from sqlalchemy import Column, Integer, Unicode,Unicode, ForeignKey, DateTime,Float,Boolean,String
from sqlalchemy import create_engine
from sqlalchemy import  Column, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from sqlalchemy import *

echo=False
#engine = create_engine('mysql://'+'root:vilu7240@localhost',echo=True)
 
#metadata = #metadata(bind=engine)

#def __init__(self):
Base = declarative_base()
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
    amministratore=Column(Integer)
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
    

    
    
