#!/usr/bin/env python3
#-*-coding:utf-8 -*-

#The list things
classmates=["Michael","Bob","Tracy"]
print(classmates)
print(len(classmates))

for i in range(0,3):
    print(classmates[i])
for i in range(-3,0):
    print(classmates[i])

classmates.append("Adam") #Add one element in the end of list
classmates.insert(1,'Jack')#Insert one element in the assigned position
classmates.pop(i)#Eliminate one element of the indicating position,the default is the end
L=[]# Create a empty list


#Tuple is looks like list, but cannot be modified once initialized
classmates1=("Michael","Bob","Tracy")
t=('a','b',['A','B']) #The change in fact is replace the list's elements
t[2][0]='x'
t[2][1]='Y'
print(t)
