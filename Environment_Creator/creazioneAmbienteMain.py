#!/usr/bin/python
# -*- coding: latin-1 -
from creazioneAmbiente import MainWindowcreazioneAmbiente
from PyQt4 import QtCore as Qt
from PyQt4 import QtGui

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui =MainWindowcreazioneAmbiente()
    ui.show()
    sys.exit(app.exec_())