#!/usr/env/python3
#client.py
#-*-coding: utf-8 -*-

import socket
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=socket.gethostname()
port=9999

s.connect((host,port))

#set data smaller than 1024 bytes
msg=s.recv(1024)
s.close()

print(msg.decode('utf-8'))