# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:36:05 2021

@author: User
"""

class A:
    def hello(self):
        print('hello')
        print('parent')
        
class B:
    def sum(self,a,b):
        print('sum',(a+b))
        
class C(A,B):
    def Hi(self):
        print("HI C")

obj=C()
obj.Hi()
obj.sum(4,5)
obj.hello()
