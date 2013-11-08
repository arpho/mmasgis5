from pvListQueryBuilderBase import PvListQueryBuilderBase
class PvListQueryBuilderMysql(PvListQueryBuilderBase):
	def __init__(self,utbs,db):
		PvListQueryBuilderBase.__init__(self, utbs)
		self.db=db.getConnection()
		
	def getIstatList(self,query):
		self.db.execute(query)
		l= self.db.fetchall()
		