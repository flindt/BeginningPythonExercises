'''
Created on Dec 6, 2011

In this file, I will be testing things before writing the actual functions

@author: pfl
'''

import os

def createAFileWithAFewLines():
    myFile = open("aTestFile.dat","w")
    myFile.write("0\t0")
    myFile.write("1\t0")
    myFile.write("2\t0")
    myFile.write("3\t0")
    
    myFile.close()
    
createAFileWithAFewLines()