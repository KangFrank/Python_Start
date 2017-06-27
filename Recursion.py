#!usr/bin/python3
#-*-coding:UTF-8-*-

#n!
def fact(n):
    if n==0 | n==1:  #single | is or in math, double || is or in logic 
        return 1
    return n*fact(n-1)
#n! avodi exceed buf memory
def fact_(n):
    return fact_filter(n,1)
def fact_filter(num,product):
    if num==1 | num==0:
        return product
    return fact_filter(num-1,num*product)
#recursion algerithm
def move_(n,a,b,c):
    if n==1:
        print(a,'->',c)
        return    #if not return, the recursion will exceed the buffer
    move_(n-1,a,c,b)
    move_(1,a,b,c) #This step must be existed ,since one cylinder will only one
    #pass
    move_(n-1,b,a,c)

#print(fact(5))
move_(15,'a','b','c')
