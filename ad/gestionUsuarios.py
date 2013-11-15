import ldap
from datetime import datetime
import lib.db as db

class gestionUsuarios:

	__usuarios = {}
	__db	   = ''


	#When searching the internet, you will find many formulas that use the number 11644473600. This 
	#is the number of seconds since 31-12-1601, which is used to calculate the "accountExpires"
	#value. The values "lastLogon" and "lastLogonTimeStamp" however use 01-01-1601 as the date to
	#calculate this value.
	def __convWinTime ( self, WinTimestamp, accExp = 0 ):

		MagicNumber = 11644473600
		if accExp:
			MagicNumber += 86400

		#Si queremos devolver directamente un string:
		#return datetime.fromtimestamp( (WinTimestamp /10000000) - MagicNumber ).strftime('%Y-%m-%d')
		return datetime.fromtimestamp( (WinTimestamp /10000000) - MagicNumber )


	def getUsr ( self, login ):

		return self.__usuarios[ login ]

	def getCaducadas ( self, dias ):

		lista = {}
		for k,v in self.__usuarios.iteritems():
			if (v['diasParaCaducar'] <> -1) and  ( v['diasParaCaducar'] < 30 ):
				lista [k] = v

		return lista

	def generarInforme ( self ):

		self.__db = db.DataBase ( 'prueba' )


	def __init__ (self,nombre, passwd, basedn, servidor):

		l = ldap.initialize( 'ldap://' + servidor )

		try:
			l.protocol_version = ldap.VERSION3
			l.set_option(ldap.OPT_REFERRALS, 0)
			l.simple_bind_s( nombre, passwd)
			scope = ldap.SCOPE_SUBTREE
			filter = "(&(objectClass=user)(name=*))"

			attributes = ['dn','sAMAccountName','accountExpires','lastLogon']

			result = l.search_s(basedn, scope, filter, attributes)
			'''results = [entry for dn, entry in result if isinstance(entry, dict)]'''

			fechaActual = datetime.today()

			for usr in result:
		
				#usr[0] contiene el dn del usuario, el nombre largo.
				#print usr[0]
				datos = dict ( usr[1])

				#Esto si funciona:
				#print datos['accountExpires'][0]
				#Pero esto otro no: ?????
				#print datos['lastLogon'][0]
				#Asi pues hacemos una chapuza que es preguntar con if por la clave ??????

				daysToLive 	= -1
				daysFromLogin	= -1

				for k,v in datos.iteritems():
					if k == 'lastLogon':
						lastL = v[0]
					if k == 'accountExpires':
						accExp = v[0]
					if k == 'sAMAccountName':
						login = v[0]

				#Si existe la fecha de expiracion del usuario, la sacamos. En caso contrario -1
				try:
					fechaExp = self.__convWinTime (int ( accExp ), 1  )
					daysToLive = (fechaExp - fechaActual).days
					#En los usuarios mas antiguos en caso de no existir se comporta de otra forma y devuelve este numero:
					if daysToLive == -150799:
						daysToLive = -1
				except:
					fechaExp = -1

				#Si existe la fecha de ultimo login del usuario, la sacamos. En caso contrario -1
				try:
					fechaLastL = self.__convWinTime (int ( lastL )  )
					daysFromLogin = (fechaActual - fechaLastL).days
				except:
					fechaLastL = -1


				#print 'Al usuario %s le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (login,daysToLive,daysFromLogin)
				datos = {}
				datos ['diasParaCaducar'] 	= daysToLive
				datos ['fechaCaducidad']	= fechaExp
				datos ['diasUltimoLogin']	= daysFromLogin
				datos ['fechaUltLogin']		= fechaLastL

				self.__usuarios [ login ] = datos
		
	

		except ldap.LDAPError as e:
			print(e)


