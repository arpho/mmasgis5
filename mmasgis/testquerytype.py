import MySQLdb
from constants import cons
from MySQLdb.constants import FIELD_TYPE
my_conv = { FIELD_TYPE.LONG: int }
cons=cons()
field_type = {
 0: 'DECIMAL',
 1: 'TINY',
 2: 'SHORT',
 3: 'LONG',
 4: 'FLOAT',
 5: 'DOUBLE',
 6: 'NULL',
 7: 'TIMESTAMP',
 8: 'LONGLONG',
 9: 'INT24',
 10: 'DATE',
 11: 'TIME',
 12: 'DATETIME',
 13: 'YEAR',
 14: 'NEWDATE',
 15: 'VARCHAR',
 16: 'BIT',
 22:'LONG',
 33:'long',
 100:'STRING',
 'pv_id':'string',
 'cliente':'boolean',
 'cap':'string',
 'cod_cliente':'long',
 50:'Boolean',
 246: 'NEWDECIMAL',
 247: 'INTERVAL',
 248: 'SET',
 249: 'TINY_BLOB',
 250: 'MEDIUM_BLOB',
 251: 'LONG_BLOB',
 252: 'BLOB',
 253: 'VAR_STRING',
 254: 'STRING',
 255: 'GEOMETRY',
 'nome1':'STRING',
 'indirizzo':'STRING' }

tipo='comune'
area='giarre'
def field2Type(t):
	print t
	return field_type[t]
def tupleTranslation(t):
	t1=[]
	for i in t:
		t1.append(field2Type(i))
	return t1
def descriptionConverter(rs):
	listaTipi=[]
	for i in rs:
		listaTipi.append(tupleTranslation(i))
	return listaTipi
def test(crs):
	print crs.execute("describe pv")
query=cons.queryList.format(tipo,area)
print query
db = MySQLdb.connect(host="localhost", user="root", passwd="vilu7240",db="parafarmacie")
crs=db.cursor()
crs.execute(query)
print crs.description
description=crs.description
#print descriptionConverter(description)
print len(crs.description)
print field2Type(254)
print tupleTranslation([254,255,246])
q=crs.fetchone()
types = [type(col) for col in q]
print q
print types
