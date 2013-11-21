'''

@author: mcanes

'''



import lib.gestionUsuarios as ad
import lib.db as db
from datetime import datetime, timedelta
import ConfigParser
import logging
import argparse


if __name__ == "__main__":

	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python.Fija una fecha de caducidad a los usuarios con cuentas inactivas' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('log'  , action = "store", metavar='log', type=str, help='directorio donde volcar el log con los resultados')
	parser.add_argument('dias'  , action = "store", metavar='dias', type=str, help='se fija la caducidad para usuarios que no entran desde, como minimo, dias')
	parser.add_argument('meses'  , action = "store", metavar='meses', type=str, help='se fija la caducidad a esas cuentas para meses')

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

		listaBlanca	=[]

		cuentasSinLogin = ListaUsrs.getSinLogin (int (args.dias) )
		for usuario, datos in cuentasSinLogin.iteritems ():
			if not (usuario in listaBlanca):
				logger.info ('El usuario %s lleva sin entrar al sistema %s dias' % (usuario,datos['diasUltimoLogin']))
				#Que caduque en cuatro meses:
				fecha_caducidad	= ((datetime.today() + timedelta( int (args.meses) *365/12)))
				ListaUsrs.setFechaCaducidad ( datos ['cn'], fecha_caducidad )
				logger.info ('Fijada nueva fecha de caducidad para el usuario %s a dia: %s' % (usuario,datos['diasUltimoLogin']))

