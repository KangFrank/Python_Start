#!usr/bin/env python3
#-*-coding: utf-8 -*-
#Filename:Error_deal_test.py

def foo():
    r=some_function() #??? What's this?
    if r==(-1):
        return (-1)
    return r

def bar():
    r=foo()
    if r==(-1):
        print('Error')
    else:
        pass
#The error deal insitute
try:
    print('try...')
    r=10/0
    print('result: ',r)
except ZeroDivisionError as e:
    print('except: ',e)
finally:
    print('fianlly...Error')
print('END')
"""
import logging
#Try...except...finally...end
#This error will not affect the run of the rest code
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)*2
def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main()
print('END')
"""
#Use raise to throw out an Error
class FooError(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value: %s'%s)
    return 10/n
foo('0')

##Debug
'''
#The first method is to print the error 1st
def foo(s):
    n=int(s)
    print('>>> n=%d'%n)
    return 10/n
def main():
    foo('0')
main()  '''

#Use the assert to instead of print 2nd
def foo(s):
    n=int(s)
    assert n!=0,'n is zero!'
    return 10/n

def main():
    foo('0')

#Use the logging to instead of print 3rd
import logging
logging.basicConfig(level=logging.INFO)
s='0'
n=int(s)
logging.info('n=%d'%n)
print(10/n)
