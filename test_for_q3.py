

def test():
    
    #copy the following code and paste in your skeleton file,
    # (instead of the existing tests for question 3)

    #Question 3  
    h = SimpleDict(200)
    h.insert("ab", 2)
    h.insert("ef", 1)
    h.insert("cd", 3)
    if len(h.items()) != 3:
        print("error in insert()")
    if h.find("ab") != 2:
        print("error in find()")
    if h.find("ef") != 1:
        print("error in find()")
    if h.find("cd") != 3:
        print("error in find()")
    
    d = count_words(["ab", "cd", "cd", "ef", "cd", "ab"]) 
    if d is None:
        print("error in count_words()")
    if len(d.items()) != 3:
        print("error in count_words()")
    if d.find("ab") != 2:
        print("error in count_words()")
    if d.find("ef") != 1:
        print("error in count_words()")
    if d.find("cd") != 3:
        print("error in count_words()")
    
    if sort_by_cnt(d) != [['cd', 3], ['ab', 2], ['ef', 1]] and sort_by_cnt(d) != [('cd', 3), ('ab', 2), ('ef', 1)]:
        print("error in sort_by_cnt()")

    
