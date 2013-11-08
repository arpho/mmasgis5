import MySQLdb
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
class cons():
	dbDrivers={'mysql':MySQLdb,'postgresql':psycopg2}
	typeItem={'cap':'cap','pro':'provincia','com':'comune','reg':'regione','ope':'regione'}
	queryList=unicode("select distinct nome1, indirizzo,pv_id,cliente,cap,cod_cliente,comune,provincia,tel1,cod_mmas,tel3,cf_pi from pv where {0} like '{1}'")
	queryListByIstat=unicode("select  nome1, indirizzo,pv.pv_id,cliente,cap,cod_cliente,comune,provincia,tel1,cod_mmas,tel3,cf_pi,(case rel_pv_pot.tc_clpot_id when 1 then rel_pv_pot.valore else null end) AS potenziale from pv left JOIN rel_pv_pot ON pv.pv_id = rel_pv_pot.pv_id  where  {0} order by nome1 desc")
	istatList=unicode(" SELECT tc_istat_id FROM mmasgisDB.tc_istat JOIN mmasgisDB.regioni ON tc_istat.tc_regione_id = regioni.tc_regione_id WHERE regioni.codice = {0} ")

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
		

