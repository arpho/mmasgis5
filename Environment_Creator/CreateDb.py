from PyQt4 import QtCore,QtGui
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
from sqlalchemy.engine.url import URL

class CreateDb():
	def __init__(self,utonto):
		
		self.cons=dbCons
		self.activeDb=utonto.getActiveDb()
		dbfile=self.activeDb.getUserName()+":"+self.activeDb.getPassword()+'@'+self.activeDb.getHost()+":"+str(self.activeDb.getPort())
		family=self.activeDb.getRDBMS()
		self.dbfile=dbfile
		self.family=self.cons.queries[family]
		


		



	
