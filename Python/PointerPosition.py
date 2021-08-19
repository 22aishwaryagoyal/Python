# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 15:16:19 2021

@author: User
"""

f=open('Data','r')
st=f.read(150)
print(st)
pos=f.tell()

print("Position..",pos)
pos=f.seek(0,0)
st=f.read(10)
print(st)
f.close()