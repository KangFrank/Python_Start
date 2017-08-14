#!usr/bin/env python3
#-*-coding:utf-8 -*-

x="There are %d types of people."% 10
binary="binary"
do_not="don't"
y="Those who know %s and those who %s."%(binary,do_not)
print(x)
print(y)

print("I said:%r."%x)
print("I also said:'%s'."%y)

hill=False
joke="Isn't that joke so funny?! %r" #%r and %s sometimes are different in priginal type
print("joke")

w="This is the left side of ..."
e="a string with a right side."

print(w+e)

#Get the print skill thoroughly
formatter="%r %r %r %r"
print(formatter % (1,2,3,4))
print(formatter %("one","two","three","four"))
print(formatter %(True,False,False,True))
print(formatter %(formatter,formatter,formatter,formatter))
print(formatter %("I had thsi thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goognight."
))