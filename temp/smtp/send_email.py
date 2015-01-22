from email.mime.text import MIMEText
import getpass
msg = MIMEText('hello, send by python', 'plain', "utf-8")

from_addr = "greatlhsforever@163.com"
password = getpass.getpass() 
smtp_server = "smtp.163.com"
to_addr = raw_input("To: ")

import smtplib
server = smtplib.SMTP(smtp_server,port=25,timeout=20)
print "222"
server.set_debuglevel(1)
print "111"
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_srting())
server.quit()
