import numpy as np
import pylab as pl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches


def asses_gaussian(t):
    return (1/(np.sqrt(2*np.pi) )* np.exp((-(t**2))/2))
    
def asses_top_hat(t):
    if t > 3 and t < 5:
        return 4
    else:
        return 0

def fft_asses():
    start = 0           #this has to be zero
    stop = 50
    step_size = 0.1
    
    
    t = np.arange(start,stop,step_size)
    no_points = t.size
                
         
    gt = np.array([asses_gaussian(x)  if x<stop/2 else asses_gaussian(stop-x) for x in t])   
    ht = np.array([asses_top_hat(x) for x in t])
    
        
    hfft = np.fft.fft(ht)           #fourier trasnform of h
    gfft = np.fft.fft(gt)           #fourier trasnform of g
    
    conv = step_size*np.fft.ifft(gfft*hfft)   #the convolution of g and h using the convolution theorem
    #step_size is the normalisation constant
    
    
    fft_freq = np.fft.fftfreq(no_points)      #the frequencies that the fourier transform returns
    
    pl.figure(24)        #plot the functions
    pl.figure(figsize=(10,7.5))
    pl.xlabel("time (s)",fontsize = 20)
    pl.ylabel("g(t),h(t)",fontsize = 20)
    pl.title("A graph showing g(t) and h(t)",fontsize = 20)
    orange_line = mlines.Line2D([], [], color='orange', marker='+', markersize=15, label='g(t)')
    blue_line = mlines.Line2D([], [], color='blue', marker='+', markersize=15, label='h(t)')
    pl.legend(handles=[orange_line,blue_line])
    pl.plot(t,gt,'orange')
    pl.plot(t,ht,'b')
    pl.savefig("gtht.png",bbox_inches = 'tight',dpi = 200)
    
    pl.figure(8)        #plot the real parts of the fourier transform
    pl.figure(figsize=(10,7.5))
    pl.xlabel("frequency",fontsize = 20)
    pl.ylabel("real part of fft(g(t)) and fft(h(t))",fontsize = 20)
    pl.title("A graph showing the fast fourier transform of g(t) and h(t)",fontsize = 20)
    orange_line = mlines.Line2D([], [], color='orange', marker='+', markersize=15, label='fft of g(t)')
    blue_line = mlines.Line2D([], [], color='blue', marker='+', markersize=15, label='fft of h(t)')
    pl.legend(handles=[orange_line,blue_line])
    pl.plot(fft_freq,hfft.real,'b')
    pl.plot(fft_freq,gfft.real,'orange')
    pl.savefig("ffts.png",bbox_inches = 'tight',dpi = 200)
    
    
    pl.figure(10)    #plot the convolution of g and h
    pl.figure(figsize=(10,7.5))
    pl.xlabel("time (s)",fontsize = 20)
    pl.ylabel("convolution of g(t) and h(t)",fontsize = 20)
    pl.title("A graph showing the convolution of g(t) and h(t)",fontsize = 20)
                    
    pl.plot(t,conv.real)
    pl.savefig("conv.png",bbox_inches = 'tight',dpi = 200)








if __name__ == '__main__': #if running as main then run asses func
    fft_asses()
































