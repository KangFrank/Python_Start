#!bin/env python3
#-*-coding:utf-8 -*-

"""
import  os
print("How old are you?")
age=input()  #Up python 2.7 all raw_input() are integreted to input()
print("How tall are you?")
height=input()
print("So, you are %r tall,%r old"%(age,height))
"""
from sys import argv
script, first, second, third = argv
#When compile ,need to python input.py first second third 
print ("The script is called:", (script,first,second,third))
