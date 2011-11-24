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

print( "----------------- ex 4.1 done -------------------------------------------------------------------------")

# ex 4.3
lookFor = "milk"
lookIn = ["butter","milk", "cheese"]

if lookFor == lookIn[0]:
    print("found it")
elif lookFor == lookIn[1]:
    print("found it ...")
else:
    print("did not find it")

print( "----------------- ex 4.3 done -------------------------------------------------------------------------")

#ex 4.4
fridge = { "Milk":"Thise minimælk", "Cheese":"Emmentaler", "Butter":"Unsalted butter"}

food_sought = "Butter"

for foodKey in fridge:
    print("\nlooking at : %s", foodKey)
    if foodKey == food_sought:
        print("key: %s \tValue: %s"%(foodKey, fridge[food_sought] ))
        break
else:
    print("it was not there")
    
print( "------------------ ex 4.4 done -------------------------------------------------------------------------")