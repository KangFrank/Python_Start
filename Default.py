#!usr/bin/levno python3
#-*-coding:utf-8 -*-


#Default func
def append_list(l=None):  
    if l is None:    #This makes the l=[] won/t be repeat used ['end']
       l=[]
     l.append('end')
     return l
def append_list(l=None):  
   
     l.append('end') #This makes l will be repeat used  ['end','end','end'...]
     return l
 #Input numbers can be changed
 def clc(*num):   #This you can input any thing,like clc(1,2,3),clc([1,2,3]),clc((1,2,3))
     sum=0
     for n in num:
       sum=sum+n*n
     return sum
 
  def clc(num):   #This you can input only list or tuple thing,like clc([1,2,3]),clc((1,2,3))
     sum=0
     for n in num:
       sum=sum+n*n
     return sum
 
