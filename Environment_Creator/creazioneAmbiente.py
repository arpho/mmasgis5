from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_creazioneAmbientePort import *

class MainWindowcreazioneAmbiente(QMainWindow, Ui_CreazioneAmbiente):
	def __init__(self,parent=None):
			QMainWindow.__init__(self,parent)
			self.setupUi(self)
			self.porta={}
			self.porta['mysql']='3306'
			self.porta['mssql']='1433'
			self.text_pass_DB.setText('vilu7240')#("labcad")
			self.text_utente.setText('root')#("sa")
			self.porta['postgresql']='5432'
			self.box_DB.addItem("mysql", userData=QtCore.QVariant("mysql"))
			self.box_DB.addItem("mssql", userData=QtCore.QVariant("mssql"))
			self.box_DB.addItem("postgresql", userData=QtCore.QVariant("postgresql"))
			self.text_utente_gis.setText("admin")
			self.text_pass_utente.setText("metmi")
			self.text_host.setText("localhost")
			self.box_DB.activated[str].connect(self.onActivated)
			self.text_porta.setText(self.porta[str(self.box_DB.currentText())])
			self.data={}
			
	def onActivated(self,t):
		print "activated "+t
		self.text_porta.setText(self.porta[str(self.box_DB.currentText())])
	def on_AnnullaButton_released(self):
		self.close()

	def on_OK_Button_released(self):
		self.data['host']=str(self.text_host.text())
		self.data['passDB']=str(self.text_pass_DB.text())
		self.data['adminPass']=str(self.text_pass_utente.text())
		self.data['admin']=str(self.text_utente_gis.text())
		self.data['dbUser']=str(self.text_utente.text())
		self.data['familyDb']=str(self.box_DB.currentText())
		self.data['port']=str(self.text_porta.text())
		self.emit(QtCore.SIGNAL("start"), self.data)
		self.close
		
	def on_box_DB_changeEvent (self, e):
		print "change"
