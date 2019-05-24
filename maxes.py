def max1(L): 
    if len(L)==1:
        return L[0]
    return max(L[0], max1(L[1:]))



def max2(L): 
    if len(L)==1:
        return L[0]
    l = max2(L[:len(L)//2])
    r = max2(L[len(L)//2:])    
    return max(l,r)

def max22(L, left, right):
    if left == right:
        return L[right]
    mid = (left+right)//2
    l = max22(L, left, mid)
    r = max22(L, mid + 1, right)
    return max(l,r)


def max_list22(L):
    return max22(L,0,len(L)-1)

def max11(L,left,right):
    if left==right:
        return L[left]
    return max(L[left], max11(L,left+1,right))

def max_list11(L):
    return max11(L,0,len(L)-1)

#Competition!!

import time
import random
import sys
sys.setrecursionlimit(5000)


for f in [max1, max2, max_list11, max_list22]:
    print(f.__name__)
    for n in [1000,2000,4000]:
        L = [i for i in range(n)]
        random.shuffle(L)
        tic = time.clock()
        for x in range(4):
            f(L)
        toc =time.clock()
        print("n=",n,": ",toc-tic)

