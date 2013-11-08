#!/usr/bin/python
# -*- coding: latin-1 -
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Ui_anagrafica import Ui_MainWindowAnagrafica
import MySQLdb
#from entities_sqlalchemy import *
from mysql_sqlalchemy_class import *
from Odict import Odict
import MySQLdb.cursors
import sys
import os
import logging
import time
from entities_sqlalchemy import *
import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, mapper, relation, sessionmaker
#from mysqlEntities import *
from elixir import *
from sqlalchemy import *
from AnagraficaDb import *
from fpdf import *
from Odict import Odict
from reportlab.pdfgen import canvas
#import sys
#sys.path.append("C:\Users\giuseppe\AppData\Local\Aptana Studio 3\plugins\org.python.pydev_2.7.0.2012080220\pysrc")
#from pydevd import *


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



class ListaDialog():
	"""
	questa classe e' una struttura dati per la generazione dell'elenco degli elementi presenti nella selezione,  usata in testdialog
	@todo: rivederne l'utilita'
	"""
	def __init__(self):
		self.lista=Odict()

	def checkElement(self,i):
		b=self.lista.has_key(i)
		return b

	def addElement(self,i):
		self.lista[i]=""

	def getList(self):
		return self.lista

	def cleanList(self):
		self.lista.clear()

	def replaceList(self,l):
		self.lista=l

class utility():

	def getTime(self):
		year=time.localtime()[0]
		month=time.localtime()[1]
		day=time.localtime()[2]
		hour=time.localtime()[3]
		min=time.localtime()[4]
		sec=time.localtime()[5]
		return"%d:%d:%d:%d/%d/%d"%(hour,min,sec,day,month,year)

	def initDB(self,dbfile):
		metadata.bind = "mysql://%s"%dbfile
		metadata.bind.echo = False
		setup_all()
		if not os.path.exists(dbfile):
			create_all()

          # This is so Elixir 0.5.x and 0.6.x work
          # Yes, it's kinda ugly, but needed for Debian
          # and Ubuntu and other distros.

		global saveData
		import elixir
		if elixir.__version__ < "0.6":
			saveData=session.flush
		else:
			saveData=session.commit

	tables=[]
	def getRegioni(self):
		t=[i.nome for i in Regione.query.all()]
		return t

	def brandsAdapter(self,brand):
		"""
		wrapper di tableDb.brandsdapter
		converte la lista ottenuta da putBrands in self.util.getBrands4class_pv
		in una lista di Odict
		@param l: [string]
		@return:[Odict] con chiavi marche e Id
		@note: Id e' un campo dummy
		"""
		return self.tableDb.brandsAdapter(brand)

	def getRegioneId_sql(self,nome):
		conn = sqlite3.connect('regioni.sql')

		c = conn.cursor()
		self.log("cursore= {0}".format(c),"utiliry.py 52")
		query="select id from regione where nome like '{0}'".format(nome)
		e=c.execute(query)
		self.log("execute= {0}".format(e),"utiliry.py 55")
		r=c.fetchone()
		conn.close()
		self.log("resultset= {0}".format(r),"utiliry.py 58")
		return r[0]

	def getBrands4class_pv(self,id_class,Id):
		"""
		wrapper di anagraficaDb.getBrands4class_pv e anagraficaDb.putBrands

		interroga la tabella rel_pv_mar per conoscere gli id dei brand relativi alla classe id_class trattati da pv_id
		@param int,int::id_class,Id, rispettivamente lo id della classe marca e lo id del pv
		@return: [tc_mar.testo]
		"""

		return self.tableDb.putBrands(self.tableDb.getBrands4class_pv(id_class,Id))

	def populateTables(self, pv_id):
		nt=0
		for table in  self.tables.iterkeys():
			self.log("numero tables={0}".format(nt),"utility.py 82")
			#modifica qui
			parametri= self.tableDb.fetchData(table,pv_id)#self.fetchData(self.queries[table].format(pv_id))
			if parametri is not None:
				self.populateTable( table,parametri)
			else:
				infoString=" potenziale MMAS non disponibile {0}".format(nt)
				d=QtGui.QMainWindow()
				QtGui.QMessageBox.information(d,"Warning",infoString)
				break
			nt=nt+1

	def listPlusDict(self,l,d):
		"""
		ritorna una tupla  che ha come  elementi il dict seguito dagli elementi della lista
		"""
		t=[d]
		for i in l:
			t.append(i)
		return t

	def fetchData( self, query):
		self.log(" query per fetchdata {0}".format(query),"utility.py 93")
		db = self.db.getConnection()
		crs = MySQLdb.cursors.DictCursor(db)
		crs.execute( query)
		onerow=crs.fetchone()
		rs=crs.fetchall()
		if onerow is not None:
			firstRow=[onerow]
			tutto= self.listPlusDict(rs,onerow)
			self.log("rs valido ","utility.py 75")
		else:
			#tutto=None
			#devo ritornare un lista con un dict come elementi il primo e' viene usato per popolare lo header
			# gli altri elementi popolano la tabella
			tutto=[{"Errore del database":"dati non reperebili"}]
		self.log("resultset {0}".format(rs),"utility.py 120")
		db.close()
		self.log(" tutto : {0}".format(tutto),"utility.py 122")
		return tutto

	def itemMaker(self, txt):
		item = QtGui.QTableWidgetItem()
		item.setText(QtGui.QApplication.translate("MainWindow", unicode(txt), None, QtGui.QApplication.UnicodeUTF8))
		#self.tabella.setHorizontalHeaderItem(c, item)
		return item
	def getRegioneId(self,nome):
		self.log(" regione {0}".format(nome),"utility.py getRegioneId 68")
		t=[]
	#	print "nome={0}".format(nome)
		rs=Regione.query.filter(Regione.nome.like(str(nome)))
		for i in rs:
			self.log("elemento in rs {0}".format(i),"utility.py 72")
			t.append(i)

		self.log(" resultset per id di  {0}={1}".format(nome,t),"utility.py 70")
		if len(t)==0:
			id_regione=-1
			self.log(" regione non presente nel db","utility.py 73")
		else:
			id_regione=t[0]
		#	print "id regione={0}".format(id_regione)
		return id_regione
	def regionExpander(self,regione):
		regione_id=self.getRegioneId_sql(regione)
		self.log("regione da espandere {0}".format(regione),"utility.py 79")
		t=[r.nome for r in Provincia.query.filter(Provincia.regione_id==regione_id)]
		return t

	def populateRow(self, row, i, table):
		"""
		popola la tabella per righe pertanto @param row dict della riga
		@param i indice della riga
		@param table: QTableWidget
		"""
		# Id e' il valore che viene impostato in item.data(5)
		Id=-1
		if row.has_key('Id'):
			Id=row['Id']
		table.insertRow(i)
		j=0# indice della colonna
		for key in row.iterkeys():
			if key!='Id':
				item=self.itemMaker(unicode(row[key]))
				item.setData(1,Id)
				table.setItem(i, j, item)
				# sposto il cursore della colonna
				j=j+1

	def tablePopulator(self, table,rs):
		"""
		popola la tabella table
		dato il resultset rs
		@param table: string chiave della tabella in self.tables
		@param rs:([Odict]) contiene i dati che verranno visualizzati sulla table
		"""
		if len(rs)>0:
			self.populateHeaders(rs[0], table)
		else:
			item=self.itemMaker('marche')
			table.setHorizontalHeaderItem(0, item)
		for r in range(0, len(rs)):
			self.populateRow(rs[r], r, table)

	def  populateTable(self, table, rs):
		"""
		popola la tabella table
		dato il resultset rs
		@param table: string chiave della tabella in self.tables
		@param *rsp:([Odict]) contiene i dati che verranno visualizzati sulla table
		per compatibilita' con le versioni precedenti dove rs non era parametrico
		assegno al vecchio rs il valore del primo termine del param che contiene i dati
		 da stampare sulla tabella
		"""
		#popolo lo header della tabella
		if len(rs)>0:
			self.populateHeaders(rs[0], self.tables[table])
		#popolo la tabella
		for r in range(0, len(rs)):
			self.populateRow(rs[r], r, self.tables[table])

	def poulateAnagrafica(self):
		db = self.db.getConnection()
		crs=db.cursor()
		crs.execute("select * from pv ehere pv_id={0}".format(self.id))


	def log(self, title, txt):
		logging.debug(self.getTime()+" "+title+" "+str(txt))

	def getPotenziale(self,Id):
		"""
		ritorna il potenziale del pv_id, se questo e' potenziale mmas, se presente solo il potenziale
		esteso con tc_clpot_id pari a 10 ritorna il testo valore non calcolabile
		@return: string
		"""
		p=self.getTcPotId(Id)
		#self.log("query utility: {0}".format(query),"utility.py 192")
		#self.log("potenziale= {0}".format(item),"utility.py 213")
		return p.valore

	def getTcPotId(self,Id):
		"""
		ritorna un oggetto rel_pv_pot che riporta il valore del potenziale per pv_id
		in particolare ritorna il primo elemento della lista ottenuta dalla query con sqlAlchemy
		@note: un pv puo' avere sino a due diverse categorie di potenziale: MMAS ed esteso, il valore
		di potenziale da considerare e' solo il primo identificato da  tc_clpot_id=1, quando il
		 potenziale mmas non e' presente dovra' essere riportata la stringa non calcolabile, quest'operazione
		 e' eseguita da getPotenziale
		 @note: il potenziale mmas  nella lista di sqlalchemy occupa sempre il primo posto, quindi getTcPotId
		 ritorna sempre il primo elemento di tale lista
		@param Id::int
		@return: rel_pv_pot
		"""
		p=[]
		for i in self.session.query(rel_pv_pot).filter_by(pv_id=Id).filter_by(tc_clpot_id=1):
			p.append(i)
		if len(p)==0:
			d=Dummy("non disponibile")
			p.append(d)
		return p[0]
		#p1=[i.tc_pot_id for i in p]

		return p
	def getPv(self,Id):
		#return Pv.filter_by(pv_id=id).one()
		p=[]
		for i in self.session.query(Pv).filter_by(pv_id=Id):
			p.append(i)
		return p[0]
	#def getTcPot(self,pv_id,tcpot):
	#	return rel_pv_pot.query.filter_by(pv_id=pv_id and tc_pot_id=tcpot).one()

	def transcodeDate(self,data):
		qdate=None
		if type(data)==type("str"):
			data= data[0:10]
			c= data.split('-')
			qdate=QtCore.QDate(int(c[0]),int(c[1]),int(c[2]))
		else:
			qdate=data
		return qdate

	def fixData(self,d):
		if d is not None:
			stri=d
		else:
			stri=""
		return stri

	def populateFields(self, ui, pv_id):
		p= self.getPv(pv_id)
		#db = MySQLdb.connect(host="localhost", user="root", passwd="ringil-87",db="parafarmacie")
		#crs=db.cursor()
		#crs.execute("select * from pv where pv_id={0}".format(pv_id))
		#item= crs.fetchone()
		ui.checkBox_cliente.setCheckState(int(self.fixData(p.cliente)))#item[6]
		ui.text_codice_mmas.setText(str(self.fixData(p.cod_mmas)))#item[3]
		ui.text_ragione_sociale.setText(unicode(p.ragione_sociale))#item[8]
		ui.text_note.setPlainText(unicode(p.note))
		ui.text_titolare.setText(unicode(p.titolare))#item[9]
		ui.text_indirizzo.setText(unicode(p.indirizzo))#item[11]
		ui.text_cap.setText(str(self.fixData(p.cap)))#item[12]
		ui.text_comune.setText(unicode(self.fixData(p.comune)))#item[13]
		ui.text_codice_cliente.setText((self.fixData(p.cod_cliente)))
		ui.text_telefono_2.setText(self.fixData(self.fixData(p.tel2)))
		ui.text_codice_fiscale.setText(self.fixData(p.cf_pi))
		ui.setId(pv_id)
		ui.setTcPotId(self.getTcPotId(pv_id))
		ui.text_provincia.setText(str(self.fixData(p.provincia)))#item[14]
		ui.text_telefono.setText(str(self.fixData(p.tel1)))#item[15]
		ui.text_mail.setText(str(self.fixData(p.email)))#item[21]
		ui.text_sito.setText(str(self.fixData(p.sito)))#item[20]
		ui.text_fax.setText(str(p.fax))
		data=str(p.data_aggiornamento)#item[23]
		if p.data_aggiornamento is not None:
			qdate=self.transcodeDate(self.fixData(p.data_aggiornamento))
		else:
			qdate=QtCore.QDate()
		ui.date_aggiornamento.setDate(qdate)

		ui.text_potenziale.setText(str(self.getPotenziale(pv_id)))
		#db.close()
	def __init__(self,Id, tables,user,db,census=False):
		#mysql://username:password@localhost/mydb
		self.user=user
		self.db=db
		if not census:
			dbfile=db.getConnectionStringMMasgisDB()
		else:
			dbfile=db.getConnectionString()
		#print "utility dbfile",dbfile
		engine = create_engine("mysql://"+dbfile+"?charset=utf8&use_unicode=1", echo=echo,convert_unicode=True)
		Session = sessionmaker(bind=engine)
		self.session=Session()
		self.initDB(dbfile)
		self.id=Id
		self.tables=tables
		self.tableDb= tableDb(user,db)

	def getDb(self):
		"""ritorna l'istanza di tableDb inizializata da __init__
		@return: tableDb
		"""
		return self.tableDb

	def setId(self,Id):
		self.id=Id

	def writeReportLab(self,headers, values, path,title,pv_id):
		"""
		genera il file pdf per l'esportazione dell'anagrafica
		@param [string]: lista degli headers o intestazioni dei campi che compariranno nel file
		@param [string]: lista dei valori da riportare accanto alle intestazioni
		@param string: url del file da generare
		@param string: url del logo da riportare nello header del file pdf
		@attention: la lunghezza delle due liste headers e values deve esseree la stessa
		@param string: titolo dell'anagrafica da esportare, solitamente la ragione sociale o il codice mmas
		"""
		c = canvas.Canvas(path)
		y=800
		x=100
		pad=0
		c.drawString(round((600-c.stringWidth(unicode(title)))/2),y,unicode(title))
		pad=20
		for i in range(0,len(headers)):
			c.drawString(x,y-pad,headers[i])
			c.drawString(x+c.stringWidth(headers[i])+10,y-pad,unicode(values[i]))
			pad+=10
		parametri= self.tableDb.fetchData("parametro",pv_id)
		getField=lambda l,k: l[k]
		pad+=20
		c.drawString(round((600-c.stringWidth("PARAMETRI"))/2),y-pad,"PARAMETRI")
		pad+=30
		for i in parametri:
			c.drawString(x,y-pad,i['parametro']+":")
			c.drawString(x+c.stringWidth(i['parametro']+":")+10,y-pad,unicode(i['valore']))
			pad+=15
		marche= self.tableDb.fetchData("marca",pv_id)
		pad=0
		c.showPage()
		c.drawString(round((600-c.stringWidth("MARCHI"))/2),y-pad,"MARCHI")
		pad+=30

		for i in marche:
			c.drawString(x,y-pad,i['classe marca']+":")

			brand= self.getBrands4class_pv(i["Id"],pv_id)
			if len(brand)>0:
				shift=0
				shift+=c.stringWidth(i['classe marca']+":")
				n=0
				putsComma=lambda x,y: "," if x<len(y) else ""
				newLine=lambda x,y,z: 15 if (x<3 and z!="") else 0
				for j in range(0,min(3,len(brand))):
					n+=1
					print brand[j]['brand']
					c.drawString(x+shift,y-pad,brand[j]['brand'])
					#shift+=c.stringWidth(j['brand'])+shiftsComma(n,brand)
					pad+=newLine(n,brand,brand[j]['brand'])


			pad+=15


		c.showPage()
		c.save()


	def sessionCommit(self):
		self.session.commit()


	def pdfWrite(self,headers, values, path, pics,title):
		"""
		genera il file pdf per l'esportazione dell'anagrafica
		@param [string]: lista degli headers o intestazioni dei campi che compariranno nel file
		@param [string]: lista dei valori da riportare accanto alle intestazioni
		@param string: url del file da generare
		@param string: url del logo da riportare nello header del file pdf
		@attention: la lunghezza delle due liste headers e values deve esseree la stessa
		@param string: titolo dell'anagrafica da esportare, solitamente la ragione sociale o il codice mmas
		"""
		class PDF(FPDF):
			def header(self):
					self.image(pics,10,0,22)
					#Arial bold 15
					self.set_font('Arial','B',15)
					#Calculate width of title and position
					w=self.get_string_width(title)+6
					self.set_x((210-w)/2)
					#Colors of frame, background and text
					self.set_draw_color(0,80,180)
					self.set_fill_color(230,230,0)
					self.set_text_color(220,50,50)
					#Thickness of frame (1 mm)
					self.set_line_width(1)
					#Title
					self.cell(w,9,title,1,1,'C',1)
					#Line break
					self.ln(10)

			def footer(self):
				#Position at 1.5 cm from bottom
				self.set_y(-15)
				#Arial italic 8
				self.set_font('Arial','I',8)
				#Text color in gray
				self.set_text_color(128)
				#Page number
				self.cell(0,10,'Page '+str(self.page_no()),0,0,'C')

			def section_title(self,num,label):
				#Arial 12
				self.set_font('Arial','',12)
				#Background color
				self.set_fill_color(200,220,255)
				#Title
				self.cell(0,6,"Sezione %s : %s"%(num,label),0,1,'L',1)
				#Line break
				self.ln(4)

			def chapter_list(self,headers,values,label):
				"""
				inserisce nel file pdf una pagine con gli headers e corrispondenti values passati
				@param [string]:lista degli headers
				@param [string]:lista dei valori
				@attention:le due liste devono avere uguale lunghezza
				@param string: titolo della sezione
				"""
				self.add_page()
				self.section_title("", label)
				self.set_font('Times','',12)
				for i in range(0,len(headers)):
					self.cell(round(len(headers[i])*2.5),5,headers[i],'L')
					self.cell(100,5,unicode(values[i]),0,1)
		pdf=PDF()
		pdf.set_title(title)
		pdf.chapter_list(headers, values,"anagrafica")
		pdf.output(path,'F')


	def translateProvincia(self,pr):
		print "translate"
		db = self.db.getConnectionMMASGISDB()
		like={}
		like['mysql']="like"
		like['postgresql']='ilike'
		crs=db.cursor()
		query="select sigla from provincia where provincia {0} '{1}'".format(like[self.db.getRDBMS()],pr.replace("'","`").upper())
		#print ("query in translateProvincia xxx {0}".format(query),"utility.py 167")
		crs.execute(query)
		sigla=crs.fetchone()[0]
		db.close
		return sigla


	def populateHeaders(self, row, table):
		"""
		scrive i nomi delle colonne @param row il dict di una delle righe
		@param i l'indice della tabella
		"""
		n=0# contatore per inserire le colonne
		table.setColumnCount(len(row)-1)# devo eliminare una colonna Id
		for key in row.iterkeys():
			if key!='Id':
				item=self.itemMaker(key)
				table.setHorizontalHeaderItem(n, item)
				n=n+1
