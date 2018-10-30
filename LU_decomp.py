import numpy as np
import pylab as pl




def decomposition(input_array):
    """decomposes a square matrix into Lower and upper triangular matrices
    returns lower + upper triangle matrices with leading edge lower removed
    and the determinant of the matrix. Only accepts square matrices"""
    
    if input_array.shape[0] != input_array.shape[1]:
        return "input array not a square matrix"
    
    N = input_array.shape[0]
    L = np.zeros((N,N))
    U = np.zeros((N,N))
    
    for i in range(0,N):
        L[i][i] = 1.0               #crouts method used so leading edge on Lower set to 1
    
    for j in range(0,N):            #stepping through the columns
        for i in range(0,j+1):      #this for loop fills in the upper matrix, steps through the row up to the number of the column
            my_sum = 0.0
            for k in range(0,i):
                my_sum += L[i][k]*U[k][j]       #summing up the previous terms in the sum when row of L x col U. 
            U[i][j] = input_array[i][j] - my_sum #This leaves 1 term that is the new term in the Upper matrix
       
        
        for i in range(j+1,N):  #this for loop fills in the lower matrix
            my_sum2 = 0.0
            for k in range(0,j):
                my_sum2 += L[i][k]*U[k][j] 
            L[i][j] = (1/U[j][j])*(input_array[i][j] - my_sum2)   #same as above but for the lower matrix
            
    for i in range(0,N):
        L[i][i] = 0.0       #for putting L and U into 1 matrix remove the leading edge of lower that we set all to 1 at start (crouts method)
        
    det = 1
    for i in range(0,N):
        det *= U[i][i]      #determinant is the product of the leading edge
        
    return L+U,det


    
def L_U_split(input_array):
    """Takes in an array that is L+U and splits it into L and U. Returns L,U.
    only accepts square matrices"""
    if input_array.shape[0] != input_array.shape[1]:
        return "input array not a square matrix"
    N = input_array.shape[0]
    L = np.zeros((N,N))
    U = np.zeros((N,N))
    
    for i in range(0,N):
        for j in range(0,i):
            L[i][j] = input_array[i][j]
        for j in range(i,N):
            U[i][j] = input_array[i][j]
            
    for i in range(0,N):
        L[i][i] = 1.0
    
    return L,U


def forward_back_substitution(L,U,b):
    """does forward and back substitution to return x for an equation of the form L.U.x = b ."""
    if  input_array.shape[0] != input_array.shape[1]:
        return "input array not a square matrix"
    N = L.shape[0]
    y = np.zeros(N)
    x = np.zeros(N)
    
    for i in range(0,N):
        my_sum = 0.0
        for j in range(0,i):
            my_sum += L[i][j]*y[j]
        y[i] = (1.0/L[i][i])*(b[i] - my_sum)
        
    for i in range(N-1,-1,-1):
        my_sum = 0.0
        for j in range(i+1,N):
            my_sum += U[i][j]*x[j]
        x[i] = (1.0/U[i][i])*(y[i] - my_sum)
        
        
    return x
    

def find_inverse(input_array):
    """returns the inverse of a square matrix by LU decomposition and the forward back substitution"""
    if  input_array.shape[0] != input_array.shape[1]:
        return "input array not a square matrix"
    N = input_array.shape[0]
    L,U = L_U_split(decomposition(input_array)[0])
    inv_A = np.zeros((N,N))
    
    for j in range(0,N):
        b = np.zeros(N)
        b[j] = 1.0
        x = forward_back_substitution(L,U,b)
        for i in range(0,N):
            inv_A[i][j] = x[i]
    
    return inv_A


input_array = np.array([[3,1,0,0,0],[3,9,4,0,0],[0,9,20,10,0],[0,0,-22,31,-25],[0,0,0,-55,60]])
#print(decomposition(input_array))

b = np.array([2,5,-4,8,9])

L,U = L_U_split(decomposition(input_array)[0])

#out = decomposition(input_array)
#print(out)
#L,U = L_U_split(out[0])

#print(L)
#print(U)
#print(L_U_split(out[0]))


#print(forward_back_substitution(L,U,b))

x = forward_back_substitution(L,U,b)

A = np.dot(L,U)

Ax = np.dot(A,x)
#print(Ax)

x0 = forward_back_substitution(L,U,np.array([1,0,0,0,0]))
#print(x0)

inv_A = find_inverse(A)
#print(inv_A)
#print(np.dot(A,inv_A))




















































