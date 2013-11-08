from DataSourceUserWithClasses import *
from PyQt4 import QtCore,QtGui
from MySQLdb import *
from gui import *

user={'uname':'root','pwddb':'vilu7240','passAdmin':'metmi'}
user['familyDb']='mysql5'
user['host']='localhost'

ds=DataSource(user,True)