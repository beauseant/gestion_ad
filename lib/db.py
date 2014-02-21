# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import os
import logging
import argparse
import time

class db:

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
		    
		    
		except lite.Error, e:
		    
		    print "Error %s:" % e.args[0]
		    sys.exit(1)		    
	    

	def __del__ ( self ):
		if self._con:
			self._con.close()


	def createConnectionsTable ( self ):
		with self._con:    
			cur = self._con.cursor()    
			#cur.execute("DROP TABLE IF EXISTS connections")
			cur.execute("CREATE TABLE if not exists  connections  (name TEXT, server TEXT, cn TEXT, user TEXT)")


	def saveConnectionConfiguration ( self , name, server, cn, user):
		with self._con:    
			cur = self._con.cursor()
			cur.execute("INSERT INTO connections (name, server, cn, user) VALUES (?,?,?,?)", (name, server, cn, user)  )
			self._con.commit()

	def recoverConnectionConfiguration ( self, name ):
		with self._con:    
			cur = self._con.cursor()    
			cur.execute( "SELECT * FROM connections WHERE name=?", (name,))
			rows = cur.fetchone()
			return rows

	def recoverAllConfigurations ( self ):
		with self._con:    
			cur = self._con.cursor()    
			cur.execute( "SELECT * FROM connections")
			rows = cur.fetchall()
			return rows

