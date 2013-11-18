import ldap
from datetime import datetime



#When searching the internet, you will find many formulas that use the number 11644473600. This 
#is the number of seconds since 31-12-1601, which is used to calculate the "accountExpires"
#value. The values "lastLogon" and "lastLogonTimeStamp" however use 01-01-1601 as the date to
#calculate this value.
def convWinTime ( WinTimestamp, accExp = 0 ):

	MagicNumber = 11644473600
	if accExp:
		MagicNumber += 86400


	#return datetime.fromtimestamp( (WinTimestamp /10000000) - MagicNumber ).strftime('%Y-%m-%d')
	return datetime.fromtimestamp( (WinTimestamp /10000000) - MagicNumber )


l = ldap.initialize("ldap://ofelia.tsc.uc3m.es")
try:
	l.protocol_version = ldap.VERSION3
	l.set_option(ldap.OPT_REFERRALS, 0)
	l.simple_bind_s("administrador@tsc.uc3m.es", "S@edE3#;")
	basedn = "cn=Users,dc=tsc, dc=uc3m,dc=es"
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
			fechaExp = convWinTime (int ( accExp ), 1  )
			daysToLive = (fechaExp - fechaActual).days
		except:
			fechaExp = -1

		#Si existe la fecha de ultimo login del usuario, la sacamos. En caso contrario -1
		try:
			if ( lastL ):
				fechaLastL = -1
			else:
				fechaLastL = convWinTime (int ( lastL )  )
				daysFromLogin = (fechaActual - fechaLastL).days
		except:
			fechaLastL = -1


		print 'Al usuario %s le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (login,daysToLive,daysFromLogin)
		
	

except ldap.LDAPError as e:
	print(e)