from Ui_progressBar import *
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature

class ProgressBarWindow(QMainWindow, Ui_ProgressBar):
	""" wrapper di Ui_Progressbar
	"""
	def __init__(self,visible1, visible2,parent=None):	
			"""
			@param bool: True per visualizzare la progressBar per l'avanzamento complessivo
			@param bool: True per visualizzare la progresBar per l'avanzamento parziale  
			"""
			QMainWindow.__init__(self,parent)
			#self.w=Ui_ProgressBar()
			self.setupUi(self)
			self.progressBar_1.setVisible(visible1)
			self.progressBar_2.setVisible(visible2)		
			#self.progressBar_1.setMaximum(100)	
			#self.progressBar_1.setValue(40)
			
	def setMaximumPartial(self,max):
		"""
		setta il valore massimo in progressBarOverall
		@param int:
		"""
		self.progressBar_2.setMaximum(max)
		
	def setMaximumOverall(self,max):
		"""
		setta il valore massimo in progressBarPartial
		@param int:
		"""		
		self.progressBar_1.setMaximum(max)
			
	def setValueOverall(self,v):
		"""setta il valore della progressBar in alto, indicante l'avanzamento complessivo
		@param int:
		"""
		self.progressBar_1.setValue(v)

	def setValueParticular(self,v):
		"""setta il valore della progressBar in basso, indicante l'avanzamento complessivo
		@param int:
		"""
		self.progressBar_2.setValue(v)
		
	def setValueLabel(self,txt):
		""" setta il testo della label nella finestra
			@param string
		"""
		self.label.setText(txt)
		