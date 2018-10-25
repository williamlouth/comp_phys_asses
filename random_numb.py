import numpy as np
import pylab as pl



np.random.seed(10)




uniform_0to1 = np.random.uniform(0,1,10**5)
pl.figure(1)
pl.hist(uniform_0to1,100)



uniform_0topi = uniform_0to1 * np.pi
pl.figure(2)
pl.hist(uniform_0topi,100)


hsin = np.array([np.arccos(1-2*x) for x in uniform_0to1])  #intergrate 0.5sinx then inverse it. Check limits
pl.figure(3)
pl.hist(hsin)





keep = np.array([x for x in uniform_0topi if np.random.uniform(0,1) < (2/np.pi)*(np.sin(x))**2])
pl.figure(4)
pl.hist(keep)

#keep = np.array([x if np.random.uniform(0,1) < (2/np.pi)*(np.sin(x))**2 for x in uniform_0topi])


# =============================================================================
# for i in c:
#     if np.random.uniform(0,1) < (2/np.pi)*(np.sin(i))**2:
#         keep = np.append(keep,i)
# =============================================================================
        
    





# =============================================================================
# keep2 = np.array([0.0])
# for i in d:
#     if np.random.uniform(0,1) * 0.5*np.sin(i)  <  (2/np.pi)*np.sin(i)**2:
#         keep2 = np.append(keep2,i)
#     
# pl.figure(4)
# pl.hist(keep)
# 
# =============================================================================







































