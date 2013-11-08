#!/usr/bin/python
# -*- coding: latin-1 -
from gestioneUtenti import MainWindowUserManager
from PyQt4 import QtCore as Qt
from PyQt4 import QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui =MainWindowUserManager(1)

    #util=utility(id, tables)
    #util.populateTables(id)
    #util.populateFields(ui, id)
    #util.getTcPotId(id)
    #ui.populateTable()
    ui.show()
    sys.exit(app.exec_())