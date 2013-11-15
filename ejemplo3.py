import ad.gestionUsuarios as ad
import lib.db as db
import ConfigParser




if __name__ == "__main__":


	cfg = ConfigParser.ConfigParser()
	if not cfg.read(['../private/gestion_ad.ini']):
		print 'Archivo de configuracion no encontrado :('
	else:
		try:
			nombre 		= cfg.get ( 'LDAP','nombre')
			passwd 		= cfg.get ( 'LDAP','passwd')
			basedn		= cfg.get ( 'LDAP','basedn')
			servidor	= cfg.get ( 'LDAP','servidor')
		except:
			exit ()


		ListaUsrs 	= ad.gestionUsuarios ( nombre, passwd, basedn, servidor )

		cuentasSinLogin = ListaUsrs.getSinLogin (720)
		for usuario, datos in cuentasSinLogin.iteritems ():
			print 'El usuario \033[91m%s\033[0m lleva sin entrar al sistema %s dias' % (usuario,datos['diasUltimoLogin'])

