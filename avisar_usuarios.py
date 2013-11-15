import ad.gestionUsuarios as ad
import lib.db as db
import ConfigParser


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''



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

		'''
			SI QUEREMOS SACAR DATOS INDIVIDUALES DE UN USUARIO:
		'''

		login		= 'sblanco'
		usr		=  ListaUsrs.getUsr ( login )

		print 'Al usuario %s le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (login,usr['diasParaCaducar'],usr['diasUltimoLogin'])
		print '\t\t\t Fecha caducidad: %s, fecha ult login: %s' % (usr['fechaCaducidad'],usr['fechaUltLogin'])


		'''
			SI QUEREMOS SACAR DATOS GENERALES DE FECHAS:
		'''
	
		#Usuarios cuya fecha caducidad en dias < que parametro (se descarta los que no tengan fecha de caducidad asignada)
		cuentasPorCaducar	= ListaUsrs.getCaducadas ( 30 )

		for usuario, datos in cuentasPorCaducar.iteritems ():
			if ( datos['diasParaCaducar'] < 0 ):
				print 'Al usuario \033[91m%s\033[0m le ha caducado la cuenta en %s dias, y hace %s dias que no entra al sistema' % (usuario,datos['diasParaCaducar'],datos['diasUltimoLogin'])
			else:
				print 'Al usuario \033[92m%s\033[0m le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (usuario,datos['diasParaCaducar'],datos['diasUltimoLogin'])


		ListaUsrs.generarInforme ()





