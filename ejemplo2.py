'''

@author: breakthoven
'''

import lib.gestionUsuarios as ad
import lib.db as db
import ConfigParser
import argparse



if __name__ == "__main__":

	parser	= argparse.ArgumentParser ( description='Gestion de un Active Directory desde python. Muestra cuentas caducadas.' )

	parser.add_argument('config'  , action = "store", metavar='config', type=str, help='fichero de configuracion')
	parser.add_argument('dias'  , action = "store", metavar='dias', type=str, help='mostrar cuentas caducadas hace dias')

	args	 =	parser.parse_args()



	cfg = ConfigParser.ConfigParser()
	if not cfg.read([ args.config]):
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
			SI QUEREMOS LAS CUENTAS CADUCADAS HACE X DIAS:
		'''

		#Usuarios cuya fecha caducidad en dias < que parametro (se descarta los que no tengan fecha de caducidad asignada)
		cuentasPorCaducar	= ListaUsrs.getCaducadas ( int (args.dias) )

		for usuario, datos in cuentasPorCaducar.iteritems ():
			if ( datos['diasParaCaducar'] < 0 ):
				print 'Al usuario \033[91m%s\033[0m le ha caducado la cuenta en %s dias, y hace %s dias que no entra al sistema' % (usuario,datos['diasParaCaducar'],datos['diasUltimoLogin'])
			else:
				print 'Al usuario \033[92m%s\033[0m le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (usuario,datos['diasParaCaducar'],datos['diasUltimoLogin'])
