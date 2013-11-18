'''

@author: breakthoven
'''


import lib.gestionUsuarios as ad
import lib.db as db
import ConfigParser
import argparse




if __name__ == "__main__":


	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python. Muestra cuentas sin uso.' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('dias'  , action = "store", metavar='dias', type=str, help='mostrar usuarios que no entran desde, como minimo, dias')

	args	 =	parser.parse_args()



	cfg = ConfigParser.ConfigParser()
	if not cfg.read([ args.config ]):
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

		cuentasSinLogin = ListaUsrs.getSinLogin ( int (args.dias ))
		for usuario, datos in cuentasSinLogin.iteritems ():
			print 'El usuario \033[91m%s\033[0m lleva sin entrar al sistema %s dias' % (usuario,datos['diasUltimoLogin'])

