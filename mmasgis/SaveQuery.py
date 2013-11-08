from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_SaveQuery import *

class SaveQueryWindow(QMainWindow, Ui_SaveQueryWindow):
    """
    wrapper di Ui_SaveQueryWindow
    """
    def __init__(self,lista,db,censimento,parent=None):
        """
        @param lista:  [Filter]: lista dei filtri definiti dalla query
        @param db: queriesDb
        @note: l'istanza di queriesDb deve essere la stessa usata dalle istanze di Filter
        """
        self.lista=lista
        QMainWindow.__init__(self,parent)
        mainWindow=QtGui.QMainWindow(self)
        self.setupUi(self)
        self.db=db
        self.censimento=censimento
        
    def checkInput(self):
        """
        verifica che sia stato editato qualcosa nelle due caselle di testo  effettuando un AND 
        su  self.NomeQuery.isModified() e self.DescrizioneQuery.document().isModified()
        @return boolean
        """
        return self.NomeQuery.isModified() and self.DescrizioneQuery.document().isModified()
        
    def on_Salva_released(self):
        d=QtGui.QMainWindow()
        #print "query_id",query_id
        if not self.checkInput():
            infoString="nome e descrizione sono campi obbligatori"
            QtGui.QMessageBox.information(d,    "Warning", infoString)
        else:
			query_id=self.db.insertQuery( self.NomeQuery.text(), self.DescrizioneQuery.toPlainText(),self.censimento)
			for i in self.lista:
				i.save(query_id)
			# eseguo il commit
			self.db.commitQuery()
			#self.db.insertQuery(self.lista,str(self.NomeQuery.text()),str(self.DescrizioneQuery.text()))
			infoString="Query salvata sul disco"
			QtGui.QMessageBox.information(d,    "esito salvataggio", infoString)
			self.close()
        
    