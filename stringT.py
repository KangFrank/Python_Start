def printPic(it,left,right):
	print('Picnic items'.center(left+right,'-'))
	for k,v in it.items():
		print(k.ljust(left,'.')+str(v).rjust(right))

meallist={'sandwich':4,'apple':12,'cups':5,'cookies':8}



passwd={'email':'1234','blog':'weer','luggage':'1212'}

import sys
if len(sys.argv)<2:
	print('Usage: python passwd account passwd')
	sys.exit()

account=sys.argv[1]

if account in passwd:
	pyperclip.copy(passwd[account])
	print('Password for '+account+" copied to clipboard.")
else:
	print("There is no account named "+account)
