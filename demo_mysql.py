#!usr/env/python3
#-*-coding:utf-8 -*-

import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123456"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("CREATE DATABASE ai8py_db")