from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from DataSourceUser import *
from MySQLdb import *
#from dbDict import *
from Ui_login import *
from sessionClasses import *

class preset():
	def __init__(self):
		self.porta=""
		self.user=""
		self.pwd=""
		self.host=""
		self.familyDb=""
		
	def __repr__(self):
		return "presetting per user {0}, host: {1}, porta: {2}, pwd: {3}".format(self.user,self.host,self.porta,self.pwd)
		
	def getPorta(self):
		return self.porta
	
	def getUser(self):
		return self.user
	
	def getPassword(self):
		return self.pwd
	
	def getHost(self):
		return self.host
	
	def getFamilyDb(self):
		return self.familyDb
	
	def setPorta(self,p):
		self.porta=p
	
	def setUser(self,u):
		self.user=u
	
	def setPassword(self,p):
		self.pwd=p
	
	def setHost(self,h):
		self.host=h
	
	def setFamilyDb(self,f):
		self.familyDb=f


class LoginRefactored(QMainWindow, Ui_Login):
	def __init__(self,debug=False,parent=None):
			QMainWindow.__init__(self,parent)
			self.w=Ui_Login()
			self.setupUi(self)
			self.Box_DB.addItem("mysql", userData=QtCore.QVariant("mysql"))
			self.Box_DB.addItem("postgresql", userData=QtCore.QVariant("postgresql"))
			self.Box_DB.activated[str].connect(self.onActivated) 
			self.qs=QtCore.QSettings("metmi", "MMASGIS")   
			loginPreset=self.qs.value("loginPresettings",-1).toPyObject()
			self.check_conn.setCheckState(2)
			if loginPreset!=-1:
				self.text_pass.setText(loginPreset.getPassword())
				self.text_user.setText(loginPreset.getUser())
				self.text_porta.setText(loginPreset.getPorta())
				print "host",loginPreset.getHost()
				self.text_host.setText(loginPreset.getHost())
				print "presetted rdbms",loginPreset.getFamilyDb()
				print " index incombo",self.Box_DB.findText(loginPreset.getFamilyDb())
				self.Box_DB.setCurrentIndex(self.Box_DB.findText(loginPreset.getFamilyDb()))
			else:
				print "no loginPresettings found"   
			
			
			self.porta={}
			self.porta['mysql']=str(3306)
			self.porta["postgresql"]=str(5432)
			self.text_porta.setText(self.porta[str(self.Box_DB.currentText())])
			self.ds=None
			
	def onActivated(self,t):
			self.text_porta.setText(self.porta[str(self.Box_DB.currentText())])
			
	def getDataSource(self):
		return self.ds 
	
	def on_AnnullaButton_released(self):
		self.emit(QtCore.SIGNAL("undo"))
			
	def on_ResetButton_released(self):

		self.text_user.setText("")
		self.check_conn.setCheckState(0)
		self.text_porta.setText("")
		self.text_user.setText("")
		self.text_pass.setText("")
	
	def on_check_conn_stateChanged(self,i):
		print "check",i
		if i==2:
			self.text_host.setText("localhost")
		elif i==0:
			self.text_host.setText("")
			
	def on_LoginButton_released(self):
		#dbfile="metmi:metmi@{0}".format(self.text_host.text())
		nome=str(self.text_user.text())
		passdb=str(self.text_pass.text())
		db=Db('mmasgisDB',-1)
		db.setUserName("metmi")
		db.setPassword("metmi")
		db.setHost(str(self.text_host.text()))
		db.setPort(str(self.text_porta.text()))
		db.setRDBMS(str(self.Box_DB.currentText()))  
		print "logged db",db
		user=User(str(self.text_user.text()),-1)	  
		user.setActiveDb(db)
		loginSet=preset()
		loginSet.setUser(str(self.text_user.text()))
		loginSet.setPorta(str(self.text_porta.text()))
		loginSet.setHost(str(self.text_host.text()))
		loginSet.setFamilyDb(str(self.Box_DB.currentText()))
		loginSet.setPassword(str(self.text_pass.text()))
		self.qs.setValue("loginPresettings",loginSet)
		
	

#		dbName,Id,descrizione="",user_name="",pwd="",host="",rdbms="")
		print "activedb utente loggato", user.getActiveDb()
		self.ds=DataSource(user)
		print "credenziali utente",str(self.text_user.text()),str(self.text_pass.text())
		if self.ds.isRegistered(str(self.text_user.text()),str(self.text_pass.text())):
			print "utente registrato"
			user=self.ds.getUser(str(self.text_user.text()),str(self.text_pass.text()))
			db=Db(str(self.text_user.text()),str(self.text_pass.text()),str(self.text_host.text()),'host')
			db.setPort(str(self.text_porta.text()))
			user.setLogged(True)
		   # user.setProfile(self.ds.getUserProfile(user.getId()))
			print "logged user",user
			familyDb=self.Box_DB.itemData(self.Box_DB.currentIndex(), 2)
			print "db server",familyDb.toString()
			db.setRDBMS(familyDb.toString())
			db.setPort(str(self.text_porta.text()))
			db.setHost(str(self.text_host.text()))
			user.setActiveDb(db)
			self.emit(QtCore.SIGNAL("logged"), user)
			print "emesso segnale per {0}".format(user.getName())
		else:
			print "utente non registrato"
			infoString="le credenziali inserite non corrispondono con quelle di nessun utente registrato"
			print infoString
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"LOG IN", infoString) 
			
