#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_login import *
from commands import *
from sessionClasses import *
from logCensimento import *
from functools import partial
from DataSource import *
import re 
import threading
import datetime
import time


class MainWindowLogin(QMainWindow, Ui_Login):
	
		def __init__(self,parent=None):
			QMainWindow.__init__(self,parent)
			self.w=Ui_Login()
			self.db_list=[]
			self.logCensimento=None
			self.setupUi(self)	
			self.ds= DataSource("Metmi","MMASGIS")
			self.user=None	
			self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent )
			
		def closeEvent(self,event):
			print "chiuso log in "
			if self.user is not None:
				print "utente loggato",self.user 
				self.emit(QtCore.SIGNAL("loggedUser"), self.user)
			#print "uesr",self.user
			
		def parser(self,txt,pattern):
			match=re.compile(pattern)
			return match.findall(txt)
		
		def fetchDb(self,Id):
			""" interroga il dataSource per recuperare la descrizione del db data il suo Id
			@param <int>,<string>: Id del db su session.db
			@return: DB
			"""		
			text= getstatusoutput("python dataSource.py getDb {0}".format(Id))
			print "fetchDb text",text
			db=Db(text[1])
			return db
		
		def slotSelectedCensimento(self):
			infoString="benvenuto {0}".format(self.user.getName())
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"Welcome", infoString)
			self.user.setLogged(True)	
			#self.emit(QtCore.SIGNAL("loggedUser"), self.user)			
			self.close()
			
		def logIn(self,uname,pwd):
			"""verifica le credenziali dell'utente
			@param string:user name
			@param string: password
			@return (User,bool)::(logged_user,logged)
			""" 
			uname="morwen"
			pwd="ringil-87"
			#settrace()
			#text = getstatusoutput('python dataSource.py log {0} {1}'.format(uname,pwd))
			#print "login text", text
			# recupero la lista di utenti registrati
			users= self.ds.getUserList()
			#print "utenti registrati",users
			logged=False
			#cerco la parola True o False nel testo di risposta dal datasource
			user=None
			for i in users:
				if (i.getPassword()==pwd) and(i.getName()==uname):
					logged=True
					user=i
					user.setLogged(True)
					Id=i.getId()
				#instanzio l'oggetto User				
				else:
					logged=False
					Id=-1
			#text=getstatusoutput('python dataSource.py dbs {0}'.format(Id))
			#print "user loggato ",user.isLogged()
			return (user,logged)		
		
		def getAvailableDbs(self,user_Id):
			""" ritorna la li sta degli Id dei db registrati per l'utente di cui e' passato lo id
			@param int: user_Id
			@return: [string]::[db_Id]
			"""
			text = getstatusoutput('python dataSource.py dbs {0} '.format(user_Id))
			return self.parser(text[1],"\d")
		
		def logTrue(self,user):
			"""esegue le operazioni di log in per l'utente accreditato"
			@param user
			""" 
			
			#recupero la lista dei db registrati dall'utente
			#dbs= user.getRegisteredDb()
			# creo la lista dei db
			self.db_list= user.getRegisteredDb()
			print "db registrati",self.db_list
			self.user=user
			# la gui censimento provvederà a settare attivo quello scelto dall'utente
			#apro la gui per la selezione del db
			self.logCensimento=MainWindowLogCensimento(self.db_list)
			screen = QtGui.QDesktopWidget().screenGeometry()
			size =  self.logCensimento.geometry()
			self.logCensimento.move((screen.width()/2)-(size.width()/2),(screen.height()/2)-(size.width()/2))
			self.logCensimento.show()	
			QtCore.QObject.connect(self.logCensimento,QtCore.SIGNAL("logCensimento"),self.slotSelectedCensimento)
			
		def resetForm(self):
			self.text_user.setText("")
			self.text_pass.setText("")
		
				
		def on_LoginButton_released(self):
			uname=self.text_user.text()
			pwd=self.text_pass.text()
			user=self.logIn(uname,pwd)
			if user[1]:
				self.logTrue(user[0])
				self.user=user[0]
				
			else:
				infoString="le credenziali inserite non coincidono con quelle di nessun utente registrato,riprova!"
				d=QtGui.QMainWindow()
				QtGui.QMessageBox.information(d,"Warning",infoString)
				# resetto la form
				self.resetForm()
			#print "available db",text[1]
			#dbs=self.parser(text[1],"\d")
			#print "dbs",dbs,len(dbs)
			# recupero ladefinizione del db da sqlite
			#text= getstatusoutput("python dataSource.py getDb {0}".format(dbs[0]))

			#self.message="selected censimento"
			#wrapped_slot = partial(self.slotSelectedCensimento, self.message)
			
			#print db
			#print dbs