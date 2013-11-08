from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from settings import *
#from dbDict import *
from Ui_gestioneutenti import *
from DataSourceUser import *
from sessionClasses import *


class MainWindowUserManager(QMainWindow, Ui_GestioneUtenti):
	def itemFactory(self,user):
		item= QtGui.QListWidgetItem(user.getName())
		item.setData(5,user.getId())
		return item
	
	def populate_list(self,company_id):
		usersList=self.ds.getUsersList(company_id)
		for n,u in enumerate(usersList):
			item=self.itemFactory(u)
			#self.list_utenti.insertRow(n)
			self.list_utenti.addItem(item)
			
	def on_ModificaUtente_released(self):
		user_id=self.list_utenti.currentItem().data(5).toInt()[0]
		self.settingsGui=MainWindowSettings(self.admin,user_id,ds=self.ds,company_id=self.user.getCompany())
		size =  self.settingsGui.geometry()
		screen = QtGui.QDesktopWidget().screenGeometry()
		self.settingsGui.move((screen.width()/2)-(size.width()/2),(screen.height()/2)-(size.width()/3))
		self.settingsGui.show()
		
	def on_CreaUtente_released(self):
		copy=User('',-1)
		self.settingsGui=MainWindowSettings(self.admin,-1,ds=self.ds,company_id=self.company_id)
		size =  self.settingsGui.geometry()
		screen = QtGui.QDesktopWidget().screenGeometry()
		self.settingsGui.move((screen.width()/2)-(size.width()/2),(screen.height()/2)-(size.width()/3))
		self.settingsGui.show()

		
	def on_EliminaUtente_released(self):
		infoString=QtCore.QString("elininazione utente")
		user_id=self.list_utenti.currentItem().data(5).toInt()[0]
		reply=QtGui.QMessageBox.question(self,infoString,"sei sicuro di volere eliminare l'utente e tutte le sue relazioni?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.No)
		self.ds.deleteUser(user_id)
		if reply==QtGui.QMessageBox.Yes:
			self.ds.commitOperations()
			
	def on_list_utenti_itemClicked(self,item):
		
		self.ModificaUtente.setEnabled(True)
		self.EliminaUtente.setEnabled(True)
		
		
	def __init__(self,user,parent=None):
			QMainWindow.__init__(self,parent)
			
			self.admin=user
			self.user=user
			self.company_id=user.getCompany()
			company_id=self.company_id
			self.w=Ui_GestioneUtenti()
			self.setupUi(self)
			self.settingsGui=None
			self.ModificaUtente.setEnabled(False)
			self.EliminaUtente.setEnabled(False)
			db=user.getActiveDb()
			db1=Db('mmasgisDB',-1)
			db1.setHost(db.getHost())
			db1.setPort(db.getPort())
			db1.setRDBMS(db.getRDBMS())
			db1.setUserName("metmi")
			db1.setPassword("metmi")  
			user=User('amministratore',-1)	  
			user.setActiveDb(db1)
			self.ds=DataSource(user)
			self.populate_list(company_id)
