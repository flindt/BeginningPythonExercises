# -*- coding: utf-8 -*-
'''
Created on Nov 27, 2012

@author: flindt
'''


myFile = open("ferieplan2013 14.txt", encoding="utf-8")

myFile.readline()
myFile.readline()

listOfHolidays = []
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
    
    EndDate = DateParts[1]
    EndDate = EndDate.strip().strip(")(")
    print( EndDate )
    
    thisHoliday = { "Description":Description, "StartDate":StartDate,"EndDate":EndDate}
    print (thisHoliday)
    listOfHolidays.append( thisHoliday )
    
print( listOfHolidays )

    
    
    