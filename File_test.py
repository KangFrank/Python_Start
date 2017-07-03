#!usr/bin/env python3
#-*-coding:utf-8 -*-
#Filename:File_test.py

import re
m=re.search('(?=abd)def','abcdef')
m.group(0)

#The statement should be clearly describe the func
def abs(n):
    '''
    Function to get the absolute value of number.
Example: >>>abs(-1)=1, >>>abs(1)=1
'''
    if n>=0:
        return n
    else:
        return -n
class Dict(dict):
    """
  Simple dict but also support access as x.y style
"""
    def __init__(self,**kw):
        super(Dict,self).__init__(**kw)
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'"%key)
if __name__=='main':
    import doctest
    doctest.testmod()
