import MySQLdb
class QueryBuilder():
	"""
	contiene le utilities per generare le queries da usare in interrogazioni
	@note: il risultato del filtro e' ottenuto intersecando i risultati di un massimo di tre query con l'insieme delle anagrafiche derivante dalla selezione geografica:
	 in particolare viene eseguita una query per ogni tab della gui in cui viene  selezionato qualcosa
	 @note:  il criterio per la costruzione dei  filtri richiede: che i parametri appartenenti allo stesso tab vengano messi in AND, cioe'
	 voglio trovare i pv che abbiano tre addetti e 2 vetrine e piu' di quattro vetrine, inoltre iparametri appartenenti alla stessa classe devono essere in OR, cio' significa
	 cerca i pv che abbiano 1, 2 o 3 addetti, i parametri tra i diversi tab sono in AND cioe'
	 voglio i pv che abbiano potenziale mmas 80 o 90 e tre o quattro addetti e 2 vetrine, i tab vengono messi in AND  tramite l'intersezione tra i risultati delle queries  
	"""
	def __init__(self):
		self.columns={'parametri':['tc_clpar_id', 'tc_par_id'], 'marchi':['tc_clmar_id', 'tc_mar_id'], 'potenziali':['tc_clpot_id', 'tc_pot_id']}
		self.Query={"parametri":"SELECT pv_id FROM rel_pv_par r  where ",
			"marchi":"SELECT pv_id FROM rel_pv_mar where ",
			"potenziali":"SELECT pv_id FROM rel_pv_pot r  where "}
		self.d=[[8L, 82L], [10L, 101L], [10L, 102L]]


	def groupList(self,l):
		"""
		produce le liste di parametri separati per class_id  
		genera un dict le cui chiavi sono il class_id, mentre i valori sono le liste dei parameters_id che afferiscono alla classe
		@param l: [[int,int]] con il seguente significato [class_id,parameter_id]
		@return: {int:[int]}{class_id:[parameter_id]}: la chiave e' il class_id degli elementi in l, 
		"""
		groups={}
		for k in l:
			if not (groups.has_key(k[0])):
				groups[k[0]]=[]
				groups[k[0]].append(k[1])
			else:
				groups[k[0]].append(k[1])
		return groups

#
#print grupList(d)
	def selectFormatter(self,key,d):
		"""
		genera le clausole select   da unificare con union all
		@param key: string 'parametri','marchi','potenziali'  chiave che identifica il tab
		@param   {int:string}:{class_id:string} out di orPackager
		@return: [string]
		"""
		query= self.Query[key]
		l=[]
		for o in d.itervalues():
			l.append("( %s)"%(query+o))
		return l
			
	def queryUnifier(self,d):	
		""" 
		congiunge le select generate da selectFormatter tramite union all
		@param [string]:
		@return: string 
		"""
		queryHead="select * from ("
		queryTail=")as tb1 GROUP BY tb1.pv_id HAVING COUNT(*) = %d"%len(d)
		query=""
		for s in d:
			query=query+s+" union all"
		#rimuovo l'ultimo  union all
		query=query[0:len(query)-9]
		query= queryHead+query+queryTail
		return query
		


	def coupleMaker(self,d,key):
		"""
		@param {class_id:[parameter_id]}: prende l'output di groupList e genera le condizioni and che formeranno la query del filtro: coppie del tipo tc_cl_mar_id= key and tc_mar_id=parameter_id
		@return:{k:[string]} la chiave e' la stessa del dict in input  
		@note: l'output e' una lista perche' cosi' e' piu' facile gestire i casi speciali del primo e dell'ultimo elemento, infatti questi saranno combinati con degli or che vanno posizionati solo tra gli elementi interni
		"""
		l={}
		for k in d.iterkeys():
			l[k]=[]
			for p in d[k]:
				l[k].append("(%s=%d and %s=%d)"%(self.columns[key][0],k,self.columns[key][1],p))# il senso e'(tc_cl.._id= chiave del dict,tc_.._id= parameter_id)
		return l

	def orPackager(self,l):
		"""
		combina le liste in uscita da   keyList2keyCouple con clausole 'or'
		@param {class_id:[string]} { class_id:[coupleFormatter]}:output di  keyList2keyCouple
		@return: {class_id:string}
		@note: il risultato deve ancora essere lavorato: gli elementi del dict vanno messi in and  tramite andPackager
		"""
		dictOut={}
		for k in   l.iterkeys():
			if not dictOut.has_key(k):
				dictOut[k]=[]
				preOut="( " 
				for i in range(0,len(l[k])):
					preOut=preOut+str(l[k][i])
					if i<len(l[k])-1:
						preOut=preOut+" or "
					else:
						preOut=preOut+")"
				dictOut[k]=preOut
		return dictOut

	def andPackager(self,l):
		"""
		costituisce l'ultimo step nella preparazione della query riceve l'uscita  di orPackager e ritorna la clausola where da aggiungere alla query
		@param {class_id:[string]}:out di orPackager
		@return: string 				
		"""
		q="("
		for e in l.iterkeys():
			q=q+l[e]+ " and "
			#rimuovo l'ultimo and e chiudo la clausola
		q=q[0:len(q)-4]+")"
		return q


	def groupMaker(self,l):
		"""
		combina assieme le clausole nelle coppie AND con la clausola OR
		@param [string] : l'input del metodo e' l'output di coupleMaker 
		@return: string: l'insieme delle clausole da aggiungere alla query 
		"""
		gm=" "
		for i in range(0,len(l)):
			gm=gm+l[i]
			if ((i>0)or(i<len(l)-1)):
				gm=gm+" or "
		return gm
	
	def coupleFormatter(self,key,class_id,parameter_id):
		"""
		genera una "coppia and" del tipo '(tc_cl_.._id =class_id and tc_.._id=parameter_id' cioe' mette assieme classe parametro e parametro id 
		risponde al requisitocerca i pv che classe parametro = addetti e parametro_id= 3 addetti etc., va ripetuto per ogni parametro selezionato
		@param class_id: int id della classe
		@param parameter_id: id del parametro
		@return: string   
		"""
		couple="(%s=%d and %s=%d)"%(self.columns[key][0],int(class_id),self.columns[key][1],int(parameter_id))
		return couple
	
	def buildQuery(self,l,key):
		"""
		produce la query dalla lista dei parametri
		@param [[class_id,parameter_id]]:[[int,int]]
		@return: string 
		"""
		gl=self.groupList(l)#{8L: [82L], 10L: [102L, 101L]}#
		#gl=db.groupList(d)
		cplm=self.coupleMaker(gl, key)
		op=self.orPackager(cplm)
		sf= self.selectFormatter(key,op)
		cplm=self.coupleMaker(gl, key)
		op=self.orPackager(cplm)
		sf= self.selectFormatter(key,op)
		query= self.queryUnifier(sf)

		return query

class dbQuery():
	"""
	classe per la gestione del db per conto di interrogazioni
	"""
	def __init__(self,user,activeDb):
		self.user=user
		self.activeDb=activeDb
		self.maker=QueryBuilder()
#		self.key='parametri'
		#dizionario che codifica le colonne da usare nelle queries
		self.columns={'parametri':['tc_clpar_id', 'tc_par_id'], 'marchi':['tc_clmar_id', 'tc_mar_id'], 'potenziali':['tc_clpot_id', 'tc_pot_id']}
		#dizionario che codifica le queries da usare 
		self.Query={"parametri":"SELECT pv_id FROM rel_pv_par   where ",
		    "marchi":"SELECT pv_id FROM rel_pv_mar where ",
		    "potenziali":"SELECT pv_id FROM rel_pv_pot   where "}
		# tabelle da usare 
		self.dictTables={'parametri':'tc_clpar', 'marchi':'tc_clmar', 'potenziali':'tc_clpot'}
		#specifica le colonne da usare nelle queries 
		self.dictValue={'parametri':'tc_par', 'marchi':'tc_mar', 'potenziali':'tc_pot'}
		self.dictPolita={'parametri':'tc_clpar', 'marchi':'tc_mar', 'potenziali':'tc_clpot'}
		self.query="select %s_id, testo,tc_stato_id from %s where tc_stato_id=1"
		# le queries per ricavare i testi dei checkbox per caricare veccie queries
		self.dictReverseQuery={}
		#popolo le reversequeries
		self.dictReverseQuery['parametri']="select testo from tc_par  where tc_clpar_id=%d and tc_par_id=%d"
		self.dictReverseQuery['potenziali']="SELECT testo FROM tc_pot t where tc_clpot_id=%d and  tc_pot_id=%d"
		self.dictReverseQuery['marchi']="SELECT testo FROM tc_mar t where tc_mar_id=%d"
		self.db = self.activeDb.getConnection()#MySQLdb.connect(host="localhost", user="root", passwd="ringil-87",db="parafarmacie",charset="utf8",use_unicode=True)
		self.crs=self.db.cursor()
		
	def getMarchiText(self,Id,dummy):
		"""
		@note recupera il testo relativo alle marche
		@param Id:	[int] id   e' una lista perche' questa funzione deve essere compatibile con getOtherText quindi piu' che di una lista si tratta di una tupla
		@param dummy: variabile di comodo per le stesse ragioni di Id
		@return: String
		"""
		#interrogo il db 
		self.crs.execute(self.dictReverseQuery['marchi']%(Id[0]))# uso le quadre per compatibilita
		#ricavo un solo item, poche'  fetchall ritorna una lista di tuple
		text= self.crs.fetchall()[0][0]
		return text
	
	def getOtherText(self,(classe,Id),key):
		"""
		@note: recupera il testo relativo a parametri e potenziali
		@param id:	Integer
		@param classe:	integer
		@param key:	'marchi'/'parametri'/'potenziali'
		@return: String
		"""  
		query= self.dictReverseQuery[key]%(classe,Id)
		self.crs.execute(query)
		rs=self.crs.fetchall()
		return rs[0][0]
	
	def getAllText(self,tab,*param):
		"""
		@note usa i giusti metodi per ricavare il testo per tutte le chiavi 
		@param *param:	 id/ id,classe
		"""
		func={}
		func['marchi']=self.getMarchiText
		func['potenziali']=self.getOtherText
		func['parametri']=self.getOtherText
		text=func[tab](param,tab)
		#print "dbQuery.getAllText",text
		return text
	def getPvById(self, Id):
		"""
		interroga il db e ritorna i parametri di un Pv dato il suo Id
		@param Id:	Integer
		@return: ((),())	 
		"""
		query="select nome1, indirizzo,pv_id,cliente,cap,		cod_cliente,comune,provincia,tel1,tel2,tel3,cf_pi from pv where pv_id= %d"%(Id)
		##print query
		self.crs.execute(query)
		return self.crs.fetchall()

	def addOr(self, b):
		"""
		implementa la logica per introdurre la clausola 'or' nella query
		lo or e' usato tra regole che afferiscono a tab diversi della gui interrogazioni
		@param b: Boolean
		@note: e' usata da interrogazioni
		"""
		if b:
			return 'or '
		else:
			return ""

	def getResultSet(self, query):
		"""
		esegue la query sul db di parafarmacie tramite semplice mysqldb
		@todo: check se realmente serve controllare se query!=[]; if introdotto con il passaggio a sqlalchemy=> forse non serve
		"""
		if query!=[]:
			self.crs.execute(query)
			return self.crs.fetchall()
		else:
			return ""
		
	def coupleMaker(self,d,key):
		"""
		@param {class_id:[parameter_id]}: riceve l'uscita di groupList e genera le condizioni and che formeranno la query del filtro: coppie del tipo tc_cl_mar_id= key and tc_mar_id=parameter_id
		@return:{k:[string]} la chiave e' la stessa del dict in input  
		@note: l'output e' una lista perche' cosi' e' piu' facile gestire i casi speciali del primo e dell'ultimo elemento, infatti questi saranno combinati con degli or che vanno posizionati solo tra gli elementi interni
		"""
		l={}
		for k in d.iterkeys():
			l[k]=[]
			for p in d[k]:
				l[k].append("(%s=%d and %s=%d)"%(self.columns[key][0],k,self.columns[key][1],p))# il senso e'(tc_cl.._id= chiave del dict,tc_.._id= parameter_id)
		return l
	
	def groupMaker(self,l):
		"""
		combina assieme le clausole nelle coppie and con la clausola or
		@param [string] : l'input del metodo e' l'output di coupleMaker 
		@return: string: l'insieme delle clausole da aggiungere alla query 
		"""
		gm=" "
		for i in range(0,len(l)):
			gm=gm+l[i]
			if ((i>0)or(i<len(l)-1)):
				gm=gm+" or "
		return gm
	
	def coupleCombiner(self,di):
		"""
		 combina assieme i  gruppi di parametri prodotti da coupleMaker in modo che  i parametri  di classi diverse siano combinati mediante and mentre i parametri della stessa classe siano collegati tramite or
		 @param
		 @return: string
		"""
		query=" "
		first= True
		for k in di.iterkeys():
			firstOr=True
			#se non e' il primo elemento del dict devo congiungerlo con and agli altri
			if not first:
				query=""+query+") and ("
			else:
				query=query+"("
				first=False
			for c in di[k]:
				if not firstOr:
					query=query+" or "
				else:
					firstOr=False
				
				query=query+str(c)
			query+query+")"# chiudo la parentesi della classe
			#chiudo la parentesi dei gruppi
		query=query+")"
		return query	
		
	def groupList(self,l):
		"""
    	produce le liste di parametri separati per class_id  
    	genera un dict le cui chiavi sono il class_id, mentre i valori sono le liste dei parameters_id che afferiscono alla classe
    	@param l: [[int,int]] con il seguente significato [class_id,parameter_id]
    	@return: {int:[int]}{class_id:[parameter_id]}: la chiave e' il class_id degli elementi in l, 
    	"""
		groups={}
		for k in l:
			if not (groups.has_key(k[0])):
				groups[k[0]]=[k[1]]
			else:
				groups[k[0]].append(k[1])
		return groups
	
	def queryBuilder(self, key, l):
		"""
		costruisce la query sulla base della key<=> tab
		@param key: <'parametri','marchi','potenziali'>
		@param l:{'parametri':[(classe,id_parametro)],'marchi':[(classe,id_parametro)],'potenziali':[(classe,id_parametro)]} 
		"""
		#estraggo la lista dei parametri relativi a key
		parameters=l[key]

		query=self.maker.buildQuery(parameters,key)#self.addwhere(query, parameters, key)
		##print "query from queryBuilder: %s"%query
		return query
	
	def getValuesBrand(self, idClass):
		brands=self.getBrands(self.getIdBrands( idClass))
		return brands
	
	def getValuesFunc(self, key, Id):
		"""
		ritorna
		la lista dei valori con il loro id data la chiave del tab key
		@param key:	'parametri','marchi','potenziali'
		@param id:	Integer
		@return ((int,string,int))::((class_id,testo,parametro_id))
		@note class_id puo essere tc_mar_id, tc_pot_id o tc_par_id in funzione di key che puo'
		 assumere rispettivamente i valori 'marchi','potenziali','parametri'
		"""
		query=self.query%(self.dictValue[key],self.dictValue[key])
		#se parametro o potenziale devo ordinare i risultati della query
		order={}
		order['parametri']=True
		order['potenziali']=True
		order['marchi']=False
		#polita=self.dictValue[key].replace('_', "_cl")
		polita=self.dictPolita[key]
		query=query+" and %s_id=%d"%(polita,Id)
		if order[key]:
			query+=" order by ordine"
		self.crs.execute(query)
		return self.crs.fetchall()
	
	def getCodMMAS(self, Id):
		query="SELECT cod_mmas FROM pv WHERE pv_id=%d"%Id
		self.crs.execute(query)
		return self.crs.fetchall()[0][0]
				
	def getBrand(self, Id):
		"""
		recupera il nome del marchio dal db dato lo id
		@param id: Integer
		@return: String
		"""
		query="select testo, tc_mar_id from tc_mar where tc_mar_id=%d"%(Id)
		#print query
		self.crs.execute(query)
		return self.crs.fetchall()[0][0]
	def getBrands(self, l):
		"""
		genera la lista di nomi di brand relativa alla lista di id
		@param l: [Integer]
		@return: [String]
		"""
		brands=[]
		for id in l:
			brands.append([ id[0], self.getBrand(id[0])])
		return brands
	def getIdBrands(self, brand_class_id):
		"""
		recupera i tc_mar_id relativi a tc_clmar_id
		cioe' i marchi che vendono una data classe di prodotti
		@param brand_class_id: Integer
		@return: (('tc_mar_id,Integer))
		@note: non usa sqlalchemy ne' elixir, ma la query e' standard dovrebbe funzionare pure con rdbms diversi da mysql 
		"""
		query="select tc_mar_id from tc_rel_clmar_mar where tc_clmar_id=%s"%(brand_class_id)
		self.crs.execute(query)
		return self.crs.fetchall()

	def getParameters(self, key):
		"""
		@param key: 'parametri'/'potenziali'
		@attention: 'marchi' non va perche' cambia un po' il procedimento per questo si usano getBrand, getBrands e getIdBrands
		@return: ((int, string,int))::(id, testo, tc_stato_id)
		"""
		query=self.query%(self.dictTables[key],self.dictTables[key])
		#print "query parametri "+query
		self.crs.execute(query)
		return self.crs.fetchall()

	def getValues(self, key, id):
		"""
		ritorna i valori delle classi dato lo id
		@param id:	integer
		@return: ((id,text))
		@param key:string  chiave del tab 'parametri o 'marchi' o 'potenziali' 
		
		"""
		#popolo un dizionario di funzioni, che usero' per ricavare i valori a seconda della chiave
		self.getValuesFunctions={'parametri':self.getValuesFunc(key, id), 'marchi':self.getValuesBrand( id), 'potenziali':self.getValuesFunc(key, id)}

		#print " id {0},  key {1}".format(key, id)
		return self.getValuesFunctions[key]


