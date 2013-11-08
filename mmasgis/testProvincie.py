import MySQLdb 

def translateProvincia(pr):
		db = MySQLdb.connect(host="localhost", user="root", passwd="vilu7240",db="test")
		crs=db.cursor()
		query="select sigla from provincia where provincia like '{0}'".format(pr)
		crs.execute(query) 
		sigla=crs.fetchone()[0]
		return sigla
		db.close

print translateProvincia('catania')

