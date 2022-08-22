#!/usr/env/python3
#server.py
#-*-coding: utf-8 -*-

import socket
import sys

#create socket object
serversocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#get host name
host=socket.gethostname()

port=9999

serversocket.bind((host,port))

serversocket.listen(5)

while True:
	clientsocket,addr=serversocket.accept()
	print("Connect Addr is: %s"%str(addr))

	msg='Welcome!\n'
	clientsocket.send(msg.encode('utf-8'))
	clientsocket.close()