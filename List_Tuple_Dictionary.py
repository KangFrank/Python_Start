#-*-coding:UTF-8-*-
#FileName:List_Tuple_Dictionary.py
#This program is used to familized with list/tuple and dictionary

#Basic sample
List_=[]
Tuple_=()
Dictionary_={}

#Assign members in the list
for i in range(1,10):
    List_.append(i)

Tuple_=(1,"2","Frank","Kang")
#The tuple is like a const thing in C program language
Dictionary_={"Key1":"Value1","Key2":"Value2","Key3":"Value3"}

#Print the items in a dictionary
for items in Dictionary_:
     print(items) 
