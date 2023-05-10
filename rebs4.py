#requests and bs4:https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3
#-*-coding: utf-8 -*-
#By Mr. Kang
#######  http response ######
#1xx informational response – the request was received, continuing process
#2xx successful – the request was successfully received, understood, and accepted
#3xx redirection – further action needs to be taken in order to complete the request
#4xx client error – the request contains bad syntax or cannot be fulfilled
#5xx server error – the server failed to fulfil an apparently valid request

""" 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'

Turtle Soup
Beautiful Soup, so rich and green,
Waiting in a hot tureen!
Who for such dainties would not stoop?
Soup of the evening, beautiful Soup!
Soup of the evening, beautiful Soup!

Beau--ootiful Soo--oop!
Beau--ootiful Soo--oop!
Soo--oop of the e--e--evening,
Beautiful, beautiful Soup!

Beautiful Soup! Who cares for fish,
Game or any other dish?
Who would not give all else for two
Pennyworth only of Beautiful Soup?
Pennyworth only of beautiful Soup?

Beau--ootiful Soo--oop!
Beau--ootiful Soo--oop!
Soo--oop of the e--e--evening,
Beautiful, beauti--FUL SOUP!
"""
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

url = 'https://assets.digitalocean.com/articles/eng_python/beautiful-soup/mockturtle.html'
res = requests.get(url)

soup = bs(res.text,'html.parser')
data=pd.DataFrame(soup.find_all('p'))
data.to_excel('try.xlsx',index=True)
#print(soup.prettify()) #turn the Beautiful Soup parse tree into a nicely formatted Unicode string
#print(soup.find_all('p'))
#print(soup.find_all('p')[2]) #'p' is a list, [2] means the third 'p' tag
#print(soup.find_all('p')[2].get_text()) #how to write get_text()
#print(soup.find_all(class_='chorus')) #locate class 'chorus'
#print(soup.find_all(id='third')) #locate id 'third'

"""
print(res)
print(res.status_code)
print(res.text)
"""