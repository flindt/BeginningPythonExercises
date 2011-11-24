'''
Created on Nov 17, 2011

@author: ubuntu
'''


# ex 4.1 and 4.2 uses this function   
def printTrueFalse( X ):
    if X:
        print("%i is true"%X)
    else:
        print("%i is false"%X)
        
printTrueFalse(0)

#ex 4.4
fridge = { "Milk":"Thise minimælk", "Cheese":"Emmentaler"}

food_sought = "Milk"

for foodKey in fridge:
    if foodKey == food_sought:
        print("key: %s"%foodKey)