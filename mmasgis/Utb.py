"""
classe base per la rappresentazione delle utb per generare le  query per la lista dei pv
"""
class Utb:
	def __init__(self, header, type, istat):
		self.header=header
		self.type=type
		self.istat=istat
		
	def getHeader(self):
		return self.header
	
	def getType(self):
		return self.type
	
	def getIstat(self):
		return self.istat
	def __repr__(self):
		return "utb: {0}".format(self.header)