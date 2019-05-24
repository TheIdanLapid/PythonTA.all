#Skeleton file for HW6 - Spring 2015 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).

from matrix import *


############
# QUESTION 1
############

def fingerprint(mat):
    assert isinstance(mat,Matrix)
    k,makesure = mat.dim()
    assert k==makesure

    return sum(mat[i,j] for i in range(k) for j in range(k))

def move_right(mat, i, j, k, fp):
    left = sum(mat[x,j] for x in range(i,i+k))
    right = sum(mat[x,j+k] for x in range(i,i+k))

    return fp - left + right


def move_down(mat, i, j, k, fp):
    up = sum(mat[i,x] for x in range(j,j+k))
    down = sum(mat[i+k,x] for x in range(j,j+k))

    return fp - up + down

    
def has_repeating_subfigure(mat, k):
    row,col = mat.dim()
    fp = fingerprint(mat[:k,:k])
    fps={fp}
    
    for i in range(row-k):
        
        for j in range(col-k):
            fp_right = move_right(mat,i,j,k,fp if j==0 else fp_right)

            if fp_right in fps:
                return True
            
            else:
                fps.add(fp_right)
                
        fp = move_down(mat,i,0,k,fp)
        
        if fp in fps:
            return True
        
        else:
            fps.add(fp)
            
    return False   



########
# Tester
########

def test():
    #Question 1
    im = Matrix.load("./sample.bitmap")
    k = 2
    if fingerprint(im[:k,:k]) != 384 or \
       fingerprint(im[1:k+1,1:k+1]) != 256 or \
       fingerprint(im[0:k,1:k+1]) != 511:
        print("error in fingerprint()")
    if move_right(im, 0, 0, k, 384) != 511:
        print("error in move_right()")
    if move_down(im, 0, 1, k, 511) != 256:
        print("error in move_down()")
    if has_repeating_subfigure(im, k) != True or\
       has_repeating_subfigure(im, k=3) != False:
        print("error in repeating_subfigure()")





