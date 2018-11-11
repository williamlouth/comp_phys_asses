import numpy as np
import pylab as pl
import matplotlib.lines as mlines
import LU_decomp as LU



def linear_interp(x,y,test_x):
    """For given arrays of x and y values function will return the y value of a given x value that is in the range of x values"""
    if not (type(x) is np.ndarray or type(x) is np.array or type(x) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of x",type(x))
    if not (type(y) is np.ndarray or type(y) is np.array or type(y) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of y",type(y))
        
    if test_x > x[x.shape[0]-1] or test_x < x[0]:
        raise ValueError("test_x value", test_x, "outside of x values given",x[0],"to",x[-1], ". Cannot interpolate")
    
    low_i = 0
        
    for i in range(0,x.shape[0]):
        if test_x  > x[i+1]:
            low_i = i+1             #finds the two values of x the test_x value is between
        else:
            break
    
    x0 = x[low_i]       #the x and y values below and above the test_x value
    x1 = x[low_i+1]
    y0 = y[low_i]
    y1 = y[low_i+1]         
        
    test_y = (y0*(x1-test_x) + y1*(test_x - x0) )   /  (x1-x0)    #definition of the y value using linear interpolation
    
    return  test_y
    

def cubic_spline_derivatives(x,y):
    """Computes the second derivatives matrix for a natural cubic spline from a given
    set of x and y data"""
    if not (type(x) is np.ndarray or type(x) is np.array or type(x) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of x",type(x))
    if not (type(y) is np.ndarray or type(y) is np.array or type(y) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of y",type(y))
    n = x.shape[0]
        
    b = np.array([(y[i+1] - y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1]) for i in range(1,n-1)]) #b[0] and b[n-1] are boundary cond and are set below
    
    b = np.insert(b,1,0.0)  #Boundary cond
    b = np.append(b,0.0)    #these boundary conditions make it a natural cubic spline
                            #by forcing the second derivative to be zero at the ends
    
    
    A = np.zeros((n,n))
    A[0][0] = 1.0       #these values can be any number other than 0
    A[n-1][n-1] = 1.0   #just there so that x * y = 0 solves to y = 0  
    for i in range(1,n-1,1):
        A[i][i-1] = (x[i] - x[i-1])/(6.0)
        A[i][i] = (x[i+1] - x[i-1])/(3.0)
        A[i][i+1] = (x[i+1] - x[i])/(6.0)
    
    L,U = LU.decomposition(A)[2:4]      #solve the matrix equation A.f11 = b using LU decomposition
    f11 = LU.forward_back_substitution(L,U,b) #an array of the second derivatives
    
    return f11


def  cubic_spline_interpolation(x,y,f11,test_x):
    """computes a single interpolated y value at test_x. Requires x,y coordinates and the 
    second derivative array from the cubic_spline_derivatives function"""
    if not (type(x) is np.ndarray or type(x) is np.array or type(x) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of x",type(x))
    if not (type(y) is np.ndarray or type(y) is np.array or type(y) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of y",type(y))
    if not (type(f11) is np.ndarray or type(f11) is np.array or type(f11) is list):
        raise Exception("find_inverse only accepts numpy arrays and list. Given type of f11",type(f11))
        
    
    if test_x > x[x.shape[0]-1] or test_x < x[0]:
        raise ValueError("test_x value", test_x, "outside of x values given",x[0],"to",x[-1], ". Cannot interpolate")
    
    low_i = 0
        
    for i in range(0,x.shape[0]):
        if test_x  > x[i+1]:     #finds the two values of x the test_x value is between
            low_i = i+1
        else:
            break
    
    x0 = x[low_i]           #the x and y values below and above the test_x value
    x1 = x[low_i+1]
    y0 = y[low_i]
    y1 = y[low_i+1]
    

    A = (x1-test_x)/(x1-x0)         #equations for the coeficients of the equations
    B = 1.0 - A                     #using the same notation as the lecture notes
    C = (1/6.0)*(A**3 - A)*(x1-x0)**2
    D = (1/6.0)*(B**3 - B)*(x1-x0)**2
    Y = A*y0 + B*y1 + C*f11[low_i] + D*f11[low_i+1]
    
    
    return  Y

def interp_asses_func():
    """Runs the assessment tasks. Plots on a single graph the initial points 
    the linear and cubic interpolations"""
    x = np.array([-2.1,-1.45,-1.3,-0.2,0.1,0.15,0.8,1.1,1.5,2.8,3.8])
    y = np.array([0.012155,0.122151,0.184520,0.960789,0.990050,0.977751,0.528292,0.298197,0.105399,3.936690e-4,5.355348e-7])
    #the arrays given to use in the assignment
    cubic_number = 100
    linear_number = 100

    xs = np.linspace(x[0],x[-1],linear_number)       #create lots of x values between x start and x end for linear interpolation
    xs = np.append(xs,x)                #adding the given points to the curve as else can appear 
    xs = np.sort(xs)                    #as if there is an odd gradient between the two points either side of a given point.

    ys = np.array([linear_interp(x,y,j) for j in xs])
    
    pl.figure(1)               #figure set up
    pl.figure(figsize=(10,7.5))
    pl.xlabel("x",fontsize = 15)
    pl.ylabel("y")
    green_line = mlines.Line2D([], [], color='green', marker='.', markersize=15, label='Raw data')
    blue_line = mlines.Line2D([], [], color='blue', marker='*', markersize=15, label='linear interpolation')
    red_line = mlines.Line2D([], [], color='red', marker='+', markersize=15, label='Cubic spline')
    pl.legend(handles=[green_line,blue_line,red_line])
    pl.title("A plot showing linear interpolation and a natural cubic spline of a set of data",fontsize = 20)
    

   
    
    pl.plot(xs,ys,'b*',markersize = 7.5)          #plot interpolated values
    pl.plot(x,y,'g.',markersize = 7.5)       #plot initial values

    


    X = cubic_spline_derivatives(x,y) #an array of the second derivatives

    interp_x = np.linspace(x[0],x[-1],cubic_number)    #x values for the cubic spline
    interp_y = np.array([cubic_spline_interpolation(x,y,X,interp_x[i]) for i in range(interp_x.shape[0])])
 
    pl.plot(interp_x,interp_y,'r+',markersize = 7.5)
    pl.savefig('interpolation.png',bbox_inches='tight',dpi = 250)
    
    
    


if __name__ == '__main__': #if running as main then run asses func
    interp_asses_func()







