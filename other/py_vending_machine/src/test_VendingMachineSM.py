'''
Created on Dec 13, 2012

@author: flindt
'''
import unittest

import VendingMachine as VM
from VendingMachine import CANCELBUTTON

class Test(unittest.TestCase):

    def test_VM_reqA1(self):
        myVM = VM.VendingSM()
        
        myVM.inputEvent( VM.COIN_1 )
        self.assertEqual(1, myVM.getCredit(), "Amount of credit is wrong")
        
        myVM.inputEvent( VM.COIN_2 )
        self.assertEqual(3, myVM.getCredit(), "Amount of credit is wrong")
        
        myVM.inputEvent( VM.COIN_5 )
        self.assertEqual(8, myVM.getCredit(), "Amount of credit is wrong")
        
        myVM.inputEvent( VM.COIN_10 )
        self.assertEqual(18, myVM.getCredit(), "Amount of credit is wrong")
        
        myVM.inputEvent( VM.COIN_20 )
        self.assertEqual(38, myVM.getCredit(), "Amount of credit is wrong")
        
        
    def test_VM_reqA3(self):
        myVM = VM.VendingSM()
        
        myVM.inputEvent( VM.PRODUCTSELECT, VM.COLA)
        self.assertEqual(VM.SALE, myVM.getState(), "VM did not get into correct state")
        
    def test_VM_cancelButton(self):
        myVM = VM.VendingSM()
        
        myVM.inputEvent( VM.COIN_1 )
        self.assertEqual(1, myVM.getCredit(), "Amount of credit is wrong")
        
        myVM.inputEvent( CANCELBUTTON )
        self.assertEqual(0, myVM.getCredit(), "Amount of credit is wrong")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()