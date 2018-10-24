import numpy as np
import pylab as pl



np.random.seed(10)
a = np.random.uniform(0,1)
b = np.array([0.0])
for i in range(0,10**5):
    b = np.append(b,np.random.uniform(0,1))

pl.figure(1)
pl.hist(b,100)

c = np.array([0.0])

for i in b:
    c = np.append(c,i*2)

print(c)

d = np.array([0.0])
for i in b:
    d = np.append(d,np.arccos(1-2*i))

#print(d)
pl.figure(2)
pl.hist(d)





keep = np.array([0.0])
for i in c:
    if np.random.uniform(0,1) < (2/np.pi)*(np.sin(i))**2:
        keep = np.append(keep,i)
        
    


pl.figure(3)
pl.hist(keep)










































