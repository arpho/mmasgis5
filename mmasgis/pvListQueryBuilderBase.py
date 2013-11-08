from constants import *
class PvListQueryBuilderBase:
	"""
	@param utbs:[Utb]
	"""
	def __init__(self,utbs):
		self.utbs=utbs
		self.cons=cons
		
	def usesIstat(self):
		b=False
		for u in self.utbs:
			b=b or u.usesIstat()
		return b 
	
	def usesCap(self):
		b=False
		for u in self.utbs:
			b=b or u.usesCap()
		return b 
	"""
	estrae i cap presenti in self.utbs
	@return: [CAP]
	"""
	def getCAPusers(self):
		l=[]
		for i in self.utbs:
			if i.usesCap():
				l.append(i)
				
		return l
	
	def getIstatUser(self):
		l=[]
		for i in self.utbs:
			if i.usesIstat():
				l.append(i)
		return l 
	
	def combineIstat(self):
		c=""
		for u in self.getIstatUser():
			c+=u.getSelect()
			
			c+=" union "
		c=c[0:len(c)-6]
		return c
			
				
		
	
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
		
	def getQuery(self):
		query=""
		if(self.usesCap()):
			first=True
			
			cap=self.getCAPusers()
			query=""
			queryCap=""
			for c in cap:
				if not first:
					queryCap+=" or "
					first=False
				first=False
				queryCap+=c.getSelect()
			query=self.cons.queryListByIstat.format(queryCap)
			if( self.usesIstat()):
				query+=" or tc_istat_id in ("
				query+=self.combineIstat()
				query+=")"
		return query
	
	def getIstatQuery(self):
		return "("+self.combineIstat()+")"
	
	def getFullQuery(self):
		query=""
		if(self.usesCap() and self.usesIstat()):
			query=self.cons.queryListByIstat.format(self.getCapQuery())
			query+=" or tc_istat_id in("
			query+=self.combineIstat()
			query+=")"
			return query

		if(self.usesCap()):
			query=self.cons.queryListByIstat.format(self.getCapQuery())
			return query
		if(self.usesIstat()):
			q=" tc_istat_id in ("
			q+=self.combineIstat()
			q+=")"
			query=self.cons.queryListByIstat.format(q)
			return query
		
			
			
			
		
		return query
		
		
		