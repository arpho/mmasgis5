from PyQt4 import QtCore,QtGui
from PyQt4.QtGui import QMainWindow
from PyQt4.QtCore import pyqtSignature
from Ui_selezioneQuery import *
from queriesDb import *

class SelectionQueryWindow(QMainWindow, Ui_SelectionQueryWindow):
	"""
	wrapper di Ui_SelectionQueryWindow
	"""
	def populateList(self):
		"""
		popola la tabella delle queries e' invocato dal costruttore
		"""
		# recupero le queries presenti nel db
		queries=self.db.getQueries()
		# popolotableQuery
		for q in queries:
			if q.censimento == self.censimento:
				#instanzio lo item del nome
				itemNome =self.itemMaker(q.nome,q.id)
				# instanzio lo item della descrizione
				itemDescrizione=self.itemMaker(q.descrizione,q.id)
				#numero di righe nella tabella
				n = self.tableQuery.rowCount()
				# aggiungo una riga
				self.tableQuery.setRowCount(n+1)
				#self.tableQuery.insertRow(self.tableQuery.rowCount())
				# setto la cella del nome
				self.tableQuery.setItem(n,0,itemNome)
				# setto la cella della descrizione
				self.tableQuery.setItem(n,1,itemDescrizione)
			
	def getItemId(self,row):
		"""
		recupera lo id dello item  alla riga row
		@param row: Integer
		@return: Integer
		"""
		#recupero il primo item della colonna row
		item= self.tableQuery.item(row, 0)
		Id=int( item.data(1).toString())
		return Id
	
	def itemMaker(self, txt,Id):
		"""
		genera gli elementi da inserire nella tabella
		@param txt:	String
		@param Id:	Integer  query_id
		"""
		item = QtGui.QTableWidgetItem(txt)
		# assegno lo Id al campo data1 dello item
		item.setData(1,Id)
		#setto il testo di item
		item.setText(QtGui.QApplication.translate("MainWindow", txt, None, QtGui.QApplication.UnicodeUTF8))
		#self.tabella.setHorizontalHeaderItem(c, item)
		return item
	def getSelectedItem(self):
		return self.tableQuery.selectedIndexes()[0]
	
	def __init__(self,queries,db,censimento,parent=None):
		"""
		@param queries:istanza di interrogazioni, viene usata per invocare il metodo
		 loadQuery che popola le selezioni nella finestra dei filtri
		@param db:QueriesDb, l'istanza di QueriesDb deve essere la stessa per tute la classi che lavorano su dbQuery.sql 
		"""
		# inizializzo QmainWindow
		self.queriesWin=queries
		QMainWindow.__init__(self,parent)
		mainWindow=QtGui.QMainWindow(self)
		#inizializzo la gui
		self.setupUi(self)
		#void QTableWidget::setCurrentCell ( int row, int column, QItemSelectionModel::SelectionFlags command )
		# 1 sta per selezione singola
		self.tableQuery.setCurrentCell(0,0)
		#self.tableQuery
		self.db=db
		self.censimento=censimento
		#popolo l'elenco delle queries
		self.populateList()
		
	def on_Selezione_released(self):
		#recupero lo item selezionato
		self.openQuery()
		
	def on_tableQuery_cellDoubleClicked(self, row,column):
		"""
		sul doppio click esegue self.openQuery
		"""
		self.openQuery()
		
	def openQuery(self):
		"""
		legge la query selezionata sulla gui dal db e invoca loadQuery su interrogazioni.py
		"""
		item=self.getSelectedItem()
		Id=self.getItemId(item.row())
		query= self.db.getFullQuery(Id)
		#print "selezione: {0} id: {1}, query: {2}".format(item.row(),Id,query)
		self.queriesWin.loadQuery(query)
		self.close()
		
	def getRowId(self, row):
		"""
		 ritorna lo Id dello item alla riga row
		 @param row: int 
		 @return: int id dello item
		"""
		item= self.tableQuery.item(row, 0)
		return item.data(1).toString()
		
		
