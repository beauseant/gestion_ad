# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import logging
import argparse
import time

class DataBase:

	_name	= 'docs.db'
	_con	= None
	_dir	= ''
	
	def __init__ ( self, direct ):

		self._dir = direct

		try:
		    self._con = lite.connect( self._name )

		    #Base de datos solo en memoria, no se guarda nada el terminar:
		    #self._con = lite.connect( :memory )
		    
		    cur = self._con.cursor()    
		    cur.execute('SELECT SQLITE_VERSION()')
		    
		    data = cur.fetchone()
		    
		    print "SQLite version: %s" % data                
		    
		except lite.Error, e:
		    
		    print "Error %s:" % e.args[0]
		    sys.exit(1)
		    
	    

	def __del__ ( self ):
		if self._con:
			self._con.close()


	def cargarDatos ( self ):


		totales = []


		for base, dirs, files in os.walk( self._dir):
			logging.debug ( 'Cargando %s' % ( base ) )
			for fich in files:
				with self._con:    
					cur = self._con.cursor()
					with open(base + '/' + fich) as f:
						data = f.read()
						totales.append  ((fich, unicode (data, "utf-8")) )

		#Grabamos las cosas en una tabla de tipo fts4 que se supone se encuentra optimizida para buscar textos en ella:
		with self._con:    
			cur = self._con.cursor()    
			cur.execute("DROP TABLE IF EXISTS Documentos_fts4")
			cur.execute("CREATE VIRTUAL TABLE Documentos_fts4 USING fts4 (Name TEXT, Contenido TEXT)")
			cur = self._con.cursor()
			cur.executemany ("INSERT INTO Documentos_fts4 (Name, Contenido) VALUES (?,?)", totales  )
			self._con.commit()

		#Grabamos las cosas en una tabla normal que deberia dar unos resultados netamente inferiores a una tabla fts4 al buscar textos:
		with self._con:    
			cur = self._con.cursor()    
			cur.execute("DROP TABLE IF EXISTS Documentos")
			cur.execute("CREATE TABLE Documentos  (Name TEXT, Contenido TEXT)")
			cur = self._con.cursor()
			cur.executemany ("INSERT INTO Documentos (Name, Contenido) VALUES (?,?)", totales  )
			self._con.commit()



	def _lanzarConsulta ( self, consulta ):
		with self._con:    
			cur = self._con.cursor()    
			cur.execute( consulta )
			rows = cur.fetchall()
			return rows


	def buscarPalabra ( self, palabra,fts4 = 0 ):

		#¿Queremos hacer la busqueda en la tabla fts4 o en una tabla normal?

		if not (fts4):
			return self._lanzarConsulta ( "SELECT rowid, Name FROM " + 'Documentos' + " WHERE Contenido LIKE '%" + palabra + "%'" )
		else:
			return self._lanzarConsulta ( "SELECT rowid, Name FROM " + 'Documentos_fts4' + " WHERE Contenido MATCH '" + palabra + "'" )
