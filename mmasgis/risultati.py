# -*- coding: latin-1 -*-
"""
/***************************************************************************
 testDialog
								 A QGIS plugin
 test
						     -------------------
		begin			    : 2011-11-09
		copyright			: (C) 2011 by test
		email			    : test@iol.it
 ***************************************************************************/

/***************************************************************************
 *																		 *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.								   *
 *																		 *
 ***************************************************************************/
"""
import PyRTF as rtf

from pvListQueryBuilderBase import PvListQueryBuilderBase
from appy.pod.renderer import Renderer
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature, QLatin1String
from ui_test import Ui_test
from Ui_risultati import Ui_MainWindowResults
from Ui_anagrafica_modificato import *
from Ui_anagrafica import *
from anagrafica import *
from utility import *
from interrogazioni import MainWindowQuery,Pv_item
import MySQLdb
import time
from constants import cons
import sys
import pyExcelerator as xl
from separatore import *
from Profilo import *
import os
from esportazione import *
from Ui_ricercaAnagrafica import *
from PvListQueryBuilderMysql import PvListQueryBuilderMysql
from PvListQueryBuilderPostgres import PvListQueryBuilderPostgres
from ComunePg import ComunePg
from ProvinciaPg import ProvinciaPg
from RegionePg import RegionePg
"""
import sys
sys.path.append("C:\Users\giuseppe\AppData\Local\Aptana Studio 3\plugins\org.python.pydev_2.7.0.2012080220\pysrc")
from pydevd import *
"""
class Decoder():
    def __init__(self):
        self.sieve={}
        self.l=lambda x,y:len(y)-1==y.find(x)
        self.sieve[1]=unicode("è")
        self.sieve[2]=unicode("é")
        self.sieve[3]=unicode("ì")
        self.sieve[4]=unicode("à")
        self.sieve[5]=unicode("ò")
        self.sieve[6]=unicode("ù")
        self.change={}
        self.change[unicode("è")]='e'
        self.change[unicode("é")]='e'
        self.change[unicode("ì")]='i'
        self.change[unicode("ò")]='o'
        self.change[unicode("ù")]='u'
    def isTail(self,s):
        b=False
        for i in self.sieve.itervalues():
            #print i
            b=b or (self.l(i,unicode(s)))
        return b

    def unidecode(self,s):
        b=self.isTail(s)
        for i  in self.change.iterkeys():
            s=s.replace(i,self.change[i])
        if b:
            s+="_"
        return unicode(s)



class testDialog(QtGui.QMainWindow):
	"""
	e' un wrapper di Ui_risultati
	prima versione di gui del plugin
	e come tale stampa i pv relativi alla selezione geografica
	"""
	def cleanTable(self):
			"""
			rimuove tutti gli elementi dalla tabella
			"""
			self.ui.tabella.clearContents()
			self.ui.tabella.setRowCount(0)

	def mostra(self):
		self.ui.repaint()

	def itemBuilder(self, value, id):
		item = QtGui.QTableWidgetItem()
		item.setText(unicode(value))
		item.setData(1, id)
		return item

	def populateFilteredTable(self):
		#self.log("filtered list {0}".format(self.lista.getList()),"testdialog.py 58")
		#self.log("lunghezza filtered list {0}".format(len(self.lista.getList())),"testdialog.py 59")
		for r in self.lista.getList().iterkeys():
			self.addRow(r[0])


	def newDoit(self,id):
		"""
		 apre anagrafica
		"""
		self.ui =MainWindowAnagrafica(id)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.ui.geometry()
		self.ui.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.height()/2)
		self.ui.setWindowTitle("Scheda Anagrafica "+self.nomeDb.capitalize())
		self.ui.show()

	def doSearch(self,cl):
		self.filtered=True
		if self.uiFilter is None:
			self.uiFilter =MainWindowQuery(self.user,self.activeDb)
			self.uiFilter.addGeographicList(self.lista.getList())
			self.uiFilter.setRisultati(self)
		self.uiFilter.cerca(cl)

	def doFilter(self):
		#self.log("lista prima del filtro {0}".format(self.lista.getList())," testDialog.py 68")
		self.uiFilter =MainWindowQuery(self.user,self.activeDb)
		self.uiFilter.addGeographicList(self.lista.getList())
		self.uiFilter.setRisultati(self)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.uiFilter.geometry()
		self.uiFilter.move((screen.width()/2)-size.width()/2,(screen.height()/3)-size.height()/3)
		self.uiFilter.setWindowTitle("Ulteriore Selezione "+self.nomeDb.capitalize())
		self.uiFilter.show()

	@pyqtSignature("")
	def on_filter_triggered(self):
		self.filtered=True
		self.doFilter()
		#self.cleanTable()

	@pyqtSignature("")
	def on_findButton_triggered(self):
		self.trova_ui=MainWindowRicercaAnagrafica()
		self.trova_ui.show()
		QtCore.QObject.connect(self.trova_ui,QtCore.SIGNAL("cerca"),self.doSearch)

	def addRow(self,Id):
		"""
		 aggiunge una riga alla tabella
		 @param id: Integer
		"""
		riga=self.db.getPvById(Id)
		##self.log( "campi per id {0} {1}".format(riga, id),"testdialog.py 115")
		self.ui.tabella.insertRow(0)
		items=self.packetBuilder(riga)
		##self.log("riga di pv {0}".format(items),"testdialog.py 150")
		##self.log(" dati per riga {0}".format(riga),"testdialog.py 151")
		for colonna in range(len(items)):
			self.ui.tabella.setItem(0,colonna,items[colonna])
			#self.indice_tabella=self.indice_tabella+1
		#print "added row for id={0}".format(id)




	def getTime(self):
		year=time.localtime()[0]
		month=time.localtime()[1]
		day=time.localtime()[2]
		hour=time.localtime()[3]
		minu=time.localtime()[4]
		sec=time.localtime()[5]
		return"{0}:{1}:{2}:{3}/{4}/{5}".format(hour,minu,sec,day,month,year)



# self.ui.textArea.home(True)
		#self.ui.textArea.insert(txt)

	def getPotenziale(self, Id):
		"""
		recupera il potenziale di un pv
		@attention: non usa sqlalchemy: maybe db compatibility issue, ma la query e' semplice dovrebbe essere ok
		@todo: test db compatibility
		"""
		db = self.activeDb.getConnection()
		crs=db.cursor()
		##self.log("mmas Id={0}".format(Id),"testdialog.py 57")
		query="select valore from rel_pv_pot where pv_id = {0}".format(Id)
		##self.log("query potenziale="+query,"testdialog.py 58")
		crs.execute(query)
		if   type(crs.fetchone())==type(()):
			potenziale=crs.fetchone()
		#	#self.log("potenziale nullo","testdialog.py 63")
		else:
			##self.log("potenziale valido","testdialog.py 65")
			##self.log("tipo crs= {0}".format(type(crs.fetchone())), "test")
			potenziale=("non pervenuto")
			##self.log("potenziale mmas={0}".format(potenziale),"testdialog.py 60")
		db.close()
		if type(potenziale)==type(()):
			potenziale= potenziale[0]
		return potenziale

	def get4Comune(self,item):
		"""
		interroga il db per ottenere la lista sei punti vendita per comune
		in seguito e' stata adattata per funzionare pure con gli altri layers, rendendo la query parametrica

		"""
		tipo,area=item[0],item[1]
		#print "item in get4comune",item
		lista=[]
		#self.log("parametri di get4Comune testDialog 61","tipo={0} area={1}".format(tipo,area))
		db = self.activeDb.getConnection()
		crs=db.cursor()
		query=self.cons.queryList.format(tipo,area.replace("'","`"))
		##"select nome1, indirizzo,pv_id,cliente,cap,cod_cliente,comune,provincia,tel1,tel2,tel3,cf_pi from pv where comune like '{0}'".format(comune)
		crs.execute(query)

		for row in crs:
			lista.append( {'ragione sociale':row[0],'potMMAS':self.getPotenziale(row[2]),'indirizzo':row[1],'cliente':row[3], 'cap':row[4],'comune':row[6],'provincia':row[7],'telefono1':row[8],'cod_mmas':row[9],'telefono3':row[10],'cf':row[11],'id':row[2], 'cod_cliente':row[5]})
		return lista

	def getPvList(self,selection):

		#print "query:",query
		lista=[]

		q=self.pvListQueryBuilder[self.activeDb.getRDBMS()](selection,self.activeDb)
		query=q.getFullQuery()
		db = self.activeDb.getConnection()#mi connetto al censimento
		crs=db.cursor()
		crs.execute(query)
		for row in crs:
			#print "row",row
			lista.append( {'ragione sociale':row[0],'potMMAS':row[12],'indirizzo':row[1],'cliente':row[3], 'cap':row[4],'comune':row[6],'provincia':row[7],'telefono1':row[8],'cod_mmas':row[9],'telefono3':row[10],'cf':row[11],'id':row[2], 'cod_cliente':row[5]})
			#print lista
		return lista

	def on_tabella_cellDoubleClicked(self,row,column):
		self.currentRow=row
		id=self.ui.tabella.item(row,column).data(1).toString()

		self.doit(id)

	@pyqtSignature("")
	def on_openselButton_triggered(self):
		selected=self.ui.tabella.selectedItems()
		if len(selected)==0:
			infoString="Nessuna anagrafica selezionata"
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"Attenzione", infoString)
		else:
			row=self.ui.tabella.currentRow();
			id=self.ui.tabella.item(row,0).data(1).toString()
			self.doit(id)

	@pyqtSignature("")
	def on_firstButton_triggered(self):
		self.getFirst()

	@pyqtSignature("")
	def on_lastButton_triggered(self):
		self.getLast()

	@pyqtSignature("")
	def on_nextButton_triggered(self):
		self.getNext()

	@pyqtSignature("")
	def on_previousButton_triggered(self):
		self.getPrevious()

	def packetBuilder(self,t):
		"""
		dalla lista dei campi della query
		genera una lista di QTableWidgetItem con il giusto ordine
		"""
		p=[]
		#print t
		p.append(self.itemBuilder(t['cod_mmas'],unicode (t['id'])))
		p.append(self.itemBuilder(t['potMMAS'],unicode(  t['potMMAS'])))
		p.append(self.itemBuilder(t['ragione sociale'],unicode (t['id'])))
		p.append(self.itemBuilder(t['indirizzo'],unicode( t['id'])))
		p.append(self.itemBuilder(t['cap'],unicode(  t['id'])))
		p.append(self.itemBuilder(t['comune'],unicode(  t['id'])))
		p.append(self.itemBuilder(t['provincia'], unicode( t['id'])))
		p.append(self.itemBuilder(t['telefono1'],unicode(  t['id'])))
		p.append(self.itemBuilder(t['cf'], unicode( t['id'])))
		#,t[1],t[3],t[5],t[4],t[2]
		return p

	def updateList(self,l):
		#self.log("lista dopo il filtro {0}".format(l),"testdialog.py 233")
		self.lista.replaceList(l)


	def itemsBuilder(self,dicto):
		"""
		genera la lista degli items da inserire nella riga
		@param dicto la tupla che viene dalla query
		"""
		t=[]
		for key in dicto.iterkeys():
			#print key+ str(dicto[key])
			item = QtGui.QTableWidgetItem()
			item.setData(1, dicto['id'])
			item.setText(unicode(dicto[key]))
			t.append(item)
			return t

	def getCurrentRow(self):
		return self.ui.tabella.row(self.ui.tabella.currentItem())

	def getRowId(self, row):
		#self.log(" row interrogata {0}".format(row),"testdialog.py 257")
		item= self.ui.tabella.item(row, 0)
		id=item.data(1).toString()
		#self.log("id trovato={0}".format(id),"testdialog.py 259")
		return id

	def setOriginalList(self,l):
		self.originalList=l

	def on_cartButton_triggered(self):
		if self.filtered:
			self.cleanTable()
			#print "lista originale",self.originalList,
			self.populateTableByDb(self.lista.getList())

	def pvList2dict(self,l):
		"""
		converte la lista dei pv in un dizionario di pv  per compatibilità con risultati e testdialog
		@note: i pv sono tutti visibili
		@return:{(int):""}::{(pv_id):""}
		"""
		d={}
		for p in l:
			p.setVisible(True)
			d[(p.getId())]=""
		return d

	def populateTableByDb(self,l):
		"""
		popola le righe della tabella con i pv presenti in l
		@param l: {(pv_id,):"",}
		"""
		#self.log( " lista={0}".format(l),"testdialog 282")
		if type(l)==type([]):
			l=self.pvList2dict(l)
		for r in l.iterkeys():
			self.addRow(r[0])
		self.ui.text_numero_risultati.setText(str(self.ui.tabella.rowCount()))
	def getPrevious(self):
		if self.currentRow>0:
			self.currentRow=self.currentRow-1
			self.ui.tabella.setCurrentCell(self.currentRow, 0)
		id= self.getRowId(self.currentRow)
		return id
	def getLast(self):
		self.currentRow=self.ui.tabella.rowCount()-1
		self.ui.tabella.setCurrentCell(self.currentRow, 0)
		id= self.getRowId(self.currentRow)
		return id
	def getFirst(self):
		self.currentRow=0
		self.ui.tabella.setCurrentCell(self.currentRow, 0)
		id= self.getRowId(self.currentRow)

		return id


	def getNext(self):
		#se non sono alla fine della lista
		if self.currentRow<(self.ui.tabella.rowCount()-1):
			#setto la variabile con il valore  della riga successiva
			self.currentRow=self.currentRow+1
			#aggiorno la riga corrente
			self.ui.tabella.setCurrentCell(self.currentRow, 0)
		id= self.getRowId(self.currentRow)
		#self.log("id ricevuto da getNext={0}".format(id),"testdialog.py 259")
		return id


	def doit(self,pv_id):
		#self.w = Ui_MainWindowAnagrafica(QtGui.QMainWindow)
		# mainWindowAnagrafica necessita del riferimento a chi la invoca per poter scorrere la lista
		self.w = MainWindowAnagrafica(pv_id,self,self.user,self.activeDb)
		#self.w.setGeometry(QtCore.QRect(100, 100, 400, 200))
		tables={}
		tables['parametro']=self.w.table_parametri_mmas
		tables['marca']=self.w.table_marchi_classe
		tables['potenziale']=self.w.table_potenziali_mmas

		#print "doit activedb",self.activeDb
		util=utility(pv_id, tables,self.user,self.activeDb,census=True)
		#util.populateTables(pv_id)
		util.populateFields(self.w, int(str(pv_id)))
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.w.geometry()
		self.w.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.height()/2)
		self.w.setWindowTitle("Scheda Anagrafica "+self.nomeDb.capitalize())
		self.w.show()
	"""
	dato lo item di selections popola la lista
	con gli elementi del db
	"""
	def populateList(self,pv):
		#print "item in populateList risultati 395",item

		if len(pv	)!=0:
			for riga in pv:
				self.lista.addElement((riga['id'],))

	def populateRow(self,item):
		#self.log("lunghezza  iniziale di self.lista={0}".format(len(self.lista.getList())),"testdialog.py 276")
		pv=self.get4Comune(item[0],item[1])
		#self.ui.textArea.insert(item[0]+" "+str(item[1]))
		#self.log("resulset per item {0}={1}".format(pv,item),"testdialog.py 146")
		if len(pv	)!=0:
			for riga in pv:
				#self.ui.tabella.insertRow(0)
				#items=self.packetBuilder(riga)
				self.lista.addElement((riga['id'],))
				#for colonna in range(len(items)):
				#									self.ui.tabella.setItem(0,colonna,items[colonna])
				#									self.indice_tabella=self.indice_tabella+1
		else:
			pass
			#self.log("query vuota","testdialog.py 288")
		#self.log("lunghezza  finale di self.lista={0}".format(len(self.lista.getList())),"testdialog.py 289")
#		self.populateFilteredTable(self.lista.getList())


	def exportRtf(self):
		infoString=QtCore.QString("estrazione anagrafiche in word")
		reply=QtGui.QMessageBox.question(self,infoString,"Esportare solo le anagrafiche selezionate?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.No)
		if reply==QtGui.QMessageBox.Yes:
			selected=self.selectSome(self.ui.tabella.selectedItems())
		elif reply==QtGui.QMessageBox.No:
			selected=self.selectAll()
		else:
			return
		filexl=QFileDialog(self)
		#setto filexl in anymode cioe' ritorna il path del file anche se non esiste
		filexl.setFileMode(0)#
		filexl.setNameFilter("word(*.doc *.rtf)")
		nfile= filexl.getSaveFileName(self,"esporta anagrafiche in word","",filter="(*.doc *.rtf)")

		DR = rtf.Renderer()
		doc = rtf.Document()

		ss	  = doc.StyleSheet

		n=0
		thin_edge  = rtf.BorderPropertySet( width=20, style=rtf.BorderPropertySet.SINGLE )
		thick_edge = rtf.BorderPropertySet( width=80, style=rtf.BorderPropertySet.DOUBLE )
		mixed_frame = rtf.FramePropertySet( thin_edge,  thick_edge, thin_edge,  thick_edge )
		for i in enumerate(selected):
			section = rtf.Section()
			table = rtf.Table( rtf.TabPropertySet.DEFAULT_WIDTH * 7,
					   rtf.TabPropertySet.DEFAULT_WIDTH * 3)

			#section.append(table)
			img=rtf.Image("pictures/logo.jpg")
			c1 = rtf.Cell( rtf.Paragraph( img  ) )
			c2 = rtf.Cell( rtf.Paragraph( ss.ParagraphStyles.Heading2,"Scheda anagrafica	{0}".format(self.activeDb.getNameDb())   ) )
			table.AddRow(c1,c2)
			section.Header.append( table )
			oggi=datetime.date.today()
			section.Footer.append(rtf.Paragraph(ss.ParagraphStyles.Normal,"® Copyright Marketing & Telematica mail: info@metmi.it Data Esportazione: {0}/{1}/{2}".format(oggi.day,oggi.month,oggi.year)))
			Id= i[1].data(1).toInt()[0]
			p = rtf.Paragraph( rtf.ParagraphPS().SetPageBreakBefore( True ), '' )
			section.append( p )
			doc=self.makeRtf(doc,section,Id,i[0]+1,len((selected)))

		#doc=self.makeRtf(doc,section)
		##print "scrivo",self.OpenFile( 'rtf/vero' )
		DR.Write( doc, self.OpenFile( nfile ) )


	@pyqtSignature("")
	def on_wordButton_triggered(self):
		#t0=time.time()
		self.esportazione=MainWindowEsportazione(self, self.db,self.user,self.activeDb)
		#t1=time.time()
		self.profilo=Profilo(self.db,self.user,self.activeDb)
		#t2=time.time()
		##print "TEMPO ESPORTAZIONE", (t1-t0)
		##print "TEMPO PROFILO", (t2-t1)
		self.esportazione.setAfterSelection(self.exportRtf)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.esportazione.geometry()
		self.esportazione.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.width()/2)
		self.esportazione.setWindowTitle("Esportazione "+self.nomeDb.capitalize())
		self.esportazione.show()
		"""
		self.esportazione=MainWindowEsportazione(self, self.db,self.user,self.activeDb)
		#t1=time.time()
		self.profilo=Profilo(self.db,self.user,self.activeDb)
		#t2=time.time()
		##print "TEMPO ESPORTAZIONE", (t1-t0)
		##print "TEMPO PROFILO", (t2-t1)
		self.esportazione.setAfterSelection(self.wordExport)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.esportazione.geometry()
		self.esportazione.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.width()/2)
		self.esportazione.setWindowTitle("Esportazione "+self.nomeDb.capitalize())
		self.esportazione.show()
		"""


	def populateTable(self,selection):
		self.lista.cleanList()
		#interrogo il db
		#self.log("selections {0}".format(selection),"testdialog.py 145")
		self.ui.tabella.insertRow(self.indice_tabella)
		for item in selection:
			pv=self.get4Comune(str(item[0]),str(item[1]))
			#self.log("resultset per item={0}:{1}".format(item,pv),"testdialog 148")
			#scrivo nella textArea il comune ricercato
			self.ui.textArea.insert(item[0]+str(item[1]))
				#popolo la tabella
			for riga in range(len(pv)):
#			#self.log("resultSet "+str( pv[riga]))
					#aggiungo un riga alla tabella
					self.ui.tabella.insertRow(self.indice_tabella)

					#trasformo il dizionario in una lista di items
					items=self.packetBuilder(pv[riga])
					#inserisco gli items nella tabella
					for colonna in range(len(items)):
												self.ui.tabella.setItem(self.indice_tabella,colonna,items[colonna])
												self.indice_tabella=self.indice_tabella+1
		#self.log("numero righe nella tabella ={0}".format(self.ui.tabella.rowCount()),"testdialog.py 305")


	def __init__(self,t,user,db):
		"""
		inizializza testDialog
		@param t: lista delle selezioni [[chiave,nome,istat]]
		@note: le chiavi sono 'comune','reggione','provincia'
		@note: si occupa di eseguire le query
		"""
		self.user=user
		profilo=user.getProfile()
		self.trova_ui=None
		self.activeDb=db
		self.esportazione=None
		self.currentRow=0
		self.db=tableDb(user,self.activeDb)
		#creo un dict che contiene le classi di pvListQueryBuilderper ogni famiglia di db riconosciuta
		self.pvListQueryBuilder={}
		self.pvListQueryBuilder['mysql']=PvListQueryBuilderMysql
		self.pvListQueryBuilder['postgresql']=PvListQueryBuilderPostgres
		self.profilo=None
		self.lista=ListaDialog()
		self.filtered=False
		QtGui.QMainWindow.__init__(self)
		#self.log("partenza testdialog","testDialog.py 382")
		self.cons=cons()
		self.ui = Ui_MainWindowResults()
		self.ui.setupUi(self)
		self.ui.excelButton.setEnabled(profilo.isPermitted(3))
		self.ui.textButton.setEnabled(profilo.isPermitted(1))
		self.ui.wordButton.setEnabled(profilo.isPermitted(2))
#		print "esporta word permitted ",profilo.isPermitted(2)
		self.ui.tabella.setColumnWidth(0,85)
		self.ui.tabella.setColumnWidth(1,93)
		self.ui.tabella.setColumnWidth(2,450)
		self.ui.tabella.setColumnWidth(3,400)
		self.ui.tabella.setColumnWidth(4,95)
		self.ui.tabella.setColumnWidth(5,250)
		self.ui.tabella.setColumnWidth(6,80)
		self.ui.tabella.setColumnWidth(7,150)
		self.ui.tabella.setColumnWidth(8,150)
		#inizializzo l'indice delle righe
		self.utbFactory={}
		self.utbClasses={}
		self.utbClasses['mysql']=[Regione,Provincia,Comune]
		self.utbClasses['postgresql']=[RegionePg,ProvinciaPg,ComunePg]
		self.utbFactory['regione']=self.utbClasses[db.getRDBMS()][0]
		self.utbFactory['provincia']=self.utbClasses[db.getRDBMS()][1]
		self.utbFactory['comune']=self.utbClasses[db.getRDBMS()][2]
		self.originalList=[]
		self.uiFilter=None
		self.indice_tabella=0
		self.populateList(self.getPvList(t))
		"""
		for i in t:
			self.populateList(i)
			"""
		self.populateFilteredTable()
		self.ui.text_numero_risultati.setText(str(self.ui.tabella.rowCount()))
		self.Separator=MainWindowSeparazione(self)
		self.separator="\t"
		self.nomeDb=user.getActiveDb().getNameDb()
		#self.show()

	def getDb(self):
		return self.db

	def setProfile(self,p):
		self.profile=p

	def setSeparator(self,s):
		self.separator=s

	def packet4ExportFactory(self,t):
			"""
			dalla lista dei campi della query
			genera una lista di string per l'esportazione in tsv solo test
			@todo:heavy  refactoring
			@return [QTableWidgetItem]
			"""
			p=[]
			p.append(t['cod_mmas'])
			p.append(t['potMMAS'])
			p.append(t['ragione sociale'])
			p.append(t['indirizzo'])
			p.append(t['cap'])
			p.append(t['comune'])
			p.append(t['provincia'])
			p.append(t['telefono1'])
			p.append(t['cf'])
			#,t[1],t[3],t[5],t[4],t[2]
			return p

	def header4extraction(self):
		"""
		ritorna la lista degli header per le colonne dell'estrazione
		@return: [string]
		"""
		p=[]
		p.append('cod_mmas')
		p.append('potMMAS')
		p.append('ragione sociale')
		p.append('indirizzo')
		p.append('cap')
		p.append('comune')
		p.append('provincia')
		p.append('telefono1')
		p.append('cf')
		return p

	def writeTsv(self,tsv,item):
		l=lambda x: self.separator if x>0 else ''
		for i in enumerate(item):
			s=unicode(i[1])
			ss=s.encode('utf8')
			tsv.write(l(i[0])+ss)
		tsv.write("\n")

	def writeExcel(self,headers,value,path):
		mydoc=xl.Workbook()
		#Add a worksheet
		mysheet=mydoc.add_sheet("anagrafiche")
		header_font=xl.Font() #make a font object
		header_font.bold=True
		header_font.underline=True
		#font needs to be style actually
		replies={}
		header_style = xl.XFStyle(); header_style.font = header_font
		xl.UnicodeUtils.DEFAULT_ENCODING = 'cp1251'
		for col,values in enumerate(headers):
			mysheet.write(0,col,values,header_style)
		for row in enumerate (value):
			Id= row[1].data(1).toInt()[0]
			if not replies.has_key(Id):
				replies[Id]=""
				pv=self.db.getPvById(Id)
				packet=self.profile.getData(Id)
				for col in range(0,len(packet)):
					mysheet.write(row[0]+1,col,unicode(packet[col]))
		if str(path)!="":
			mydoc.save(path)
			infoString="%d anagrafiche esportate correttamente"%len(replies)
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"Info", infoString)

	def excelExport(self):
		infoString=QtCore.QString("estrazione anagrafiche")
		reply=QtGui.QMessageBox.question(self,infoString,"Esportare solo le anagrafiche selezionate?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.No)
		if reply==QtGui.QMessageBox.Yes:
			selected=self.selectSome(self.ui.tabella.selectedItems())
		elif reply==QtGui.QMessageBox.No:
			selected=self.selectAll()
		else:
			return
		filexl=QFileDialog(self)
		#setto filexl in anymode cioe' ritorna il path del file anche se non esiste
		filexl.setFileMode(0)#
		filexl.setNameFilter("Excel-Files (*.xls)")
		nfile= filexl.getSaveFileName(self,"esporta anagrafiche in excel","*.xls",filter="(*.xls *.xlt)")
		self.writeExcel(self.profile.getHeaders(),selected,nfile)
		self.esportazione.reset()

	def tsvExport(self):
		infoString=QtCore.QString("estrazione anagrafiche")
		reply=QtGui.QMessageBox.question(self,infoString,"Esportare solo le anagrafiche selezionate?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel, QtGui.QMessageBox.No)
		#print len(self.w.tabella.selectedItems())
		if reply!=QtGui.QMessageBox.Yes and reply!=QtGui.QMessageBox.No:
			return
		filetsv=QFileDialog(self)#file("tsv.txt","w")
		#filetsv.show()
		filetsv.setFileMode(0)
		nfile= filetsv.getSaveFileName(self, "Save File","*.txt", filter="(*.txt *.csv *.tsv)")
		if str(nfile)!="":
			tsv=file(nfile,'w')
			# scrivo gli header sul file
			self.writeTsv(tsv,self.profile.getHeaders())
			#uso un dict per evitare di esportare piu' volte la stessa anagrafica
			replies={}
			if reply==QtGui.QMessageBox.No:
				selected=self.selectAll()
			else:
				selected=self.ui.tabella.selectedItems()
			for i in selected:
				Id=i.data(1).toInt()[0]
				if not replies.has_key(Id):
					replies[Id]=""
					#print "esportata anagrafica per",Id
					#print replies
					packet=self.profile.getData(Id)
					self.writeTsv(tsv,packet)
				else:
					pass
					#print "replica per",Id
			infoString="%d anagrafiche esportate correttamente"%len(replies)
			d=QtGui.QMainWindow()
			QtGui.QMessageBox.information(d,"Info", infoString)
			self.esportazione.reset()

	def selectAll(self):
		l=[]
		for r in range(0,self.ui.tabella.rowCount()):
			l.append(self.ui.tabella.item(r,0))
		return l

	def selectSome(self, l):
		df={}
		lf=[]
		for i in l:
			if df.has_key(i.data(1).toInt()[0]):
				pass
			else:
				df[i.data(1).toInt()[0]]=""
				lf.append(i)
		return lf

	@pyqtSignature("")
	def on_excelButton_triggered(self):
		t0=time.time()
		self.esportazione=MainWindowEsportazione(self, self.db,self.user,self.activeDb)
		t1=time.time()
		self.profilo=Profilo(self.db,self.user,self.activeDb)
		t2=time.time()
		#print "TEMPO ESPORTAZIONE", (t1-t0)
		#print "TEMPO PROFILO", (t2-t1)
		self.esportazione.setAfterSelection(self.excelExport)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.esportazione.geometry()
		self.esportazione.move((screen.width()/2)-size.width()/2,(screen.height()/2)-size.width()/2)
		self.esportazione.setWindowTitle("Esportazione "+self.nomeDb.capitalize())
		self.esportazione.show()

	@pyqtSignature("")
	def on_textButton_triggered(self):
		self.esportazione=MainWindowEsportazione(self, self.db,self.user,self.activeDb)
		self.profilo=Profilo(self.db,self.user,self.activeDb)
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.Separator.geometry()
		self.Separator.move((screen.width()/2)-size.width(),(screen.height()/2)-size.height())
		self.esportazione.setAfterSelection(self.Separator.show())


