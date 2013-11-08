from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from settings import *
#from dbDict import *
from Ui_gestioneutenti import *
from DataSourceUser import *

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
        self.settingsGui=MainWindowSettings(user_id,ds=self.ds,company_id=self.company_id)
        self.settingsGui.show()
        
    def on_CreaUtente_released(self):
        print "ok"
        self.settingsGui=MainWindowSettings(-1,ds=self.ds,company_id=self.company_id)
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
        
        
    def __init__(self,company_id,parent=None):
            QMainWindow.__init__(self,parent)
            self.company_id=company_id
            self.w=Ui_GestioneUtenti()
            self.setupUi(self)
            self.settingsGui=None
            self.ModificaUtente.setEnabled(False)
            self.EliminaUtente.setEnabled(False)
            db1=Db('mmasgisDB',-1)
            db1.setUserName("metmi")
            db1.setPassword("metmi")
            db1.setHost('localhost')
            db1.setPort('3306')
            db1.setRDBMS('mysql')  
            user=User('amministratore',-1)      
            print "porta",db1.getPort()
            user.setActiveDb(db1)
            print "db",db1
            self.ds=DataSource(user)
            self.populate_list(company_id)