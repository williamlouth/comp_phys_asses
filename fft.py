import numpy as np
import pylab as pl

start = -16
stop = 16
no_points = 1000
step_size = 0.1

#t= np.linspace(start,stop,no_points)
t = np.arange(start,stop,step_size)
            
gt = np.array([(1/(np.sqrt(2*np.pi) )* np.exp((-(i**2))/2)) for i in t])       #gaussian response function 
ht = np.array([4 if i >3 and i <5 else 0 for i in t])                           #signal function

    

    
hfft = np.fft.fft(ht)           #fourier trasnform of h
gfft = np.fft.fft(gt)           #fourier trasnform of g

#print(gt)
#print(ht)


pl.figure(1)        #plot the funcitons
pl.plot(t,gt)
pl.plot(t,ht)

pl.figure(2)        #plot the real parts of the fourier transform
pl.plot(t,hfft.real)
pl.figure(4)
pl.plot(t,gfft.real)


pl.figure(3)
conv = np.fft.ifft(1/(np.pi*2)*gfft*hfft)                   #the convolution of g and h using the convolution theorem  there is a normalisation factor
#pl.plot(t+((stop - start)/2),conv.real)   
pl.plot(t,conv)                      # +(stop - start)/2 is half the freq range,  because of aliasing













































