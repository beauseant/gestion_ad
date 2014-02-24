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

		    self._con.text_factory = str

		    self.createCacheTable ()  
             
		    
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
			cur.execute("SELECT rowid FROM connections WHERE name=?", (name,))
			d = cur.fetchone()
			print d
			if not (d):
				cur.execute("INSERT INTO connections (name, server, cn, user) VALUES (?,?,?,?)", (name, server, cn, user))
				self._con.commit()
			else:
				cur.execute("UPDATE connections SET name=?, server=?, cn=?, user=? WHERE rowid=? ", (name, server, cn, user,d[0]))

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
		
		
	def createCacheTable (self ):
		with self._con:    
			cur = self._con.cursor()
			cur.execute("DROP TABLE IF EXISTS cache")
			cur.execute("CREATE TABLE cache  (login TEXT, lastAccess DATE, expiryDate DATE, cn TEXT, daysFromLastAccess INT, daysToExpire INT)")
			self._con.commit()

	def saveUsersCacheTable (self, login, lastAccess, expiryDate, cn, daysFromLastAccess, daysToExpire):
		with self._con:
			cur = self._con.cursor()
			cur.execute("INSERT INTO cache  (login, lastAccess, expiryDate, cn, daysFromLastAccess, daysToExpire) VALUES (?,?,?,?,?,?)", (login, lastAccess, expiryDate, cn, daysFromLastAccess, daysToExpire))
			#self._con.commit()

			
			
		
		

