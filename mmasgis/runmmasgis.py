from plugin_anagrafica import *
import sys
from utility import *
class show():
	def __init__(self, id):
		db = MySQLdb.connect(host="localhost", user="root", passwd="ringil-87",db="parafarmacie")
		crs=db.cursor()
		crs.execute("select * from pv where pv_id={0}".format(id))
		item= crs.fetchone()
#		
		ui = Ui_MainWindow(id)
#		print ui
		#ui.text_fax.insert("test anagrafica")
		ui.checkBox_cliente.setCheckState(int(item[6]))
		ui.text_codice_mmas.setText(str(item[3]))
		ui.text_ragione_sociale.setText(str(item[8]))
		ui.text_titolare.setText(str(item[9]))
		ui.text_indirizzo.setText(str(item[11]))
		ui.lineEdit_10.setText(str(item[12]))
		ui.text_comune.setText(str(item[13]))
		ui.text_provincia.setText(str(item[14]))
		ui.text_telefono.setText(str(item[15]))
		ui.text_mail.setText(str(item[21]))
		ui.text_sito.setText(str(item[20]))
		ui.text_fax.setText(str(item[19]))
		tables=[]
		tables.append(ui.table_parametri_mmas)
		tables.append(ui.table_marchi_mmas)
		tables.append(ui.table_potenziali_mmas)
		db.close()
		util=utility(795, tables)
		util.populateTables(795)
		ui.show()
#		sys.exit(app.exec_())
