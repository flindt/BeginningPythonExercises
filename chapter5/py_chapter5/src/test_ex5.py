'''
Created on Nov 16, 2011

@author: ubuntu
'''
import unittest
import ex_5


class Test(unittest.TestCase):


    def testEx51_correct_input(self):
        self.assertEqual(1, ex_5.do_plus(0,1), "do_plus returned wrong result")



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testEx51_correct_input']
    unittest.main()