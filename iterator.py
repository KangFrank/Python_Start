"""
def traverse(iterable):
    it=iter(iterable)
    while True:
        try:
            item=next(it)
            print(item)
        except StopIteration:
            break
#L1=[1,2,3,4,5,6,7,8]
#it=iter(L1)
def Generator():
    print("first item")
    yield 10

    print("second item")
    yield 20
def square(x):
    return x*x
def Isprime(x):
    for n in range(2,x):
        if x%n==0:
            return False
        else:
            return True

def fac(n):
    if n==1:
        print(n)
        return 1
    else:
        print(n,'*',end=' ')
        return n*fac(n-1)
"""
try:
    print("try block")
    x=int(input('Enter a number: '))
    y=int(input('Enter another number: '))
    z=x/y
except ZeroDivisionError:
    print("except ZeroDivisionError block")
    print("Division by 0 not accepted")
else:
    print("else block")
    print("Division = ", z)
finally:
    print("finally block")
    x=0
    y=0
print ("Out of try, except, else and finally blocks." )
