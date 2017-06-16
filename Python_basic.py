#!/usr/bin/env python3(python use the unicode)
#-*-coding: utf-8 -*-

"""Basic gramer and data type and variable"""
"""
n=123
print(n)
f=456.789
print(f)
s1='Hellow,world'
print(s1)
s2='Hello,\'Adam\''
print(s2)
s3=r'Hello,"Bart"'
print(s3)
s4=r'''Hello,
Lisa!'''
print(s4)
s2=f
print(s2)
"""
#show the unicode UTF-8
print(ord('中'))
x=b'ABC'
print(x)

#code in different code type
'ABC'.encode('ascii')
'ABC'.encode('utf-8')
b'ABC'.decode('ascii')
len('ABC')

#format output
print("Hello %s, your score is %d.\n"%('Michael',89))
s1=72
s2=85
r=(s2-s1)/s1
print("Improve %.2f"%r)
