#!usr/bin/env python
#-*-coding: utf-8 -*-
#Filename: Urllib_Pic.py

'''#Url
from urllib import request
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data:',data.decode('utf-8'))
'''

#Make decode
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random

#random numbers
def rndChar():
    return chr(random.randint(65,90))
#random color1
def rndColor1():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))
#random color2
def rndColor2():
    return (random.randint(32,127),random.randint(32,127),random.randint(32,127))
#picture size: 240*60
width=60*4
height=60
image=Image.new('RGB',(width,height),(255,255,255))
#creat font object
font=ImageFont.truestyle('Arial.ttf',36)
#creat draw object
draw=ImageDraw.Draw(image)
#fixed all object
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor1())
#output the font
for x in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
#obscure
image=image.filter(ImageFilter.BLUR)
image.save('code.jpg','jpeg')
