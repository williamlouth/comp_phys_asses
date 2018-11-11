import unittest
import numpy as np
import fft

class test(unittest.TestCase):
	def test_fft_top_hat(self):
		self.assertEqual(fft.asses_top_hat(0),0)
		self.assertEqual(fft.asses_top_hat(4),4)
		self.assertEqual(fft.asses_top_hat(10),0)
	def test_fft_gaussian(self):
         self.assertAlmostEqual(fft.asses_gaussian(0),1.0/np.sqrt(2*np.pi))
         self.assertAlmostEqual(fft.asses_gaussian(10),0)
         self.assertAlmostEqual(fft.asses_gaussian(-10),0)

if __name__ == '__main__': #if running as main then run test scripts
    unittest.main()