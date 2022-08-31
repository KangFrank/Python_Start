def squares(n=10):
	print("Generating squares from 1 to {}".format(n**2))
	for i in range(1,n+1):
		yield i**2 #store all the generated data
		           #generator: yield

gen=squares()

for x in gen:
	print(x,end=' ')

print('\n')
#generator expression
gen=(x ** 2 for x in range(100))
print(gen)

for x in gen:
	print(x,end=' ')