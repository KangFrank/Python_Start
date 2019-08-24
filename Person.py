class Person:
    totalObjects=0
    def __init__(self):
        Person.totalObjects=Person.totalObjects+1

    @classmethod
    def showcount(cls):
        print("Total objects: ",cls.totalObjects)

class quadrilateral:
    def __init__(self,a,b,c,d):
        self.side1=a
        self.side2=b
        self.side3=c
        self.side4=d
    def perimeter(self):
        p=self.side1+self.side2+self.side3+self.side4
        print("perimeter= ",p)

class rectangle(quadrilateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
