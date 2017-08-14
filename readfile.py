#!usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename:readfile.py

#how to ger its path
#if in the specific file, no need to find the path
#else if the file is in the default path
#import os/os.getcwd()/then print it 
#the library
#import sys, sys.apth

#open file
from sys import argv
scaipt,filename=argv

text=open(filename) #only read the exist file, the default is 'r'

print("Here's your file %r:"%filename)
print(text.read())

print("Type the filename again:")
file_again=input("> ")
text_again=open(file_again)
print(text_again.read())

#write file
from sys import argv
script,filename=argv
print("We're going to erase %r."%filename)
print("If you don't want that, hot CTRL-C(^C).")
print("If you do want that, hot RETURN.")

input("?")
print("Opening the file...")
target=open(filename,'w') #Excute to write content in the file 'w'
                          #if the file is not exist, it will create the new file and then write 
print("Truncating the file, Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")

line1=input("line1: ")
line2=input("line2: ")
line3=input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally ,we close it.")
target.close()

"""
#copy file to another, but cat only can be used in linux or os, windows cannot
from sys import argv
from os.path import exists

script,from_file,to_file=argv # need to input two files' name
print("Copying from %s to %s"%(from_file,to_file))

in_file=open(from_file)
in_data=in_file.read()

print("The input file is %d bytes long"%len(in_data))
print("Does the output file exist?%r"%exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file=open(to_file,'w')
out_fi;e.write(in_data)
print("Alright, all done.")

out_file.close()
in_file.close()
"""