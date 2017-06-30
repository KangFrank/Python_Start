#!usr/bin/env python
#-*-coding:utf-8 -*-
#Filename:Object.py

#Object_method_together
class MyObject(object):
    def __init__(self):
        self.x=9
    def power(self):
        return self.x*self.x
obj=MyObject()
hasattr(obj,'x')
setattr(obj,'y',19)
getattr(obj,'y')
obj.y

#Dynamic to distribute a case
class Student(object):
    pass
s=Student()
s.name='Michael'  #Dynamic give an attribution
                  #The attribution is opening
from types import MethodType

#Dynamic the attribution within limited
class St(object):
    __slots__=('name','age','score')   #Only limit the present class
                                       #has no limits on the subclass

#Using @ property
#to limit the area of value
class Student1(object):
    def __init__(self):
        pass
    def get_score(self):
        return self.score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer!\n')
        if value<0 or value>100:
            raise ValueError('Score must be a natural num between 0~100.\n')
        self.score=value
"""
s=Student1()
s.set_score(70)
print(s.get_score())
s.set_score(999)  """
#@property decorator
class Student2(object):
    @property
    def score(self):
        return self.score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('Score must be an integer!\n')
        if value<0 or value>100:
            raise ValueError('Score must be a natural num between 0~100.\n')
        self.score=value 
