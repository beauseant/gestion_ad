'''

@author: mcanes

'''


import lib.gestionUsuarios as ad
import lib.db as db
import ConfigParser
import logging
import argparse


if __name__ == "__main__":


	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python. Envia un correo a los usuarios cuyas cuentas hayan caducado' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('log'  , action = "store", metavar='log', type=str, help='directorio donde volcar el log con los resultados')
	parser.add_argument('dias'  , action = "store", metavar='dias', type=str, help='se enviara el correo sobre las cuentas que lleven caducadas dias o mas')

	args	 =	parser.parse_args()


	logger = logging.getLogger('gestionCuentasAD')
	hdlr = logging.FileHandler( args.log )
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.INFO)

	cfg = ConfigParser.ConfigParser()
	if not cfg.read([ args.config ]):
		print 'Archivo de configuracion no encontrado :('
	else:
		try:
			nombre 		= cfg.get ( 'LDAP','nombre')
			passwd 		= cfg.get ( 'LDAP','passwd')
			basedn		= cfg.get ( 'LDAP','basedn')
			servidor	= cfg.get ( 'LDAP','servidor')
			useremail 	= cfg.get ( 'CORREO','usuario')
			passwdemail 	= cfg.get ( 'CORREO','passwd')
			servidoremail	= cfg.get ( 'CORREO','servidor')
			puertoemail	= cfg.get ( 'CORREO','puerto')
			textoemail	= cfg.get ( 'CORREO','texto')
			asuntoemail	= cfg.get ( 'CORREO','asunto')
				
		except Exception as e:
			logger.error( e )
			exit ()
	


		ListaUsrs 	= ad.gestionUsuarios ( nombre, passwd, basedn, servidor )

		remitemail	= '%s@tsc.uc3m.es'%(useremail)
		
		#Por si queremos que algun usuario no se le tenga en cuenta:
		listaBlanca	= []


		cuentasPorCaducar	= ListaUsrs.getCaducadas ( int (args.dias) )
		
		
		for usuario, datos in cuentasPorCaducar.iteritems ():
			if not (usuario in listaBlanca):
				print (usuario)
				



