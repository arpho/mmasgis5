from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from DataSourceUser import *
#from dbDict import *
from Ui_settings import *
from registrazioneCensimento import MainWindowRegistrazioneCensimento
import sys

class MainWindowSettings(QMainWindow, Ui_Settings):
    def populateDbs(self,user):
        """popola il tab db
        @param User: utente di cui visualizzare i db registrati
        """
        dbSet=user.getDbset()
        dbList=self.ds.getDbs(user.getCompany())
        for i in dbList:
            c=self.checkFactory(i)
            c.setId(i.getId())
            if dbSet.isPermitted(i.getId()):
                c.setChecked(True)
            QtCore.QObject.connect(c, QtCore.SIGNAL("mySignal"),self.on_DbChecked)
            nodo=QtGui.QTreeWidgetItem("hjfgjkhv")
            self.list_DB.insertTopLevelItem (0, nodo)
            self.list_DB.setItemWidget(  nodo,0,c)
            
    
    def populateFunctions(self,user):
        """popola iltab del profilo
        @param User:  utente visualizzato
        """
        profile=user.getProfile()
        liste={}
        liste['mod/esp']=self.list_esp
        liste['amm']=self.list_amm
        liste['funzioni']=self.list_funzioni
        functionList=self.ds.getFunctions()
        for i in functionList:
            c=self.checkFactory(i)
            self.functionChecks.append(c)
            c.setId(i.getId())
            if profile.isPermitted(i.getId()):
                c.setChecked(True)
            QtCore.QObject.connect(c, QtCore.SIGNAL("mySignal"),self.on_FunctionChecked)
            #dummy= QtGui.QListWidgetItem("dummy")
            nodo=QtGui.QTreeWidgetItem("")
            #self.list_funzioni.insertItem(0,dummy)
            liste[i.getCategory()].insertTopLevelItem (0, nodo)
            #self.list_funzioni.setItemWidget(dummy,c)
            liste[i.getCategory()].setItemWidget(  nodo,0,c)
    
    def on_OKButton_released(self):
        print "commit operations" 
        self.modified=False
        self.ds.commitOperations() 
        mode={}
        mode["creation"]="creato"
        mode["modifying"]="modificato"
        infoString="dati registrati sul database correttamente"
        print infoString
        d=QtGui.QMainWindow()
        QtGui.QMessageBox.information(d,"logged user", infoString) 
        self.close() 
        
    def on_DbChecked(self,msg): 
        self.modified=True
        if msg[3].isChecked():
            dbrelUtente=self.ds.createNewRDU()
            dbrelUtente.utente_id=self.user_Id
            dbrelUtente.db_id=msg[0]
            self.ds.addObject(dbrelUtente)
        else:
            dbrelUtente=self.ds.getRDU(self.user_Id,msg[0])
            self.ds.deleteObject(dbrelUtente)
            
        
    def on_FunctionChecked(self,msg):
        """
        msg[2]=categoria
        msg[1]=nome
        msg[0]=function_id
        """
        self.modified=True
        if msg[3].isChecked():# e' stata aggiunta una funzione al profilo
            profile=self.ds.createNewProfile()
            profile.funzione_id=msg[0]
            profile.utente_id=self.user_Id
            self.ds.addObject(profile)
        else:
            profile=self.ds.getProfile(self.user_Id,msg[0])
            self.ds.deleteObject(profile)
            
    def on_ammFunction(self,msg):
        print "amm{0}".format(msg)
        
    def on_funzFunction(self,msg):
        print "funzioni{0}".format(msg)
        
    def checkFactory(self,f):
        """genera i checkBox da mettere nelle liste
        @param Function: funzione che sara' rappresentata dal checkbox
        @return ceckBox
        """
        
        c=ceckBox(f.getHeader(),f.getId,f.getCategory())
        return c 
    
    def on_text_user_textEdited(self):
        print "nome amministratore changed"
        self.modified=True
        if self.ds.isNametaken(str(self.text_user.text()), self.company_id):
            infoString="il nome digitato e' gia' utilizzato"
            d=QtGui.QMainWindow()
            QtGui.QMessageBox.information(d,"Attenzione", infoString)   
        else:
            self.itemUtente.nome_utente=str(self.text_user.text())      
        
    def on_text_pass_textEdited(self):
        self.itemUtente.password=str(self.text_pass.text())
    def populateTabs(self,user):
        self.populateFunctions(user)
        self.populateDbs(user)
        self.text_user.setText(user.getName())
        l=lambda x:True if x==1 else False 
        self.check_amm_DB.setChecked(l(user.getAmministratore()))
        self.text_pass.setText(user.getPassword())
        
    def amministratore(self,i):
        l=lambda x: 1 if x==2 else 0
        self.modified=True
        self.itemUtente.amministratore=l(i)
        
    def closeEvent(self, event):
        #s=Saver(self.p,"test saver2",'ragione_sociale')
        reply=QtGui.QMessageBox.No
        if self.modified:
            infoString=QtCore.QString("sono state apportate delle modifiche")
            reply=QtGui.QMessageBox.question(self, infoString,    "vuoi salvare ?", QtGui.QMessageBox.Yes |     QtGui.QMessageBox.No, QtGui.QMessageBox.No)
            if reply==QtGui.QMessageBox.Yes:
                self.ds.commitOperations()
    
    def on_Registra_released(self):
        self.uiDb=MainWindowRegistrazioneCensimento(self.ds,self.admin)  
        QtCore.QObject.connect(self.check_amm_DB, QtCore.SIGNAL("insertedDb"), self.modify)  
        self.uiDb.show()   
        
    def modify(self):
        """slot per il segnale insertedDb emesso da registrazioneCensimento
        setta a True self.modified
        """

        self.modified=True
        
    def on_AnnullaButton_released(self):
        #test std_profile
        test_profile= self.ds.getStdProfile(1,1)
        self.applyProfile(test_profile)
            
    def __init__(self,admin,user_id,company_id=1,parent=None,ds=None):
            """
            @param User: utente amministratore che sta effettuando l'operazione
            @param int:id dell'utente su cui si opera
            @param int:id aziendale dell'utente da settare
            @param DataSourceUser: e' l'istanza di DataSource connessa al db se omessa usa la mia per debug
            """
            self.uiDb=None
            self.functionChecks=[]
            QMainWindow.__init__(self,parent)
            self.admin=admin
            self.company_id=company_id
            if user_id==-1:
                self.mode="creation"
            else:
                self.mode="modifying"
            print "aperto settings in {0} per utente {1} company: {2}".format(self.mode,user_id,company_id)
            self.w=Ui_Settings()
            self.setupUi(self)
            self.ModificaButton.hide()
            self.EliminaButton.hide()
            QtCore.QObject.connect(self.check_amm_DB, QtCore.SIGNAL("stateChanged(int)"), self.amministratore)
            self.modified=False
            if ds is None:
                userds={'uname':'root','pwddb':'vilu7240','passAdmin':'metmi'}
                userds['familyDb']='mysql5'
                userds['host']='localhost'
                self.ds=DataSource(userds)
            else:
                self.ds=ds
            if user_id!=-1:
                user=self.ds.getUserById(user_id)
                self.itemUtente=self.ds.getItemUtente(user_id)
                self.user_Id=user_id
                print user
                #qlistItem=QtGui.QListWidgetItem("testoprova")
                self.populateTabs(user)
            else:
                print "creazione nuovo utente"
                self.itemUtente=self.ds.createNewUser()
                self.itemUtente.azienda_id=company_id
                self.itemUtente.password="" #per default la password e' vuota'
                self.ds.addObject(self.itemUtente)
                self.ds.flushOperations()
               
                self.user_Id=self.itemUtente.utente_id
                user=User("",self.user_Id)
                user.setCompany(self.company_id)
                user.setProfile(Profile({}))
                self.populateTabs(user)
                print self.user_Id
            self.modified=False
            self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent )
            
    def applyProfile(self,profilo):
        """applica un profilo standard all'utente  in esame
        @param Profile_standard:profilo da applicare
        @param string:categoria su cui applicare il profilo
        """  
        for i in self.functionChecks:
            print "funzione:{0} permessa {1}".format(i.getId(),profilo.isPermitted(i.getId()))
            b=profilo.isPermitted(i.getId())
            i.setChecked(b)
                

    def on_mySignal(self, *msg):
        print msg
            
            
class ceckBox(QtGui.QCheckBox):
    """
    estende QCheckBox con un segnale (mySignal) per poter interagire con il resto della gui  
    """
    def __init__(self, testo, Id, tab):
        """
        @param testo:    String
        @param Id:    Integer
        @param category:    Integer  
        """
        QtGui.QCheckBox.__init__(self, testo)
        self.text=testo
        self.tab=tab
        self.id=Id
        self.inhibit=False
        QtCore.QObject.connect(self, QtCore.SIGNAL("stateChanged(int)"), self.on_checkChanged)
        #QtCore.QObject.connect(self, QtCore.SIGNAL("reset"), self.reset)
        
    def setId(self,Id):
        self.id=Id
        
    def getId(self):
        """ritorna lo id assegnato al checkBox
        @note: e' lo id dell'oggetto ad esso associato
        @return: int
        """
        return self.id
        
    def on_checkChanged(self):
        """
        @note: formato del messaggio msg=[self.id,self.text,self.tab,self]<[int,string,string,ceckBox>
        @note: self.text e' il testo che accompagna il boxpyqt contextmenu last selection
        emette il segnale mySignal se il checkbox cambia stato
        """
        msg=[self.id,self.text,self.tab,self]
        self.emit(QtCore.SIGNAL("mySignal"), msg)
       # print "checkChanged"
#        if (self.checkState() and (not self.inhibit)):
 #           self.emit(QtCore.SIGNAL("mySignal"), msg)