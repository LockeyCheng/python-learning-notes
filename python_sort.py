# -*- coding: UTF-8 -*-
'''
Created on 2017年9月2日
Running environment：win7.x86_64 eclipse python3
@author: Lockey
'''
import math
lst = [65,56,9,23,84,34,8,6,9,54,11,167]
    
def radix_sort(lists, radix=100):
    k = int(math.ceil(math.log(max(lists), radix)))
    bucket = [[] for i in range(radix)]
    for i in range(1, k+1):
        for j in lists:
            gg = int(j/(radix**(i-1))) % (radix**i)
            bucket[gg].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
            print(lists)
    return lists
radix_sort(lst)
def merge(left, right):
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    print(result)
    return result
def merge_sort(lists):# 归并排序
    if len(lists) <= 1:
        return lists
    num = int(len(lists) / 2)
    left = merge_sort(lists[:num])
    right = merge_sort(lists[num:])
    return merge(left, right)
def adjust_heap(lists, i, size):# 调整堆
    lchild = 2 * i + 1;rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)
def build_heap(lists, size):# 创建堆
    halfsize = int(size/2)
    for i in range(0, halfsize)[::-1]:
        adjust_heap(lists, i, size)
def heap_sort(lists):# 堆排序
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
        print(lists)
 
def shell_sort(lists):
    count = len(lists)
    step = 2
    times = 0
    group = int(count/step)
    while group > 0:
        for i in range(0, group):
            times += 1
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
            print('The {} sorted: {}'.format(times,lists))
        group = int(group/step)
    return lists

def insert_sort(lst):
    count = len(lst)
    for i in range(1, count):
        key = lst[i]
        j = i - 1
        while j >= 0:
            if lst[j] > key:
                lst[j + 1] = lst[j]
                lst[j] = key
            j -= 1
        print('The {} sorted: {}'.format(i,lst))
    return lst

def selection_sort(lst):
    lstlen = len(lst)
    for i in range(0,lstlen):
        min = i
        for j in range(i+1,lstlen):
            if lst[min] > lst[j]:
                min = j
        lst[min],lst[i] = lst[i],lst[min]       
        print('The {} sorted: {}'.format(i+1,lst))
    return lst



def bubble_sort_improve(lst):
    lstlen = len(lst)
    i = lstlen -1
    times = 0
    while i > 0:
        times += 1
        change = 0
        for j in range(0,lstlen):
            if j < i and lst[j] > lst[j+1]:
                change =j
                lst[j],lst[j+1] = lst[j+1],lst[j]
        print('The {} sorted: {}'.format(times,lst))
        i = change
    return lst
