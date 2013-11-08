from Entity import *
class Profilo():
	"""
	rappresenta l'insieme di entita' che vengono selezionate per l'esportazione
	"""
	def addEntity(self,el):
		"""
		aggiunge un'entita' alla lista delle entita' self.entitylList
		@param el:Entity
		@note: le entita' vengono identificate tramite un id che viene generato  in automatico dal metodo secondo il loro ordine in lista
		la prima entita' avra' id 0 e cosi' via
		"""
		Id=len(self.entityList)
		if not self.needsConfiguration():
			el.setEntityId(Id)
		self.entityList.append(el)
		
		
	def getHeaders4Parameters(self,value=False,Id=0):
		"""
		ritorna gli header  delle entita' parametro presenti in self.entityList
		@param bool opzionale: se True ritorna una lista di  dict dei parametri {srting:string}::{header:valore}  
		@return: [string] se value=False
		"""		
		ld=[]
		lp=[]	
		if value:
			for i in self.entityList:
#			print i,i.needsConfiguration()
				if i.getType()=="parametri":
					values=i.getValue(Id,i.getHeader(),True)
					param={}
					headers=i.getHeaders()
					if type(headers)==type([]):
						for j in enumerate(headers):
							param[j[1]]=values[j[0]]
						ld.append(param)
		else:
			for i in self.entityList:
#			print i,i.needsConfiguration()
				if i.getType()=="parametri":	
					h=i.getHeaders()
					values=i.getValue(Id,i.getHeader(),True)
					if type(h)==type([]):	
						for j in h:
							ld.append(j)	
			
		return ld
		
	def getHeaders4Brands(self,value=False,Id=0):
		"""
		ritorna gli header  delle entita' parametro presenti in self.entityList
		@param bool opzionale: se True ritorna una lista di  dict dei parametri {srting:string}::{header:valore}  
		@return: [string]
		"""		
		ld=[]
		lp=[]	
		if value:
			for i in self.entityList:
#			print i,i.needsConfiguration()
				if i.getType()=="marche":
					values=i.getValue(Id,i.getHeader(),True)
					param={}
					headers=i.getHeaders()
					if type(headers)==type([]):
						for j in enumerate(headers):
							param[j[1]]=values[j[0]]
						ld.append(param)
		else:
			for i in self.entityList:
#			print i,i.needsConfiguration()
				if i.getType()=="marche":	
					h=i.getHeaders()
					values=i.getValue(Id,i.getHeader(),True)
					if type(h)==type([]):	
						for j in h:
							ld.append(j)	
			
		return ld
			
	
		
	def getsHeadersWithData(self,tipo,value=False,Id=0,onlyDict=False):
		"""
		ritorna gli header  delle entita' di tipo type in self.entityList
		@param string: tipo di entita' ricercato<'parametri'>,<'marche'>,<'anagrafica'>
		@param bool opzionale: se True ritorna una lista di  dict dei parametri {srting:string}::{header:valore}  
		@param bool opzionale:se True ritorna  un dict {string:string}::{header:valore} default False
		@note:  l'ultimo parametro opzionale hala prealenza sul precedente 
		"""	
		ld=[]
		lp=[]	
		hAndv={}
		if value:
			param=Odict()
			for i in self.entityList:
#			print i,i.needsConfiguration()
				if i.getType()==tipo:
					values=i.getValue(Id,i.getHeader(),True)
					headers=i.getHeaders(False) #non voglio suffisso
					
					#print "allora",hAndv
					if type(headers)==type([]):
						
						for j in enumerate(headers):
							param[j[1]]=values[j[0]]
						ld.append(param)
						if onlyDict:
							for i in range(0,len(headers)):
								if not hAndv.has_key(headers[i]):
									hAndv[headers[i]]=[]
									if values[i]!="":
										hAndv[headers[i]].append(values[i])
								else:
									if values[i]!="":
										hAndv[headers[i]].append(values[i])
							#print "aaaallora",hAndv
					else:
						param[headers]=values
						#ld.append({headers:values})
			ld=param
		else:
			for i in self.entityList:
#			print i,i.needsConfiguration()
				if i.getType()==tipo:	
					headers=i.getHeaders()
					values=i.getValue(Id,i.getHeader(),True)
					if type(headers)==type([]):	
						for j in headers:
							ld.append(j)	
		if onlyDict:
			return hAndv
		else:	
			return ld
				
	
	def setId(self,Id):
		"""
		setter degli Id per le entita' in self.entityList
		@param int:Id 
		"""
		for i in self.entityList:
			i.setId(Id)
		
	def getData(self,Id):
		"""
		ritorna i dati forniti dalle entita' in self.entityList
		
		@param int:Id del pv da interrogare
		@return: [string]
		"""
		
		#instanzio la lista che sara' ritornata
		ld=[]
		# aggiorno le entita' con lo Id attuale
		self.setId(Id)
		for i in self.entityList:
			h=i.getHeader()
			a=i.getValue(Id,h)
			#print "getdata from getValue",a
			if type(a)==type([]):
				for j in a:
					ld.append(j)
			else:
				ld.append(a)
			#print "ld",ld
		return ld

	def getData4Parameters(self,Id,dict=False):
		"""
		ritorna i dati forniti dalle entita'  di tipo partametro in self.entityList
		
		@param int:Id del pv da interrogare
		@param bool opzionale: se True ritorna un dict che ha per chiave lo header dei parametri
		@return: [string]
		"""
		
		#instanzio la lista che sara' ritornata
		if dict:
			ld={}
		else:
			ld=[]
		# aggiorno le entita' con lo Id attuale
		self.setId(Id)
		for i in self.entityList:
			if i.getType()=="parametri":
				h=i.getHeader()
				a=i.getValue(Id,h,True)#sono interessato ad ottenere i valori quindi setto populate a True
				#print "getdata from getValue",a
				if type(a)==type([]):
					if dict:
						ld[h]=[]
					for j in a:
						if not dict:
							ld.append(j)
						else:
							ld[h].append(j)
				else:
					if not dict:
						ld.append(a)
					else:
						ld[h]=a
		return ld
	
	def getData4Brands(self,Id):
		"""
		ritorna i dati forniti dalle entita'  di tipo partametro in self.entityList
		
		@param int:Id del pv da interrogare
		@return: [string]
		"""
		
		#instanzio la lista che sara' ritornata
		ld=[]
		# aggiorno le entita' con lo Id attuale
		self.setId(Id)
		for i in self.entityList:
			if i.getType()=="marche":
				h=i.getHeader()
				a=i.getValue(Id,h)
				#print "getdata from getValue",a
				if type(a)==type([]):
					for j in a:
						ld.append(j)
				else:
					ld.append(a)
		return ld		

	def needsConfiguration(self):
		""" ritorna vero se c'e' almeno un'entita' ancora da configurare
		 ad ogni entita' applica la funzione Entity.needsConfigured and not Entity.isConfigured
		 quindi ritornera' True solo se la prima e' True e la seconda False, in tutti gli altri casi ritornera' False
		 per sapere se il profilo necessita di configurazione mette in Or il risultato della funzione suddetta applicata ad ogni entita'
		 @return: boolean
		 """
		#nella funzione OR l'elemento neutro e' False
		
		b=False
		#instanzio la funzione logica che calcola se l'entita' ha bisogno di configurazione
		l=lambda a,b: a and not b
		for i in self.entityList:
			b=b or l(i.needsConfiguration(),i.isConfigured())
		return b
		
	def getAvailableEntity(self):
		"""ritorna la lista delle entita' non configurabili disponibili
		@return: [string]
		"""
		#instanzio un entita' fittizzia per avere accesso all'elenco delle entita' disponibili
		dummy=Entity2Export('ragione sociale',False,271,self.user,self.activeDb,self.db,"dummy")
		return dummy.getAvailableEntity()
	
	def getHeaders(self):
		"""
		ritorna gli header  delle entita' in self.entityList
		@return: [string
		"""
		#instanzio la lista che sara' ritornata
		ld=[]
		for i in self.entityList:
			#print i,i.needsConfiguration()
			h=i.getHeaders()
			if type(h)==type([]):
				for j in h:
					ld.append(j)
			else:
				ld.append(h)
		return ld	
		
		
	def __init__(self,db,user,activeDb):
		self.entityList=[]
		self.pv_id=None
		self.db=db
		self.user=user
		self.activeDb=activeDb
	
