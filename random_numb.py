import numpy as np
import pylab as pl



np.random.seed(10)      #seed the random number generator

rand_number = 10**5    #the number of random numbers
histogram_bin_number = 100


uniform_0to1 = np.random.uniform(0,1,rand_number)         #use numpy random to generate a np array of random numbers uniform between 0 and 1
pl.figure(1)
pl.hist(uniform_0to1,histogram_bin_number)                           #plot a histogram of the uniform random numbers



uniform_0topi = uniform_0to1 * np.pi                #create a uniform distribution of random numbers from 0 to pi
pl.figure(2)
pl.hist(uniform_0topi,histogram_bin_number)                          #plot the histogram


#transform method
hsin = np.array([np.arccos(1-2*x) for x in uniform_0to1])  #create random numbers with a half sin(x) distribution
pl.figure(3)                                        #intergrate 0.5sinx then inverse it. Check limits
pl.hist(hsin,histogram_bin_number)




#rejection method  with a comparison function of y = 1
#creates a np array with random nuumbers with a 2/pi *sin squared distribution
sin2 = np.array([x for x in uniform_0topi if np.random.uniform(0,1) < (2/np.pi)*(np.sin(x))**2])
pl.figure(4)
pl.hist(sin2,histogram_bin_number)



#rejection method  with a comparison function of y = 0.5sin(x)
#creates a np array with random nuumbers with a 2/pi *sin squared distribution
my_sin =  np.array([np.arccos(1-x) for x in uniform_0to1*2])    #I wrote my own sin distribution instead of the numpy one :)

sin3 = np.array([x for x in my_sin if np.random.uniform(0,1) *  np.sin(x)  < (2/np.pi)*(np.sin(x))**2])
pl.figure(5)
pl.hist(sin3,histogram_bin_number)



#many more rejected in first rejection method








































