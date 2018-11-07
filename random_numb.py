import numpy as np
import pylab as pl


def random_numb_asses(rand_number = 10**5):
    np.random.seed(10)      #seed the random number generator
    
    histogram_bin_number = 50
    
    
    uniform_0to1 = np.random.uniform(0,1,rand_number)         #use numpy random to generate a np array of random numbers uniform between 0 and 1
    pl.figure(1548)
    pl.figure(figsize=(15,10))
    pl.xlabel("x",fontsize = 20)
    pl.ylabel("Number of random numbers",fontsize = 20)
    pl.title("A histogram showing a uniform distribution between 0 and 1",fontsize = 20)
    pl.hist(uniform_0to1,histogram_bin_number)                           #plot a histogram of the uniform random numbers
    pl.savefig("uniform01",bbox_inches = 'tight')
    
    
    uniform_0topi = uniform_0to1 * np.pi                #create a uniform distribution of random numbers from 0 to pi
    pl.figure(2)
    pl.figure(figsize=(15,10))
    pl.xlabel("x",fontsize = 20)
    pl.ylabel("Number of random numbers",fontsize = 20)
    pl.title("A histogram showing a uniform distribution between 0 and pi",fontsize = 20)
    pl.hist(uniform_0topi,histogram_bin_number)                          #plot the histogram
    pl.savefig("uniform0pi",bbox_inches = 'tight')
    
    #transform method
    hsin = np.array([np.arccos(1-2*x) for x in uniform_0to1])  #create random numbers with a half sin(x) distribution
    pl.figure(3)                                        #intergrate 0.5sinx then inverse it. Check limits
    pl.figure(figsize=(15,10))
    pl.xlabel("x",fontsize = 20)
    pl.ylabel("Number of random numbers",fontsize = 20)
    pl.title("A histogram showing a " + r'$\frac{1}{2}$'+  "sin(x) distribution",fontsize = 20)
    pl.hist(hsin,histogram_bin_number)
    pl.savefig("halfsinx",bbox_inches = 'tight')
    
    
    
    #rejection method  with a comparison function of y = 1
    #creates a np array with random nuumbers with a 2/pi *sin squared distribution
    uniform_0topi_4length = np.pi*np.random.uniform(0,1,rand_number*4) #epsilon aprox equal to 0.3 -> need 4 times length to get rand_number of random numbers
    sin2 = np.array([x for x in uniform_0topi_4length if np.random.uniform(0,1) < (2/np.pi)*(np.sin(x))**2])
    print("epsilon for rejection method with comparison function y = 1",len(sin2)/len(uniform_0topi_4length))
    
    sin2 = sin2[:rand_number]
    pl.figure(4)
    pl.figure(figsize=(15,10))
    pl.xlabel("x",fontsize = 20)
    pl.ylabel("Number of random numbers",fontsize = 20)
    pl.title("A histogram showing a " + r'$\frac{2}{\pi}sin^2(x)$'+  " distribution\n using a y = 1 comparison function",fontsize = 20)
    pl.hist(sin2,histogram_bin_number)
    pl.savefig("1sin2x",bbox_inches = 'tight')
    
    
    
    #rejection method  with a comparison function of y =2/pi sin(x)
    #creates a np array with random nuumbers with a 2/pi *sin squared distribution
    uniform_0to1_2length =  np.random.uniform(0,1,rand_number*2)  #epsilon aprox equal to 0.7 -> need 2 times length to get rand_number of random numbers
    my_sin =  np.array([np.arccos(1-x*np.pi/2) for x in uniform_0to1_2length*4/np.pi])     #4/pi so that arcos domain is 1 -> -1
    

    sin3 = np.array([x for x in my_sin if np.random.uniform(0,1) * 2/np.pi * np.sin(x)  < (2/np.pi)*(np.sin(x))**2])
    print("epsilon for rejection method with comparison function y = 2/pi sin(x)",len(sin3)/len(uniform_0to1_2length))
    
  
    sin3 = sin3[:rand_number]
    pl.figure(5)
    pl.figure(4)
    pl.figure(figsize=(15,10))
    pl.xlabel("x",fontsize = 20)
    pl.ylabel("Number of random numbers",fontsize = 20)
    pl.title("A histogram showing a " + r'$\frac{2}{\pi}sin^2(x)$'+  " distribution\n using a y = " + r'$\frac{2}{\pi}sin(x)$' +" comparison function",fontsize = 20)
    pl.hist(sin3,histogram_bin_number)
    pl.savefig("2pisin2x",bbox_inches = 'tight')
    
    
    
if __name__ == '__main__': #if running as main then run asses func
    random_numb_asses()
































