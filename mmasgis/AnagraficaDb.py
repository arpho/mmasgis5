#!/usr/bin/env python
# -*- coding: latin-1 -*-
from mysql_sqlalchemy_class import *
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
from collections import OrderedDict
#from mysqlEntities import *
from elixir import *
from sqlalchemy import *
from sqlalchemy import and_
from sqlalchemy.engine.url import URL
"""
import sys
sys.path.append("C:\Users\giuseppe\AppData\Local\Aptana Studio 3\plugins\org.python.pydev_2.7.0.2012080220\pysrc")
from pydevd import *
"""
class Odict(dict):
	"""
	implementa un' ordered dict estendendo la classe dict
	crea una lista che memorizza le chiavi inserite nel dict  con lo stesso ordine di inserimento
	"""
	def __init__(self):
		self.order=[]

	def clear(self):
		"""
		override del metodo clear
		"""
		dict.clear(self)
		self.order=[]

	def __setitem__(self, key, value):
		"""
		override di __setitem__
		oltre alle normali operazioni di __setitem__ inserisce le chiavi in self.order
		@param key: come in dict
		@param value:come in dict
		"""
		#aggiungo le chiavi nell'ordine di inserimento
		self.order.append(key)
		dict.__setitem__(self, key, value)
	def iterkeys(self):
		"""
		override del metodo iterkeys invece dell'iteratore di dict ritorna la lista delle chiavi
		"""
		return self.order

class toText():
	"""
	classe  usata da Dummy perche' possa funzionare come i mapper di sqlalchemy,
	 cioe' l'istruzione mapper.nome_campo, ritorna il valore del campo  di una riga della tabella mappata
	@param string: testo che ritornera' Dummy.testo
	"""
	def __init__(self,txt):
		self.testo=txt

	def __repr__(self):
		"""
		override di __repr__ ritorna il parametro passato al costruttore
		"""
		return self.testo

class Dummy():
	"""
	classe di comodo, usata per 'riempire' i parametri mancanti o bloccati cioe' con tc_stato_id=0,
	 contiene il solo parametro testo, ma soprattutto ha il metodo testo, un getter del parametro passato al costruttore di Dummy
	  implementato in modo che possa essere invocato come Dummy.testo, cioe' allo stesso modo in
	   cui si invocano i campi del  mapper di sqlalchemy

	@note: questo e' possibile perche' instanzio un oggetto toText(string)  chiamato testo, cosi' che l'istruzione Dummy.testo invoca
	 il metodo __repr__ di toText
	"""
	testo=""
	def __init__(self,t):
		"""
		@param string: testo del dummy
		"""
		#self.text= t
		self.testo=toText(t)
		self.valore=toText(t)

	def testo(self):
		return self.testo

class tableDb():
	"""
	questa classe gestisce la connessione al db tramite sqlalchemy per la tabella di anagrafica,
	 contiene tutti i metodi per il retrieving dei dati dal db, la loro elaborazione in un formato compatibile con le tab di anagrafica
	"""

	def fetchOnePv(self):
		"""recupera il primo pv dal db
		serve per ottenere le entità disponibili per le esportazioni
		@return:istanza di sqlAlchemy per pv
		"""
		return self.session.query(Pv).all()[0]


	def getPvById(self, Id):
		"""
		@param Id: int id del pv
		@return {'ragione sociale':string,'indirizzo':string,'Id':int,'cap':string,'cod_cliente':string,...}
		"""
		p=[]
		for i in self.session.query(Pv).filter_by(pv_id=Id):
			d=Odict()
			d['cod_mmas']=i.cod_mmas
			d['ragione sociale']=i.ragione_sociale
			d['indirizzo']=i.indirizzo
			d['id']=i.pv_id
			d['cliente']=i.cliente
			d['cap']=i.cap
			d['cod_cliente']=i.cod_cliente
			d['comune']=i.comune
			d['provincia']=i.provincia
			d['telefono1']=i.tel1
			d['telefono2']=i.tel2
			d['telefono3']=i.tel3
			d['cf']=i.cf_pi
			d['potMMAS']=self.getPotentialValueById(Id).valore
			p.append(d)
		return p[0]

	def fetchPv(self,Id):
		"""
		recupera il pv relativo allo Id memorizzato in self.pv_id
		@param int:
		@return
		"""
		p=[]
		for i in  self.session.query(Pv).filter_by(pv_id=Id):
			p.append(i)
		return p[0]

	def getPotentialValueById(self,Id):
		l=[]
		for q in self.session.query(rel_pv_pot).filter_by(pv_id=Id).filter_by(tc_clpot_id=1):

			l.append(q)
		if len(l)==0:
			d=Dummy("")
			l.append(d)
		return l[0]

		def getPotentialById(self,Id):
			"""
			recupera l'oggetto tc_clpot relativo allo id Id, cioe' recupera la classe potenziale (esteso,mmas)
			@param int:id del parametro richiesto
			@return: :tc_clpot
			"""

		#t=.tc_clpar_id
		for q in self.session.query(tc_clpot).filter_by(tc_clpot_id=Id):
			r=q
		return r

	def brandsAdapter(self,l):
		"""
		converte la lista ottenuta da putBrands in self.util.getBrands4class_pv
		in una lista di Odict
		@param l: [string]
		@return:[Odict] con chiavi marche e Id
		@note: Id e' un campo dummy
		"""
		li=[]
		for i in l:
			d={}
			d['marche']=i['brand']
			d['Id']=i['Id']
			li.append(d)
		return li

	def putBrands(self,li):
		"""
		sostituisce gli id dei brands nella lista in input ottenuta da getBrands4class_pv con i  nomi dei rispettivi brands
		@param [int]:[rel_pv_mar.tc_mar_id]
		@return: {'brand':tc_mar.testo,'Id':brand_id}]
		"""
		lo=[]
		for i in li:
			brand={}
			brand['brand']=self.getBrand(i)[0]
			brand['Id']=i
			lo.append(brand)
		return lo

	def initDB(self,dbfile):
		"""
		@param string:stringa di connessione al db, con il seguente formato di stringa "user:pwd@host/nomedb" esempio root:xxxxx@localhost/parafarmacie
		inizializza il db
		"""
		metadata.bind = "mysql://%s"%dbfile
		metadata.bind.echo = False
		setup_all()

	def fetchPotentials(self,Id):
		"""
		legge dal db i valori dei potenziali relativi ad un pv dato il suo pv_id
		ritorna la lista di valori da riportare sulla tabella di anagrafica
		@note: la lista  puo' essere utilizzata direttamente dalla tabella di anagrafica
		 perche' gia' convertita da translateDict
		@param int: pv_id  id del punto vendita
		@return  [{string:string,string:string,string:string}]::[{'classe':tc_clpot,'valore':float,'Id':Int}]
		@note:  la chiave Id nel dict serve per compatibilita' con la lista dei marchi, infatti nel tab relativo
		ai marchi ci sono due tabelle correlate dallo id della classe, che deve quindi essere riportato
		"""
		d= self.mergePotentials(Id)
		return self.translateDict(d)

	def fetchValue4Extraction(self,tab,Id):
		""" wrapper di fetchValue4Brands e fetchValue4Parameters
		ritorna il valore relativo al campo da estrarre
		@param int: class_id
		@param string:tab e' usato per discriminare tra le due funzioni da usare valori ammessi: 'marche' e 'parametri'
		"""
		fetcher={}
		fetcher['marche']=self.fetchValue4Brands
		fetcher['parametri']=self.fetchValue4Parameters
		return fetcher[tab](Id)

	def fetchValue4Brands(self,Id):
		"""ritorna il testo della marca, ottenuto interrogando la tabella tc_mar
		@param int:tc_mar_id
		@return: string
		"""
		l=[]
		for i in self.session.query(tc_mar).filter_by(tc_mar_id=Id):
			l.append(unicode(i.testo))
		return l

	def fetchParameters4Pv(self,Id,class_id):
		"""
		ritorna il parametro assegnato alla classe class_id per il pv con pv_id Id
		@param int: pv_id
		@param int: class_id
		@return: string
		"""
		r=[]
		for i in self.session.query(rel_pv_par).filter_by(pv_id=Id).filter_by(tc_clpar_id=class_id):
			r.append(i.tc_par_id)
		if len(r)==0:
			return self.fetchValue4Parameters(-1)#non esiste questo parametro per pv quindi tornerà []
		else:
			return self.fetchValue4Parameters(r[0])

	def fetchBrands4Pv(self,Id,class_id):
		"""
		ritorna le marche  trattate per la classe  class_id dal pv con pv_id Id
		@param int: pv_id
		@param int: class_id
		@return: string
		"""
		class_id
		r=[]
		for i in self.session.query(rel_pv_mar).filter_by(pv_id=Id).filter_by(tc_clmar_id=class_id):
			r.append(unicode(self.fetchValue4Brands(i.tc_mar_id)[0]))
		return r

	def fetchValue4Pv(self,tab,Id,class_id):
		"""
		wrapper di fetchValue4Parameters e fetchValue4Brands
		@param string: distigue quale delle due funzioni usare, valori ammessi: 'marche','parametri'
		@return: string
		"""
		fetcher={}
		fetcher['marche']=self.fetchBrands4Pv
		fetcher['parametri']=self.fetchParameters4Pv
		return fetcher[tab](Id,class_id)

	def fetchValue4Parameters(self, class_id):
		"""ritorna il testo del parametro, ottenuto interrogando la tabella tc_par
		@param int:tc_par_id
		@return: string
		"""
		l=[]
		for i in self.session.query(tc_par).filter_by(tc_par_id=class_id):
			l.append(unicode(i.testo))
		return l


	def classBrandsRetriever(self):
		"""
		interroga il db per ottenere la lista delle classi dei marchi ordinate secondo il campo ordine della tabella tc_clmar
		@return: [ tc_clmar]
		"""
		l=[]
		for c in self.session.query(tc_clmar).all():
			l.append(c)
		return l
	def toText(self,t):
		"""
		traduce in stringa 'attivo'o  'non attivo' il valore del campo tc_stato_id
		@param t:int
		@return: string
		"""
		if t==1:
			return 'attivo'
		else:
			return 'non attivo'

	def outputFormatter(self,li):
		"""
		formatta la lista generata da classBrandRetriever in una lista accettabile da populatetable di utility.py
		@param li::[ tc_clmar]
		@return: [{string:string,string:string,string:Int}]::[{'classe marca':tc_clmar.testo,'stato':self.toText(tc_clmar.tc_stato_id):'Id':tc_clmar_id}]
		@note: ritorna una lista di Odict con le chiavi suddette
		"""
		lo=[]
		for i in li:
			d=Odict()
			d['classe marca']=unicode(i.testo)
			#d['stato']=self.toText(i.tc_stato_id)
			d['Id']=i.tc_clmar_id
			lo.append(d)
		return lo

	def fetchBrands(self,dummy):
		"""
		combina i  metodi classBrandsRetriever e outputFormatter per generare la lista da
		 fornire a populateTable in utility.py
		@param dummy: e' un parametro dummy per rendere la signature di questo metodo  uguale a quella degli altri fetchers
		@return:[({string:string,string:string},tc_clmar_id)]::[({'classe marca':tc_clmar.testo,'stato':self.toText(tc_clmar.tc_stato_id)},tc_clmar_id)]
		@note: ritorna una lista di Odict con le chiavi suddette
		"""
		li= self.classBrandsRetriever()
		lo= self.outputFormatter(li)
		return lo

	def getBrand(self,Id):
		"""
		ritorna il nome del brand relativo al tc_mar_id passato come parametro
		@param int: id del brand
		@return: (string,int)::(tc_mar.testo,tc_mar.tc_stato_id)
		"""
		brand=[]
		for b in self.session.query(tc_mar).filter_by(tc_mar_id=Id):
			brand.append(b)
		return (brand[0].testo,brand[0].tc_stato_id)

	def getBrands4class_pv(self,id_class,Id):
		"""
		interroga la tabella rel_pv_mar per conoscere gli id dei brands relativi alla classe id_class trattati da pv_id

		@param id_class:int id della classe marca
		@param Id: int id del pv
		@return: [int]::[(rel_pv_mar.tc_mar_id]
		"""
		lb=[]
		#print "pv_id: {0}, class_id:{1}".format(Id,id_class)
		for i in self.session.query(rel_pv_mar).filter_by(pv_id=Id).filter_by(tc_clmar_id=id_class).order_by(rel_pv_mar.ordine):
			lb.append(i.tc_mar_id)
		return lb

	def getBrands4Extraction(self):
		"""
		ritorna la lista delle classi marche disponibili per l'estrazione
		@note: interroga il db tramite sqlalchemy quindi usa il mapper tc_clmar
		@attention: ritorna solo quei parametri il cui tc_stato_id e' pari a 1, ordinati secondo il campo ordine di tc_clmar
		@return: [{string:string,string:int}]::[{'header':testo,'Id':class_id}]
		"""
		l=[]
		for i in self.session.query(tc_clmar).order_by(tc_clmar.ordine).filter_by(tc_stato_id=1):
			d={}
			d['header']=i.testo
			d['Id']=i.tc_clmar_id
			l.append(d)
		return l

	def getAllParameters(self):
		"""
		ritorna la lista dei parametri disponibili presenti nella tabella tc_clpar
		insieme con il loro id, ordine secondo il campo ordine
		@return: [{string:string,string:int}]:[{header:class_id}
		"""
		l=[]
		for i in self.session.query(tc_clpar).order_by(tc_clpar.ordine).all():
			if i.tc_stato_id==1:
				d={}
				d['header']=unicode(i.testo)
				d['Id']=i.tc_clpar_id
				l.append(d)
		return l

	def getHeader4Marche(self,Id):
		"""
		ritorna lo header della marca avente tc_clmar_id =Id
		@param class_id:int
		@return: string
		"""
		l=[]
		for i in self.session.query(tc_clmar).filter_by(tc_clmar_id=Id):
			l.append(i)
		return unicode(l[0].testo)

	def getHeader(self,tab,class_id):
		"""
		wrapper di getHeader4marche e getHeader4parametri
		ritorna lo header relativo a claas_id per i tab 'marche' o 'parametri'
		@param tab:string <'marche'>,<'parametri'>
		"""
		getHeader={}
		getHeader['marche']=self.getHeader4Marche
		getHeader['parametri']=self.getHeader4Parametri
		return getHeader[tab](class_id)

	def getHeader4Parametri(self,Id):
		"""
		ritorna lo header del parametro avente tc_clpar_id =Id
		@param class_id:int
		@return: string
		"""
		l=[]
		for i in self.session.query(tc_clpar).filter_by(tc_clpar_id=Id):
			l.append(i)
		return unicode(l[0].testo)

	def fetchParameters(self,Id):
		"""
		recupera le coppie parametro-valore  per un pv dato il suo id
		@param int: id del pv
		@return: [{'parametro':string,'valore':string,'Id':int}]:: [{'parametro':tc_clpar.testo,'valore':,'Id':int}]
		@note: il campo Id nel dizionario di uscita serve solo a uniformare il formato di output con quello di fetchBrands
		"""
		r=self.getQuestionsAndParameters(Id)
		a=self.makeDigest(self.getAllQuestions())
		b=self.makeDigest(r)
		c= self.difference(b, a)
		d=self.dummyGenerators(c)
		cl= self.putAllTogether(d,r)
		#print "param di sorter: {0}".format(cl)
		cl1=self.sorter(cl)
		#print "prodotto di sorter: {0}".format(cl1)
		return self.dictConverter(cl1)

	def ricerca(self,w):
		l=[]
		for i in self.session.query(Pv).filter(Pv.ragione_sociale.op('regexp')('[[:<:]]{0}[[:>:]]'.format(w))).all():
			l.append((i.ragione_sociale,i.pv_id,i.comune,i.cod_cliente,i.cod_mmas))
		return l

	def ricercaContiene(self,w):
		l=[]
		for i in self.session.query(Pv).filter(Pv.ragione_sociale.like("%{0}%".format(w))).all():
			l.append((i.ragione_sociale,i.pv_id,i.comune,i.cod_cliente,i.cod_mmas))
			return l

	def ricercaAnd(self,l,wholeWord=False,caseSensitive=False):
		"""
		ritorna i pv che corrispondono ai parametri richiesti
		@param {string:string}::{chiave di ricerca:'valore'}:definisce i campi di ricerca su cui fare lo and chiavi
		@note:  le chiavi sono <'ragione_sociale'>,<'comune'>,<'codice_cliente'>,<'codice_mmas'>
		@param bool opzionale: ricerca parole intere se True ritorna quei punti vendita che possiedono almeno un'occorrenza del termine cercato, se False ricerca il match perfetto
		@return: {int:""}::{pv_id:""}
		"""
		clauses=[]
		columns={}
		rs={}
		columns["ragione_sociale"]=Pv.ragione_sociale
		columns["comune"]=Pv.comune
		columns["codice_cliente"]=Pv.cod_cliente
		columns["codice_mmas"]=Pv.cod_mmas
		for k in l.iterkeys():
			if wholeWord:
				clauses.append(columns[k].op('regexp')('[[:<:]]{0}[[:>:]]'.format(l[k])))
			else:
				clauses.append(columns[k].like("%{0}%".format(l[k])))
		conditions=and_(*clauses)
		for i in self.session.query(Pv).filter(conditions).all():
			rs[i.pv_id]=""
		return rs

	def closeSession(self):
		self.session.close()

	def __init__(self,user,db):
		#mysql://username:password@localhost/mydb
		self.db=db
		dbfile=self.db.getConnectionString()
		self.user=user
		#self.initDB(dbfile)
		url = URL(drivername=db.getRDBMS(), username='metmi', password='metmi', host=db.getHost(),port=str(db.getPort()), database=db.getCensimento())
		engine = create_engine(url,convert_unicode=True,encoding='latin1')
		Session = sessionmaker(bind=engine)
		self.session=Session()
		self.questionsList=self.retrieveAllQuestions()
		self.potentialsList=self.retrieveAllPotentials()
		#dizionario dei  fetchers
		self.fetchers={}
		self.fetchers['marca']=self.fetchBrands
		self.fetchers['parametro']=self.fetchParameters
		self.fetchers['potenziale']=self.fetchPotentials

	def fetchData(self,k,Id):
		"""
		genera gli item per la tabella designata dalla chiave k per il pv il cui pv_id e' passato in Id
		@param k:string::['marca','parametro','potenziale']
		@return:k='marca'| [{string:string,string:string,string:Int}]::[{'classe marca':tc_clmar.testo,'stato':self.toText(tc_clmar.tc_stato_id):'Id':tc_clmar_id}]
		@return: k='parametro' | [{'parametro':string,'valore':string,'Id':int}]
		@return: k='potenziale'| [{string:string}]::[{'classe':tc_clpot,'valore':float,'Id':int}]
		@note: eccetto che nel caso marca il campo Id nel dizionario non ha nessun valore, ma l'unica funzione di uniformare il formato dei valori di uscita

		"""
		data= self.fetchers[k](Id)
		return data

	def dictConverter(self,lp):
		"""
		ultimo step del processo per produrre  un output compatibile con anagrafica
		data una lista di dizionari contenenti i mapper di tc_par e tc_clpar produce una lista di
		dizionari i cui valori sono il campo testo nei mapper
		@param lp:[{'parametro':tc_clpar,'valore':tc_par/Dummy}]
		@return :[{'parametro':string,'valore':string:'Id':int}]
		@note lo Id ritornato serve solo per uniformare il formato di uscita con quello di fetchBrands non ha un vero significato
		"""
		l=[]
		for e in lp:
			d=Odict()
			d['parametro']=e['parametro'].testo
			d['valore']=unicode(e['valore'].testo)
			#d['Stato']=e['Stato']
			d['Id']=-1
			l.append(d)
		return l

	def getAllQuestions(self):
		"""
		e' il getter per la lista di tutti i parametri di pertinenza con il punto vendita, questa lista
		 e' generata nel momento in cui l'oggetto tableDb e' instanziato e memorizzata in self.questionList
		 @return: {int:{string:mysql_sqlalchemy_class.tc_clpar}}: {tc_clpar_id:{'parametro':mysql_sqlalchemy_class.tc_clpar}}
		"""
		return self.questionsList

	def dummyGenerators(self,l):
		"""
		genera la lista dei parametri non dichiarati che verra' aggiunta alla lista dei parametri forniti dal pv
		@note: genera un dict in out
		@param [int]:[tc_cl_par_id]
		@return: {int{'parametro':tc_clpar,'valore':Dummy}}:{tc_clpar_id{'parametro':tc_clpar,'valore':Dummy}}
		"""
		dummy=Dummy("")
		d={}
		for i in l:
			d[i]={'parametro':self.filterTcClPar(i),'valore':dummy}#,'Stato':self.isParameterActive(i)}
		return d

	def putAllTogether(self,dl,pl):
		"""
		mette assieme il dict dei parametri dichiarati con quello dei parametri dummy
		"""
		for k in dl.iterkeys():
			pl[k]=dl[k]
		return pl


	def difference(self,a, b):
		""" show whats in list b which isn't in list a
		@param a,b: lista generica nello specifico {int:{string:tc_clpar}} {tc_clpar_id:{'parametro':tc_clpar','valore':string}}
		@return [tc_clpar_id]
		"""
		return list(set(b).difference(set(a)))

	def getQuestionById(self,Id):
		"""
		recupera l'oggetto tc_clpar relativo allo id Id
		@param int:id del parametro richiesto
		@return: {'parametro':tc_clpar}
		"""
		r={}
		#t=.tc_clpar_id
		for q in self.session.query(tc_clpar).filter_by(tc_clpar_id=Id):
			r['parametro']=q
		return r

	def getPotentialById(self,Id):
		"""
		recupera l'oggetto tc_clpot relativo allo id Id, cioe' recupera la classe potenziale (esteso,mmas)
		@param int:id del parametro richiesto
		@return: :tc_clpot
		"""

		#t=.tc_clpar_id
		for q in self.session.query(tc_clpot).filter_by(tc_clpot_id=Id):
			r=q
		return r

	def isPotentialEnabled(self,Id):
		l=[]
		for e in self.session.query(tc_clpot).filter_by(tc_clpot_id=Id):
			l.append(e)
		if l[0].tc_stato_id==1:
			return True
		else:
			return False


	def getPotential_value4Pv(self,Id,Id2):
		""" recupera il potenziale di classe Id2 per il pv con id Id
		@param Id:: id di pv
		@param Id2::tc_cl_pot
		@return {'classe':tc_clpot,'valore':float}
		"""
		pot={}

		for q in self.session.query(rel_pv_pot).filter_by(pv_id=Id).filter_by(tc_clpot_id=Id2):
			if self.isPotentialEnabled(Id2):
				pot['valore']=q.valore
				pot['classe']=self.getPotentialById(Id2)
				#pot['Stato']='Attivo'
			else:
				pot['classe']=self.getPotentialById(Id2)
				#pot['Stato']='Non Attivo'
		return pot

	def getOrder(self,e):
		"""
		ritorna il campo ordine di tc_clpar
		e' usato come chiave per ordinare i parametri dal metodo order
		"""
		return e['parametro'].ordine
	def sorter(self,cl):
		"""
		ordina una lista di tc_clpar secondo il campo ordine
		@return: [{'parametro':tc_clpar,'valore':tc_par}]
		@param {int:{'parametro':tc_clpar,'valore':tc_par}}:: {tc_clpar_id:{'parametro':tc_clpar,'valore':tc_par}}
		"""
		l=[]
		for v in cl.itervalues():
			l.append(v)
		l=sorted(l,key=self.getOrder)
		return l

	def filterTcPot(self,Id,Id2):
		""" ritorna la query su tc_pot in base a tc_pot_id e tc_clpot_id
		 e' usata da putAnswer4Parameter per associare ad ogni parametro la sua risposta
		 @return :tc_pot
		"""
		l=[]
		d={}
		for pa in self.session.query(tc_pot).filter_by(tc_clpot_id=Id).filter_by(tc_pot_id=Id2):
			d['text']=pa
			d['Id']=Id2
			l.append(pa)
		return l[0]

	def filterTcPar(self,Id,Id2):
		""" ritorna la query su tc_par in base a tc_par_id e tc_clpar_id
		 e' usata da putAnswer4Parameter per associare ad ogni parametro la sua risposta
		 @return :tc_par
		"""
		l=[]
		d={}
		for pa in self.session.query(tc_par).filter_by(tc_clpar_id=Id).filter_by(tc_par_id=Id2):
			d['text']=pa
			d['Id']=Id2
			l.append(pa)
		return l[0]

	def retrieveAllQuestions(self):
		"""
		recupera dal db tutti  i possibili parametri
		@return {int:{'parametro':tc_clpar}
		"""
		l={}
		for q in self.session.query(tc_clpar):
			#l.append(self.getQuestionById(q.tc_clpar_id))
			l[q.tc_clpar_id]=self.getQuestionById(q.tc_clpar_id)
		return l

	def retrievePotential4Pv(self,Id):
		"""
		recupera tutti potenziali definiti per il pv
		@param int:id del pv
		@return:[rel_pv_pot
		"""
		p=[]
		for i in self.session.query(rel_pv_pot).filter_by(pv_id=Id):
			p.append(i)
		return p

	def retrieveAllPotentials(self):
		"""
		recupera dal db tutti i possibili potenziali
		@return:
		"""
		l=[]
		for q in self.session.query(tc_clpot).all():
			#l.append(q)
			l.append(q)
		return l

	def mergePotentials(self,Id):
		"""
		associa alle classi di potenziale disponibili il relativo valore numerico
		@param Id:pv_id
		@return: [{'classe':tc_clpot,'valore':float}]
		"""
		#lista dei potenziali di pv
		l=[]
		for p in self.potentialsList:
			a=self.getPotential_value4Pv(Id,p.tc_clpot_id)
			if len(a)>0:
				l.append(a)

		return l

	def isActive(self, t):
		"""
		ritorna il testo da usare per tc_stato_id
		@return string::'attivo' per t==1
		"""
		if t==1:
			return 'Attivo'
		else:
			return 'Non attivo'
	def getText(self,t):
		dummy=Dummy("")
		if type(t)==type(dummy):
			r=t.testo
		else:
			r=t
		return r

	def translateDict(self,d):
		"""
		estrae il valore testuale dei campi del dict in input per adattarlo al formato accettato dalla tabella cioe' [{string:value}]
		@param param: [{string:tc_clpot,string:float}]::[{'classe':tc_clpot,'valore':float}]
		@return: [{string:Float}]::[{'potenziale':tc_clpot.testo:'valore':float,'Id':int}]
		@note: da notare che le chiavi del dizionario di output verranno usate
		per l'intestazione delle colonne della tabella di anagrafica,
		questo e' il motivo per cui classe viene sostituito con potenziale
		@note: il campo Id nel dizionario di uscita serve solo a uniformare il formato di output con quello di fetchBrands

		"""
		l=[]
		for i in d:
			di=Odict()
			di['potenziale']=str(i['classe'].testo)
			di['valore']= i['valore']
			#di['Stato']=i['Stato']
			di['Id']=-1
			l.append(di)
		return l


	def filterTcClPar(self,Id):
		l=[]
		for pa in self.session.query(tc_clpar).filter_by(tc_clpar_id=Id):
			f={}
			f['text']=pa
			f['Id']=Id
			l.append(pa)
		return l[0]

	def makeDigest(self,d):
		l=[]
		for k in d.iterkeys():
			l.append(k)
		return l

	def putAnswer4Parameter(self,parametro,q):
		if parametro.tc_stato_id==1:
			ans=self.filterTcPar(q[0],q[1])
		else:
			ans=Dummy("dato nascosto")
		return ans

	def isParameterActive(self,Id):
		"""
		verifica se un parametro con e' attivo
		@param int:tc_clpar_id
		@return: string:'attivo'/'non Attivo'
		"""
		l=[]
		for i in self.session.query(tc_par).filter_by(tc_clpar_id=Id):
			l.append(i.tc_stato_id)
		if l[0]==1:
			return 'Attivo'
		else:
			return 'non Attivo'
	def getQuestionsAndParameters(self,Id):
		"""
		genera la lista dei dict composti da parametro,valore
		"""
		p={}
		#c=self.session.query(rel_pv_par)
		#print c.column_descriptions
		for pa in self.session.query(rel_pv_par).filter_by(pv_id=Id):
			parametro =self.filterTcClPar(pa.tc_clpar_id)

			p[pa.tc_clpar_id]={'parametro':parametro,'valore':self.putAnswer4Parameter(parametro,(pa.tc_clpar_id, pa.tc_par_id))}#,'Stato':self.isParameterActive(pa.tc_clpar_id)}


		return p

	def getPvPotentials(self,Id):
		p={}


	def getPotentialValueById4Extraction(self,Id):
		l=[]
		for q in self.session.query(rel_pv_pot).filter_by(pv_id=Id):

			l.append(q)
		if len(l)<1:
			l.append("")
		return l[0]