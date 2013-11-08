from AnagraficaDb import *
class EntityElement():
	"""
	questa classe rappresenta gli elementi di parametri e marche
	 visualizzabili nell'esportazione di un'angrafica
	"""

	def getHeader(self):
		""" 
		getter di self.header
		@return string:header della colonna
		"""
		return self.header 
	
	def setMax(self,m):
		"""rappresenta il massimo numero elementi visualizzabili per class_id: il valore di default e' 1, in quanto per ogni parametro e' sufficiente visualizzare un solo valore, mentre per le marche in genere vengono richiesti piu' risultati
		@param int:
		"""
		self.max=m
		
	def fetchValue(self,Id,class_id):
		"""
		ritorna i primi self.max  valori relativi al class_id per un pv
		@param int:pv_id del pv
		@return: [string] 
		"""
		lv=[]
		#print "fetchValue in entityElements Id, class",Id,class_id
		l=self.db.fetchValue4Pv(self.tab,Id,class_id)
		for i in range(0,self.max):
			#print i 
			try:
				lv.append(l[i])
			except IndexError:
				lv.append("") #aggiunge i campi vuoti dove ci sono piu colonne che risultati
		return lv
			
	def getHeaders(self,subfix=True):
		"""
		ritorna gli header per marchi o parametri
		@return: [string]
		"""
		l=[]
		a=lambda x:x+1 if self.max>1 else ""
		b=lambda x:"_"if x>0 or self.max>1 else ""
		c=lambda x,y:x if y==True else ""
		for i in range(0,self.max):
			s=b(i)+str(a(i))# genero un suffisso per gli headers con max>1 del tipo _0, _n
			l.append(self.header+c(s,subfix))
		return l
		
	def getClassId(self): 
		return self.class_id
	
	def setClassId(self,Id):
		"""
		setter di class_id
		si occupa di settare il valore appropriato dello header
		@param int:class_id puo' essere tc_clmar_id o tc_clpar_id
		"""
		self.class_id=Id 
		self.header=self.db.getHeader(self.tab,Id)
		
	def getMax(self):
		"""
		getter di self.max
		@return: int
		"""
		return self.max
	
	def setRequired(self,b):
		"""
		setter per self.required
		@param bool:
		"""
		self.required=b  
	
	def isRequired(self):
		"""
		getter per self.required
		@return: bool
		"""
		return self.required
	
	def getId(self):
		"""
		getter di self.class_id, questo parametro e' usato come Id delle entita' configurabili
		@return: int:class_id
		"""
		return self.class_id
	
	def setDb(self,db):
		self.db=db
	
	def __init__(self,class_id,tab,db):
		"""
		@param class_id:int rappresenta l'identificativo della classe dell'entita' sara' tc_clmar_id nel caso delle marche tc_clpar_id nel caso dei parametri
		@param header:string rappresenta l'intestazione che mostrera' la colonna esportata, viene preso direttamente dal db
		@param tab:string distingue se l'entita' e' un parametro o una marca i valori ammessi sono 'marche' e 'parametri'
		@attention: i valori ammessi sono quelli presenti nel db e corrispondenti al class_id settato, percio' si sconsiglia di settare direttamente questo parametro, ma di avvalersi di setClass_id
		che oltre a settare class_id, recupera dal db il corretto valore per lo header  

		"""
		self.db=db
		self.tab=tab
		self.class_id=None
		self.header=None
		self.setClassId(class_id)
		
		self.max=1
		self.required=False
		
	def __repr__(self):
		return "EntityElement:%s, required:%s,tab %s"%(self.header,self.required,self.tab)
		
		