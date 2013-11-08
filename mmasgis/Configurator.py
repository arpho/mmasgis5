#!/usr/bin/python
# -*- coding: latin-1 -*-

from AnagraficaDb import *

class Configurator():
	"""
	rappresenta la lista degli elementi selezionati per  le entita' configurabili e agisce da wrapper per i metodi getHeaders, getAvailableElements e getData 
	"""
	def __repr__(self):
		return "Configuratore: %s"%self.tab
	
	def __init__(self,tab,db):
		"""
		@param string:tab di appartenenza dell'entita' configurabile
		@note: i valori previsti per tab sono 'marche' e 'parametri' 
		"""
		self.max=10
		self.entityList=[]
		self.tab=tab
		self.db=db
	
	def setMax(self,m):
		self.max=m
		
	def getMax(self):
		return self.max
	
	def addElement(self,e,db):
		"""
		aggiunge un item a self.entityList
		@param EntityElement:
		"""
		e.setDb(db)
		self.entityList.append(e)
		
		
	def getData(self,Id):
		"""
		ritorna i dati delle entita' selezionate, per lo Id passato come parametro
		@param int: Id del pv sotto analisi
		@return: [string]
		"""
		l=[]
		for i in self.entityList:
			h=i.fetchValue(Id,i.getClassId())
			if type(h)==type([]):
				for j in h:
					l.append(j)
			else:
				l.append(h)
		return l 
	
	#TODO
	def print2Pdf(self,Id):
		"""
		genera il l'anagrafica in formato pdf per un  pv
		@param int: pv_id del pv da esportare 
		"""
		pass
	
	#TODO
	def getHeaders(self,subfix=True):
		""" ritorna la lista degli headers da esportare
		@return: [string]
		"""
		l=[]
		for i in self.entityList:
			#print "configur",i.getHeaders()
			for j in i.getHeaders(subfix):
				l.append(j)
		return l
	
	#TODO
	def getAvailableElements(self,tab):
		"""
		ritorna la lista degli elementi selezionabili per configurare l'entita'
		@param string:<'marche'>,<'parametri'> specifica il tipo di entita' 
		@return: [{string:int}]::[{header:class_id}]
		"""
		d={}
		d['marche']=self.db.getBrands4Extraction
		d['parametri']=self.db.getAllParameters
		return d[tab]()
	
	def setEntityList(self,l):
		"""
		setter per self.entityList
		@param [EntityElement]: rappresentala lista delle entita' selezionate, questa viene popolata e passata a Configurator dalla gui configurazione
		"""
		self.entityList=l
	
		

		
	
	