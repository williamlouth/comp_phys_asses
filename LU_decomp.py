import numpy as np
import pylab as pl




input_array = np.array([[2,2,3],[4,5,6],[7,8,9]])
input_array = np.array([[3,1,0,0,0],[3,9,4,0,0],[0,9,20,10,0],[0,0,-22,31,-25],[0,0,0,-55,60]])
print(input_array)
print(input_array.shape)

N = input_array.shape[0]
print(N)
L = np.zeros((N,N))
U = np.zeros((N,N))
print(L)
print(U)

for i in range(0,N):
    L[i][i] = 1.0
    
print(L)
print("start")

for j in range(0,N):
    for i in range(0,j+1):
        my_sum = 0.0
        for k in range(0,i):
            my_sum += L[i][k]*U[k][j] 
        U[i][j] = input_array[i][j] - my_sum
    

               
        
        
        
    for i in range(j+1,N):
        print("here" , i,j)
        my_sum2 = 0.0
        for k in range(0,j):
            print("test", i, j ,k)
            print(L[i][k])
            print(U[k][j])
            print(L[i][k]*U[k][j])
            my_sum2 += L[i][k]*U[k][j] 

        print("hereeeeeee", my_sum2, i , j)
        
        print("bob", U[j][j],L[i][j],i,j)
        L[i][j] = (1/U[j][j])*(input_array[i][j] - my_sum2)




print("out")
print(L)
print(U)
print("answer",np.dot(L,U))






















































