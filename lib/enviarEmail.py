import os
import socket
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.utils import *

class enviarEmail:
	__prueba 	= ""
	__asunto 	= ""
	__texto 	= ""
	__remitente 	= ""
	__destinatario 	= ""
	__servidor 	= ""
	__puerto 	= 0
	__usuario  	= ""

	def __init__(self, asunto, texto, remitente, destinatario, servidor, puerto, usuario, contrasenya ):
		self.__prueba 		= texto
		self.__asunto 		= asunto
		self.__texto 		= texto
		self.__remitente 	= remitente
		self.__destinatario 	= destinatario
		self.__servidor 	= servidor
		self.__puerto 		= puerto
		self.__usuario 		= usuario
		
		
	def enviar(self):

	    COMMASPACE = ', '

	    dest_to_addrs = self.__destinatario 
	    message = MIMEMultipart()
	    message["Subject"] = self.__asunto
	    message["From"] = self.__remitente
	    message["To"] = self.__destinatario
	    message["Date"] = formatdate(localtime=True)
	    message.attach(MIMEText(self.__texto))

	    smtp_server = smtplib.SMTP()

	    try:
		smtp_server.connect(self.__servidor, self.__puerto)
	    except socket.gaierror:
		print("mail error", "Wrong server, are you sure is correct?")
	    except socket.error:
		print("mail error", "Server unavailable or connection refused")

	    try:
		smtp_server.sendmail(self.__remitente, dest_to_addrs, message.as_string())
	    except smtplib.SMTPRecipientsRefused:
		print("mail error", "All recipients were refused."
		      "Nobody got the mail.")
	    except smtplib.SMTPSenderRefused:
		print("mail error", "The server didnt accept the from_addr")
	    except smtplib.SMTPDataError:
		print ( "mail error", "An unexpected error code, Data refused" )

	    smtp_server.quit()

	    #print 'Se ha enviado un correo electronico a %s'%(self.__destinatario)

