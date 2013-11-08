from utility import *

util=utility([],0)
dicto=open("dict.py",'a')
dicto.write("regione={")
def writeList(regione,t):
	
	l= "'{0}':{1},".format(regione,str(t))
	dicto.write(l)
#print util.getRegioneId_sql("SICILIA")
lista= util.getRegioni()
for i in lista:
	provincie=util.regionExpander(i)
	writeList(i,provincie)


