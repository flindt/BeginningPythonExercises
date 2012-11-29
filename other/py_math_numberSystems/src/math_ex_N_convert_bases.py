'''
Created on Nov 29, 2012

@author: flindt
'''

    

print("Hello binary world ")
var = 1
while var == 1:
    mode = int(str(input("For hex type 1, for bin type 2, Dec to Hex Bin Oct type 3 Prog-exit type 4, here:>") ))
    print("")
    if mode == 1:
        n = str(input('Input a Hex nr here:>') )
        a = int(n, 16)
        print("Hex to Decimal =:",n, "=",a)
    if mode == 2:
        n = str(input('Input a Binary nr here:>') )
        b = int(n, 2)
        print("Bin to Decimal =:",n, "=",b)
    if mode == 3:
        y = int( str(input('Type a decimal number:') ))
        b = bin(y)
        x = hex(y)
        o = oct(y)
        print("Decimal=",y, "Bin=",b, "Hex=",x, "Octal=",o)
    if mode == 4:
        var = 0
        print("Program Exit")
