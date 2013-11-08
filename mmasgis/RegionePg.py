from Utb import Utb

"""
astrae le utb di tipo regione
"""
class RegionePg(Utb):
	
	def __init__(self,header="header",istat=-1):
		Utb.__init__(self, header, 'reg', istat)
		
	def getSelect(self):
		query=" SELECT tc_istat_id FROM tc_istat JOIN regioni ON tc_istat.tc_regione_id = regioni.tc_regione_id WHERE regioni.codice = {0}".format(self.istat)
		return query
		
	def __repr__(self):
		return "utb regione for postgres: {0},istat:{1}".format(self.header,self.istat)
	
	def usesIstat(self):
		return True
	
	def usesCap(self):
		return False