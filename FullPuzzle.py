############
# QUESTION 1
############

class Polynomial():
    def __init__(self, coeffs_lst):
        self.coeffs = coeffs_lst
        
    def __repr__(self):
        terms = [" + ("+str(self.coeffs[k])+"*x^" + \
                 str(k)+")" \
                 for k in range(len(self.coeffs)) \
                 if self.coeffs[k]!=0]
        terms = "".join(terms)
        if terms == "":
            return "0"
        else:
            return terms[3:] #discard leftmost '+'

    def degree(self):
        return len(self.coeffs) - 1

    def evaluate(self, x):
        result = 0
        if len(self.coeffs) == 0:
            return 0

        for i in self.coeffs[:0:-1]:
            result = x * (i + result)

        return result + self.coeffs[0]
        
    def derivative(self):
        der=[]
        p = Polynomial(self.coeffs)

        for i in range(1, len(p.coeffs)):
            der.append(i*p.coeffs[i])

        return Polynomial(der)    

    def __eq__(self, other):
        assert isinstance(other, Polynomial)
        if self.degree() != other.degree():
            return False

        for i in range(len(self.coeffs)):
            if (self.coeffs[i] != other.coeffs[i]):
                return False

        return True

    def __lt__(self, other):
        assert isinstance(other, Polynomial)  
        pass #replace this with your code
    
    def __add__(self, other):
        assert isinstance(other, Polynomial)  
        sum_terms = [0] * max(len(self.coeffs),len(other.coeffs))

        for i in range(len(self.coeffs)):
            sum_terms[i] = self.coeffs[i]

        for i in range(len(other.coeffs)):
            sum_terms[i] = sum_terms[i] + other.coeffs[i]

        return Polynomial(sum_terms)

    def __neg__(self):
        negs = [-x for x in self.coeffs]
        return Polynomial(negs)

    def __sub__(self, other):
        assert isinstance(other, Polynomial)  
        return Polynomial(self.coeffs) + (-Polynomial(other.coeffs))

    def __mul__(self, other):
        assert isinstance(other, Polynomial)  
        n = self.degree() + other.degree()
        mul_coeffs = [0]*(n+1)

        for i in range(0, self.degree() + 1):
            for j in range(0, other.degree() + 1):
                mul_coeffs[i+j] += self.coeffs[i] * other.coeffs[j]

        return Polynomial(mul_coeffs)

    def find_root(self):
        return NR(lambda x: self.evaluate(x), diff_param(lambda x: self.evaluate(x)))

## code for Newton Raphson, needed in find_root ##
from random import *

def diff_param(f,h=0.001):
    return (lambda x: (f(x+h)-f(x))/h)


def NR(func, deriv, epsilon=10**(-8), n=100, x0=None):
    if x0 is None:
        x0 = uniform(-100.,100.)
    x=x0; y=func(x)
    for i in range(n):
        if abs(y)<epsilon:
            #print (x,y,"convergence in",i, "iterations")
            return x
        elif abs(deriv(x))<epsilon:
            #print ("zero derivative, x0=",x0," i=",i, " xi=", x)
            return None
        else:
            #print(x,y)
            x = x- func(x)/deriv(x)
            y = func(x)
    #print("no convergence, x0=",x0," i=",i, " xi=", x)
    return None

############
# QUESTION 2
############

### Tree node class - code from lecture, You need to add a field ###

class Tree_node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None
        self.max=None

    def __repr__(self):
        return "[" + str(self.left) + " " + str(self.key) + " " + \
                    str(self.val) + " " + str(self.right) + "]"

### Binary search tree - code from lecture - DO NOT CHANGE ! ###

def insert(root,key,val):
    if root==None:
        root = Tree_node(key,val)
    elif key==root.key:
        root.val = val     # update the val for this key
    elif key<root.key:
        root.left = insert(root.left,key,val)
    elif key>root.key:
        root.right = insert(root.right,key,val)
    return root

def lookup(root,key):
    if root==None:
        return None
    elif key==root.key:
        return root.val
    elif key < root.key:
        return lookup(root.left,key)
    else:
        return lookup(root.right,key)


### End code from lecture ###

# a
def weight(node):
    if node == None:
        return None
    sLeft = weight(node.left)
    sRight = weight(node.right)
    if not sLeft and not sRight:
        node.max = node.val
    elif not sLeft:
        node.max = node.val + sRight
    elif not sRight:
        node.max = node.val + sLeft
    else:
        node.max = node.val + max(sLeft, sRight)

    return node.max
    
    
# b
def heavy_path(node):
    heavy=[]
    weight(node)

    while node.right and node.left:
        if node.right!=None and node.left!=None:
            if node.right.max > node.left.max:
                heavy += [node.key]
                node = node.right
            else:
                heavy += [node.key]
                node = node.left
            continue
        if node.right==None:
            heavy += [node.key]
            node = node.left
        else:
            heavy += [node.key]
            node=node.right

    heavy += [node.key]

    return heavy

# c
import math
def find_closest_key(node, k):

    while node.right and node.left:
        if node.right!=None and node.left!=None:
            if (abs(node.key-k) < abs(node.right.key-k)) and (abs(node.key-k) < abs(node.left.key-k)):
                return node.key
            else:
                if abs(node.key-k) > abs(node.right.key-k):
                   node = node.right
                else:
                   node = node.left
            continue
        if node.right==None:
             if abs(node.key-k) > abs(node.left.key-k):
                   node = node.left
             else:
                return node.key
        else:
             if abs(node.key-k) > abs(node.right.key-k):
                    node = node.right
             else:
                return node.key        

    return node.key
   



############
# QUESTION 3
############



#########################################
### SimpleDict CODE ###
#########################################

class SimpleDict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """      
        self.table = [ [] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def __eq__(self, other):#for testing
        return self.table == other.table

    def items(self):
        return [item for chain in self.table for item in chain]

    def values(self):
        vals = []
        for i in range (len(self.table)):
            for j in range(len(self.table[i])):
                vals.append(self.table[i][j][1])
        return (vals)
    
    def find(self, key):
        i = self.hash_mod(key)
        for j in range (len(self.table[i])):                   
            if key in self.table[i][j]:
                return self.table[i][j][1]
        return None
            
    def insert(self, key, value):
        j=0
        i = self.hash_mod(key)
        for j in range (len(self.table[i])):                   
            if key in self.table[i][j]:
                self.table[i][j][1]=value
                return None
        self.table[i].append([key,value])
            
#########################################
### SimpleDict CODE - end ###
#########################################

def download(url):
    ''' url should be a string containing the full path, incl. http://  '''
    f=urlopen(url)
    btext=f.read()
    text = btext.decode('utf-8')
    #read from the object, storing the page's contents in text.
    f.close()
    return text

def clean(text):
    ''' converts text to lower case, then replaces all characters except
       letters, spaces, newline and carriage return by spaces '''
    letter_set = "abcdefghijklmnopqrstuvwxyz \n\r"
    text = str.lower(text)
    cleaned = ""
    for letter in text:
        if letter in letter_set:
            cleaned += letter
        else:
            cleaned += " "
    return cleaned

def count_words_naive(words):
    count_list=[]
    words_set = set(words) #set of different words (no repetition)
    
    for word in words_set:
        count_list += [ [word, words.count(word)] ]
        
    return count_list

def count_words(words):
    dic = SimpleDict(m=200)
    count_list=[]
    words_set=set(words)
    
    for word in words_set:
        dic.insert(word,words.count(word))
        
    return dic

def sort_by_cnt(count_dict):
    return(sorted(count_dict.items(),key=lambda x: x[1],reverse=True))


############
# QUESTION 4
############

# a
def next_row(lst):
    pasrow = [1 for i in range(len(lst)+1)]
    pasrow[-1] = 1
    
    for i in range(1, len(pasrow)-1):
        pasrow[i] = lst[i-1] + lst[i]
        
    return pasrow

# b   
def generate_pascal():
    pascal = next_row([])
    
    while True:
        yield (pascal)
        pascal = next_row(pascal)

# c
def generate_bernoulli():
    ber = []
    
    while True:
        ber=next_row(ber)
        ber_row = [[1] for i in ber]
        ber_row[0] = 1
        for i in range(1,len(ber)):
            ber_row[i] = ber[i] + ber_row[i-1]
            
        yield ber_row
    


############
# QUESTION 5
############

##In order to test Q5 uncomment the following line
from matrix import * #matrix.py needs to be at the same directory

# a
def upside_down(im):
    n,m = im.dim()
    im2 = matrix(n,m)
    for i in range(n):
        for j in range(m):
            im2[i,j] = im[(n-i-1, j)]
    return im2


# b
def join_v(matrix1, matrix2):
    """ joins two matrices, one on top of the other with some separation """
    n1,m1 = matrix1.dim()
    n2,m2 = matrix2.dim()
    m = max(m1,m2)
    n = n1+n2-1
    new = Matrix(n, m, val=255)

    for i in range(n1):
        for j in range(m1):
            new[i,j] = matrix1[i,j]
            
    for i in range(n2-1):
        for j in range(m2):
            new[i+n1,j] = matrix2[i+1,j]
    
    return new

def join_h(matrix1, matrix2):
    """ joins two matrices, side by side with some separation """
    n1,m1 = matrix1.dim()
    n2,m2 = matrix2.dim()
    m = m1+m2-1
    n = max(n1,n2)
    new = Matrix(n, m, val=255)

    for i in range(n1):
        for j in range(m1):
            new[i,j] = matrix1[i,j]
            
    for i in range(n2):
        for j in range(m2-1):
            new[i,j+m1] = matrix2[i,j+1]

    return new


def reconstruct_image(m):
    pieces=[0]

    for i in range(1,m*m+1):
        pieces += [Matrix.load("./puzzle/im"+str(i)+".bitmap")]
    leftlst=makecol(m,pieces)
    allpieces=[]

    for i in leftlst:
        allpieces+=[makerow(i,m,pieces)]
    puzzle=pieces[allpieces[0][0]]

    for x in range(1,m):
        im_next_right=pieces[allpieces[0][x]]
        puzzle=join_h(puzzle,im_next_right)         

    for y in range(1,m):
        im_row=pieces[allpieces[y][0]]
        for x in range(1,m):
            im_next_right=pieces[allpieces[y][x]]
            im_row=join_h(im_row,im_next_right)
        puzzle=join_v(puzzle,im_row)

    return puzzle

    


def find_top(i,m,pieces):
    pieces=pieces
    x = pieces[i]

    for matrix in range(1,m*m+1):
            y = pieces[matrix]
            cnt=0

            for pix in range(y.dim()[1]):
                if (x[0,pix] != y[y.dim()[0]-1,pix]):
                    break
                else:
                    cnt+=1

            if cnt==y.dim()[1]:
                return False

    return True

def find_left(i,m,pieces):
    x = pieces[i]

    for matrix in range(1,m*m+1):
            y = pieces[matrix]
            cnt=0

            for pix in range(y.dim()[0]):
                if (x[pix,0] != y[pix,y.dim()[1]-1]):
                    break
                else:
                    cnt+=1

            if cnt==y.dim()[0]:
                return False

    return True



def topleft(m,pieces):
    pieces=pieces

    for matrix in range(1,m*m+1):
            if find_top(matrix,m,pieces) and find_left(matrix,m,pieces):
                return matrix
    
def makecol(m,pieces):
    pieces=pieces
    newlst=[topleft(m,pieces)]

    for item in newlst:
        flag=True
        first_matrix = pieces[item]

        for matrix in range(1,m*m+1):
                if flag==False:
                    break
                second_matrix = pieces[matrix]
                cnt=0

                for pix in range(second_matrix.dim()[1]):
                    if (first_matrix[second_matrix.dim()[0]-1,pix] != second_matrix[0,pix]):
                        break
                    else:
                        cnt+=1

                if cnt==second_matrix.dim()[1]:
                    newlst+=[matrix]
                    flag=False
                    
    return newlst  

def makerow(x,m,pieces):
    pieces = pieces
    newlst = [x]

    for item in newlst:
        flag=True
        first_matrix = pieces[item]

        for matrix in range(1,m*m+1):
                if flag==False:
                    break
                second_matrix = pieces[matrix]
                cnt=0

                for pix in range(second_matrix.dim()[0]):
                    if (first_matrix[pix,second_matrix.dim()[1]-1] != second_matrix[pix,0]):
                        break
                    else:
                        cnt+=1

                if cnt==second_matrix.dim()[0]:
                    newlst+=[matrix]
                    flag=False      

    return newlst









########
# Tester
########

def test():

    #Question 1
    q = Polynomial([0, 0, 0, 6])
    if str(q) != "(6*x^3)":
        print("error in Polynomial.__init__ or Polynomial.in __repr__")
    if q.degree() != 3:
        print("error in Polynomial.degree")
    p = Polynomial([3, -4, 1])
    if p.evaluate(10) != 63:
        print("error in Polynomial.evaluate")
    dp = p.derivative()
    ddp = p.derivative().derivative()
    if ddp.evaluate(100) != 2:
        print("error in Polynomial.derivative")
    if not p == Polynomial([3, -4, 1]) or p==q:
        print("error in Polynomial.__eq__")
    r = p+q
    if r.evaluate(1) != 6:
        print("error in Polynomial.__add__")
    if not (q == Polynomial([0, 0, 0, 5]) + Polynomial([0, 0, 0, 1])):
        print("error in Polynomial.__add__ or Polynomial.__eq__")
    if (-p).evaluate(-10) != -143:
        print("error in Polynomial.__neg__")
    if (p-q).evaluate(-1) != 14:
        print("error in Polynomial.__sub__")
    if (p*q).evaluate(2) != -48:
        print("error in Polynomial.__mult__")
    if (Polynomial([0])*p).evaluate(200) != 0:
        print("error in Polynomial class")
    root = p.find_root()
    if root-3 > 10**-7 and root-1 > 10**-7:
        print("error in Polynomial.find_root")


    #Question 2
    t = None
    t = insert(t, 1, 85) #the first time we change t from None to a "real" Node
    insert(t, 2.3, -30)
    insert(t, -10, 7.5)
    insert(t, 2, 10.3)
    if weight(t) != 92.5:
        print("error in weight()")
    if heavy_path(t) != [1, -10]:
        print("error in heavy path()")

    if find_closest_key(t, -5) != -10:
        print("error in find_closest_key()")
    if find_closest_key(t, 2.2) != 2.3:
        print("error in find_closest_key()")



    #Question 3  
    h = SimpleDict(200)
    h.insert("ab", 2)
    h.insert("ef", 1)
    h.insert("cd", 3)
    d = count_words(["ab", "cd", "cd", "ef", "cd", "ab"]) 
    if d is None:
        print("error in count_words()")
    elif d != h:
        print("error in count_words()")
    if sort_by_cnt(d) != [['cd', 3], ['ab', 2], ['ef', 1]]:
        print("error in sort_by_cnt()")

    
    # Question 4
    gp = generate_pascal()
    if gp == None:
        print("error in generate_pascal()")
    elif next(gp)!=[1] or next(gp)!=[1,1] or next(gp)!=[1,2,1]:
        print("error in generate_pascal()")

    
