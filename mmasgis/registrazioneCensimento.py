from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_registrazioneCensimento import *
#import sys
#sys.path.append("c:/Users/giuseppe/AppData/Local/Aptana Studio 3/plugins/org.python.pydev_2.7.0.2012080220/pysrc/")
#from pydevd import *


class MainWindowRegistrazioneCensimento(QMainWindow, Ui_RegistrazioneCensimento):
    def __init__(self,ds,user,parent=None):
            self.ds=ds
            self.user=user
            QMainWindow.__init__(self,parent)
            self.w=Ui_RegistrazioneCensimento()
            self.setupUi(self)
            #self.AnnullaButton
            
    def on_lineEdit_textEdited(self):
        if len(str(self.lineEdit.text()))>20:
                infoString="il nome del database non puo' eccedere i 20 caratteri"
                print infoString
                d=QtGui.QMainWindow()
                QtGui.QMessageBox.warning(d,"attenzione!!", infoString) 
                
    def is_number(self,s):
        try:
            float(s)
            return True
        except ValueError:
            return False
        
    def on_lineEdit_2_textEdited(self):
        if not self.is_number(str(self.lineEdit_2.text())):
            infoString="nel campo censimento non e' stato inserito un numero"
            d=QtGui.QMainWindow()
            QtGui.QMessageBox.warning(d,"attenzione!!", infoString)    
            
    def on_lineEdit_3_textEdited(self):
        if not self.is_number(str(self.lineEdit_3.text())):
            infoString="nel campo versione non e' stato inserito un numero"
            d=QtGui.QMainWindow()
            QtGui.QMessageBox.warning(d,"attenzione!!", infoString)          
     
    def on_OKButton_released(self):
        if str(self.lineEdit.text())=="":
            infoString="devi inserire un nome database"
            print infoString
            d=QtGui.QMainWindow()
            QtGui.QMessageBox.warning(d,"attenzione!!", infoString)  
        else:

                infoString="il database e' presente sul server, sara'  registrato nel sistema MMASGIS premendo iltasto OK sulla finestra Settings"
                print infoString
                d=QtGui.QMainWindow()
                #creo una lambda che adatta i valori di versione e censimento, qualora questi fossero nulli passerebbe 1  a registraCensimento
                l=lambda x:1 if x=="" else x
                self.ds.registraCensimento(str(self.lineEdit.text()),self.user,l(str(self.lineEdit_3.text())),l(str(self.lineEdit_2.text())))
                self.emit(QtCore.SIGNAL("insertedDb"))
                QtGui.QMessageBox.information(d,"OK", infoString)  
                self.close()
                      
            
    def on_AnnullaButton_released(self):
        self.close()
