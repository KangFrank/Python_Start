#!usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename: XML.py

#Use python data to parser the XML
from xml.parsers.expat import ParserCreate
class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s'%(name,str(attrs)))
    def end_element(self,name):
        print('sax:end_element: %s'%name)
    def char_data(self,text):
        print('sa:char_data: %s'%text)

xml=r'''<?xml version="1.0"?>
<ol>
  <li><a href="/python">Python</a></li>
  <li><a href="/ruby">Ruby</a></li>
</ol>
'''
handler=DefaultSaxHandler()
parser=ParserCreate()
parser.StartElementHandler=handler.start_element
parser.EndElementHandler=handler.end_element
parser.CharacterDataHandler=handler.char_data
parser.Parse(xml)

#Be contrary to parser, use list to create a XML
l=[]
l.append(r'<?xml version="1.0"?>')
l.append(r'<root>')
l.append(encode('some & data'))  #What's encode here?
l.append(r'</root>')
print(l)
return ''.join(l)
