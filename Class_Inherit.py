#!usr/bin/env python
#-*-coding:utf-8 -*-
#Filename:Class_Inherit.py
########This chapter is the most beautiful that can be felt from all the based practice
#Multi-inherit to classify
#Main
class Animal(object):
    pass
#Big class
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#Small class
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

#Another self-defined main class
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

#Inherit many parent/base/super class, called MixIn
#While Java is allowed single parent-class inherited
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass

#Special defined class

#Original class
class Student(object):
    def __init__(self,name):
        self.name=name
print(Student('Michael'))   #This will print a address in hex

#Speacil in __xx__ the inside method
#The first is __str__ 
class SStudent(object):
    def __init__(self,name):
        self.name=name
    def __str__(self):     #This inside method limits return the name as a str
        return 'SStudent object (name: %s)'%self.name
print(SStudent('Michael'))
#The second is __iter__,as its name seen, it's always used in iteration
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1  #initialize two beginning number
    def __iter__(self):
        return self        #the iteration is itself so return itself
    def __next__(self):
        self.a,self.b,=self.b,self.a+self.b  #calculate the next fib-num
        if self.a>100000:    #Terminate the loop
           raise StopIteration()
        return self.a
#Test the __iter__ in Fib class
def test(s):
    for n in s:
        print(n)
        #print(n,end=' ')
test(Fib())
"""
#Make the fib a list
class Fiblist(object):
    def __getitem__(self,n=100):  #Default to print the first 100 numbers
        a,b=1,1
        for x in range(n): #Be care! This appear a x  #This loop no stop sentence
            a,b=b,a+b
        return a
for i in Fiblist():
    print(i)
    if i>1000000:    #use the error to stop the loop
        raise ValueError()
f=Fiblist()
f[10]  #Seen as a list
#but f[5:10] will be an error, because the slice might be a integer
"""
#Fiblist in slice
class Fibslice(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for x in range(n):
                a,b=b,a+b
            return a
        if isinstance(n,slice):
            start=n.start
            stop=n.stop
            if start is None:
                start=0
            a,b=1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b=b,a+b
            return L
#f=Fibslice()
#f[5:18]
#customized class attribution
class student(object):
    def __init__(self,name):
        self.name=name
    def __getattr__(self,attr):  #Student.
        if attr=='age':
            return lambda:25
        raise AttributeError('\'Student\' object has no attribution \'%s\'' %attr)
#Change the url for write the new APi, the path can be write once a time
class Chain(object):
    def __init__(self,path=''): #Attention the '' or ' ',always end=' ' has a blank space
        self.path=path
    def __getattr__(self,path):  #Made the attribution as the path!!!!!!!!!!!
        return Chain('%s/%s'%(self.path,path))
    def __str__(self):
        return self.path
    __repr__=__str__
        
