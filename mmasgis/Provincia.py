from Utb import Utb

"""
astrae le utb di tipo provincia
"""
class Provincia(Utb):
	
	def __init__(self,header="header",istat=-1):
		Utb.__init__(self, header, 'pro', istat)
		
	def getSelect(self):
		query=" SELECT tc_istat_id FROM mmasgisDB.tc_istat JOIN mmasgisDB.province ON tc_istat.tc_provincia_id = province.tc_provincia_id WHERE province.codice = {0}".format(self.istat)
		return query
	
	def __repr__(self):
		return "utb provincia: {0},istat:{1}".format(self.header,self.istat)
		
	def usesIstat(self):
		return True
	
	def usesCap(self):
		return False