import unittest
import LU_decomp as LU
import numpy as np

class test(unittest.TestCase):
    def test_simple_decomp(self):
        a = np.array([[1,2,3],[4,5,5],[7,8,9]])
        np.testing.assert_almost_equal(LU.decomposition(a)[0] , np.array([[ 1.,2.,3.],[4.,-3.,-7.],[7.,2.,2.]]))
        np.testing.assert_almost_equal(LU.decomposition(a)[1] , -6.0)
        np.testing.assert_almost_equal(LU.decomposition(a)[2] , np.array([[1.,0.,0.],[4.,1.,0.],[7.,2.,1.]]))
        np.testing.assert_almost_equal(LU.decomposition(a)[3] , np.array([[1.,2.,3.],[0.,-3.,-7.],[0.,0.,2.]]))
        
    def test_simple_find_inverse(self):
        a = np.array([[1,2,3],[4,5,5],[7,8,9]])
        inv_a = np.array([[-0.83333333,-1.,0.83333333],[0.16666667,2.,-1.16666667],[0.5,-1.,0.5]])
        np.testing.assert_almost_equal(LU.find_inverse(a) , inv_a)
        
    def test_forward_back(self):
        L = [[1,2],[4,5]]
        U = [[1,2],[4,5]]
        b = [[2],[2]]
        np.testing.assert_almost_equal(LU.forward_back_substitution(L,U,b), [2.48,-0.24])
        
if __name__ == '__main__': #if running as main then run test scripts
    unittest.main()