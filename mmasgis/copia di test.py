"""
/***************************************************************************
 test
                                 A QGIS plugin
 test
                              -------------------
        begin                : 2011-11-09
        copyright            : (C) 2011 by test
        email                : test@iol.it
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
import logging
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from testdialog import testDialog
import time
import logging

class test:
	
    def getTime(self):
        year=time.localtime()[0]
        month=time.localtime()[1]
        day=time.localtime()[2]
        hour=time.localtime()[3]
        min=time.localtime()[4]
        sec=time.localtime()[5]
        return"{0}:{1}:{2}:{3}/{4}/{5}".format(hour,min,sec,day,month,year)
    def log(self,title,txt):
		logging.debug(self.getTime()+" "+title+" "+str(txt))

    def __init__(self, iface):
        # Save reference to the QGIS interface
        logging.basicConfig(filename='/home/giuseppe/.qgis/log/mmasgis.log',level=logging.DEBUG)
        self.nLayers=0
        self.iface = iface
        self.textArea=None
		

    def initGui(self):
        logging.basicConfig(filename='/home/giuseppe/.qgis/log/mmasgistest.log',level=logging.DEBUG)
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/test/icon.png"), \
            "test", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run)
        
        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&test", self.action)
        
        #td.ui.textArea.insert("ciao bello txt: tst.py riga 47")
    def getSelections(self,curLayer):
	if (curLayer == None):
	  infoString = QString("No layers selected")
	  QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
	  return
	if (curLayer.type() <> curLayer.VectorLayer):
	  infoString = QString("Not a vector layer")
	  QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
	  return
	featids=curLayer.selectedFeaturesIds()
	if (len(featids) == 0):
	  infoString = QString("No features selected, using all " + str(curLayer.featureCount()) + " features")
	  QMessageBox.information(self.iface.mainWindow(),"Warning",infoString)
	  #featids = range(curLayer.featureCount())
	fProvider = curLayer.dataProvider()
	myFields = fProvider.fields()
	allFieldsNames= [f.name() for f in myFields.values()]
	#Layer0=self.iface.mapCanvas().layer("Regioni2006")
	myFieldsNames=[]
	for f in myFields.values():
	   if f.typeName() == "String":
		  myFieldsNames.append(f.name())
	if len(myFieldsNames) == 0:
	   QMessageBox.information(self.iface.mainWindow(),"Warning","No string field names. Exiting")
	   return
	elif len(myFieldsNames) == 1:
	   attrfield = myFieldsNames[0]
	else:
	  
		self.log("myFieldsname","myfieldsName "+str(myFieldsNames))
	  #res = dlgSelField(myFieldsNames)
	 # if res.exec_():
		  #
		attrfield=attrindex =myFieldsNames[0]
		self.log(" attrfield"," in test riga 101 "+attrfield)
	 # else:
		attrindex = allFieldsNames.index(attrfield)
		return attrindex 
   # adumpfile = QFileDialog.getSaveFileName(None, "save file dialog", attrfield +'.txt', "Text (*.txt)")
	selectionList =[]# open (adumpfile, 'w')
	for fid in featids:
	   features={}
	   result={}
	   features[fid]=QgsFeature()
	   curLayer.featureAtId(fid,features[fid])
	   attrmap=features[fid].attributeMap()
	   attr=attrmap.values()[attrindex]
	   logging.debug(self.getTime()+" attr "+attr.toString())
	   #fileHandle.write(attr.toString()+"\n")
	   selectionList.append(attr.toString())
	#fileHandle.close()
	return selectionList

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&test",self.action)
        self.iface.removeToolBarIcon(self.action)
    def addList(self,a,b):
		return a+b
	
    def dumpField(self):
		layersmap=QgsMapLayerRegistry.instance().mapLayers()
		selectionList=[]
		curLayer = self.iface.mapCanvas().currentLayer()
		mc=self.iface.mapCanvas() 
		self.nLayers=mc.layerCount() 
		
		for key in layersmap.iterkeys():
			self.log(" selectionList iniziale","selectionList "+str(selectionList))
			self.log("layers"," numero layers  for key={0} : ".format(key)+str(self.getSelections(layersmap[key])))
			selectionList= self.addList(selectionList,self.getSelections(layersmap[key]))
			self.log(" selectionList finale ","selectionList "+str(selectionList))
		return selectionList
		

    # run method that performs all the real work

    def run(self):

        # create and show the dialog
        curLayer = self.iface.mapCanvas().currentLayer()
        featids = range(curLayer.featureCount())
        dlg = testDialog(self.dumpField())
        # show the dialog
        dlg.show()
        result = dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code
            pass
