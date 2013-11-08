import MySQLdb
import psycopg2
#import pymssql
class cons():
	dbDrivers={'mysql':MySQLdb,'postgres':psycopg2}
	typeItem={'cap':'cap','pro':'provincia','com':'comune','reg':'regione','ope':'regione'}
	queryList="select distinct nome1, indirizzo,pv_id,cliente,cap,cod_cliente,comune,provincia,tel1,tel2,tel3,cf_pi from pv where {0} like '{1}'"
	def __getitem__(self,t):
		return self.typeItem
	attributes={'cap':1,'pro':2,'com':3,'reg':1}
	attributes2convert={'cap':False,'pro':True,'com':False,'reg':False}
	attributes2expand={'cap':False,'pro':False,'com':False,'reg':True}
	regione={'PIEMONTE':['TORINO','VERCELLI','NOVARA','CUNEO','ASTI','ALESSANDRIA','BIELLA','Verbano Cusio Ossola'],
'LOMBARDIA':['MONZA E DELLA BRIANZA','VARESE','COMO','SONDRIO','MILANO','BERGAMO','BRESCIA','PAVIA','CREMONA','MANTOVA','LECCO','LODI'],
'VENETO':['VERONA','VICENZA','BELLUNO','TREVISO','VENEZIA','PADOVA','ROVIGO'
],
'FRIULI VENEZIA GIULIA':['UDINE','GORIZIA','TRIESTE','PORDENONE'],
'LIGURIA':['IMPERIA','SAVONA','GENOVA','LA SPEZIA'],
'EMILIA ROMAGNA':['PIACENZA','PARMA','REGGIO NELL`EMILIA','MODENA','BOLOGNA','FERRARA','RAVENNA','FORLI-CESENA','RIMINI'],
'TOSCANA':['MASSA-CARRARA','LUCCA','PISTOIA','FIRENZE','LIVORNO','PISA','AREZZO','SIENA','GROSSETO','PRATO'],
'UMBRIA':['PERUGIA','TERNI'],
'MARCHE':['PESARO E URBINO','ANCONA','MACERATA','ASCOLI PICENO','FERMO'],
'LAZIO':['VITERBO','RIETI','ROMA','LATINA','FROSINONE'],
'ABRUZZO':['L`AQUILA','TERAMO','PESCARA','CHIETI'],
'MOLISE':['CAMPOBASSO','ISERNIA'],
'CAMPANIA':['CASERTA','BENEVENTO','NAPOLI','AVELLINO','SALERNO'],
'PUGLIA':['BARLETTA-ANDRIA-TRANI','FOGGIA','BARI','TARANTO','BRINDISI','LECCE'],
'BASILICATA':['POTENZA','MATERA'],
'CALABRIA':['COSENZA','CATANZARO','REGGIO DI CALABRIA','CROTONE','VIBO VALENTIA'],
'SICILIA':['TRAPANI','PALERMO','MESSINA','AGRIGENTO','CALTANISSETTA','ENNA',
'CATANIA','RAGUSA','SIRACUSA'],
'SARDEGNA':['OLBIA - TEMPIO','OGLIASTRA','CARBONIA - IGLESIAS','MEDIO CAMPIDANO','SASSARI','NUORO','CAGLIARI','ORISTANO'],
"VALLE D'AOSTA":['Aosta'],
"TRENTINO ALTO ADIGE":['TRENTO','BOLZANO']} 
		

