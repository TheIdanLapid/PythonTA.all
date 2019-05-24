

############
# QUESTION 3
############

# b
import copy
def multi_merge_v2(lst_of_lsts):
    lst_of_lsts_copy = copy.deepcopy(lst_of_lsts)
    merged = []
    min_list = [lst[0] for lst in lst_of_lsts_copy] #O(m)
    index_lst = [0 for lst in lst_of_lsts_copy] #O(m)
    index_minimum = 0
    minimum = 0
    while True:
        minimum = min(min_list) #O(m)
        if minimum == float("inf"):
           break  
        for i in range(len(min_list)): #O(m)           
            if min_list[i] == minimum:
                index_minimum = i
                break
        merged += [minimum]
        index_lst[index_minimum] += 1
        if index_lst[index_minimum] > len(lst_of_lsts_copy[index_minimum])-1: #out of range
           index_lst[index_minimum] -= 1 #put it in range
           lst_of_lsts_copy[index_minimum][index_lst[index_minimum]] = float("inf") #put infinity in last index                   
        min_list[index_minimum] = lst_of_lsts_copy[index_minimum][index_lst[index_minimum]] #update the minimum
    return merged

def merge(lst1, lst2):
    """ merging two ordered lists using
        the two pointer algorithm """
    n1 = len(lst1)
    n2 = len(lst2)
    lst3 = [0 for i in range(n1 + n2)]  # alocates a new list
    i = j = k = 0  # simultaneous assignment
    while (i < n1 and j < n2):
        if (lst1[i] <= lst2[j]):
            lst3[k] = lst1[i]
            i = i +1
        else:
            lst3[k] = lst2[j]
            j = j + 1
        k = k + 1  # incremented at each iteration
    lst3[k:] = lst1[i:] + lst2[j:]  # append remaining elements
    return lst3

# c
def multi_merge_v3(lst_of_lsts):
    m = len(lst_of_lsts)
    merged = []

    for i in range (0,m): #O(m)
        merged = merge(merged,lst_of_lsts[i]) #O(max(n1,n2))

    return merged



############
# QUESTION 5
############

# a
def steady_state(lst):
    low = 0
    high = len(lst) - 1
    while low <= high:
        middle = (high + low) // 2
        if middle == lst[middle]:
            return middle
        elif middle < lst[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return None

# d
def cnt_steady_states(lst):
    pass #replace this with your code



############
# QUESTION 6
############
def sort_num_list(lst):
    pass #replace this with your code



   
    
########
# Tester
########

def test():
    
    f1 = lambda x : x - 1
    res = find_root(f1 , -10, 10)
    EPS=0.001
    if res == None or abs(f1(res)) > EPS  or \
       find_root(lambda x : x**2  , -10, 10) != None:
        print("error in find_root")
        
   
    if multi_merge_v2([[1,2,2,3],[2,3,5],[5]]) != [1, 2, 2, 2, 3, 3, 5, 5] :
        print("error in multi_merge_v2")

    if multi_merge_v3([[1,2,2,3],[2,3,5],[5]]) != [1, 2, 2, 2, 3, 3, 5, 5] :
        print("error in multi_merge_v3")

    if steady_state([-4,-1,0,3,5]) != 3 or \
       steady_state([-4,-1,2,3,5]) not in [2,3] or \
       steady_state([-4,-1,0,4,5]) != None:
        print("error in steady_state")
        
    if cnt_steady_states([-4,-1,0,3,5]) != 1 or \
       cnt_steady_states([-4,-1,2,3,5]) != 2 or \
       cnt_steady_states([-4,-1,0,4,5]) != 0:
        print("error in cnt_steady_states")

    if sort_num_list([10, -2.5, 0, 12.5, -30, 0]) \
       != [-30, -2.5, 0, 0, 10, 12.5]:
        print("error in sort_num_list")
        

