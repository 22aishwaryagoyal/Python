# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 11:23:15 2021

@author: User
"""

class Employee:
    empno=0
    salary=0
    grade=''
    
    def __init__(self,a,b,c):
        self.empno=a
        self.salary=b
        self.grade=c
        print('Constructor called')
    
    def show(self):
        print(self.empno)
        print(self.salary)
        print(self.grade)
    def __del__(self):
        print('Bye..')

obj=Employee(101,40000,"A")
obj.show()
            