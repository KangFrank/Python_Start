#!usr/bin/env python3
#-*-coding:utf-8 -*-
#hello.py
print('Hello world!')
print('Hello, my program life')

#Escape sequence \n is called back-slash and will cause a new line
tabby="\tI'm tabbed in."
persian="I'm split\non a line."
black="I'm \\ a \\ cat"
fat="""
I'll do a list:
\t* cat food
\t* fishes
\t* catnip\n\t* grass
"""
print(tabby)
print(persian)
print(black)
print(fat)

l=["/","-","|","\\","|"]

for i in l:
    print ("%s\r" % i)

for i in ["/","-","|","\\","|"]:
    print(i)