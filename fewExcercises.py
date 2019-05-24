############
# QUESTION 1
############
def max22(L, left, right):
    if left == right:
        return L[right]
    mid = (left+right)//2
    l = max22(L, left, mid)
    r = max22(L, mid + 1, right)
    return max(l,r)


def max_list22(L):
    return max22(L,0,len(L)-1)


############
# QUESTION 2
############
d2 = {}
def change_fast(amount, coins):

    if (amount < 0 or coins == [0] or coins == []):
        return 0
    elif (amount == 0):
        return 1
    else:
        if (str(amount) + str(coins)) not in d2:
            d2[str(amount) + str(coins)] = change_fast(amount, coins[:-1]) + change_fast((amount - coins[-1]), coins)
        return d2[str(amount) + str(coins)]
    


############
# QUESTION 3
############
def win_fast(n, m, hlst, show=False):
    d = {}
    assert n>0 and m>0 and min(hlst)>=0 and max(hlst)<=n and len(hlst)==m
    if sum(hlst)==0:
        return True
    for i in range(m):  # for every column, i
        for j in range(hlst[i]): # for every possible move, (i,j)
            move_hlst = [n]*i+[j]*(m-i) # full height up to i, height j onwards
            new_hlst = [min(hlst[i],move_hlst[i]) for i in range(m)] # munching
            hlst_str = "".join(str(i) for i in new_hlst)
            if hlst_str in d:
                val = d[hlst_str]
            else:
                d[hlst_str] = win_fast(n, m, new_hlst)
            if not d[hlst_str]:
                if show:
                    print(new_hlst)
                return True
    return False

############
# QUESTION 4
############
def choose_sets(lst, k):
    if k == 0:
        return [[]]
    elif len(lst) == k:
        return [lst]
    else:
        with_1st = [lst[0:1] + subs for subs in choose_sets(lst[1:], k - 1)]
        return with_1st + choose_sets(lst[1:], k)

############
# QUESTION 5
############

import random

def is_prime(m,show_witness=False,sieve=False):
    """ probabilistic test for m's compositeness 
    adds a trivial sieve to quickly eliminate divisibility
    by small primes """
    if sieve:
        for prime in [2,3,5,7,11,13,17,19,23,29]:
            if m % prime == 0:
                return False
    for i in range(0,100):
        a = random.randint(1,m-1) # a is a random integer in [1..m-1]
        if pow(a,m-1,m) != 1:
            if show_witness:  # caller wishes to see a witness
                print(m,"is composite","\n",a,"is a witness, i=",i+1)
            return False
    return True
        

def density_primes(n, times=10000):
    counter = 0
    
    for i in range(times):
        if is_prime(random.randint(2**n,2**(n+1)-1)):
            counter += 1

    return counter/times
   

########
# Tester
########

def test():

    # Q1 basic tests

    if max_list22([1,20,3]) != 20:
        print("error in max22()")
    if max_list22([1,20,300,400]) != 400:
        print("error in max22()")
        
    # Q2 basic tests
    if change_fast(10, [1,2,3]) != 14:
        print("error in change_fast()")

    # Q3 basic tests
    if win_fast(3, 4, [3,3,3,3]) != True:
        print("error in win_fast()")
    if win_fast(1, 1, [1]) != False:
        print("error in win_fast()")

    # Q4 basic tests
    if choose_sets([1,2,3,4], 0) != [[]]:
        print("error in choose_sets()")
    tmp = choose_sets(['a','b','c','d','e'], 4)
    if tmp == None:
        print("error in choose_sets()")
    else:
        tmp = sorted([sorted(e) for e in tmp])
        if tmp != [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'], ['b', 'c', 'd', 'e']]:
            print("error in choose_sets()")




    
