#!/usr/bin/env python3
#-*-coding:utf-8 -*-
"""
#Judgements
age=20/2
if age>=18:
    print("Your age is %d"%age)
    print("Your age is ",age)
elif age>=8:
    print("Teenager, your age is ",age)
else:
    print('Your age is %d'%age) #The %d used here is to make the result an integer
    print('Get away,little child')

#The user_defined input things
birth=int(input('birth: ')) #The input returns a 'str' type, need a compulsive transfer to int type
if birth>2000:
    print('00 after')
elif birth>1990:
    print('90 after')
else:
    print('You are old now, go to die plz!')
"""
#Loop
sum=0

#for type loop
for i in range(1001):
    sum=sum+i
print(sum)

#while type loop
sum1=0
n=999
while n>0:
    sum1=sum1+n
    n-=1
print(sum1)

#Dictionary
M={"Michael":95,'Bob':75,'Tracy':85}
print(M['Bob'])
M['Adams']=99 #Add element directly
print(M)
#judge one element is in the Dic or not
M.get('Tomas',-1) #if not in, return a num, the default number is 0
M.pop('Bob') #Use pop() to cancle a key just as the list,and the value is cancled too
#Set created,need a list as the input,and only contains the keys without the values
s=set([1,2,3])
ss=set([4,2,3])
s.add(4) #Add an element
s.remove(4) #Cancle an element
print(s & ss) #And logic
print(s | ss) #Or logic
##The only distinguish between set and dic is whether there is a correponding value to the key

