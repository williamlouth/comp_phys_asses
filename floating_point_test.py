import numpy as np
import pylab as pl


#np.set_printoptions(formatter = float,floatmode = None)
a = np.float64(1.0)







print(np.finfo(np.longdouble))
print(a-2**-52)
c = 0

for i in range(1,100,1):
    b = np.float64(2**-i)      #python does irratating type allocations
    if  a-b != 1.0:
        print(b)
        print("%.64f" % (a-b))
    else:
        print(b)
        print("%.64f" % (a-b))
        print(i-1)
        c= i-1
        break

# =============================================================================
# print(c)
# print(2**-c)
# print(a)
# print(np.float64(a-2**-c))
# =============================================================================



























