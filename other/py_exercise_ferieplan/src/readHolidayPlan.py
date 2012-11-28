'''
Created on Nov 27, 2012

@author: flindt
'''


myFile = open("ferieplan2013 14.txt", encoding="utf-8")

for thisLine in myFile.readlines():
    print( thisLine )
    
    