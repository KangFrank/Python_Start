#1usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename:Mail.py

#The email from user->MUA->MTA->another user
#It obeys the SMTP(simple mail tranfer protol)
from email.mime.text import MIMEText
msg=MIMEText('hello,send by Frank...','plain','utf-8')
#input the Email address
from_addr=input('From: ')
password=input('Password: ')
#input receiver address
to_addr=input('To: ')
#input SMTP server address
smtp_server=input('SMTP server: ')

import smtplib
server=smtplib.SMTP(smtp_server,25)  #default port is 25
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()

#This is a unperfectable code, the email send and receive things will be finished in august
#need an optimization of SMTP and a complement/supplement of POP3
