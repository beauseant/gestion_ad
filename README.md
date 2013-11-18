Gestión Active Directory desde Python
==========

Programa en python para gestionar los usuarios de un servidor Active Directory basado en un Windows Server 2k. Se utiliza la libreria python-ldap como base para poder realizar todas las operaciones.
--------------

Programa que muestra como acceder a un servidor Active Directory basado en Windows desde python. 

**Condiciones iniciales:**

- Tener instaladas las librerias de python: python-ldap y datetime en el sistema.
- Un fichero de configuración .ini con los datos de acceso al sistema (usuario del ldap, cn...) se muestra el fichero *configuracionejemplo.ini* como ejemplo a seguir.

**Objetivos**

- Crear una libreria que permita sacar un listado de todos los usuarios que se encuentran en el sistema. Es decir, la rama Users del active directory.
- Sacar un listado de todos los usuarios que tengan las cuentas caducadas desde X días.
- Obtener un listado de todos los usuarios que haga Y días que no entren al sistema.
- Enviar un correo a los usuarios que tengan las cuentas caducadas avisando que la cuenta caducará en breve.
- Fijar una fecha de caducidad a los usuarios que lleven Y días sin entrar al sistema.

Con esta librería, por lo tanto, es posible administrar a los usuarios de un entorno Windows desde una consola python. Se puede crear un programa que se ejecute en el cron del sistema cada 30 días y que haga un barrido de las cuentas a punto de caducar y avise a los usuarios. De esta forma, evitamos que los usuarios se encuentren las cuentas caducadas. También podemos gestionar las cuentas inactivas durante mucho tiempo para poder borrarlas o fijarles una fecha de caducidad.

La librería provee, además, herramientas para poder convertir el timestamp de sistemas Windows en un timestam de sistema Unix (y viceversa):
	
	*Convierte un Windows timestamp en un Unix timestamp:*
	def __convWinTime ( self, WinTimestamp, accExp = 0 ):

	*Convierte un Unix timestamp en un Windows timestamp:*
	def __convUnixTime ( self, UnixTimesTamp, accExp = 0 ):

Analizando el código de la libreria se pueden extraer nuevas funcionalidades que incluyan la búsqueda o la modificación de un Active Directory.


**Ejecución de los ejemplos**

	Ejemplo 1:
	python ejemplox.py fichero.ini usuario --meses 2 
	Mostraría la información de cuenta del usuario usuario y le pondría una fecha de caducidad de 2 meses. --meses es opcional.

	Ejemplo2:
	python ejemplo2.py ficheroini 30 
	Mostraria información de aquellos usuarios cuyas cuentas caducaron hace 30 días o más.


	Ejemplo3:
	python ejemplo2.py ficheroini 720 
	Mostraria información de aquellos usuarios que no han entrado al sistema, como mínimo, desde hace 720 días.


	Ejemplo4:
	python ejemplo4.py ../private/gestion_ad.ini ../tmp/loggestion.log 30
	Envia un correo avisando que la cuenta caducará en breve a todos los usuarios cuyas cuentas lleven 30 o más días caducadas.


	





