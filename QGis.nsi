;QGis.nsi

;--------------------------------

;The name of the installer
Name "QGis"

;The file to write
OutFile "MMASGIS.exe"

;The default installation directory
InstallDir "$PROGRAMFILES\Quantum GIS Wroclaw"
;$PROGRAMFILES==c:/programmi
;Request application privileges for Windows Vista
RequestExecutionLevel user

;--------------------------------

;Pages

Page directory
Page instfiles

;--------------------------------

;he stuff to install
Section "" ;No components page, name is not important

	;Call the standard installer for Qgis
	File QgisSetup_174.exe
	ExecWait QgisSetup_174.exe
	Goto fase1
	fase1:
	
	;Delete the installer file after the install
	Delete $INSTDIR\QgisSetup_174.exe
 
	;Set output path to the installation directory.
	SetOutPath $INSTDIR\apps
  
	;Put file there (/r is for directories recursively)
	File /r Python27
	
	;Sets directory for projects
	SetOutPath $INSTDIR\apps\qgis

	File /r cartografia
	
	;Sets directory for qgis' plugins
	SetOutPath $INSTDIR\apps\qgis\python\plugins
	
	File /r	Albero
	File /r mmasgis
	File /r Environment_Creator

	
	
SectionEnd ;end the section
