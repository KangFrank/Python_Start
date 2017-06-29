#!usr/bin/env python3
#-*- coding: utf-8 -*-
#Filename:Partial_func.py

#Partial function
import functools
int2=functools.partial(int,base=2)  #Means that the input are based on Bin(2) style
int2('10001')                       #And output Dec(10)
#Init prototype
dict1={'name':'Michael','score':98}
dict2={'name':'Bob','score':91}
def print_score_(std):
    print('%s: %s'%(std['name'],std['score']))

#Class method:Attention! the upper and lower alpha is different
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print('%s : %s'%(self.name,self.score))
    def get_name(self):
        return self.name
    def get_score(self):
        return self.score
    def set_name(self,name):
        self.name=name
    def set_score(self,score):
        if 0<=score<=100:
            self.score=score
        else:
            raise ValueError('bad score')

ba=Student('Bart',99)
li=Student('Lisa',69)
ba.print_score()
li.print_score()

#The inherit of class
class School(object):
    def __init__(self,teacher,student):
        self.teacher=teacher
        self.student=student
class Teacher(School):
    def __init__(self,name):
        self.teacher=name
class Student(School):
    def __init__(self,marks):
        self.student=marks

#The inherit of class 2
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

class Cat(Animal):
    pass
#Also the child can cover the parent
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):  #self_defined run() to cover the func in parent
        print('Dog is running...')
    #pass

class Cat(Animal):
    def run(self):  #self_defined run() to cover the func in parent
        print('Cat is running...')
    #pass
#Multi_class
def run_twice(A):
    A.run()
    A.run()
#Used
run_twice(Animal())  #Attention to the difference of Animal() and Animal
run_twice(Dog())
run_twice(Cat())
dog=Dog()
dog.run()
cat=Cat()
cat.run()
