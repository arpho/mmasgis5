from Ui_selezionegeo import *
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Tree import *
import re


class SelezioneGeoWindow(QMainWindow, Ui_SelezioneGeo):
	""" wrapper di Ui_Progressbar
	"""
	def __init__(self,albero,parent=None):	
			"""
			@param bool: True per visualizzare la progressBar per l'avanzamento complessivo
			@param bool: True per visualizzare la progresBar per l'avanzamento parziale  
			"""
			QMainWindow.__init__(self,parent)
			#self.w=Ui_ProgressBar()
			self.fontBold=QtGui.QFont('Arial', 12)
			self.fontBold.setBold(True)
			self.albero=albero
			self.setupUi(self)
			self.selectedList=SelectionList()
			
	def reset(self):
		""" resetta la lista delle selezioni
		"""
		self.selectedList.reset()
	
			
	def updateList(self):
		""" aggiorna la lista
		"""
		self.selection_list.clear()
		l=self.selectedList.getList()
		#non voglio ripetizioni 
		#creo un dict per tenere traccia dei nodi visualizzati
		visualized={}
		for i in l:
			item=QtGui.QListWidgetItem(i.getHeader()+" "+i.getSubHeader())
			item.setData(3,i)
			if i.isVisible():
				#di default testo nero
				item.setForeground(QtGui.QColor(0, 0, 0))
				nodo=item.data(3).toPyObject()
				"""
				if self.selectedList.isPresent(nodo):
					#coloro il testo di rosso
					print "sovrapposizione"
					item.setForeground(QtGui.QColor(255,0, 0))
					"""
					
				if i.hasChildren():
					item.setFont(self.fontBold)
				if not visualized.has_key(nodo):
					self.selection_list.addItem(item)
					visualized[nodo]=""
					
	def retrieveLayer(self,metadata):
		"""
		determina il nome del layer dai suoi metadata
		@param string:metadata del layer
		@return: string sigla layer:<'cap',<'pro'>,<'reg'>,<'com'>
		"""
		#settrace()
		layersTest=[]
		layersTest.append(('reg','reg'))
		layersTest.append(('pro','prov'))
		layersTest.append(('com','com2'))
		layersTest.append(('cap','Cap'))
		for i in layersTest:
			if self.search(metadata, i[1]):
				return i[0]					
			
			
	def search(self,string,pattern):
			"""
			esegue il metodo search su una stringa:
			@param string: stringa da analizzare
			@param string: pattern dell' espressione regolare
			@return: boolean  
			"""
			match=re.compile(pattern)
			b=False
			if match.search(string):
				b=True
			return b
					
	def on_selection_list_itemDoubleClicked(self,item):
		nodo=item.data(3).toPyObject()
		self.albero.deSelectFeature(nodo)
		# deseleziono ricorsivamente il nodo  e i suoi discendenti
		nodo.setSelected(False,True)
		# nascondo il nodo e i suoi discendenti
		nodo.setVisible(False,True)		
		#rimuovo il nodo dalla lista
		self.selectedList.removeElement(nodo)
		#aggiorno la visualizzazione della lista
		self.updateList()
		#self.albero.se
		
	def on_minusNodes_released(self):
		item= self.selection_list.currentItem()
		if item is not None:
			item.setFont(self.fontBold)
			#item=self.selection_list.itemAt(index)
			nodo= item.data(3).toPyObject()
			nodo.collapse()
			self.updateList()		
		
	def on_plusNodes_released(self):
		item= self.selection_list.currentItem()
		if item is not None:
			item.setFont(self.fontBold)
			#item=self.selection_list.itemAt(index)
			nodo= item.data(3).toPyObject()
			nodo.explode()
			self.updateList()
			
	def addElement(self,e):
		"""
		aggiunge un elemento alla lista delle selezioni
		@param Nodo
		"""
		#e.setVisible(True)
		# seleziono il nodo e tutti i nodi sottostanti  nella gerarchia
		self.selectedList.addElement(e)
