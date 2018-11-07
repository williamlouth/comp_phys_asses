import numpy as np
import floating_point_test as fpt
import LU_decomp as LU
import interpolation as interp
import random_numb as ran
import fft

print("*************************************FLOATING POINT VARIABLES*************************************")
fpt.float_test_asses()
print("*************************************MATRIX METHODS*************************************")
LU.LU_asses_func()
print("*************************************INTERPOLATION*************************************")
interp.interp_asses_func()
print("*************************************FOURIER TRANSFORMS*************************************")
fft.fft_asses()
print("*************************************RANDOM NUMBER METHODS*************************************")
ran.random_numb_asses()





















