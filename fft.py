import numpy as np
import pylab as pl

start = -10
stop = 15
#no_points = 100
step_size = 0.05

#t= np.linspace(start,stop,no_points)
t = np.arange(start,stop,step_size)
no_points = t.size
            
#gt = np.array([(1/(np.sqrt(2*np.pi) )* np.exp((-(i**2))/2)) for i in t]) 
#ht = np.array([(1/(np.sqrt(2*np.pi) )* np.exp((-(i**2))/2)) for i in t])       #gaussian response function 
#ht = np.array([4 if i >3 and i <5 else 0 for i in t])
#gt = np.array([4 if i >3 and i <5 else 0 for i in t])

gt = np.array([1 if i >-0.5 and i <0.5 else 0 for i in t])
ht = np.array([1 if i >0 and i <1 else 0 for i in t])

                           #signal function
#print(ht)

def f(t):
    if t > -0.5 and t < 0.5:
        return 1
    else:
        return 0
    
def g(t):
    if t > 0 and t < 1:
        return 1
    else:
        return 0
    
def asses_gaussian(t):
    return (1/(np.sqrt(2*np.pi) )* np.exp((-(t**2))/2))

def asses_top_hat(t):
    if t > 3 and t < 5:
        return 4
    else:
        return 0
    
    
    
gt = np.array([asses_gaussian(x) for x in t])   
ht = np.array([asses_top_hat(x) for x in t])
    


    

    
hfft = np.fft.fft(ht)           #fourier trasnform of h
gfft = np.fft.fft(gt)           #fourier trasnform of g
# =============================================================================
# 
# test = np.array(gfft)
# gfft = np.append(test[int(len(test)/2):] , test[:int(len(test)/2)] )
# gfft  = np.array(gfft)
# 
# 
# test2 = np.array(hfft)
# hfft = np.append(test2[int(len(test2)/2):] , test2[:int(len(test2)/2)]  )
# hfft = np.array(hfft)
# =============================================================================


fft_freq = np.fft.fftfreq(no_points)
#fft_freq = np.fft.fftshift(fft_freq)

#print(gt)
#print(ht)


pl.figure(1)        #plot the funcitons
pl.plot(t,gt)
pl.plot(t,ht)

pl.figure(2)        #plot the real parts of the fourier transform
pl.plot(fft_freq,hfft)
pl.figure(3)
pl.plot(fft_freq,gfft)


pl.figure(7)
x = gfft*hfft
pl.plot(fft_freq,x)


pl.figure(4)
conv = np.fft.ifft(hfft*gfft)                   #the convolution of g and h using the convolution theorem  there is a normalisation factor
#pl.plot(t+((stop - start)/2),conv.real)   
pl.plot(t,conv.real)                      # +(stop - start)/2 is half the freq range,  because of aliasing

pl.figure(5)
#t2 = np.linspace(start*2,stop*2,(no_points*2)-1)
t2 = np.arange(start*2,stop*2,step_size)
t2 = t2[0:t2.size-1]
npconv = np.convolve(gt,ht)
pl.plot(t2,npconv)










# =============================================================================
# my_f = [f(x) for x in t]
# my_g = [g(x) for x in t]
# conv = np.empty([len(t)])
# 
# for x in range(len(t)):
#     msum = 0.0
#     for i in t:
#         msum += ( f(t[x]-i)* g(i) )
#     conv[x] = msum
#    
# pl.figure(99)
# pl.plot(t,conv)     
# =============================================================================


conv = np.empty([len(t)])

for x in range(len(t)):
    msum = 0.0
    for i in t:
        msum += ( asses_gaussian(t[x]-i)* asses_top_hat(i) )
    conv[x] = msum
   
pl.figure(99)
pl.plot(t,conv)     

































