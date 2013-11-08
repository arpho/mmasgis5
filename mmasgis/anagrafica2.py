from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from dbDict import *
from Ui_anagrafica import *
from utility import *
from interrogazioni import *
from Ui_risultati import Ui_MainWindowResults

class MainWindowAnagrafica(QMainWindow, Ui_MainWindowAnagrafica):
	"""
	wrapper di Ui_MainWindowAnagrafica
	"""
	def __init__(self,risultati,parent=None):
			self.risultati= risultati
			self.tables=[]
			self.id=None
			QMainWindow.__init__(self,parent)
			mainWindow=QtGui.QMainWindow(self)
			#self.w=Ui_MainWindowAnagrafica()

			self.setupUi(self)





	def populateAnagrafica(self, id):
			self.tables=[]
			self.id=id
			self.tables.append(self.table_parametri_mmas)
			self.tables.append(self.table_marchi_mmas)
			self.tables.append(self.table_potenziali_mmas)	
			self.util=utility(self.id, self.tables)
			self.util.populateTables(self.id)
			self.util.populateFields(self, self.id)
	
	
	def on_nextButton_released(self):
		id= self.risultati.getNext()
		self.populateAnagrafica(id)
	def on_previousButton_released(self):
		id= self.risultati.getPrevious()
		self.populateAnagrafica(id)
	def on_lastButton_released(self):
		id= self.risultati.getLast()
		self.populateAnagrafica(id)
	def on_firstButton_released(self):
		id= self.risultati.getFirst()
		self.populateAnagrafica(id)
