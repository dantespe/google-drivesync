import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def notify(contact, error, subject='Error'):
	msg = MIMEMultipart('alternative')
	msg['Subject'] = subject
	msg['From'] = contact
	msg['To'] = contact

	text = MIMEText(error, 'plain')

	msg.attach(text)

	server = smtplib.SMTP('localhost')
	server.sendmail(contact, contact, msg.as_string())
	server.quit()
