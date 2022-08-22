#!usr/env/python3
#-*-:utf-8 -*-
#Class test

class people:
	#basic attributes
	name=''
	age=0
    #define private attributes
	__weight=0

	def __init__(self,name,age,wei):
		self.name=name
		self.age=age
		self.__weight=wei

	def speak(self):
		print("{0} say: I'm {1} now.".format(self.name,self.age))
p=people('Rain',10,100)
p.speak()

#inheritance
class student(people):
	grade=''
	def __init__(self,name,age,wei,gra):
		people.__init__(self,name,age,wei)
		self.grade=gra
	def speak(self):
		print("Wow you {0} say: I'm {1} in {2}th grade now".format(self.name,self.age,self.grade))


s=student('Rain',10,60,4)
s.speak()