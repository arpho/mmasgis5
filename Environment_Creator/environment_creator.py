# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Environment_Creator
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
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from DataSourceUser import *
from gui import *
from PyQt4 import QtGui
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from environment_creatordialog import Environment_CreatorDialog
from creazioneAmbiente import MainWindowcreazioneAmbiente
from sessionClasses import *
class Environment_Creator:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        self.gui=MainWindowcreazioneAmbiente() 
        # Create the dialog and keep reference
        self.dlg = Environment_CreatorDialog()
        # initialize plugin directory
        self.plugin_dir = QFileInfo(QgsApplication.qgisUserDbFilePath()).path() + "/python/plugins/environment_creator"
        # initialize locale
        localePath = ""
        locale = QSettings().value("locale/userLocale").toString()[0:2]
       
        if QFileInfo(self.plugin_dir).exists():
            localePath = self.plugin_dir + "/i18n/environment_creator_" + locale + ".qm"

        if QFileInfo(localePath).exists():
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
   

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/environment_creator/icon.png"), \
            u"crea il db di servizio di mmasgis", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&crea il db di servizio di mmasgis", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&crea il db di servizio di mmasgis",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    
    def setting(self,d1):
            #ds=DataSource(dbfile)
            d=QtGui.QMainWindow()
            infoString="operazione completata con successo!{0}".format(d1)
            QtGui.QMessageBox.information(d,"Info", infoString) 
            ds=DataSource(d1,True)
            
    def create(self,data):
        db=Db('mmasgisDB',-1)
        db.setUserName(data['dbUser'])
        db.setPassword(data['passDB'])
        db.setHost(data['host'])
        db.setPort(data['port'])
        db.setRDBMS(data['familyDb'])  
        user=User(data,1)      
        print "adminpwd",data['adminPass']
        user.setActiveDb(db)
        print user
        print "db",db
        ds=DataSource(user,True)
        ds.createDb(data)
        d=QtGui.QMainWindow()
        infoString="operazione completata con successo!"
        QtGui.QMessageBox.information(d,"Info", infoString) 
        self.gui.close()
        
    def run(self):
        # show the dialog
        self.gui.show()
        
        QtCore.QObject.connect(self.gui,QtCore.SIGNAL("start"),self.create)
        # Run the dialog event loop
        # See if OK was pressed

            # do something useful (delete the line containing pass and
            # substitute with your code)
        infoString="Attenzione adesso verra' creato il db di appoggio di mmasgis, insieme con l'utente di servizio e l'utente amministratore"
            #print infoString

 
            #QtGui.QMessageBox.information(d,"info", infoString)  
           # text, ok = QtGui.QInputDialog.getText(d, 'Input Dialog',"inserisci  username e password separati da '@' di un utente del db con i diritti di amministratore ")
            #converto qString in string 
          #  text=str(text)
           # username=text[0:text.find('@')]
            #pwd=text[text.find('@')+1:]
            #host, ok= QtGui.QInputDialog.getText(d, 'Input Dialog',"inserisci  l'indirizzo dell host")

            #print username,pwd,str(host)
            #dbfile="{0}:{1}@{2}".format(username,pwd,str(host))
            
           
            
