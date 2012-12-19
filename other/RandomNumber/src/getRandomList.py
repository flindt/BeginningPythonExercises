'''
Created on Sep 20, 2012

@author: flindt
'''

import random

maxNumber = input(" Enter maximum number : ")

print(" The maximum number is : %i"%int(maxNumber))

myListOfNumbers = []
for i in range(int(maxNumber)):
    myListOfNumbers.append(i)
    
while myListOfNumbers:
    input(" Press enter for a number...")
    print( "%i"%(myListOfNumbers.pop(random.randint(0,len(myListOfNumbers)-1))+1))