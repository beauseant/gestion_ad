'''

@author: breakthoven

'''


import lib.gestionUsuarios as ad
import lib.db as db
import ConfigParser
from datetime import datetime, timedelta
import argparse

if __name__ == "__main__":

	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python. Muestra informacion de usuario y pone caducidad a la cuenta' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('usuario'  , action = "store", metavar='usuario', type=str, help='usuario que queremos mostrar')
	parser.add_argument('--meses'  , action = "store", metavar='meses', type=str, help='los meses en los que queremos que caduque esa cuenta')



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

		'''
			SI QUEREMOS SACAR DATOS INDIVIDUALES DE UN USUARIO:
		'''

		login		=  args.usuario
		try:
			usr		=  ListaUsrs.getUsr ( login )
			print 'Al usuario %s le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (login,usr['diasParaCaducar'],usr['diasUltimoLogin'])
			print '\t\t\t Fecha caducidad: %s, fecha ult login: %s' % (usr['fechaCaducidad'],usr['fechaUltLogin'])
			print '\t\t\t CN: % s' % ( usr['cn'] )


			#Que caduque en x meses:
			if args.meses:
				fecha_caducidad	= ((datetime.today() + timedelta( int(args.meses) * 365/12)))
				print 'Fijando fecha de caducidad para el usuario %s en %s' % (login, fecha_caducidad)
				ListaUsrs.setFechaCaducidad ( usr ['cn'], fecha_caducidad )



		except Exception as e:
			print '\033[91mUsuario %s no encontrado\033[0m' % (login)
			print e





