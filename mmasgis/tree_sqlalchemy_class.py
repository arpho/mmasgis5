#!/usr/bin/python
# -*- coding: latin-1 -
from sqlalchemy import Column, Integer, Unicode,String, ForeignKey, DateTime,Float,Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker

echo=False

#def __init__(self):
Base = declarative_base()

class treeNode(Base):
	def __init__(self,text,sigla,codice,layer,parent_id):
		self.text=text
		self.sigla=sigla
		self.codice=codice
		self.layer=layer
		self.parent_id=parent_id
	__tablename__='tree'
	id=Column('id',Integer,  primary_key=True,autoincrement=True)
	parent_id=Column(Integer)
	text=Column(Unicode(50))
	sigla=Column(String(20))
	codice=Column(String(45))
	layer=Column(String(20))