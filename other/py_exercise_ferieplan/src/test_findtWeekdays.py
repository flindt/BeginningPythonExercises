'''
Created on Nov 29, 2012

@author: flindt
'''
import unittest

import readHolidayPlan

testInputA = "Kr. Himmelfartsferie torsdag 9. maj 2013 - søndag 12. maj 2013"
testOutputA = ["Kr. Himmelfartsferie", "torsdag 9. maj 2013", "søndag 12. maj 2013"]

testInputB = "torsdag 9. maj 2013 - søndag 12. maj 2013"
testOutputB = ["", "torsdag 9. maj 2013", "søndag 12. maj 2013"]

testInputC = "ferie"
testOutputC = ["ferie"]



class Test(unittest.TestCase):


    def test_findweekDaysinLineA(self):
        self.assertEqual(testOutputA, readHolidayPlan.splitAtDates( testInputA ), "splitAtDates() failed")
        pass
    
    def test_findweekDaysinLineB(self):
        self.assertEqual(testOutputB, readHolidayPlan.splitAtDates( testInputB ), "splitAtDates() failed")
        pass
    
    def test_findweekDaysinLineNoDates(self):
        self.assertEqual(testOutputC, readHolidayPlan.splitAtDates( testInputC ), "splitAtDates() failed")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()