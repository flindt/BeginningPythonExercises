'''
Created on Nov 17, 2011

@author: ubuntu
'''


# ex 4.1 and  
def printTrueFalse( X ):
    if X:
        print("%s is true"%str(X))
    else:
        print("%s is false"%str(X))
        
printTrueFalse(0)
printTrueFalse(1)
printTrueFalse(2)
printTrueFalse(3)
printTrueFalse("abc")

printTrueFalse("")


print( "----------------- ex 4.1 done -------------------------------------------------------------------------")

# ex 4.2
def inRange(X):
    if X in range(3,9):
        print( " %s is in the range"%str(X))

inRange(5)

# ex 4.3
lookFor = "milk"
lookIn = ["butter","milk", "cheese"]

if lookFor == lookIn[0]:
    print("found it")
elif lookFor == lookIn[1]:
    print("found it ...")
else:
    print("did not find it")
    
if lookFor in lookIn:
    print(" its there ")
else:
    print("its not there")
print(lookIn.index(lookFor) )

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

# ex 4.5
fridge_list = []
for foodKey in fridge:
    fridge_list.append(foodKey)
print( fridge_list )    

while fridge_list:
    if fridge_list.pop()==food_sought :
        print( "found it again ")
        break
else:
    print("not found")





















