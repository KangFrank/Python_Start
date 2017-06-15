#-*-coding:UTF-8-*-
#Filename:Easy_game.py
#All copyright by Frank_Kang

import time
import random

#define variable of health points
hp=30

#define variable object_ list to show what the adventures have
object_=[]

#define variable list about the tools
tools=["Torch","Rope","Spanner","50HP","10HP"]

#set two acceptable answers and select anyone to end the loop
def get_input(prompt,accepted):
    while True:
      valuw=input(prompt).lower()
      if value in accepted:
         return value
      else:
         print("That is not a recognized answer, must be one of ",accepted)

#define teh function to use the tools of HP
def use_tools(tool):
     global hp
     length=len(tool)
     for i in range(0,length):
         if tool[i]=="50HP":
            hp+=50
            tool.pop(i)  #cancle since the tool is used off
            print("You have use the tool of 50HP.")
            #j+=1
         elif tool[i]=="10HP":       
            hp+=10          
            tool.pop(i)  #cancle since the tool is used off     
            print("You have use the tool of 10HP.")       
            #j+=1
            
 #define the location of adventure site
 def handle_room(location):
     global hp
     if location=="start":
        print("You are standing on a path of the edge of a jungle. There is a cave to your left and a beach to your right")
        object_.append(random.choice(tools)) # the use of random's attribute to play the game
        print("Lucky, you have gained ",object_[-1])
        use_tools(object_)
        direction=get_input("Do you want to go left or right?",["left","right"])
        if direction=="left":
           return "cave"
        elif direction=="right":
           return "beach"
           
     elif location=="cave":
        print("On the entrance of cave, you find a Torch!!!!")
        object_.append("Torch")
        print("You walk to the cave and notice there is an opening.")
        print("A small snake bites you and you loss 20health points.")
        hp-=20
        direction=get_input("Do you want to go deeper?(y/n)",["y","n"])
        if direction=="y":
           return "deep_cave"
        elif direction=="n":
           return "start"
            
      elif location=="beach":
        print("You walk to the beach but remember you do not have any swimming equiment.")
        print("This cool water revitalizes you. You have felt more alive and gain 70 health points.")
        hp+=70
        direction=get_input("Do you want to go swimming?(y/n)",["y","n"])
        if direction=="y":
           return "sea"
        elif direction=="n":
           return "start"
           
      elif location=="sea":
        print("Sundenly there is a tsunami, you cannot escape.")
        hp=0
        return "end"
        
      else:
        print("Programmer error, room ",location," is unknow.")
        return "end"

#Main function
#The begin of the program
location="start"

#Game loop
while location!="end":
     location=handle_room(location)
#Check your health points
print("You now have ",hp," health points.")
if hp<=0:
   print("You are dead.\nGame over.!!!")
   #break.
print("Your adventure is over,bye~\n")
