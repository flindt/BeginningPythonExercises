'''
Created on Dec 14, 2011

@author: pfl
'''

import math

def brute(nMax):
    
    for i in range(2,nMax):
        prime = True
        for j in range(2,i):
            if i%j == 0:
                prime = False
                
        if prime :
            print("%i"%i)
    return

def optimised_1(nMax):
    
    print("2")
    for i in range(3,nMax,2):
        prime = True
        for j in range(2,int( math.sqrt(i) )):
            if i%j == 0:
                prime = False
                
        if prime :
            print("%i"%i)
    return

optimised_1(100000)