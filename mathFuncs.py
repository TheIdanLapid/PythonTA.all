
############
# QUESTION 1
############

import math

# 1c
def reverse_sublist(lst,start,end): 
    if (len(lst) != 0): #empty check 
        for index in range(0,(end - start) // 2): #for half the sublist, reverse using a temp variable
            temp = lst[start + index]
            lst[start + index] = lst[end - 1]
            lst[end - 1] = temp
            index = index + 1
            end = end - 1

# 1d
def rotate1(lst):
    if (len(lst) != 0): #if the list isn't empty, move each item to the next index, and put the last one in lst[0]
       last = lst[len(lst) - 1]
       for i in range(1,len(lst)):
          lst[len(lst) - i] = lst[len(lst) - i - 1]
       lst[0] = last

# 1e
def rotatek_v1(lst,k):
    if (len(lst) != 0): #empty check 
        k = k % len(lst) #in case that k>len(lst), minimize it
        if k != len(lst): #need to rotate
            if(k < 0):
                k = len(lst) + k
            if ((len(lst) - k) >= (len(lst) / 2)):
                    while k > 0:
                        rotate1(lst)
                        k = k - 1
            else:
                    lst.reverse()
                    k = len(lst)-k
                    while k!=0:
                        rotate1(lst)
                        k = k-1
                    lst.reverse()

# 1f
def rotatek_v2(lst,k):
    if (len(lst)!=0): #empty check
        k = k % len(lst) #in case that k>len(lst), minimize it
        if k != len(lst): #need to rotate
            if(k < 0): #same as the method above
                k = len(lst) + k
            if ((len(lst) - k) >= (len(lst) / 2)):
                    while k > 0:
                        rotate1(lst)
                        k = k - 1
            else:
                    reverse_sublist(lst,0,len(lst))
                    k = len(lst)-k
                    while k!=0:
                        rotate1(lst)
                        k = k-1
                    reverse_sublist(lst,0,len(lst))
    
############
# QUESTION 2b
############

def power_new(a,b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin:
        if bit == '1':
            result = result * a
        a = a * a
    return result


############
# QUESTION 3b
############

def add_hex(A,B):
    """ adds 2 numbers represented in hex base """
    key = "0123456789abcdef" #legit chars in hex base
    carry = ""
    result = ""


    while A != "" or B != "":
        
        if A == "":
            A = "0"
        elif B == "":
            B = "0"
            
        digit_a = str.index(key, A[-1]) #last char of A's index
        digit_b = str.index(key, B[-1]) #last char of B's index
        digit_c = str.index(key, carry)
        carry = "" #zero carry
        int_sum = (digit_a + digit_b + digit_c)
        
        if int_sum//16 != 0: #need to use carry
            hex_sum = str(int_sum//16) + key[int_sum%16]
            result = hex_sum[1] + result
            carry = hex_sum[0]
        else:
            hex_sum = key[int_sum%16]
            result = hex_sum + result
        A = A[:-1] #remove last char
        B = B[:-1] #remove last char
        
    if carry != "": #left carry
       result = carry + result
       
    return result



############
# QUESTION 4b
############


def sum_divisors(n):
    if (n == 1):
        return 0
    total = 1
    for i in range (2,int(math.sqrt(n))+1):
        if (n%i == 0):
            if (n/i == i):
                total = total + i
            else:
                total = total + i + (n/i)
                
    return int(total)
        

def is_finite(n):
    limit = 0
    while (n!=1 and limit<1000):
        n = sum_divisors(n)
        limit = limit+1
    if (n==1):
        return True
    else:
        return False

def cnt_finite(limit):
    count = 0
    for i in range (1,limit+1):
           if is_finite(i) == True:
               count += 1
    return count



############
# QUESTION 5
############

def altsum_digits(n, d):
    
    n = str(n)
    max_sum = 0
    
    for i in range(d):
        max_sum = max_sum + (((-1)**i) * int(n[i]))
    temp = max_sum
    
    for i in range(1,len(n)-d+1):
        
        if d%2 == 1:
            temp = -1 * (temp - int(n[i-1]) - int(n[d+i-1]))
        else:
            temp = -1 * (temp - int(n[i-1]) + int(n[d+i-1]))
            
        if max_sum < temp:
            max_sum = temp
            
    return max_sum

    
    
########
# Tester
########

def test():

    lst = [1,2,3,4,5]
    reverse_sublist (lst,0,4)
    if lst != [4, 3, 2, 1, 5]:
        print("error in reverse_sublist()")        
    lst = ["a","b"]
    reverse_sublist (lst,0,1)
    if lst != ["a","b"]:
        print("error in reverse_sublist()")        

    lst = [1,2,3,4,5]
    rotate1(lst)
    if lst != [5,1,2,3,4]:
        print("error in rotate1()")        

    lst = [1,2,3,4,5]
    rotatek_v1(lst,2)
    if lst != [4,5,1,2,3]:
        print("error in rotatek_v1()")        
    
    lst = [1,2,3,4,5]
    rotatek_v2(lst,2)
    if lst != [4,5,1,2,3]:
        print("error in rotatek_v2()")        

    if power_new(2,3) != 8:
        print("error in power_new()")

    if add_hex("a5","17")!="bc":
        print("error in add_hex()")
    
    if sum_divisors(6)!=6 or \
       sum_divisors(4)!=3:        
        print("error in sum_divisors()")

    if is_finite(6) or \
       not is_finite(4):
        print("error in is_finite()")

    if cnt_finite(6) != 5:
        print("error in cnt_finite()")
        
    if altsum_digits(5**36,12)!=18:
        print("error in altsum_digits()")        


