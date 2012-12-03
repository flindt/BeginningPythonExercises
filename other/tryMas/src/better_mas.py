'''
Created on Nov 8, 2012

@author: flindt
'''


def makeSandWich(sandwichParts):    
    if ("Bread" in sandwichParts) and \
    ("Butter" in sandwichParts) and\
    ("Jam" in sandwichParts):
        return "Delicious Sandwich"
    else:
        return "Unable to make sandwich"


def GoBuyFood(missingFood):
    return ["Bread", "Butter", "Jam"]


def CheckFood(availableFood):
    missingFood = []
    for ingredient in ["Bread", "Butter", "Jam"]:
        if ingredient not in availableFood:
            missingFood.append(ingredient)
    return missingFood


def MAS(availableFood):
    missingFood = CheckFood(availableFood)
    print("We do not have:", missingFood)
    foodBought = GoBuyFood(missingFood)
    print("We have bought:", foodBought)
    print(makeSandWich(availableFood + foodBought))
    
    
Food = ["Butter"]
MAS(Food)






