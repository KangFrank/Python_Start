import time

def square1(n):
	return n**2

square2=lambda n:n**2

print(time.time())

i=0
while i<100000000:
	square1(100)
	i+=1

print(time.time())

i=0
while i<100000000:
	square2(100)
	i+=1

print(time.time())