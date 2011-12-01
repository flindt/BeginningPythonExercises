'''
Created on Nov 16, 2011

@author: pfl
'''


def do_plus( firstNumber, secondNumber):
    return firstNumber + secondNumber

def do_plus_ex(firstNumber, secondNumber):
    if type(firstNumber) != type( 1 ) or type(secondNumber) != type( 1 ):
        raise KeyError
    return firstNumber + secondNumber 


#===============================================================================
# print(do_plus_ex( "5", "6"))
# print(do_plus_ex( 5, 9))
#===============================================================================