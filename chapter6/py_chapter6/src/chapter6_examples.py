'''
Created on Nov 21, 2011

This file shows some examples of how to use the classes presented in this chapter.

@author: flindt
'''

# import the classes 
from Ch6_classes import Omelet,Fridge


# making an Omelet
# Or in python speak: Instatiating an object of the class "Omelet"
o1 = Omelet()
print( o1 )
print( o1.get_kind() )

# one more
o2 = Omelet()
print( o2 )
print( o2.get_kind() )

# we need a fridge to get ingredients from
f1 = Fridge()
print( f1 )

# try to get ingredients from fridge 
o1.get_ingredients(f1)

# try to make the omelet
# this wont work since the fridge is empty
# o1.mix()      

# make a new fridge with food in
f2 = Fridge( {"cheese":5, "milk":4, "eggs":12})
print( f2 )

# now we can make an omelet
o1.get_ingredients(f2)
o1.mix()
o1.make()
print( o1 )
print( o1.cooked )


