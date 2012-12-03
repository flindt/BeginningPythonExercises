'''
Created on Oct 31, 2012

@author: flindt
'''


# This is a one line comment...


def DoesStoreHaveBread():
    return True


# A function is easily defined like this:
def buyBread():
    if DoesStoreHaveBread():
        print("Buying bread :)")
        return "Bread"
    else:
        return None



Food = ["Butter"]

if "Bread" in Food:
    pass
else:
    Food.append( buyBread() )



def DoesStoreHaveButter():
    return True


def buyButter():
    if DoesStoreHaveButter():
        print("Buying bread :)")
        return "Bread"
    else:
        return None


if "Butter" in Food:
    pass
else:
    buyButter()


print( Food )






