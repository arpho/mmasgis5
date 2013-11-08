# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Environment_CreatorDialog
                                 A QGIS plugin
 inizializzal'ambiente dimmasgis
                             -------------------
        begin                : 2012-06-05
        copyright            : (C) 2012 by Giuseppe/metmi
        email                : damicogiuseppe77@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui
from ui_environment_creator import  Ui_Environment_Creator
# create the dialog for zoom to point
class Environment_CreatorDialog(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        # Set up the user interface from Designer.
        self.ui = Ui_Environment_Creator()
        self.ui.setupUi(self)
