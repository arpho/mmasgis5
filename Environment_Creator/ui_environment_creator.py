# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_environment_creator.ui'
#
# Created: Tue Jun  5 12:11:51 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Environment_Creator(object):
    def setupUi(self, Environment_Creator):
        Environment_Creator.setObjectName(_fromUtf8("Environment_Creator"))
        Environment_Creator.resize(400, 300)
        self.buttonBox = QtGui.QDialogButtonBox(Environment_Creator)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))

        self.retranslateUi(Environment_Creator)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Environment_Creator.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Environment_Creator.reject)
        QtCore.QMetaObject.connectSlotsByName(Environment_Creator)

    def retranslateUi(self, Environment_Creator):
        Environment_Creator.setWindowTitle(QtGui.QApplication.translate("Environment_Creator", "Environment_Creator", None, QtGui.QApplication.UnicodeUTF8))

