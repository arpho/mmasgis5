#!/usr/bin/python
# -*- coding: latin-1 -
from settings import MainWindowSettings
from PyQt4 import QtCore as Qt
from PyQt4 import QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui =MainWindowSettings(1)

    #util=utility(id, tables)
    #util.populateTables(id)
    #util.populateFields(ui, id)
    #util.getTcPotId(id)
    #ui.populateTable()
    ui.show()
    sys.exit(app.exec_())