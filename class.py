class person:
    count=0 #class attribute
    def __init__(self,name="bol",age=23): #constructor
        self.__name=name #instance attribute
        self.__age=age #instance attribute
        person.count=person.count+1
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    def displayInfo(self): #method
        print(self.name, self.age)
    name=property(getname,setname)


def display(str):
    print(str)

def displaydecorator(fn):
    def display_wrapper(str):
        print('Output:', end=" ")
        fn(str)
    return display_wrapper


