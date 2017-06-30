#!usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename:Enumeration_Metaclass.py

#Define the enum class,better than int member=integer
from enum import Enum
Month=Enum('Month',('January','Februry','March','April','May','June',
                    'July','August','September','October','November','December'))
for name,member in Month.__members__.items():
    print(name,'=>',member.value)

#Customized class
from enum import Enum,unique
@unique
class Weekday(Enum):
    Sunday=0     #Weekday.XXX.value= integer
    Monday=1
    Tuesday=2
    Wednseday=3
    Thursday=4
    Friday=5
    Saturday=6

#Usage of Metaclass
#The difference between dynamic language ang static language is the fucntion is
#the function and class are not built in complied but when run

class Hello(object):
    def hello(self,name=' world.\n'):
        print('Hello %s'%name)
#Metaclass type is the model of class, so must birth from type,dynamic add
#something like C++ malloc() and new()
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add']=lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)
#Customized class
class MyList(list,metaclass=ListMetaclass):
    pass
#ORM: Object Relational Mapping
class User(Model):
    id=IntegerField('id')
    name=StringField('username')
    email=StringField('email')
    password=StringField('password')
    
