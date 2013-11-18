import ad.gestionUsuarios as ad
import lib.db as db
import ConfigParser


if __name__ == "__main__":


	cfg = ConfigParser.ConfigParser()
	if not cfg.read(['/home/sblanco/Documents/Trabajo/RepositorioGit/private/gestion_ad.ini']):
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
		ListaUsrs.generarInforme ()




