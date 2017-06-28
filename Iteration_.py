#！usr/bin/python3
#-*-coding:UTF-8-*-
#Filename:iteration.py

#iteration is better than loop in dic index
d={'a':1,'b':2,'c':3}
for key in d:     #only print k
    print(key)
for value in d.values():     #only print value
    print(value)
for k,v in d.items():     #print both k,v 
    print((k,v))
x1=[x*x for x in range(1,11)]
x2=[x*x for x in range(1,11) if x%2==0]
x3=[x*x for x in range(12,22)]
x4=[z1+z2 for z1 in x1 for z2 in x3] #Elements in x1 will multiple all the elements in x3

#Eliminate the num and turn all the str int lower style
l=['Hello','WORLD',16,'apple','Act',None]
L=[]
for x in l:
    if isinstance(x,str)==True:
        L.append(x.lower())
print(L)

x1=[x*x for x in range(1,11)]
g=(x*x for x in range(10))
for i in g:
    print(i,end=' ')
#Define fibonacci
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b,end=' ')
        a,b=b,a+b
        n+=1
    return 'done'
fib(10)

#Define triangles
"""
def triangles(n):
    l=[]
    if n==1:
        l=[1]
    elif n==2:
        l=[1,1]
    else:
        while i<n:

    
def triangles_():
    LL=[1]
    while True:
        yield LL
        LL.append(0)
        LL=[L[i-1]+L[i] for i in range(len(LL))]
    return LL

def triangles(n=10):
    ret = [1]
    while i<n:
        yield ret
        ret[i] = pre[i] + pre[i - 1]
        ret.append(1)
        pre = ret[:]
    return pre

print(triangles())
n=0
for t in triangles_():
    print()

    
def triangle(n):
    while True:
        yield LL1
        LL1=[LL1[x]+LL1[x+1] for x in range(len(LL)-1)]
        LL.insert(0,1)
        LL.append(1)
        if len(LL1)>10:
            break
a=triangle(10)
for i in a:
    print(i)
   """

#High level func
#This means that the inside func is a parameter
a=-5
b=7
f=abs
def add(x,y,f):
    return f(x)+f(y)
print(add(a,b,abs))

