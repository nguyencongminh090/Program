import os
import time


def pktool(move,q):
    list = []
    lst = []
    char = ["o","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
    for i in range(0,15):
        for j in range(0,15):
            k = j
            output = str(-(i-14)) + ',' + str(k)
            list.append(output)
    for i in range(0,15):
        for j in range(0,15):
            k = j
            output = char[i] + str(-(k-15))
            lst.append(output)
    def find(a,b):
        for i in range(len(b)):
            if a == b[i]:
                return i
                break
    def returnmove(s):
        output = 0
        for i in lst:
            if s == i:
                k = find(s, lst)
                output = list[k]
        return output
    def returnpos(s):
        output = 0
        for i in list:
            if s == i:
                k = find(s, list)
                output = lst[k]
        return output
    # q = 0 -> PO -> pk
    # q = 1 -> pk -> PO
    if q == 0:
        out = returnmove(move)
        return out
    elif q == 1:
        out = returnpos(move)
        return out




        
    

