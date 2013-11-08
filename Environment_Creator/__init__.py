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
 This script initializes the plugin, making it known to QGIS.
"""
def name():
    return "mmasgisDB"
def description():
    return "inizializzal'ambiente dimmasgis"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface):
    # load Environment_Creator class from file Environment_Creator
    from environment_creator import Environment_Creator
    return Environment_Creator(iface)
