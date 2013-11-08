from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_gestioneutenti import *

class MainWindowDbSwitcher(QMainWindow, Ui_GestioneUtenti):
    def __init__(self,user,ds,parent=None):
            self.ds=ds
            QMainWindow.__init__(self,parent)
            self.w=Ui_GestioneUtenti()
            self.setupUi(self)
            self.label.setText("censimenti")
            #nascondo i tasti della gui gestioneutenti
            self.CreaUtente.hide()
            self.ModificaUtente.hide()
            self.EliminaUtente.hide()            
            self.admin=user
            self.user=user
            self.company_id=user.getCompany()
            company_id=self.company_id
            self.populate_list(user.getCompany())
            
    def on_list_utenti_itemClicked(self,item):
        db=self.ds.getDbById(item.data(5).toInt()[0])
        self.emit(QtCore.SIGNAL("dbSelected"), db)
            
    def itemFactory(self,user):
            item= QtGui.QListWidgetItem(user.getNameDb())
            item.setData(5,user.getId())
            return item
    
    def populate_list(self,company_id):
        usersList=self.ds.getCensusList(company_id)
        for n,u in enumerate(usersList):
            item=self.itemFactory(u)
            #self.list_utenti.insertRow(n)
            self.list_utenti.addItem(item)