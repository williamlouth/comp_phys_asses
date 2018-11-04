import unittest
import interpolation as interp
import numpy as np

class test(unittest.TestCase):
    def test_linear_interp(self):
        x = np.arange(0,10,1)
        y = 2*x
        self.assertEqual(interp.linear_interp(x,y,2),  4)
        self.assertEqual(interp.linear_interp(x,y,2.5),  5)
        self.assertRaises(Exception,interp.linear_interp,x,2,2) #check that passing an int raises an error
    def test_cubic_spline_derivatives(self):
        x = np.arange(0,10,1)
        y = 2*x
        np.testing.assert_almost_equal(interp.cubic_spline_derivatives(x,y) ,np.zeros(10))
        self.assertRaises(Exception,interp.cubic_spline_derivatives,1.1,y) #check that passing an int raises an error
    def test_cubic_spline_interpolation(self):
        x = np.arange(0,10,1)
        y = 2*x
        f11 = interp.cubic_spline_derivatives(x,y)
        np.testing.assert_almost_equal(interp.cubic_spline_interpolation(x,y,f11,2.5) ,5)
        self.assertRaises(Exception,interp.cubic_spline_interpolation,x,y,1.1,2.5) #check that passing an int raises an error

        
  
        
if __name__ == '__main__': #if running as main then run test scripts
    unittest.main()





























