'''
Created on Nov 27, 2012

@author: flindt
'''


myFile = open("ferieplan2013 14.txt", encoding="utf-8")


while True:
    Description = myFile.readline()
    print( Description )
    
    if Description == '':
        break
    
    DateLine = myFile.readline()
    print(DateLine)
    
    DateParts = DateLine.split( "-" )
    print( DateParts )
    
    StartDate = DateParts[0]
    StartDate = StartDate.strip().strip(")(")
    print( StartDate )
    