# -*- coding: UTF-8 -*-
'''
Created on 2017��8��29��

@author: Lockey
'''
from math import sqrt
def ifprime(n):
    if n == 1:
        return False
    for i in (2,sqrt(n)+1):
        if n%i == 0:
            return False
    return True

def another():
    for i in range(1,6):
        print(i)