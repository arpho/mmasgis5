#!/usr/bin/python
# -*- coding: latin-1 -
from gui import *
from PyQt4 import QtCore as Qt
from gui import *

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui =MainWindowGui()
    ui.show()
    sys.exit(app.exec_())