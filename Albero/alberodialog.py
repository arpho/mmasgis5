#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
/***************************************************************************
 AlberoDialog
                                 A QGIS plugin
 permette di selezionare rapidamente gli elementi di un progetto qgis tramite una struttura ad albero
                             -------------------
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_albero import *
from selezioneGeo import *
from cercaGeo import *
class MainWindowAlbero(QMainWindow, Ui_Albero):
	"""wrapper di Ui_Albero gestisce l'interazione con la gui dell'albero delle selezioni
	"""
	
	def __init__(self,face,tree,parent=None):
			QMainWindow.__init__(self,parent)
			self.iface=face
			self.tree=tree
			self.w=Ui_Albero()
			self.setupUi(self)
			self.cerca=MainWindowCercaGeo(self)
			QtCore.QObject.connect(self.cerca, QtCore.SIGNAL("myExplode"), self.explode)
			self.layers={}
			self.selectionGui=SelezioneGeoWindow(self)
			#self.selectionGui.reset()
			
	def reset(self):
			self.selectionGui.reset()
			self.selectionGui.updateList()
			
	def addLayer(self,k,layer):
		self.layers[k]=layer
		
	def deSelectFeature(self,n):
		"""
		deseleziona la feature  identificata da Id e layer 
		@param Nodo: nodo rappresentante la feature sull'albero  

		"""
		curLayer=self.layers[n.getCathegory()[0:3]]
		print "selectedFeature", n.getFeatId()
		self.iface.setActiveLayer(curLayer)
		curLayer.deselect(n.getFeatId())#deseleziono la feature ed emetto il segnal selectionChanged 		
		
	def selectFeature(self,n):
		"""
		seleziona feature  identificata da Id e layer 
		@param Nodo: nodo rappresentante la feature sull'albero  
		@param bool:  
		"""
		curLayer=self.layers[n.getCathegory()[0:3]]
		#l=lambda a: "seleziono" if a==True else "deseleziono" 
		#print "selectedFeature", l(v),n.getFeatId()
		self.iface.setActiveLayer(curLayer)
		curLayer.select(n.getFeatId())#setto la feature ed emetto il segnal selectionChanged 
		
	def on_albero_itemDoubleClicked(self,item,column):
		#mostro la finestra delle selezioni
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.selectionGui.geometry()
		self.selectionGui.move((screen.width()/2)-size.width(),(screen.height()/2)-size.width())
		self.selectionGui.show()
		#print "clicked item {0} at {1}".format(item.data(0,1).toString(),item.data(0,3).toString())
		nodo= item.data(0,4).toPyObject()
		#aggiungo la selezione alla finestra delle selezioni
		#self.selectionGui.addElement(nodo)
		#rendo visibile il nodo
		nodo.setVisible(True)
		#seleziono  tutti i nodi coinvolti
		nodo.setSelected(True,True)
		#aggiorno la finestra delle selezioni
		self.selectionGui.updateList()
		#seleziono la feature sul layer
		self.selectFeature(nodo)
		# seleziono ricorsivamente il nodo e i suoi discendenti
		#setto visibile il nodo
		
	def showSelectionGui(self):
		"""
		rende visibile la finestra delle selezioni
		"""
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.selectionGui.geometry()
		self.selectionGui.move((screen.width()/2)-size.width(),(screen.height()/2)-size.width())
		self.selectionGui.show()		
	
	def on_cercaButton_released(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.cerca.geometry()
		self.cerca.move(screen.width()/2,(screen.height()/2)-size.height())
		self.cerca.show()

	def explode(self,msg):
		"""
		questo metodo si occupa di esplodere un nodo dell'albero e' connesso con il segnale myExplode
		 emesso dalla finestra cercageo al release del bottone cerca, questo segnale e' emesso insieme con 
		 un messaggio  il cui formato e' una coppia di string, il primo elemento e' il testo digitato nella
		  casella della gui, questo testo e' lo header del nodo cercato, il secondo campo indica la categoria
		  i valori possibili sono <'cap'>,<'comune'>,<'provincia'>
		@param (string,string): (header, categoria)
		"""		
		name=msg[0]
		cat=msg[1]	
		node=self.tree.cerca(name,cat)
		if node != None:
			node.getNode().setSelected(True)
			self.albero.scrollToItem(node.getNode(),0)
			self.albero.setCurrentItem(node.getNode())
			self.activateWindow()
		else:
			mx=QtGui.QMainWindow()
			QtGui.QMessageBox.information(mx,"Attenzione", "Territorio non trovato")

	def selectNode(self,n):
		""" wrapper del metodo addElement di selezionegeo
			@param Nodo: nodo selezionato sul layer
		"""
		self.selectionGui.addElement(n)
		self.selectionGui.updateList()

	def on_plusNodes_released(self):
		"""slot relativo al bottone plusNodes"""
		item=self.albero.itemAt(0,0)
		while item is not None:
			item.setExpanded(True)
			item=self.albero.itemBelow(item)
		
	def on_minusNodes_released(self):
		"""slot relativo al bottone minusNodes"""
		item=self.albero.itemAt(0,0)
		while item is not None:
			item.setExpanded(False)
			item=self.albero.itemBelow(item)
		self.tree.collapseAll()

	def on_albero_itemActivated(self,item,col):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.selectionGui.geometry()
		self.selectionGui.move((screen.width()/2)-size.width(),(screen.height()/2)-size.width())
		self.selectionGui.show()
		#print "clicked item {0} at {1}".format(item.data(0,1).toString(),item.data(0,3).toString())
		nodo= item.data(0,4).toPyObject()
		#aggiungo la selezione alla finestra delle selezioni
		#self.selectionGui.addElement(nodo)
		#rendo visibile il nodo
		nodo.setVisible(True)
		#seleziono  tutti i nodi coinvolti
		nodo.setSelected(True,True)
		#aggiorno la finestra delle selezioni
		self.selectionGui.updateList()
		#seleziono la feature sul layer
		self.selectFeature(nodo)
		
