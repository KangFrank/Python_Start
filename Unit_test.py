#!usr/bin/env python3
#-*-coding: utf-8 -*-
#Filename:Unit_test.py

#Set the Dict class
class Dict(dict):  #dict, object are key-words
    def __init__(self,**kw):
        super().__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
    def __setattr__(self,key,value):
        self[key]=value
d=Dict(a=1,b=2)

#Import unittest to program the unit test
import unittest
from mydict import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d=Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertEqual(a,dict)
    def test_key(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')
    def test_attr(self):
        d=Dict()
        d.key='value'
        self.assertTrue('ket' in d)
        self.assertEqual(d['key'],'value')
    def test_keyerror(self):
        d=Dict()
        with self.assertRaises(KeyError):
            value=d['Empty']
    def test_attrerror(self):
        d=Dict()
        with self.assertRaises(AttributeError):
            value=d.empty
if __name__=='__main__':
    unittest.main()
