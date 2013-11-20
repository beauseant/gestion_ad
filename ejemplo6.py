'''

@author: mcanes

'''


import lib.gestionUsuarios as ad
import lib.db as db
import lib.enviarEmail as ee
from datetime import datetime
import ConfigParser
import logging
import argparse


if __name__ == "__main__":


	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python. Envia un correo a los usuarios cuyas cuentas hayan caducado' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('log'  , action = "store", metavar='log', type=str, help='directorio donde volcar el log con los resultados')

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
			useremail 	= cfg.get ( 'CORREO','usuario')
			passwdemail 	= cfg.get ( 'CORREO','passwd')
			servidoremail	= cfg.get ( 'CORREO','servidor')
			puertoemail	= cfg.get ( 'CORREO','puerto')
			infocadcuentas	= cfg.get ( 'CORREO','texto_cad')
			asuntoemail	= cfg.get ( 'CORREO','asunto_cad')
				
		except Exception as e:
			logger.error( e )
			exit ()
	
		ListaUsrs 	= ad.gestionUsuarios ( nombre, passwd, basedn, servidor )

		remitemail	= '%s@tsc.uc3m.es'%(useremail)
		destemail	= remitemail
		textoinfo	= infocadcuentas
		textoemail	= 'LISTADO DE CUENTAS CADUCADAS:\n\n'


		cuentasPorCaducar	= ListaUsrs.getCaducadas ( int (10) )
		
		
		for usuario, datos in cuentasPorCaducar.iteritems ():
			logger.info('El usuario %s tiene la cuenta caducada desde la fecha %s'%(usuario,datos ['fechaCaducidad'].strftime('%m/%d/%Y')))
			textotmp = textoinfo.replace('--login--', usuario)
			textotmp = textotmp.replace('--salto--', '\n')
			textotmp = textotmp.replace('--fechacad--', datos ['fechaCaducidad'].strftime('%m/%d/%Y'))
			textotmp = textotmp.replace('--tab--', ':')
			textoemail=textoemail + textotmp
		logger.info('Enviando correo con cuentas caducadas.')
		ConfEmail = ee.enviarEmail (asuntoemail, textoemail, remitemail, destemail, servidoremail, puertoemail, useremail, passwdemail)
		ConfEmail.enviar()



