#!usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename:IO.py

#The IO things is divided in synchronous and asynchronous to improve the CPU effience
#The file read and open
#f=open('/UsersUsers/liangkan/AppData/Local/Programs/Python/Python36-32/README.txt','r')
"""
try:
    f=open('/path/to/file','r')
    print(f.read())
finally:
    if f:
        f.write('Hello world.')
    else:
        f.close()
"""
import os
os.name

#Json update/improve
import json
d=dict(name='bob',age=20,score=90)
json.dumps(d)  #Change the dict into a string

class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

def student2dict(std):   #Make the Student class be a Dict style
    return {
        'name':std.name,  #The spot should not missed
        'age':std.age,
        'score':std.score
        }
s=Student('Bob',20,90)
print(json.dumps(s,default=student2dict))

#Parent and children muti-process : fork()
#And fork() only for Unix/Linux, Windows system has no fork()
'''
import os
pid=os.fork()
if pid==0:
    print('I am child process(%s) and my parent is (%s)'%(os.getpid().os.getppid()))
else:
    print('I (%s) just created a child process (%s)'%(os.getpid(),pid))
'''
