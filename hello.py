def SayHello():
    print("hello")
    return 

def SayHelloName(name):
    name=input("Enter the name: ")
    print("Hello {}!".format(name))
    return 

def Compare(a0,a1,a2):
    t=a0+a1+a2
    percent=t/3
    if percent>=50:
        print("Result:pass")
    else:
        print("Result:fail")
    return
def SayHelloD(name="Frank"):
    print("hello {}".format(name))
    return
