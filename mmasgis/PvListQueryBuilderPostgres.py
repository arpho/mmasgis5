from pvListQueryBuilderBase import PvListQueryBuilderBase


class PvListQueryBuilderPostgres(PvListQueryBuilderBase):
	"""
	@param utbs:[UTB] la lista di utb selezionate sulla mappa
	@param db:Db  active db  ottenuto da mmasgis
	"""
	def __init__(self,utbs,db):
		PvListQueryBuilderBase.__init__(self, utbs)
		self.db=db.getConnectionMMASGISDB()
		self.crs=self.db.cursor()
		
		"""
		ottiene la lista di codici istat che corrispondono alla selezione geografica
		@param query: sottoquery della  query per mysql che interroga mmasgisDB per i codici istat
		@return: [string]::[tc_istat_id]
		"""  
	def getIstatList(self,query):
		#print "query in getIstatList",query
		self.crs.execute(query)
		istat=[]
		l= self.crs.fetchall()
		for i in l:
			istat.append(i)
		#print "lista istat",istat
		return istat
	
	"""
	data la lista di codici istat ottenuta tramite getIstatList
	genera la stringa dell'insieme di codici istat che va usata nella query pvList
	@param l:[(int,)]::[(codice_istat,)]
	@return String
	"""
	def buildIstatList(self,l):
		s=""
		for i in l:
			s+=str(i[0])
			s+=","
			#rimuovo l'ultima virgola
		s=s[0:len(s)-1]
		return s 
		
		
	
	def getCapQuery(self):
		cap=self.getCAPusers()
		query=""
		queryCap=""
		first=True
		for c in cap:
			if not first:
				queryCap+=" or "
				first=False
			first=False
			queryCap+=c.getSelect()
			#print "capQuery:",queryCap
		return queryCap
	
	"""
	genera la stringa che in postgres sostituisce la sottoquery per codici istat in mysql 
	"""
	def getIstatString(self):
		queryIstat=self.combineIstat()
		listIstat=self.getIstatList(queryIstat)# interrogo mmasgisdb per ottenere la lista dei codici istat selezionati
		IstatString=self.buildIstatList(listIstat)
		return IstatString
		
	def getFullQuery(self):
		query=""
		
		if(self.usesCap() and self.usesIstat()):
			query=self.cons.queryListByIstat.format(self.getCapQuery())
			queryIstat=self.combineIstat()
			listIstat=self.getIstatList(queryIstat)
			query=self.getCapQuery()
			query+=" or tc_istat_id in("
			query+=self.getIstatString()#self.combineIstat()
			query+=")"
			query=self.cons.queryListByIstat.format(query)
			print"query-istat",self.combineIstat()
			#query+=")"
			return query
		if(self.usesCap()):
			query=self.cons.queryListByIstat.format(self.getCapQuery())
			print "query cap",query
			return query
		if(self.usesIstat()):
			queryIstat=self.combineIstat()
			listIstat=self.getIstatList(queryIstat)
			q=" tc_istat_id in ("
			queryIstat=self.combineIstat()
			listIstat=self.getIstatList(queryIstat)# interrogo mmasgisdb per ottenere la lista dei codici istat selezionati
			IstatString=self.buildIstatList(listIstat)#combino la lista di codiciistat in una stringa
			q+=self.getIstatString()#IstatString
			q+=")"
			query=self.cons.queryListByIstat.format(q)
			return query