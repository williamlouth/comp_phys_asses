import numpy as np
import pylab as pl



gt = np.array([0.0])
ht = np.array([0.0])
t = np.arange(-20,20,0.1)
for i in t:
    gt = np.append(gt, [(1/(np.sqrt(2*np.pi) )* np.exp((-(i**2))/2))] )
    
    if i > 3 and i < 5:
        ht = np.append(ht,4)
    else:
        ht = np.append(ht,0)
            
    
gt = np.delete(gt,0)
ht = np.delete(ht,0)
    
hfft = np.fft.fft(ht)
gfft = np.fft.fft(gt)

print(gt)
print(ht)
#prin

pl.figure(1)
pl.plot(t,gt)
pl.plot(t,ht)

pl.figure(2)
pl.plot(t,hfft)
pl.plot(t,gfft)


pl.figure(3)
conv = np.fft.ifft(np.pi*2*gfft*hfft)
pl.plot(t+20,conv)  #   +20 is half the freq range,  because of aliasing













































