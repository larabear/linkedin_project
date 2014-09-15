import sys
import smtplib
import email.utils
from email.mime.text import MIMEText
def main(companyName):
	lines = open('EmailList').read().splitlines()
	for line in lines:
		x=line.split(",")
		if companyName in x[2]:
			emailPerson(x[0],x[1],companyName)

def emailPerson(emailAddr, name, company):
	sender = ""#sender's email, please fill in
	server = 'mail.server.com'
	user = ''
	password = ''
	msg = MIMEText('Body of the message....')
	msg['To'] = email.utils.formataddr(('Recipient', emailAddr))
	msg['From'] = email.utils.formataddr(('Author', sender))
	msg['Subject'] = 'Hello %s', %name
	ssession = smtplib.SMTP(server)
	session.login(user, password)
	session.sendmail(sender, recipients, message)
if __name__ == "__main__":
	if len(sys.argv)!=2:
		print "Wrong number of arguments! Usage: python finalStep.py veloz"
		sys.exit()
	main(sys.argv[1])

