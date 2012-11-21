'''
Created on Nov 21, 2012

@author: flindt
'''
import unittest

import binaryCalculus

class Test(unittest.TestCase):


    def testbinayaddition(self):
        self.assertEqual("101", binaryCalculus.add("100","1"), "Add returned wrong result")
        self.assertEqual("1011", binaryCalculus.add("100","111"), "Add returned wrong result")
        
        self.assertEqual("1110", binaryCalculus.add("111","111"), "Add returned wrong result")
        
        self.assertEqual("111111111", binaryCalculus.add("111000101","111010"), "Add returned wrong result")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testbinayaddition']
    unittest.main()