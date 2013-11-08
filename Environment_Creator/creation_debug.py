from DataSourceUser import *
from PyQt4 import QtCore,QtGui
from MySQLdb import *
from gui import *
from sessionClasses import *
from creazioneAmbiente import MainWindowcreazioneAmbiente

def create(data):
    db=Db('mmasgisDB',-1)
    db.setUserName(data['dbUser'])
    db.setPassword(data['passDB'])
    db.setHost(data['host'])
    db.setPort(data['port'])
    db.setRDBMS(data['familyDb'])
    user=User(data,1)
    user.setActiveDb(db)
    print " start createdb"
    ds=DataSource(user,True)
    ds.createDb(data)

app = QtGui.QApplication(sys.argv)
ui=MainWindowcreazioneAmbiente()
QtCore.QObject.connect(ui,QtCore.SIGNAL("start"),create)
ui.show()
sys.exit(app.exec_())

