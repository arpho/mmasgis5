from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from sqlAlchemyQueryClass import *
#from sqlalchemy import *

class DbQueries():
	"""
	questa classe gestisce le operazioni di interrogazione al dbQueries.sql
	"""
	def __init__(self,db):
		#engine = create_engine("sqlite:///dbQueries.sql", echo=echo)
		dbfile="metmi:metmi@{0}:{1}/mmasgisdb".format(db.getHost(),db.getPort())
		engine = create_engine("mysql+mysqldb://"+dbfile+"?charset=utf8&use_unicode=1",convert_unicode=True)
		#metadata = BoundMetaData(engine)
		#metadata.create_all()
		Session = sessionmaker(bind=engine)
		self.session = Session()
		self.insertFunctions={}
		self.insertFunctions['parametri']=self.insertParametri
		self.insertFunctions['marchi']=self.insertMarchi
		self.insertFunctions['potenziali']=self.insertPotenziale
	"""
	def test1(self):
		q=Query("test sqlAlchemy entity", " this is a test of Query inserted by queriesDb")
		self.session.add(q)
		self.session.flush()
		print q.id
	"""
	def insertParametri(self,query_id,l):
		"""
		inserisce una lista di parametri  per una query specifica va chiamato
		 da insertQuery che provvede al commit
		 @param query_id: Integer 
		 @param l:	[(category:Integer,parametro_id:Integer)]
		 @return: None
		"""
		for i in l:
				print "inserisco parametro {0} per query: {1}".format(i,query_id)
				self.session.add(Parametro(query_id,i[0],i[1]))
		  #  self.session.commit()
	def getFullQuery(self,queryId):
		"""
		recupera tutti i campi di una query
		@param queryid:	Integer
		@return: {'potenziali':[(category,potenziale_id)],'marchi':[(category,marchio_id)],'parametri':[(category,parametro_id)]}
		@note: ex getFieldsQuery
		"""
		fields={}
		fields['parametri']=self.getParametri(queryId)
		fields['marchi']=self.getMarchi(queryId)
		fields['potenziali']=self.getPotenziali(queryId)
		return fields
			
	def insertPotenziale(self,query_id,l):
		"""
		inserisce una lista di potenziali  per una query specifica va chiamato
		 da insertQuery che provvede al commit
		 @param query_id: Integer 
		 @param l:	[(category:Integer,potenziale_id:Integer)]
		 @return: None
		"""
		for i in l:
			print "inserisco potenziale {0} per query: {1}".format(i,query_id)
			self.session.add(Potenziale(query_id,i[0],i[1]))
			#self.session.commit()
			
	def insertMarchi(self,query_id,l):
		"""
		inserisce una lista di marchi  per una query specifica, va chiamato
		 da insertQuery che provvede al commit
		 @param query_id: Integer 
		 @param l:	[(category:Integer,marchio_id:Integer)]
		 @return: None
		"""
		for i in l:
			print "inserisco marchio {0} per query: {1}".format(i,query_id)
			self.session.add(Marchi(query_id,i[0],i[1]))
			#self.session.commit()

	def commitQuery(self):
		"""
		esegue il commit  su queryDb
		"""
		self.session.commit()
		
	def insertQuery1(self,nome,descr,censimento):
		"""
		inserisce una query nella tabella queries
		@param nome: String
		@param param: String  
		@return: None
		"""
		q=Query(nome,descr,censimento)
		self.session.add(q)
		self.session.commit()
	
	def insertQuery(self,nome,descrizione,censimento):
		"""
		opera il preinserimento della query,
		 cioe' non esegue il commit della query, a semplicemente il flush, per conoscere lo id della nuova query
		 
		inserisce una query con le sue liste di parametri, marchi e potenziali nel db 
		@param nome: String
		@param descrizione: String
		@return: int query_id
		"""
		#genero la nuova query
		q=Query(unicode(nome),unicode(descrizione),unicode(censimento))
		self.session.add(q)
		#devo ricavare lo id di questa query quindi 
		self.session.flush()
		query_id=q.id
		# non ho ancora committato pero' ho lo id di q
		# aggiungo i campi
		#scorro la lista dei parametri
		#for key in lista.iterkeys():
			#eseguo la funzione relativa alla chiave
		 #   self.insertFunctions[key](q.id,lista[key])
		#confermo le modifiche al db
		#self.session.commit()
		# chiudo la sessione
		#self.session.close()
		return query_id
		
		
		
	def getParametri(self,queryId):
		"""
		recupera i parametri relativi ad una query
		@param queryId:	String
		@return: [(Parametro.category,Parametro_id.potenziale_id)]
		"""
		p=[]
		for pa in self.session.query(Parametro).filter_by(query_id=queryId):
			p.append((pa.category,pa.parametro_id))
		return p
	def getMarchi(self,queryId):
		"""
		recupera i marchi relativi ad una query
		@param queryId:	String
		@return: [(Marchi.category,Marchi.potenziale_id)]
		"""
		p=[]
		for pa in self.session.query(Marchi).filter_by(query_id=queryId):
			p.append((pa.category,pa.marchio_id))
		return p
	def getPotenziali(self,queryId):
		"""
		recupera i potenziali relativi ad una query
		@param queryId:	String
		@return: [(Potenziale.category,Potenziale.potenziale_id)]
		"""
		p=[]
		for pa in self.session.query(Potenziale).filter_by(query_id=queryId):
			p.append((pa.category,pa.potenziale_id))
		return p
	def getQueries(self):
		"""
		ritorna la lista di tutte le queries presenti nel db
		@return: [Query]
		"""
		p=[]
		for pa in self.session.query(Query):
			p.append(pa)
		return p
	def getQueryById(self,queryId):
		"""
		recupera una query dato lo id
		@param queryId: Integer
		@return: Query 
		"""
		p=[]
		for pa in  self.session.query(Query).filter_by(id=queryId):
			p.append(pa)
			# lo id e' univoco ottero' un solo oggetto 
			#lo estraggo dalla lista
			# non posso return self.session.query(etc.
			# perche' ottengo la query per oscuri motivi
			# noltre cosi' e' piu' chiaro
		return p[0]
		
#
