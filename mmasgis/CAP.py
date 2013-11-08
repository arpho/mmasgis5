from Utb import Utb

"""
astrae le utb di tipo provincia
"""
class CAP(Utb):
	
	def __init__(self,header="header",istat=-1):
		Utb.__init__(self, header, 'reg', istat)
		
	def getSelect(self):
		query="cap={0}".format(self.istat)
		return query
		
	def __repr__(self):
		return "utb cap: {0}".format(self.header)
	
	def usesIstat(self):
		return False
	
	def usesCap(self):
		return True