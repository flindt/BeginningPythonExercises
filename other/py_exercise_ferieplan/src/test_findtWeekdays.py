'''
Created on Nov 29, 2012

@author: flindt
'''
import unittest

import readHolidayPlan

testInputA = "Kr. Himmelfartsferie torsdag 9. maj 2013 - søndag 12. maj 2013"
testOutput = ["Kr. Himmelfartsferie ", "torsdag 9. maj 2013 - ", "søndag 12. maj 2013"]


class Test(unittest.TestCase):


    def test_findweekDaysinLine(self):
        self.assertEqual(testOutput, readHolidayPlan.splitAtDates( testInputA ), "splitAtDates() failed")
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()