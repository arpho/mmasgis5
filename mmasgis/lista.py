from utility import *
from Utb import Utb
from Provincia import Provincia
from Comune import Comune
from Regione import Regione
from CAP import CAP
from constants import cons
from ComunePg import ComunePg
from ProvinciaPg import ProvinciaPg
from RegionePg import RegionePg

class Lista():
	"""
	gestisce la costruzione della lista di selezione geografica
	fornendo tutti i metodi utili alla sua gestione
	"""
	def __init__(self,user,db):
		self.user=user
		self.db=db
		self.lista=[]
		self.cons=cons()
		self.util=utility([],0,user,db)
		self.utbClasses={}
		self.utbClasses['mysql']=[Regione,Provincia,Comune,CAP]
		self.utbClasses['postgresql']=[RegionePg,ProvinciaPg,ComunePg,CAP]
		self.utbFactory={}
		self.utbFactory['reg']=self.utbClasses[db.getRDBMS()][0]#Regione
		self.utbFactory['pro']=self.utbClasses[db.getRDBMS()][1]#Provincia
		self.utbFactory['com']=self.utbClasses[db.getRDBMS()][2]#Comune
		self.utbFactory['cap']=self.utbClasses[db.getRDBMS()][3]#CAP
	"""
		aggiunge un item alla lista 
		
		@param t:[key,key] le chiavi possono essere 'cap,'pro','com','reg', il primo campo specifica se item deve essere convertito nella sua sigla, il secondo se va espanso 
		"""	
	def appendItem(self,t):
		item=self.utbFactory[t[0]]( t[1],t[2])
		self.lista.append(item)
	def resetList(self):
		self.lista=[]
		
	def getList(self):
		return self.lista
	
	def cleanList(self):
		self.lista=[]
	
