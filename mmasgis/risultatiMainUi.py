from PyQt4 import QtCore, QtGui
from risultati import *


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui =MainWindowResults({(2284L,): '', (2260L,): '', (270L,): '', (271L,): '', (750L,): '', (1068L,): ''} )
    #ui.populateTable()
    ui.show()
    sys.exit(app.exec_())
