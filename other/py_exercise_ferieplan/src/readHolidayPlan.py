# -*- coding: utf-8 -*-
'''
Created on Nov 27, 2012

@author: flindt
'''

def getHolidaysFromTxt( fileName ):
    myFile = open( fileName, encoding="utf-8")
    
    myFile.readline()
    myFile.readline()
    
    listOfHolidays = []
    while True:
        Description = myFile.readline()
        #print( Description )
        
        if Description == '':
            break
    
        
        DateLine = myFile.readline()
        #print(DateLine)
        
        DateParts = DateLine.split( "-" )
        #print( DateParts )
        
        StartDate = DateParts[0]
        StartDate = StartDate.strip().strip(")(")
        #print( StartDate )
        
        
        if len( DateParts ) == 2:
            EndDate = DateParts[1]
            EndDate = EndDate.strip().strip(")(")
        else:
            EndDate = StartDate
        #print( EndDate )
        
        thisHoliday = { "Description":Description, "StartDate":StartDate,"EndDate":EndDate}
        #print (thisHoliday)
        listOfHolidays.append( thisHoliday )
        
    return listOfHolidays 


    
    
def splitAtDates(inputString):
    weekdays = ("torsdag", "søndag")
    
    maxIndex = -1
    
    for thisday in weekdays:
        findIndex = inputString.find( thisday )
        if findIndex > maxIndex:
            maxIndex = findIndex
    
    lastDate = inputString[maxIndex:]
            
    inputString = inputString[:maxIndex]
    
    maxIndex = -1
    
    for thisday in weekdays:
        findIndex = inputString.find( thisday )
        if findIndex > maxIndex:
            maxIndex = findIndex
            
    firstDate = inputString[maxIndex:]
            
    inputString = inputString[:maxIndex]

    return [inputString, firstDate, lastDate]
