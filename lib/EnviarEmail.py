import os
import socket
import smtplib
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.utils import *

class EnviarEmail:

	def __init__(self, asunto, texto, remitente, destinatario, puerto, usuario, contrasenya):
		self.__asunto__ = asunto
		self.__texto__ = texto
		self.__destinatario__ = destinatario
		self.__remitente__ = ""
		self.__servidor__ = ""
		self.__puerto__ = 25
		
		

	def enviarEmail(self):

	    COMMASPACE = ', '

	    dest_to_addrs = __destinatario__ 
	    message = MIMEMultipart()
	    message["Subject"] = __asunto__
	    message["From"] = __remitente__
	    message["To"] = __destinatario__
	    message["Date"] = formatdate(localtime=True)
	    message.attach(MIMEText(text))

	    smtp_server = smtplib.SMTP()

	    try:
		smtp_server.connect(__servidor__, __puerto__)
	    except socket.gaierror:
		print("mail error", "Wrong server, are you sure is correct?")
	    except socket.error:
		print("mail error", "Server unavailable or connection refused")

	    try:
		smtp_server.sendmail(__remitente__, dest_to_addrs, message.as_string())
	    except smtplib.SMTPRecipientsRefused:
		print("mail error", "All recipients were refused."
		      "Nobody got the mail.")
	    except smtplib.SMTPSenderRefused:
		print("mail error", "The server didnt accept the from_addr")
	    except smtplib.SMTPDataError:
		print("mail error", "An unexpected error code, Data refused")
	    smtp_server.quit()

