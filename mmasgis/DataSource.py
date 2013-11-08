from PyQt4 import QtCore,QtGui
import re 
# Initialize Qt resources from file resources.py
from sessionClasses import *

class DataSource():
	"""
	gestisce le operazioni di lettura e scrittura sui settings di Qt per la gestione degli utenti
	"""
	def __init__(self,company,application):
		"""
		@param string: name-space dell'azienda
		@param string:name-space  dell'applicazione
		"""
		self.ds=QtCore.QSettings(company, application)
		
	def getUserCount(self):
		"""ritorna il valore attuale di UserCounter
		@return: int
		"""
		c= self.ds.value("UserCount", 0).toInt()[0]
		return c 
	
	def registerUser(self,user, label):
		"""
		registra un utente  nel file di sistema con l'etichetta passata come parametro
		@param extendedUser:
		@param string: etichetta di identificazione utente
		"""
		self.ds.setValue(label, user)
		
	def setUserCounter(self,c):
		"""setta il valore di UserCount
		@param int: nuovo valore di userCount
		"""
		self.ds.setValue("userCount",c) 
		
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
		
		
	def parser(self,txt,pattern):
		""" ritorna la lista di tutte le occorrenze del pattern nella stringa passata
		@param string:  stringa da esaminare
		@param string:  pattern da applicare
		@return: [string]
		"""
		match=re.compile(pattern)
		return match.findall(txt)	
	
	def getUser(self,uname):	
		"""ritorna lo user registrato con uname
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
			users.append(self.getUser(i))
		return users
	
	def getDbList(self):
		""" ritorna la lista degli utenti registrati
		@return  [extendedDb]
		"""
		self.chiavi=self.ds.allKeys()	
		userNames=[ str(i) for i in self.parser(self.chiavi.join("|"), "db\d+")]
		dbs=[]
		for i in userNames:
			dbs.append(self.getUser(i))
		return dbs	
	
	def registerDb(self,name,db):
		"""registra un db nel sistema
		@param string: nome del db nel sistema
		@param extendedDb:
		"""
		self.chiavi=self.ds.allKeys()
		Id=self.ds.value("QString", 0).toInt()[0]
		#registro il db
		self.ds.setValue(name,db)
		# incremento il contatore
		self.ds.setValue("dbCounter",Id+1)
		print "dbCounter",Id
	
			