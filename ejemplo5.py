import ad.gestionUsuarios as ad
import lib.db as db
from datetime import datetime, timedelta
import ConfigParser
import logging


if __name__ == "__main__":

	logger = logging.getLogger('gestionCuentasAD')
	hdlr = logging.FileHandler('/var/tmp/gestionCuentasAD.log')
	formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
	hdlr.setFormatter(formatter)
	logger.addHandler(hdlr) 
	logger.setLevel(logging.INFO)

	cfg = ConfigParser.ConfigParser()
	if not cfg.read(['../private/gestion_ad.ini']):
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

		listaBlanca	=['IWAM_ARCHAEOPTERIX', 'Administrador', 'com_empresa', 'gsm', 'TsInternetUser', 'ILS_ANONYMOUS_USER', 'practicas1', 'IUSR_ARCHAEOPTERIX', 'anibal', 'root']

		cuentasSinLogin = ListaUsrs.getSinLogin (720)
		for usuario, datos in cuentasSinLogin.iteritems ():
			if not (usuario in listaBlanca):
				logger.info ('El usuario %s lleva sin entrar al sistema %s dias' % (usuario,datos['diasUltimoLogin']))
				#Que caduque en cuatro meses:
				fecha_caducidad	= ((datetime.today() + timedelta(4*365/12)))
				ListaUsrs.setFechaCaducidad ( datos ['cn'], fecha_caducidad )
				logger.info ('Fijada nueva fecha de caducidad para el usuario %s a dia: %s' % (usuario,datos['diasUltimoLogin']))

