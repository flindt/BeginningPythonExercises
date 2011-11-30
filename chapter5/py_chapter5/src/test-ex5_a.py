'''
Created on Nov 16, 2011

@author: ubuntu
'''
import unittest

import ex_5

class Test(unittest.TestCase):


    def testEx5_1_correct(self):
        self.assertEqual(ex_5.do_plus(1,1), 2, "do_plus returned something wrong")
        self.assertEqual(ex_5.do_plus(-6,5), -1, "do_plus returned something wrong")
        self.assertEqual(ex_5.do_plus(1,1), 2, "do_plus returned something wrong")
        self.assertEqual(ex_5.do_plus(1,1), 2, "do_plus returned something wrong")  
        pass
    
    
    def testEx5_1_wrong_type(self):
        self.assertRaises(TypeError, ex_5.do_plus, (None, 2))
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEx5_1_correct']
    unittest.main()