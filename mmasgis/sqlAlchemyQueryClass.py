from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker

echo=False

#def __init__(self):
Base = declarative_base()

class Query(Base):
	""""""
	__tablename__ = "queries"
 
	id = Column(Integer, primary_key=True)
	nome = Column(String)
	descrizione = Column(String)
	censimento= Column(String)
 
	#----------------------------------------------------------------------
	def __init__(self, nome, descrizione, censimento):
		"""Constructor"""
		self.nome = nome
		self.descrizione = descrizione
		self.censimento= censimento
 
	def __repr__(self):
		return "Query('%s','%s', '%s')" % (self.nome, self.descrizione,self.censimento, self.id)
 
class Parametro(Base):
	"""
	Address Class
 
	Create some class properties before initilization
	"""
	__tablename__ = "parametri_mmas"
	id = Column(Integer, primary_key=True)
	parametro_id=Column(Integer)
	category = Column(Integer)
	query_id = Column(Integer, ForeignKey('queries.id'))
 
	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	user = relation(Query, backref=backref('parametri_mmas', order_by=id))
 
	#----------------------------------------------------------------------
	def __init__(self,query, category,parametro_id):
		"""Constructor"""
		self.category=category
		self.parametro_id=parametro_id
		self.query_id=query
 
	def __repr__(self):
		return "<parametro({0}-{1})>".format(self.category,self.parametro_id)
	

	

	
class Marchi(Base):
	"""
	Address Class
 
	Create some class properties before initilization
	"""
	__tablename__ = "marchi" 

	id = Column(Integer, primary_key=True,autoincrement=True)
	marchio_id=Column(Integer, nullable=False)
	category = Column(Integer, nullable=False)
	query_id = Column(Integer, ForeignKey('queries.id'))
 
	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	user = relation(Query, backref=backref('marchi', order_by=id))
 
	#----------------------------------------------------------------------
	def __init__(self,query, category,marchio_id):
		"""Constructor"""
		self.category=category
		self.query_id=query
		self.marchio_id=marchio_id
 
	def __repr__(self):
		return "<marchio(%d-%d)>" % (self.category,self.marchio_id)
 
 
class Potenziale(Base):
	"""
	Address Class
 
	Create some class properties before initilization
	"""
	__tablename__ = "potenziali"
	id = Column(Integer, primary_key=True,autoincrement=True)
	potenziale_id=Column(Integer, nullable=False)
	category = Column(Integer, nullable=False)
	query_id = Column(Integer, ForeignKey('queries.id'))
 
	# creates a bidirectional relationship
	# from Address to User it's Many-to-One
	# from User to Address it's One-to-Many
	user = relation(Query, backref=backref('potenziali', order_by=id))
 
	#----------------------------------------------------------------------
	def __init__(self,query, category,potenziale_id):
		"""Constructor"""
		self.category=category
		self.potenziale_id=potenziale_id
		self.query_id=query
 
	def __repr__(self):
		return "<potenziale({0}-{1})>".format(self.category,self.potenziale_id)
