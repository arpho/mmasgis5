"""
/***************************************************************************
 Albero
                                 A QGIS plugin
 permette di selezionare rapidamente gli elementi di un progetto qgis tramite una struttura ad albero
                             -------------------
        begin                : 2012-04-06
        copyright            : (C) 2012 by Giuseppe D'Amico
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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "selezione tramite albero"
def description():
    return "permette di selezionare rapidamente gli elementi di un progetto qgis tramite una struttura ad albero"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load Albero class from file Albero
    from albero import Albero
    return Albero(iface)
