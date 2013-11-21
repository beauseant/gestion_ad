'''
Created on Jan 13, 2012

@author: breakthoven
'''



import ldap
from datetime import datetime
import lib.db as db



class gestionUsuarios:

	__usuarios = {}
	__db	   = ''
	__ldap_con = ''


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


	def __convUnixTime ( self, UnixTimesTamp, accExp = 0 ):
		MagicNumber = 116444736000000000
		if not accExp:
			MagicNumber += 86400

		return ( (UnixTimesTamp *10000000) + MagicNumber )



	def getUsr ( self, login ):
		return self.__usuarios[ login ]

	def getCaducadas ( self, dias ):

		lista = {}
		for k,v in self.__usuarios.iteritems():
			#En los windows antiguos las cuentas en las que no se ha entrado nunca figuran fechas del anno 1600 
			#(la fecha de inicio para el timestamp (1560), en algunos de los mas modernos figura un -1:
			if (not (-160000 <= v['diasParaCaducar'] <= -150000)  ) and  ( v['diasParaCaducar'] < dias ) and (v['diasParaCaducar'] <> -1):
				lista [k] = v

		return lista

	def getSinLogin (self, dias ):
		lista = {}
		for k,v in self.__usuarios.iteritems():
			if (v['diasUltimoLogin'] > dias):
				lista [k] = v

		return lista


	def setFechaCaducidad ( self, cn, fecha ):
		tstamp = int (fecha.strftime("%s"))
		#print tstamp
		fecha = str(self.__convUnixTime ( tstamp,1 ))
		#print fecha
		#print self.__convWinTime ( int ( fecha ) )
		#print cn

		attrib = [(ldap.MOD_REPLACE, 'accountExpires', fecha )]
		self.__ldap_con.modify_s( cn, attrib)   

	def borrarUsuario (self, login):
		salida = [0,'Descripcion error']

		try:
			deleteDN = self.__usuarios[login]['cn']
			self.__ldap_con.delete_s(deleteDN)
			salida [0] = 1
		except Exception as e:
			salida [1] = e
		return salida


	def generarInforme ( self ):

		self.__db = db.DataBase ( 'prueba' )


	def __init__ (self,nombre, passwd, basedn, servidor):

		self.__ldap_con = ldap.initialize( 'ldap://' + servidor )

		try:
			self.__ldap_con.protocol_version = ldap.VERSION3
			self.__ldap_con.set_option(ldap.OPT_REFERRALS, 0)
			self.__ldap_con.simple_bind_s( nombre, passwd)
			scope = ldap.SCOPE_SUBTREE
			filter = "(&(objectClass=user)(name=*))"

			attributes = ['dn','sAMAccountName','accountExpires','lastLogon']

			result = self.__ldap_con.search_s(basedn, scope, filter, attributes)
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
				datos ['cn']			= usr[0]

				self.__usuarios [ login ] = datos	

		except Exception as e:
			print(e)


	def __del__ ( self ):
			self.__ldap_con.unbind ()


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

