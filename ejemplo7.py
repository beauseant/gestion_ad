'''

@author: breakthoven

'''


import lib.gestionUsuarios as ad
import lib.db as db
import ConfigParser
from datetime import datetime, timedelta
import argparse
import logging

if __name__ == "__main__":

	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python. Elimina un usuario del directorio' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('log'  , action = "store", metavar='log', type=str, help='directorio donde volcar el log con los resultados')
	parser.add_argument('fichero'  , action = "store", metavar='usuarios', type=str, help='fichero con los usuarios que queremos eliminar')


	args	 =	parser.parse_args()

	logger = logging.getLogger('gestionCuentasAD')
	hdlr = logging.FileHandler( args.log )
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.INFO)

	cfg = ConfigParser.ConfigParser()


	if not cfg.read([ args.config ]):
		logger.error ('Archivo de configuracion no encontrado :(')
	else:
		try:
			nombre 		= cfg.get ( 'LDAP','nombre')
			passwd 		= cfg.get ( 'LDAP','passwd')
			basedn		= cfg.get ( 'LDAP','basedn')
			servidor	= cfg.get ( 'LDAP','servidor')
		except:
			exit ()

		ListaUsrs 	= ad.gestionUsuarios ( nombre, passwd, basedn, servidor )

		try:
			with open(args.fichero) as f:
    				content = f.readlines()	
		except Exception as e:
			logger.error ( e )
			
		'''
			SI QUEREMOS ELIMINAR UN USUARIO:
		'''
		for u in content:
			login = u.replace('\n','')

			try:
				usr =  ListaUsrs.borrarUsuario ( login )
				logger.info('Se ha eliminado el usuario %s'%usr['cn'])

			except Exception as e:
				logger.info( 'Usuario %s no encontrado' % (login))
				logger.error ( e )







