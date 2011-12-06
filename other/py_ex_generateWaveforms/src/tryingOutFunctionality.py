'''
Created on Dec 6, 2011

In this file, I will be testing things before writing the actual functions

@author: pfl
'''


def createAFileWithAFewLines():
    myFile = open("aTestFile.dat","w")
    myFile.write("0\t0")
    myFile.write("1\t0")
    myFile.write("2\t0")
    myFile.write("3\t0")
    
    myFile.close()
    
createAFileWithAFewLines()


def simpleYield():
    yield 0
    yield 7
    yield 0
    yield 8
    yield 0
    for t in range(0, 50, 5):
        yield t
    
    
for x in simpleYield():
    print( x )
    