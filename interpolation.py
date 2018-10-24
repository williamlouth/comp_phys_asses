import numpy as np
import pylab as pl
import LU_decomp as LU



x = np.array([-2.1,-1.45,-1.3,-0.2,0.1,0.15,0.8,1.1,1.5,2.8,3.8])
y = np.array([0.012155,0.122151,0.184520,0.960789,0.990050,0.977751,0.528292,0.298197,0.105399,3.936690e-4,5.355348e-7])
#print(x)
#print(y)

#print(x.shape)
#print(y.shape)

def linear_interp(x,y,test_x):
    if test_x > x[x.shape[0]-1] or test_x < x[0]:
        return None
    
    low_i = 0
        
    for i in range(0,x.shape[0]):
        if test_x  > x[i+1]:
            low_i = i+1
        else:
            break
    
    x0 = x[low_i]
    x1 = x[low_i+1]
    y0 = y[low_i]
    y1 = y[low_i+1]
    #print(x0,x1,y0,y1)
        
    test_y = (y0*(x1-test_x) + y1*(test_x - x0) )   /  (x1-x0)
    
    return  test_y
    

def cubic_spline(x,y):
    n = x.shape[0]
    b = np.zeros((n,1))
    for i in range(0,n-1):
        b[i] = (y[i+1] - y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1])
    
    b[0] = 0.0          #Boundary cond
    b[n-1] = 0.0
    
    
    A = np.zeros((n,n))
    A[0][0] = 1.0       #Boundary cond
    A[n-1][n-1] = 1.0
    for i in range(1,n-1,1):
        A[i][i-1] = (x[i] - x[i-1])/(6.0)
        A[i][i] = (x[i+1] - x[i-1])/(3.0)
        A[i][i+1] = (x[i+1] - x[i])/(6.0)
    
    
    print(A)
    
    thing = LU.decomposition(A)[0]
    L,U = LU.L_U_split(thing)
    X = LU.forward_back_substitution(L,U,b)
    
    return X


def  cubic_spline2(x,y,test_x):
    f11 = cubic_spline(x,y)
    
    
    if test_x > x[x.shape[0]-1] or test_x < x[0]:
        return None
    
    low_i = 0
        
    for i in range(0,x.shape[0]):
        if test_x  > x[i+1]:
            low_i = i+1
        else:
            break
    
    x0 = x[low_i]
    x1 = x[low_i+1]
    y0 = y[low_i]
    y1 = y[low_i+1]
    

    A = (x1-test_x)/(x1-x0)
    B = 1.0 - A
    C = (1/6.0)*(A**3 - A)*(x1-x0)**2
    D = (1/6.0)*(B**3 - B)*(x1-x0)**2
    Y = A*y0 + B*y1 + C*f11[low_i] + D*f11[low_i+1]
    
    
    return  Y
xs = np.linspace(-2.1,3.8,20)
ys = np.array([])
for j in xs:
    ys = np.append(ys,linear_interp(x,y,j))
    
#bob = linear_interp(x,y,3)
#print(bob)
#print(xs)
#print(ys)

#pl.plot(xs,ys) 
""" This is not the correct plot. It plots between lines"""
#pl.plot(x,y)


X = cubic_spline(x,y)
print(X)
print(cubic_spline2(x,y,2))
interp_x = np.linspace(-2.1,3.8,100)
interp_y = np.zeros([interp_x.shape[0]])
for i in range(interp_x.shape[0]):
    interp_y[i] = cubic_spline2(x,y,interp_x[i])

print(interp_x)    
print(interp_y)    
pl.plot(interp_x,interp_y,'+')







