'''
Created on Dec 6, 2011

@author: pfl
'''

import math

def Zero(t):
    return 0

def Sawtooth(t):
    sawLength = 1/9    # in seconds
    sawPeak = 1
    output = (t%sawLength) * sawPeak / sawLength
    return output

def Sinus(t):
    sinFreq = 1
    return math.sin( 2 * math.pi * t / sinFreq)

def writeFunctionToFile(filename, timeStart, timeEnd, frequency, function):
    outputFile = open(filename,"w")
    
    t = timeStart
    timeStep = 1 / frequency
    while t < timeEnd:
        outputFile.write("%f \t%f\n"%(t,function(t) ))
        t = t + timeStep
        
    outputFile.close()
    


if __name__ == '__main__':
    writeFunctionToFile("sinus.dat", 0, 10, 8 ,Sinus)
    writeFunctionToFile("sawtoth.dat", 0, 10, 8 ,Sawtooth)