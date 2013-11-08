"""
/***************************************************************************
 mmasgis
                                 A QGIS plugin
 micromarketing analisys plugin
                             -------------------
        begin                : 2011-11-09
        copyright            : (C) 2011 by test
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
    return "mmasgis"
def description():
    return "mmasgis"
def version():
    return "Version 0.1"
def icon():
    return "icon.png"
def qgisMinimumVersion():
    return "1.0"
def authorName():
  return "Giuseppe"
def classFactory(iface):
    # load test class from file test
    from mmasgis import mmasgis
    return mmasgis(iface)
