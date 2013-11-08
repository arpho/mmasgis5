#!/usr/bin/python
# -*- coding:latin-1 -
from esportazione import *
from PyQt4 import QtCore as Qt
from Profilo import *



if __name__=="__main__":
	import sys
	app=QtGui.QApplication(sys.argv)
	p=Profilo()
	ui=MainWindowEsportazione(1)
	ui.show()
	sys.exit(app.exec_())
