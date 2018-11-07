import numpy as np




def decomposition(input_array):
    """decomposes a square matrix into Lower and upper triangular matrices
    returns lower + upper triangle matrices with leading edge lower removed
    and the determinant of the matrix. Only accepts square matrices"""
    
    if not (type(input_array) is np.ndarray or type(input_array) is np.array or type(input_array) is list):
            raise Exception("decomposition only accepts numpy arrays and list. Given type of input_array",type(input_array))
    try:
        input_array[0]
    except:
        raise ValueError("input_array is an empty array")
            
    try:
        if input_array.shape[0] != input_array.shape[1]:
            raise Exception("input array is not a square matrix. Matrix shape is",input_array.shape)
    except IndexError:
        raise Exception("input array is not a square matrix. array shape is",input_array.shape)
        
        
    
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
            
    output_L = np.copy(L)   #keep a copy of L before removing leading edge ones
    for i in range(0,N):
        L[i][i] = 0.0       #for putting L and U into 1 matrix remove the leading edge of lower that we set all to 1 at start (crouts method)
        
    det = 1.0
    for i in range(0,N):
        det *= U[i][i]      #determinant is the product of the leading edge
        
    return L+U,det,output_L,U


    


def forward_back_substitution(L,U,b):
    """does forward and back substitution to return x for an equation of the form L.U.x = b ."""
    
    if not (type(L) is np.ndarray or type(L) is np.array or type(L) is list):
            raise Exception("forward_back_substitution only accepts numpy arrays and list. Given type of L",type(L))
    if not (type(U) is np.ndarray or type(U) is np.array or type(U) is list):
            raise Exception("forward_back_substitution only accepts numpy arrays and list. Given type of U",type(U))
    if not (type(b) is np.ndarray or type(b) is np.array or type(b) is list):
            raise Exception("forward_back_substitution only accepts numpy arrays and list. Given type of b",type(b))
            
    L = np.asarray(L)   #type cast to numpy array
    U = np.asarray(U)
    b = np.asarray(b)
    
    
    
    N = L.shape[0]
    y = np.zeros(N)
    x = np.zeros(N)
    
    for i in range(0,N):        #solve for y in equation L.y = b
        my_sum = 0.0
        for j in range(0,i):    #range of the column is up to the row value
            my_sum += L[i][j]*y[j]  
        y[i] = (1.0/L[i][i])*(b[i] - my_sum)    
        
    for i in range(N-1,-1,-1):  #solve for x using the y values computed above
        my_sum = 0.0            #range counts down from N-1 to 0. This is due to the shape of the lower matrix
        for j in range(i+1,N):
            my_sum += U[i][j]*x[j]
        x[i] = (1.0/U[i][i])*(y[i] - my_sum)
        
        
    return x
    

def find_inverse(input_array):
    """returns the inverse of a square matrix by LU decomposition and the forward back substitution"""
    
    if not (type(input_array) is np.ndarray or type(input_array) is np.array or type(input_array) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of input_array",type(input_array))
    try:
        input_array[0]
    except:
        raise ValueError("input_array is an empty array")
            
    try:
        if input_array.shape[0] != input_array.shape[1]:
            raise Exception("input array is not a square matrix. Matrix shape is",input_array.shape)
    except IndexError:
        raise Exception("input array is not a square matrix. array shape is",input_array.shape)
        

    N = input_array.shape[0]
    L,U = (decomposition(input_array)[2:4]) #decompose the array into Lower and Upper triangular matrices
    inv_A = np.zeros((N,N))                 #create an empty array to fill
    
    for j in range(0,N):    #use eqn solver for L.U.x = b do this for each column in the identity matrix
        b = np.zeros(N)     
        b[j] = 1.0          #this sets the correct value of b to 1 for the relevent column of the identity matrix being calculated
        x = forward_back_substitution(L,U,b)
        for i in range(0,N):
            inv_A[i][j] = x[i]  #fill in the column of the identity matrix
    
    return inv_A


def LU_asses_func():
    input_array = np.array([[3,1,0,0,0],[3,9,4,0,0],[0,9,20,10,0],[0,0,-22,31,-25],[0,0,0,-55,60]])
    print('input_array',input_array)
    determinant,L,U = decomposition(input_array)[1:4]
    print('lower matrix', L)
    print('upper matrix', U)
    print('determinant', determinant)
    
    b = np.array([2,5,-4,8,9])
    print('input b',b)
    x = forward_back_substitution(L,U,b)
    print('x',x)


    inv_A = find_inverse(input_array)
    print('inverse of input_array',inv_A)
    return



if __name__ == '__main__': #if running as main then run asses func
    LU_asses_func()











