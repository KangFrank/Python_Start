#!/usr/bin/python
#-*-coding:UTF-8 -*-

import urllib.request,urllib.error,urllib.parse

usrname='T2017110037'
passwd='Kl@15721430'

URL="https://tpass.shs.cn/tpass/login"
REALM='Secure Archive'

def handler_version(url):
	hdlr=urllib.request.HTTPBasicAuthHandler()
	hdlr.add_password(REALM,urllib.parse.urlparse(url)[1],usrname,passwd)
	opener=urllib.request.build_opener(hdlr)
	urllib.request.install_opener(opener)
	return url

def request_version(url):
	#python2:from base64 import encodestring
	#python3:
	from base64 import encodebytes
	req=urllib.request.Request(url)
	b64str=encodebytes(bytes('%s:%s' % (usrname,passwd),'utf-8'))[:-1]
	#last one is not included
	req.add_header('Authorization','Basic %s'%b64str)
	return req

for funcType in ('handler','request'):
	print('*** using %s: '%funcType.upper())
	url=eval('%s_version'%funcType)(URL)
	f=urllib.request.urlopen(url)
	print(str(f.readline(),'utf-8'))
	f.close()
