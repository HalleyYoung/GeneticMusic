# -*- coding: utf-8 -*-
"""
Created on Sat Nov 15 12:15:31 2014

@author: halley
"""

"""
fold function
f: the function to apply
l: the list to fold
a: the accumulator
"""

def of(list, note):
    return list[note % len(list)]

def fold(f, l, a):
    return a if len(l) == 0 else fold(f, l[1:], f(a, l[0]))


#return if small is sub_str of large
def is_substr(small, large):
    for l in range(0, len(large)):
        string = ""
        for e in range(l, len(large)):
            string.append(e)
            if string == small:
                return True
    return False

#replace y with z in list
def replace(xs, y, z):
        return [z if x == y else x for x in xs]

#concat list    
def concat(xss):
    return [j for i in xss for j in i]


#get item in array number n mod len(array)    
def getWrap(array, index):
    if index < len(array):
        return array[index]
    else:
        return array [index % len(array)]


#map structure of one 2-dimensional list to another one-dimensional list
def mapStructure(origstruct, newlist):
        newstruct = []
        n = 0
        for i in range(0, len(origstruct)):
            newstruct.append([])
            for j in range(0, len(origstruct[i])):
                if len(newlist) > n:
                    newstruct[-1].append(newlist[n])
                n += 1
        return newstruct
