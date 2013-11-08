#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_creazioneAmbiente import *


class MainWindowGui(QMainWindow, Ui_CreazioneAmbiente):
    
    def __init__(self,parent=None):
            QMainWindow.__init__(self,parent)
            self.w=Ui_CreazioneAmbiente()
            self.setupUi(self)
            self.box_DB.addItem("mysql5","mysql")
            self.box_DB.addItem("mysql4","mysql4")
            self.box_DB.addItem("sqlserver","sqlserver")
    def on_OK_Button_released(self):
        user={'uname':str(self.text_utente.text()),'pwddb':str(self.text_pass_DB.text()),'passAdmin':str(self.text_pass_utente.text())}
        user['familyDb']=str(self.box_DB.itemData(self.box_DB.currentIndex(), 2).toString())
        user['host']=str(self.text_host.text())
        self.emit(QtCore.SIGNAL("data"), user)