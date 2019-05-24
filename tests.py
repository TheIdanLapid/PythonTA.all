# 1d
def reverse_sublist(lst,start,end): 
    if (len(lst) != 0): #empty check 
        for index in range(0,(end - start) // 2): #for half the sublist, reverse using a temp variable
            temp = lst[start + index]
            lst[start + index] = lst[end - 1]
            lst[end - 1] = temp
            index = index + 1
            end = end - 1


def rotate1(lst):
    if (len(lst) != 0): #if the list isn't empty, move each item to the next index, and put the last one in lst[0]
       last = lst[len(lst) - 1]
       for i in range(1,len(lst)):
          lst[len(lst) - i] = lst[len(lst) - i - 1]
       lst[0] = last

def rotatek_v1(lst,k):
    if (len(lst) != 0): 
        k = k % len(lst) #in case that k>len(lst), minimize it
        if k != len(lst): #no need to rotate
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
                        k=k-1
                    lst.reverse()


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
                    
lst1=[2,6,7,8]
print(id(lst1))
rotatek_v1(lst1,-1)
print(lst1,id(lst1))

