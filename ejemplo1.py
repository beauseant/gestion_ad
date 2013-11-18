import ad.gestionUsuarios as ad
import lib.db as db
import ConfigParser
from datetime import datetime, timedelta

def add_months(sourcedate,months):
	month = sourcedate.month - 1 + months
	year = sourcedate.year + month / 12
	month = month % 12 + 1
	day = min(sourcedate.day,calendar.monthrange(year,month)[1])
	return datetime.date(year,month,day)

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
		except:
			exit ()


		ListaUsrs 	= ad.gestionUsuarios ( nombre, passwd, basedn, servidor )

		'''
			SI QUEREMOS SACAR DATOS INDIVIDUALES DE UN USUARIO:
		'''

		login		= 'mcanes'
		try:
			usr		=  ListaUsrs.getUsr ( login )
			print 'Al usuario %s le caduca la cuenta en %s dias, y hace %s dias que no entra al sistema' % (login,usr['diasParaCaducar'],usr['diasUltimoLogin'])
			print '\t\t\t Fecha caducidad: %s, fecha ult login: %s' % (usr['fechaCaducidad'],usr['fechaUltLogin'])
			print '\t\t\t CN: % s' % ( usr['cn'] )

			#Que caduque en dos meses:
			#fecha_caducidad	= ((datetime.today() + timedelta(2*365/12)))


			#print fecha_caducidad
			#ListaUsrs.setFechaCaducidad ( usr ['cn'], fecha_caducidad )


		except Exception as e:
			print '\033[91mUsuario %s no encontrado\033[0m' % (login)
			print e





