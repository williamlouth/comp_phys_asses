import numpy as np
import pylab as pl



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
    print(x0,x1,y0,y1)
        
    test_y = (y0*(x1-test_x) + y1*(test_x - x0) )   /  (x1-x0)
    
    return  test_y
    

xs = np.linspace(-2.1,3.8,20)
ys = np.array([])
for j in xs:
    ys = np.append(ys,linear_interp(x,y,j))
    
#bob = linear_interp(x,y,3)
#print(bob)
print(xs)
print(ys)

pl.plot(xs,ys) 
""" This is not the correct plot. It plots between lines"""
pl.plot(x,y)








