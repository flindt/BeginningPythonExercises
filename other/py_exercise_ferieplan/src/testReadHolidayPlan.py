'''
Created on Nov 29, 2012

@author: flindt
'''
import unittest

import readHolidayPlan

testfile1Output = [{'StartDate': 'lørdag 30. juni 2012', 'EndDate': 'søndag 12. august 2012', 'Description': 'Sommerferie\n'}, \
                   {'StartDate': 'lørdag 13. oktober 2012', 'EndDate': 'søndag 21. oktober 2012', 'Description': 'Efterårsferie\n'}, \
                   {'StartDate': 'fredag 21. december 2012', 'EndDate': 'onsdag 2. januar 2013', 'Description': 'Juleferie\n'}, \
                   {'StartDate': 'lørdag 16. februar 2013', 'EndDate': 'søndag 24. februar 2013', 'Description': 'Vinterferie\n'}, \
                   {'StartDate': 'lørdag 23. marts 2013', 'EndDate': 'mandag 1. april 2013', 'Description': 'Påskeferie\n'}]

testfile2Output = [{'StartDate': 'lørdag 30. juni 2012', 'EndDate': 'søndag 12. august 2012', 'Description': 'Sommerferie\n'}, \
                   {'StartDate': 'lørdag 13. oktober 2012', 'EndDate': 'søndag 21. oktober 2012', 'Description': 'Efterårsferie\n'}, \
                   {'StartDate': 'fredag 21. december 2012', 'EndDate': 'onsdag 2. januar 2013', 'Description': 'Juleferie\n'}, \
                   {'StartDate': 'lørdag 16. februar 2013', 'EndDate': 'søndag 24. februar 2013', 'Description': 'Vinterferie\n'}, \
                   {'StartDate': 'lørdag 23. marts 2013', 'EndDate': 'mandag 1. april 2013', 'Description': 'Påskeferie\n'}, \
                   {'StartDate': 'lørdag 23. marts 2013', 'EndDate': 'lørdag 23. marts 2013', 'Description': 'Påskeferie\n'}]


class Test(unittest.TestCase):
    def test_ReadHolidaysFromTxt_simpleInput(self):
        self.assertEqual(testfile1Output, readHolidayPlan.getHolidaysFromTxt("testfile1.txt"), \
                         "ReadHolidaysFromTxt() did not return the correct list from testfile1.txt" )
        pass

    def test_ReadHolidaysFromTxt_RealInput(self):
        print(  readHolidayPlan.getHolidaysFromTxt("ferieplan2013 14.txt"))
        pass
    
    def test_ReadHolidaysFromTxt_simpleInput2(self):
        self.assertEqual(testfile2Output, readHolidayPlan.getHolidaysFromTxt("testfile2.txt"), \
                         "ReadHolidaysFromTxt() did not return the correct list from testfile2.txt" )
     

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_ReadHolidaysFromTxt']
    unittest.main()