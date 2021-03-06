# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import logging
import argparse
import time

class DataBase:

	_name	= 'sqlite.db'
	_con	= None
	_dir	= ''
	
	def __init__ ( self, direct ):

		self._dir = direct

		try:
		    self._con = lite.connect( self._name )
		    
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


	def createConnectionsTable ( self ):
		with self._con:    
			cur = self._con.cursor()    
			cur.execute("DROP TABLE IF EXISTS connections")
			cur.execute("CREATE TABLE connections  (server TEXT, cn TEXT, user TEXT)")


	def saveConnectionConfiguration ( self , server, cn, user):
		with self._con:    
			cur = self._con.cursor()
			cur.executemany ("INSERT INTO connections (server, cn, user) VALUES (?,?,?)", server, cn, user  )
			self._con.commit()


	def recoverConnectionConfigurations ( self ):
		with self._con:    
			cur = self._con.cursor()    
			cur.execute( "SELECT * FROM connections")
			rows = cur.fetchall()
			return rows

