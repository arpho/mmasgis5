from  filterDb import *
#from queriesDb import *
class Filter():
	"""
	permette di definire una serie di condizioni che il pv deve soddisfare, il metodo test applicato
	sul singolo pv verifica che questo le rispetti, in particolare la logica dei filtri prevede che
	piu' parametri della stessa classe siano  in OR mentre parametri di classi differenti devono
	essere in AND
	"""
	def __repr__(self):
		return "tab:{0},parametri:{1}".format(self.tab,self.parameters)
	def __init__(self,parametri, tab,db,user,activeDb):
		"""
		@param parametri: [{int:[int]}]::[{class_id:[parameter_id]}] setting del filtro
		@param tab: string chiave del Filtro
		@param db:queriesDb, stessa istanza di QueriesDb usata da interrogazioni savequery e loadQuery 
		@param USER:utente attivo
		@param Db:Db attivo
		"""
		self.user=user
		self.activeDb=activeDb
		self.db=filterDb(user,activeDb)
		self.Dbquery=db
		self.parameters=parametri
		self.tab=tab
		
	def unpackParameter(self,d):
		"""ritorna una versione dei parametri del filtro "scompattata", cioe' nel formato[(int,int)]::[(category_id,parameter_id)],
		perche' sia compatibile con le funzioni di queriesDb
		@return: [(int,int)]::[(category_id,parameter_id)]
		"""
		l=[]
		for k in d.iterkeys():
			for i in d[k]:
				l.append((k,i))
		return l		
		
	def save(self,Id):
		"""
		salva i parametri del filtro sul db usando come chiave esterna l'id della query
		@param Id:int:: query_id
		""" 
		#instanzio il dict per la selezione della tabella su cui operare in funzione del tab
		
		insertFunctions={}
		insertFunctions['marchi']=self.Dbquery.insertMarchi
		insertFunctions['potenziali']=self.Dbquery.insertPotenziale
		insertFunctions['parametri']=self.Dbquery.insertParametri
		#registro i parametri sul db
		insertFunctions[self.tab](Id,self.unpackParameter(self.parameters))
				
		
	
	def test(self,Id):
		"""
		esegue il test definito dai parametri del filtro sul pv con pv_id Id
		@param Id::int pv_id
		@return boolean 
		"""
		return self.checkTab(Id,self.tab,self.parameters)
	
	def checkTab(self,Id,tab,d):
		"""
		esegue i filtri appartenenti ad un tab
		@param Id::int pv_id
		@param tab:string specifica il tab di cui eseguire i filtri 'marchi',parametri','potenziali'
		@param d:{int:[int]}::{class_id:[parameter_id]} 
		@return boolean: il valore ritornato e' l'operazione di AND tra i check per ogni classe
		"""
		# True e' il valore neutro per l'operazione di AND
		b= True
		# definisco un dict dei metodi da usare per il check delle classi
		chekers={}   
		chekers['marchi']=self.db.checkClassBrand
		chekers['parametri']=self.db.checkClassParameter
		chekers['potenziali']=self.db.checkClassPotential
		for k in d.iterkeys():
			b=b and chekers[tab](Id,k,d[k])
		return b
		
	 	
