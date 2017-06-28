#!usr/bin/env python3
#-*- coding: utf-8 -*-
#Filename: Map_reduce_filter_sorted.py

#Map: map(func,iterable)
def f(x):
    return x*x
r=map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
#The loop can also achieve the result
L=[]
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)

#List integer be mapped in string style
print(list(map(str,[1,2,3,4,5,6,7,8,9])))

#Reduce must contain two parameters
from functools import reduce
def add(x,y):   
    return x*10+y    #This is make the number together in a order
print(reduce(add,[1,3,5,7,9]))

#Format to lower
def commonlize(l):
    for i in l:
        if isinstance(i,str)==True:
            i=lower(i)
            #i(0)=upper(i(0))
#Sorted in the order that from the minimum to the maximum
print(sorted([78,77,-78,1,6,4]))

#Closure: the variable last to the end
def count():
    fs=[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
#f11,f21,f33=count()

#To modify the closure, re_defined the function
def count_():
    def f(j):
        def g():
            return j*j
        return g
    fs=[]
    for i in range(1,4):
        fs.append(f(i))
    return fs
f1,f2,f3=count_()

#Decorator

def log(func):
    def wrapper(*args,**kw):
        print('call %s()'%func.__name__)
        return func(*args,**kw)
    return wrapper
@log    #Decorator
def now():
    print('2017-6-28')
now()
    
