#!/usr/bin/python
# -*- coding: latin-1 -*-
from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
#from dbDict import *
from Ui_anagrafica import *
from utility import *
from interrogazioni import *
from Ui_risultati import Ui_MainWindowResults
from mysql_sqlalchemy_class import Pv,rel_pv_pot
from datetime import *
import time
from Entity import *

#@todo: TODO save codice MMas
#@todo:  fix a savedata add time
#@todo: ODO fix checkbox all 
#@todo: sistemare flags anagrafica modificata

class Click():
	"""
	 questa classe implementa un timer
	 per risolvere un problema sui tasti di navigazione di anagrafica, sono troppo sensibili  e sulla lista dei risultati avanza a 2 alla volta
	 questo problema e' sorto dopo aver sostituito i QPushButton con dei QAction all'interno della toolbar
	 il costruttore e' un costruttore standard, non richiede nessun parametro
	 @param started: boolean registra lo stato del timer se lanciato e' True, altrimenti e' False
	 @param start: float memorizza il timestamp in cui il timer viene lanciato
	 @param end:float memorizza il temestamp in cui viene fermato il timer   
	"""
	def __init__(self):

		self.started=False	
		self.start=self.end=None
		
	def click(self,t):
		
		"""
		lancia il timer e lo resetta ogni volta che viene invocato 
		@param t:int timeout del click o meglio soglia di tempo al di sotto della quale non si vuole percepire il click sul pulsante e il metodo ritornera' False
		@return boolean:True al primo avvio e se self.end-self.start>t  
		"""
		b=False
		if not self.started:
			#avvio il timer
			self.start=time.clock()
			# setto il timere started a True
			self.started=True
			#setto il valore di ritorno
			b=True
			
			
			
		else:
			
			self.started=False
			self.end=time.clock()
			#print " end at {0}".format(self.end)
			if self.end is not None:
				pass
			
			if (self.end-self.start)>t:
				# reset tempo di start
				self.start= time.clock()
				
				b=True
		#print "clicked :{0} ".format(b)
		return b


class Saver():
	"""
	implementa il saver dei parametri dell'anagrafica,
	 il costruttore richiede come parametro la funziona che salva il parametro,
	 questa puo' essere di qualsiasi tipo, rendendo quest'oggetto molto flessibile: il parametro da salvare
	  viene settato nel metodo che gli viene passato, questo e' eseguito invocando il metodo Saver.save()  
	"""
	def __init__(self,func):
		self.func=func
	def save(self):
		self.func



class MainWindowAnagrafica(QMainWindow, Ui_MainWindowAnagrafica):
	"""
	wrapper di Ui_MainWindowAnagrafica
	"""
	
	def closeEvent(self, event):
		reply=QtGui.QMessageBox.No
		if self.changed:
			infoString=QtCore.QString("la scheda è stata modificata")
			reply=QtGui.QMessageBox.question(self, infoString,    "vuoi salvare le modifiche?", QtGui.QMessageBox.Yes |     QtGui.QMessageBox.No, QtGui.QMessageBox.No)
			return reply
					

	def __init__(self,Id,risultati,user,db,parent=None):
			self.click=Click()
			self.brandClass=None
			self.user=user
			self.activeDb=db
			"""questo parametro memorizza il lo item della tabella marchi che deve rimanere visualizzato durante il browsing delle anagrafiche"""
			self.tcpot=None
			self.changed=False
			self.tables=[]
			self.id=Id
			self.risultati=risultati
			QMainWindow.__init__(self,parent)
			self.w=Ui_MainWindowAnagrafica()
			self.toSave={}
			self.dateChanged=True
			self.saveFunctions={}
			self.util=None
			self.setupUi(self)
			# inizializzo la variabile self.util che poi istranzio al suo vero valore
			self.connect(self.table_marchi_classe, SIGNAL('cellClicked(int,int)'),self.doIt)
			#self.connect(self.text_note, SIGNAL('textEdited(int,int)'),self.on_text_note_textEdited)  
			self.instantiateUtil()
			self.p=self.util.getPv(self.id)
			#popolo i campi della gui
			self.util.populateFields(self, Id)			
			"""#QtextEdit non possiede il segnale textedited quindi
			# quqndo il campo note viene popolato da populateFields la scheda risulta alterata anche se non lo è
			per riportarla a not modified
			"""
			self.setSaved()
			self.util.populateTables(Id)
			
			#se;f.p e' il record che sto visualizzando

			#self.salvaButton.setEnabled(False)
			# gestisco la chiusura della gui
			self.connect(self, QtCore.SIGNAL('triggered()'), self.closeEvent )
			
	def setBrand(self,b):
		"""setter di self.brand
		@note: self.brand memorizza lo item della tabella marchi che deve rimanere visualizzato
		@param b:Item """
		self.brandClass=b 
		
	def getBrand(self):
		"""getter di self.brand
		@return Item se il brand e' stato settato, altrimenti ritorna -1
		"""
		if self.brandClass is not None:
			return self.brandClass
		else:
			return -1
		
	def populateBrands(self,item):
		"""popola la tabella dei marchi relativi allo item passato
		@param item: Item della tabella marchi
		"""
		#cancello table_marchi
		self.table_marchi.clear()
		self.table_marchi.setRowCount(0)
		brands= self.util.getBrands4class_pv(item,self.id)
		odictBrands=self.util.brandsAdapter(brands)
		self.util.tablePopulator(self.table_marchi,odictBrands)
		 
		
	
		
			
	def doIt(self, row,column):
		self.table_marchi.clearContents()
		self.table_marchi.setRowCount(0)
		item= self.table_marchi_classe.item(row,column)	
		# setto che è stato cercato un brand per bloccare la tabella durante il browsing delle anagrafiche
		self.setBrand(item.data(1).toInt()[0])
		self.populateBrands(item.data(1).toInt()[0])
			
	

	def save(self):
		if len(self.saveFunctions)>0:
			self.setSaved()
		for key in self.saveFunctions.iterkeys():
			#self.saveFunctions[key]
			self.saveFunctions[key].save()
		result= self.util.sessionCommit()
		#self.saveFunctions.clear()
		if result is None:
			infoString="esito salvataggio "
			QtGui.QMessageBox.information(self, infoString,    "scheda {0} modificata correttamente".format(self.id))
		else:
			infoString="esito salvataggio"
			QtGui.QMessageBox.information(self, infoString,    "problemi durante il salvataggio delle modifiche")
	

		
	def setId(self,Id):
		self.id=Id
	def setTcPotId(self,tcpot):
		self.tcpot=tcpot
	def setChanged(self):
		self.changed=True
		#self.salvaButton.setEnabled(True)
	def setSaved(self):
		"""
		setta self.changed a False
		e disabilita salvaButton
		"""
		self.changed=False
		#self.salvaButton.setEnabled(False)
		
	def saveCod_MMAS(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.cod_mmas=value
	def on_text_codice_mmas_textEdited(self, p0):
		s=Saver(self.saveCod_MMAS(self.text_codice_mmas.text()))
		self.saveFunctions['cod_mmas']=s
		self.setChanged()
		
	def instantiateUtil(self):
			"""
			instanzia la classe util
			@param None:
			@return: None 
			"""
			#svuoto la lista delle tabelle
			self.tables={}
			self.tables['parametro']=self.table_parametri_mmas
			self.tables['marca']=self.table_marchi_classe
			self.tables['potenziale']=self.table_potenziali_mmas
			self.util=utility(self.id, self.tables,self.user,self.activeDb,True)
	

	def populateAnagrafica(self, Id):
		"""
		si occupa di popolare i campi e le tabelle dell'anagrafica
		@param Id:	Integer 
		"""
			# mi serve un riferimento al pv dell'anagrafica per poter salvare le modifiche ora sarebbe bello fare un refactoring e portare populateFields almeno in anagrafica
			#self.p=self.util.getPv(Id)
		if self.util is None:
			self.instantiateUtil()
		self.util.populateTables(self.id)
		self.util.populateFields(self, self.id)
	def savePotenziale(self,value):
		self.tcpot.valore=value
	def on_lineEdit_3_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.savePotenziale(self.lineEdit_3.text()))
		self.saveFunctions['provincia']=s
		self.setChanged()

	@pyqtSignature("QString")
	def saveRagioneSociale(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""
	
		self.p.ragione_sociale=unicode(value)#self.toSave['ragione_sociale']
	def on_text_ragione_sociale_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s= Saver(self.saveRagioneSociale(self.text_ragione_sociale.text()))
		#self.toSave['ragione_sociale']=self.text_ragione_sociale.text()
		self.saveFunctions['ragione_sociale']=s
		
		self.setChanged()
	@pyqtSignature("QString")
	def saveTitolare(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""
	
		self.p.titolare=unicode(value)
	def on_text_titolare_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveTitolare(self.text_titolare.text()))
		self.saveFunctions['titolare']=s
		self.setChanged()

	def saveIndirizzo(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""
	
		self.p.indirizzo=unicode(value)
	def on_text_indirizzo_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveIndirizzo(self.text_indirizzo.text()))
		self.saveFunctions['indirizzo']=s
		self.setChanged()
		
	def saveTelefono(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.tel1=value
		
	@pyqtSignature("QString")
	def on_text_telefono_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveTelefono(self.text_telefono.text()))
		self.saveFunctions['telefono']=s
		self.setChanged()

	def saveNote(self,value):
		self.p.note=unicode(value)

	def on_text_note_textChanged(self):
		if self.text_note.toPlainText()!=self.p.note:
			s=Saver(self.saveNote(self.text_note.toPlainText()))
			self.saveFunctions['nota']=s
			self.setChanged()
		
	def saveCodiceCliente(self,value):


		self.p.cod_cliente=value
		
	@pyqtSignature("QString")
	def on_text_codice_cliente_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveCodiceCliente(self.text_codice_cliente.text()))
		self.saveFunctions['codice_cliente']=s
		self.setChanged()

	@pyqtSignature("int")
	def conditioningCheckBoxState(self,s):
		if s>0:
			return 1
		else:
			return 0

	def saveCliente(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.cliente=value
	def on_checkBox_cliente_stateEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		self.toSave['cliente']=self.conditioningCheckBoxState(self.checkBox_cliente.checkState())
		self.saveFunctions['cliente']=self.saveCliente()
		self.setChanged()
		
	def saveMail(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.email=value
	@pyqtSignature("QString")
	def on_text_mail_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveMail(self.text_mail.text()))
		self.saveFunctions['email']=s
		self.setChanged()


	def saveSito(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.sito=value
	@pyqtSignature("QString")
	def on_text_sito_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveSito(self.text_sito.text()))
		self.saveFunctions['sito']=s
		self.setChanged()
		
	def saveCap(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.cap=unicode(value)

	
	

	@pyqtSignature("QString")	
	def on_lineEdit_10_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveCap(self.lineEdit_10.text()))
		self.saveFunctions['cap']=s
		self.setChanged()
		
	def saveFax(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.fax=value

	@pyqtSignature("QString")
	def on_text_fax_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveFax(self.text_fax.text()))
		self.saveFunctions['fax']=s
		self.setChanged()
		
	def saveProvincia(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.provincia=value

	@pyqtSignature("QString")
	def on_text_provincia_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveProvincia(self.text_provincia.text()))
		self.saveFunctions['provincia']=s
		self.setChanged()
	#def on_lineEdit_3_textEdited(self,p0):
	def saveTelefono2(self):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.tel2=self.toSave['telefono2']	

	@pyqtSignature("QString")
	def on_lineEdit_13_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=self.saveTelefono2(self.lineEdit_13.text())
		self.saveFunctions['telefono2']=s
		self.setChanged()

	@pyqtSignature("QString")
	def on_text_certificazione_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		self.setChanged()

	def saveComune(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""
		self.p.comune=unicode(value)
	@pyqtSignature("QString")
	def on_text_comune_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveComune(self.text_comune.text()))
		self.saveFunctions['comune']=s
		self.setChanged()


	def saveCF(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""

		self.p.cf_pi=unicode(value)
		
	@pyqtSignature("QString")
	def on_text_codice_fiscale_textEdited(self, p0):
		"""
		Slot documentation goes here.
		"""
		s=Saver(self.saveCF(self.text_codice_fiscale.text()))
		self.saveFunctions['cf']=s
		self.setChanged()

	def saveCertificato(self,value):
		self.p.certificato=value

	@pyqtSignature("int")
	def on_checkBox_anagrafica_stateChanged(self, p0):
		"""
		anagrafica certificata
		"""
		s=Saver(self.saveCertificato(self.checkBox_anagrafica.isChecked()))
		self.saveFunctions['certificato']=s
		self.setChanged()



	def saveData(self,value):
		"""
		devo instanziare un paio di oggetti per poter aggiungere la funzione nel dizionario
		"""
		today = QtCore.QDate.currentDate()		
		#qdate=QtCore.QDate(value.year(),value.day(),value.month())
		#perche' la data venga salvata devo convertirla in stringa
		self.p.data_aggiornamento="{0}-{1}-{2}".format(value.year(),value.month(),value.day())#il formato per salvare una data in mysql e' anno-mese-giorno
		print self.p.data_aggiornamento
		
	def oon_date_aggiornamento_dateChanged(self,p0):
		if self.dateChanged==False:
			s=Saver(self.saveData(self.date_aggiornamento.date()))
			self.saveFunctions['data_aggiornamento']=s
			#print self.toSave['data_aggiornamento']
			self.setChanged()
		else:
			self.dateChanged= False

		#print self.date_aggiornamento.date().year()

	def clearTable(self, table):
		"""
		svuota la tabella passata come parametro
		@param table:QTableWidget 
		"""
		#cancello il contenuto
		table.clearContents()
		#azzero le dimensioni della table
		table.setRowCount(0)
				
	def clearTables(self):
		"""
		cancella tutte le tabelle
		"""
		for t in self.tables.iterkeys():
			self.clearTable(self.tables[t])
			
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
			d['marche']=i 
			d['Id']=-1
			li.append(d)
		return li
		
			
	def oon_table_marchi_classe_cellClicked(self, row,column):
		self.table_marchi.clearContents()
		self.table_marchi.setRowCount(0)
		item= self.table_marchi_classe.item(row,column)	
		brands= self.util.getBrands4class_pv(item.data(1).toInt()[0],self.id)
		odictBrands=self.brandsAdapter(brands)
		self.util.tablePopulator(self.table_marchi,odictBrands)
	
	@pyqtSignature("")
	def on_nextButton_triggered(self):
		"""
		presenta la scheda relativa al pv successivo nella lista dei risultati
		"""
		#aggiorno lo id dell'anagrafica corrente
		# chiudo la scheda attuale
		reply=self.closeEvent("er")
		if reply==QtGui.QMessageBox.Yes:
			self.save()
			self.saveFunctions.clear()
			self.setSaved()
			
		self.id= self.risultati.getNext()
		#print "carico scheda per ",self.id
		#aggiorno l'oggetto pv
		self.p=self.util.getPv(self.id)
		#aggiorno il valore di self.id in utility
		self.util.setId(self.id)
		self.clearTables()
		self.populateAnagrafica(self.id)
		item=self.getBrand()
		#se diverso da -1 allora la tabella dei brands e' stata popolata
		if item!=-1:
			self.populateBrands(item)
		#pongo lo stato a non modificato
		self.setSaved()
	
	@pyqtSignature("")	
	def on_previousButton_triggered(self):
		#chiedo di salvare eventuali modifiche
		reply=self.closeEvent("er")
		if reply==QtGui.QMessageBox.Yes:
			self.save()
			self.saveFunctions.clear()
			self.setSaved()
		self.id= self.risultati.getPrevious()
		#aggiorno il valore di self.id in utility
		self.util.setId(self.id)			
		self.clearTables()
		self.populateAnagrafica(self.id)
		item=self.getBrand()
		#se diverso da -1 allora la tabella dei brands e' stata popolata
		if item!=-1:
			self.populateBrands(item)
		#pongo lo stato a non modificato
		self.setSaved()
	
	@pyqtSignature("")	
	def on_lastButton_triggered(self):
		#chiedo di salvare eventuali modifiche
		reply=self.closeEvent("er")
		if reply==QtGui.QMessageBox.Yes:
			self.save()
			self.saveFunctions.clear()
			self.setSaved()
		self.id= self.risultati.getLast()
		#aggiorno il valore di self.id in utility
		self.util.setId(self.id)
		self.clearTables()	
		self.populateAnagrafica(self.id)
		item=self.getBrand()
			#se diverso da -1 allora la tabella dei brands e' stata popolata
		if item!=-1:
				# se devo aggiornare la tabella self.table_marchi, devo prima ripulirla
				self.clearTable(self.table_marchi)
				self.populateBrands(item)
			#pongo lo stato a non modificato
		self.setSaved()
	
	@pyqtSignature("")	
	def on_firstButton_triggered(self):
		#chiedo di salvare eventuali modifiche
		reply=self.closeEvent("er")
		if reply==QtGui.QMessageBox.Yes:
			self.save()
			self.saveFunctions.clear()
			self.setSaved()
		Id= self.risultati.getFirst()
		self.id=Id
		#aggiorno il valore di self.id in utility
		self.util.setId(self.id)
		self.clearTables()	
		self.populateAnagrafica(self.id)
		item=self.getBrand()
			#se diverso da -1 allora la tabella dei brands e' stata popolata
		if item!=-1:
				# se devo aggiornare la tabella self.table_marchi, devo prima ripulirla
				self.clearTable(self.table_marchi)
				self.populateBrands(item)
			#pongo lo stato a non modificato
		self.setSaved()
	
	@pyqtSignature("")	
	def on_savemodButton_triggered(self):
		#print "salvando"
		self.setSaved()
		if self.click.click(0.5):
			self.save()	
			self.saveFunctions.clear()
		
	@pyqtSignature("")	
	def on_pdfButton_triggered(self):
		filepdf=QFileDialog(self)
		filepdf.setFileMode(0)
		pdfFile=filepdf.getSaveFileName(self,"esportazione anagrafica in pdf","*.pdf",filter="(*.pdf)")
		dummy=Entity2Export("esportazione anagrafica in pdf", False, self.id, self.user, self.activeDb, self.util.getDb(),'anagrafica')
		headers=dummy.getAvailableEntity()
		values=[]
		for i in headers:
			values.append(dummy.getValue(self.id, i))
		self.util.writeReportLab(headers,values,pdfFile,dummy.getValue(self.id,'ragione sociale'),self.id)
		infoString="Scheda anagrafica esportata correttamente"
		d=QtGui.QMainWindow()
		QtGui.QMessageBox.information(d,"Info", infoString)
			

