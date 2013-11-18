import ad.gestionUsuarios as ad
import lib.db as db
import lib.enviarEmail as ee
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
			useremail 	= cfg.get ( 'CORREO','usuario')
			passwdemail 	= cfg.get ( 'CORREO','passwd')
			servidoremail	= cfg.get ( 'CORREO','servidor')
			puertoemail	= cfg.get ( 'CORREO','puerto')
			textoemail	= cfg.get ( 'CORREO','texto')
			asuntoemail	= cfg.get ( 'CORREO','asunto')
			listab		= cfg.get ( 'LISTA_BLANCA','listab')
			
			
		except:
			exit ()


		ListaUsrs 	= ad.gestionUsuarios ( nombre, passwd, basedn, servidor )

		remitemail	= '%s@tsc.uc3m.es'%(useremail)
		destemail	= 'mcanes@tsc.uc3m.es'
		
		listaBlanca	= ['IWAM_ARCHAEOPTERIX', 'Administrador', 'com_empresa', 'gsm', 'TsInternetUser', 'ILS_ANONYMOUS_USER', 'practicas1', 'IUSR_ARCHAEOPTERIX', 'anibal', 'root']

		print listaBlanca

		cuentasPorCaducar	= ListaUsrs.getCaducadas ( 30 )
		
		
		for usuario, datos in cuentasPorCaducar.iteritems ():
			if not (usuario in listaBlanca):
				print usuario
				textotmp = textoemail.replace('--login--', usuario)
				textotmp = textotmp.replace('--salto--', '\n')
				textotmp = textotmp.replace('--atilde--', '&aacute;')
				textotmp = textotmp.replace('--etilde--', '&eacute;')
				ConfEmail = ee.enviarEmail (asuntoemail, textotmp, remitemail, destemail, servidoremail, puertoemail, useremail, passwdemail)
				ConfEmail.enviar()



