import numpy as np



def machine_acc_test(a,b):
    """set a to 1, then use b to test if 1-b is distinguishable from 1. Returns b 
    or None if a-b is indistinguishable from a. a and b must be of the same type"""
    if type(a) != type(b): #if type(a) is not equal to type(b) then type(a-b) could be type(a) or type(b)
        raise Exception("type a",type(a), "is not equal to type b",type(b))
    if a - b != a:
        return b
    return None


def float_test_asses():
    print(np.finfo(np.longdouble)) #this outputs the machine accuracy of the system according to python
    #this will be different depending on your system. for example epsneg = 5.421e-20 on
    #my linux machine and 1.11e-16 on imperial windows machines
    
    my_float = np.array([machine_acc_test(np.float(1),np.float(2**-i)) for i in range(0,100) ])#called my_float because float is a special phrase
    my_float = [i for i in my_float if i is not None] #remove the none entries in my_float
    print('python float epsilon',my_float[-1])#print the last entry in the list. This is the smallest number which a-b != a

    my_float16 = np.array([machine_acc_test(np.float16(1),np.float16(2**-i)) for i in range(0,100) ])
    my_float16 = [i for i in my_float16 if i is not None]
    print('numpy float16 epsilon',my_float16[-1])

    my_float32 = np.array([machine_acc_test(np.float32(1),np.float32(2**-i)) for i in range(0,100) ])
    my_float32 = [i for i in my_float32 if i is not None]
    print('numpy float32 epsilon',my_float32[-1])

    my_float64 = np.array([machine_acc_test(np.float64(1),np.float64(2**-i)) for i in range(0,100) ])
    my_float64 = [i for i in my_float64 if i is not None]
    print('numpy float64 epsilon',my_float64[-1])

    my_float128 = np.array([machine_acc_test(np.float128(1),np.float128(2**-i)) for i in range(0,100) ]) #works on my linux varied success on windows
    my_float128 = [i for i in my_float128 if i is not None]
    print('numpy float128 epsilon',my_float128[-1])



    print('numpy float128(1) + float128(2**-64)- float128(1) =',np.float128(1)+np.float128(2**-64)-np.float128(1)) #this is zero therefore only 64 bits of precision
    #float128 is acting as a longdouble not a true 128

    #print(machine_acc_test(np.float16(1),np.float32(2**-4))) #test for the raise error













