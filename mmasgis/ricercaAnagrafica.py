from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_ricercaAnagrafica import *

class MainWindowRicercaAnagrafica(QMainWindow, Ui_MainWindowRicercaAnagrafica):
    def __init__(self,parent=None):
            QMainWindow.__init__(self,parent)
            self.w=Ui_MainWindowRicercaAnagrafica()
            self.setupUi(self)
            self.parametriRicerca={}
            
    def on_trovaButton_released(self):
        if str(self.text_codcliente.text())!="":
            self.parametriRicerca["codice_cliente"]=str(self.text_codcliente.text())
        if str(self.text_codiceMMAS.text())!="":
            self.parametriRicerca["codice_mmas"]=str(self.text_codiceMMAS.text())
        if str(self.text_comune.text())!="":
            self.parametriRicerca["comune"]=str(self.text_comune.text())
        if str(self.text_ragionesociale.text())!="":
            self.parametriRicerca["ragione_sociale"]=str(self.text_ragionesociale.text())
        l=lambda x: True if x>0 else False
        self.emit(QtCore.SIGNAL("cerca"), (self.parametriRicerca,l(self.check_int.checkState())))
        self.close()