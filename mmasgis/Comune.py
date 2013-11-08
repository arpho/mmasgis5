from Utb import Utb

"""
astrae le utb di tipo provincia
"""
class Comune(Utb):
	
	def __init__(self,header="header",istat=-1):
		Utb.__init__(self, header, 'com', istat)
		
	def getSelect(self):
		query=" select tc_comune_id from mmasgisDB.comuni where codice={0}".format(self.istat)
		return query
	
	def __repr__(self):
		return "utb comune: {0},istat:{1}".format(self.header,self.istat)
	
	def usesIstat(self):
		return True
	
	def usesCap(self):
		return False