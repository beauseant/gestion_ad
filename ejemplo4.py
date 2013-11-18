import ad.gestionUsuarios as ad
import lib.db as db
import lib.enviarEmail as ee
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


		cuentasPorCaducar	= ListaUsrs.getCaducadas ( 30 )
		
		
		for usuario, datos in cuentasPorCaducar.iteritems ():
			if not (usuario in listaBlanca):
				logger.info('Enviando un correo al usuario %s' % usuario)
				textotmp = textoemail.replace('--login--', usuario)
				textotmp = textotmp.replace('--salto--', '\n')
				textotmp = textotmp.replace('--atilde--', '&aacute;')
				textotmp = textotmp.replace('--etilde--', '&eacute;')
				destemail= '%s@tsc.uc3m.es'%(usuario)
				ConfEmail = ee.enviarEmail (asuntoemail, textotmp, remitemail, destemail, servidoremail, puertoemail, useremail, passwdemail)
				ConfEmail.enviar()



