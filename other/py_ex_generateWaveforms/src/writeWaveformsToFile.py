'''
Created on Dec 6, 2011

@author: pfl
'''


def Zero(t):
    return 0

def writeFunctionToFile(timeStart, timeEnd, frequency, function):
    outputFile = open("output.dat","w")
    
    t = timeStart
    timeStep = 1 / frequency
    while t < timeEnd:
        print ( t )
        outputFile.write("%f \t%f\n"%(t,function(t)))
        t = t + timeStep
        
    outputFile.close()
    


if __name__ == '__main__':
    writeFunctionToFile(0, 10, 8 ,Zero)