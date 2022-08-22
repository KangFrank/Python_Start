#!/usr/bin/python
#-*-coding:UTF-8 -*-

def fib1(n):
	a,b=0,1
	while a<n:
		print(a,end='')
		a,b=b,a+b
	print()

def fib2(n):
	f=[]
	a,b=0,1
	while a<n:
		f.append(a)
		a,b=b,a+b
	return f