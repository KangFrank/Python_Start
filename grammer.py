#!/usr/bin/python
# -*- coding: utf-8 -*-
#Filenamr:grammer.py
#print input("Want me to add those for you?")
#raw_input("Please tell me somebody's name:")
intern("Doctor, where's my intern?")
string1="1234567890"
print len(string1)
list1=['1','2','a','b']
for item in list1:
    print item
print max(5,6,7,8)
#hex()  16
#oct()  8
print pow(3,4)
print range(2,10)
print round(1.234545,2)
#repr()
#str
print tuple(list1)
def loop(x,y):
    while x>y:
        print y
        y=y+1
    return y  #make sure the func always has a input
loop(6,3)
print complex(89)
liststring="ascdefg"
print liststring[2:4]
print liststring*2
print liststring[2:4]+liststring
list2=['a','b','c']
del list2[2]
print list2
print list2.append("dc")
print list2.index("b")
print list2
list2.insert(1,"fuck u")
list2.sort()
print list2
dictionary1={"number":"two","size":"normal","angle":"sharp"}
for items in dictionary1:
    print "key is %s, value is %s "%(dictionary1.keys(),dictionary1.values())
