'''
Created on Nov 9, 2012

@author: flindt
'''







Food = ["Bread"]
storeInventory = ["Bread","Butter","Jam"]

def BuyBread():
    if "Bread" in storeInventory:
        return "Bread"
    return None
    

def BuyButter():
    if "Butter" in storeInventory:
        return "Butter"
    return None


def BuyJam():
    if "Jam" in storeInventory:
        return "Jam"
    return None


def BuyCake():
    pass


def MAS():
    Food.append( BuyBread() )
    Food.append( BuyButter() )
    Food.append( BuyJam() )
    Food.append( BuyCake() )
    
    print( "We have this food : ",Food)


MAS()




