#!usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename:GUI_Web.py

#Write the first GUI program
from tkinter import *
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.hellolabel=Label(self,text='Hello,world!')
        self.hellolabel.pack()
        self.quitbutton=Button(self,text='Intel_Quit',command=self.quit)
        self.quitbutton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, %s'%name)
'''    
app=Application()
app.master.title('Hello World')
app.mainloop
'''
#Add the function of input
from tkinter import *
import tkinter.messagebox as messagebox
class Application1(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertbutton=Button(self,text='Hello',command=self.hello)
        self.alertbutton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        messagebox.showinfo('Message','Hello, %s'%name)
'''
app1=Application1()
app1.master.title('Hello World')
app1.mainloop()
'''
#TCP/IP web network communications
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#establish the connection with sina
s.connect(('www.sina.com',80))
#send data
s.send(b'GET/HTTP/1.1\r\nHost:www.sian.com.cn\r\nConnection:close\r\n\r\n')
#receive data
buffer=[]
while True:
    #Each time can only receive no more than 1k data
    d=s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data=b''.join(buffer)
s.close
#print the HTTP, seprate the head and the content
header,html=data.split(b'\r\n\r\n',1)
print(header.decode('utf-8'))
#Write the received data into file
with open('sina.html','wb') as f:
    f.write(html)

