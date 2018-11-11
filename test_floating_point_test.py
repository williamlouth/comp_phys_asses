import unittest
import floating_point_test as fpt
import numpy as np

class test(unittest.TestCase):
    def test_machine_acc_test(self):
        self.assertEqual(fpt.machine_acc_test(np.float16(1),np.float16(0)),None)
        self.assertEqual(fpt.machine_acc_test(np.float16(1),np.float16(1)),1)
        self.assertEqual(fpt.machine_acc_test(np.float16(1),np.float16(2**-4)),2**-4)
        self.assertEqual(fpt.machine_acc_test(np.float32(1),np.float32(2**-4)),2**-4)
        self.assertEqual(fpt.machine_acc_test(np.float64(1),np.float64(2**-4)),2**-4)
        self.assertRaises(Exception,fpt.machine_acc_test,np.float16(1.0),np.float32(0.5))
        
  
        
if __name__ == '__main__': #if running as main then run test scripts
    unittest.main()
















