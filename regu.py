#Traditional string methods
"""
def isPhoneNum(text):
	if len(text)!=13:
		return False
	for i in range(0,3):
		if not text[i].isdecimal():
			return False
	if (text[3] or text[8])!='-':
		return False
	for i in range(9,13):
		if not text[i].isdecimal():
			return False
	return True

print(isPhoneNum('136-1234-1234'))

#use regular expressions
import re
phoneNum=re.compile(r'(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)')
tt=phoneNum.search('My number is 123-2231-1234')
print(tt.group(1))
print(tt.group(2))
print(tt.group(3))
print(tt.group(0))
print(tt.groups())

vowelregex=re.compile(r'[aeiouAEIOU]')
consonantregex=re.compile(r'[^aeiouAEIOU]')
"""
import pyperclip,re

phoneRe=re.compile(r'''[a-zA-Z0-9._%+-]+
	@[a-zA-Z0-9.-]+
	(\.[]a-zA-Z{2,4})''',re.VERBOSE)
text=str(pyperclip.paste())
matches=[]
for groups in phoneRe.findall(text):
	phoneNum='-'.join([groups[1],groups[2],groups[5]])
	if groups[8]!='':
		phoneNum+=' x'+groups[8]
	matches.append(phoneNum)



