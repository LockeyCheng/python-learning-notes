# -*- coding: UTF-8 -*-
'''
Created on 2017-08-29

@author: Lockey
'''
import is_prime
from _functools import reduce
from numpy.core.defchararray import rfind
def plusTo():
    counts = 0
    n = input('Please input max number of list: ')
    def recur(arg):
            nonlocal counts
            for j in range(arg,int(n)+1):
                if arg+j == int(n) and ifprime(j) == True:
                    counts = counts + 1
                else:
                    pass
    ntoNumber = int(n)
    for i in range(2,ntoNumber+1):
        if ifprime(i) == True and i >= 3:
            lst = []
            lst.append(i)
            recur(i)
    print(counts)
#print(dir(is_prime))
#n(1 ≤ n ≤ 1000)
import math
def lastZero1(num):
    if 1<= num <= 1000:
        count = 0
        flag = 5
        while flag < num+1:
            flag += 5
            count += 1
            basicNum = 25;
            while flag % basicNum == 0:
                count += 1
                basicNum *= 5
        print(count)   
    else:
        print('Number not within the range 1-1000 or not a number given!')

def lastZero2(num):
    count = 0;
    temp=num/5;
    while temp !=0 : 
        count+=math.floor(temp)
        temp/=5
    print(count)
#lastZero1(1000)
#lastZero2(1000)
def numRebuild(lst):
    lstr = [ str(item) for item in lst]
    lstorder = sorted(lstr)
    lstlen = len(lstorder)
    flag = lstlen-2
    result = ''
    while flag >= 0:
        
        print(lstorder[flag])
        flag -= 1
lst = [2,34,4,6,57,8,8653,34,23]
#numRebuild(lst)
def oo(lst):
    lstr = [ str(item) for item in lst]
    lstorder = sorted(lstr)
    lstlen = len(lstorder)
    flag = lstlen-1
    result = ''
    while flag >= 0:
        max = ''
        flaginner = flag-1
        while flaginner >= 0:
            x = lstorder[flaginner]
            y = lstorder[flaginner-1]
            lens = len(x) if len(x) <= len(y) else len(y)
            j = 0
            while j < lens:
                if x[j] == y[j]:
                    continue
                max = x if x[j] > y[j] else y
                #max = lstorder[flaginner] if lstorder[flaginner] > lstorder[flaginner-1] else lstorder[flaginner-1]
                j += 1
            flaginner -= 1
        print(max)
        flag -= 1
oo(lst)