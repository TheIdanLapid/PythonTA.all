from matrix import *

def reconstruct_image(m):
    equal=True
    use=set()
    puzzle = Matrix.load("./puzzle/im"+str(find_left_top())+".bitmap")
    for item in range(1,m*m+1):
        
        for i in range(1,m*m+1):
                 if i in use:
                     continue
                 right_im = Matrix.load("./puzzle/im"+str(i)+".bitmap")
                 for row in range(19):
                     if puzzle[row,puzzle.dim()[1]-1]!=right_im[row,0]:
                        equal=False
                 if equal==True:      
                         puzzle=join_h(puzzle,right_im)
                         use.add(i)
                 equal=True
       
    return puzzle

def build_rows(m):
    equal=True
    use=set()
    puzzle = Matrix.load("./puzzle/im"+str(find_left_top())+".bitmap")
    for item in range(1,m*m+1):
        
        for i in range(1,m*m+1):
                 if i in use:
                     continue
                 right_im = Matrix.load("./puzzle/im"+str(i)+".bitmap")
                 for row in range(19):
                     if puzzle[row,puzzle.dim()[1]-1]!=right_im[row,0]:
                        equal=False
                 if equal==True:      
                         puzzle=join_h(puzzle,right_im)
                         use.add(i)
                 equal=True
       
    return puzzle

def find_top(i):
    x = Matrix.load("./puzzle/im"+str(i)+".bitmap")
    for mat in range(1,401):
            y = Matrix.load("./puzzle/im"+str(mat)+".bitmap")
            cnt=0
            for pix in range(25):
                if (x[0,pix] == y[18,pix]):
                    cnt+=1
            if cnt==25:
                return False

    return True

def find_left(i):
    x = Matrix.load("./puzzle/im"+str(i)+".bitmap")
    for mat in range(1,401):
            y = Matrix.load("./puzzle/im"+str(mat)+".bitmap")
            cnt=0
            for pix in range(19):
                if (x[pix,0] == y[pix,24]):
                    cnt+=1
            if cnt==19:
                return False

    return True

def find_left_top():
    for mat in range(1,401):
            if find_top(mat) and find_left(mat):
                return mat

def sort_rows(firstcol): #input: list with the first column indexes (using find_left)
    newlist = [282]
    
    for item in range(len(firstcol)):
        x = Matrix.load("./puzzle/im"+str(newlist[item])+".bitmap")    
        for i in range(len(firstcol)):
            y = Matrix.load("./puzzle/im"+str(firstcol[i])+".bitmap")
            cnt=0
            for pix in range(25):
                if (x[18,pix] == y[0,pix]):
                    cnt+=1
            if cnt==25:
                newlist += [firstcol[i]]
        
    return newlist

def join_v(mat1, mat2):
    """ joins two matrices, side by side with some separation """
    n1,m1 = mat1.dim()
    n2,m2 = mat2.dim()
    m = max(m1,m2)
    n = n1+n2
    new = Matrix(n, m, val=255)  # fill new matrix with white pixels
    for i in range(n1):
        for j in range(m1):
            new[i,j] = mat1[i,j]
            
    for i in range(n2):
        for j in range(m2):
            new[i+n1,j] = mat2[i,j]
    
    return new
    
def join_h(mat1, mat2):
    """ joins two matrices, side by side with some separation """
    n1,m1 = mat1.dim()
    n2,m2 = mat2.dim()
    m = m1+m2
    n = max(n1,n2)
    new = Matrix(n, m, val=255)  # fill new matrix with white pixels

    new[:n1,:m1] = mat1
    new[:n2,m1:m] = mat2
    '''
    #without slicing:
    for i in range(n1):
        for j in range(m1):
            new[i,j] = mat1[i,j]
            
    for i in range(n2):
        for j in range(m2):
            new[i,j+m1+10] = mat2[i,j]
    '''
    return new
