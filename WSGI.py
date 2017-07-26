#!/bin/env python3
#-*-coding:utf-8 -*-
#Filenae: WSGI.py

#hello.py
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello,web!</h1>']

#server.py, both should be in the same content
from wsgiref.simple_server import make_server
from hello import application

httpd=make_server('',8000,application)
print('Serving HTTP on port 8000...')
#monitoring the HTTP request
httpd.serve_forever()

#hello1.py
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    #self custom
    body='<h1>Hello,%s!</h1>'%(environ['PATH_INFO'][1:] or 'web')
    return [b'<h1>Hello,web!</h1>']

#use the flask model/template
from flask import Flask
from flask import request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/sigin',methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><imput name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''
@app.route('/signin',methods=['POST'])
def signin():
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello,admin!</h3>'
    return '<h3>Bad usrname or password.</h3>'

if __name__=='__main__':
    app.run()
