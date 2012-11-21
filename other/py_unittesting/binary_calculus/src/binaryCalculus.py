
def add(a, b):
    if len(a) > len(b): # make sure la is the longest
        la = a
        lb = b
    else:
        la = b
        lb = a
        
    for index in range( len(la) ):
        lb = "0" +lb
    
    result = ""
    
    carry=0
    for index in range( len(la)):
        sum = 0
        if la[-1]=="1":
            sum = sum + 1
        if lb[-1]=="1":
            sum = sum + 1
        if carry == 1:
            sum = sum + 1
            
        if sum == 0:
            result = "0" + result
            carry = 0
        elif sum == 1:
            result = "1" + result
            carry = 0
        elif sum == 2:
            result = "0" + result
            carry = 1
        else:
            result = "1" + result
            carry = 1
        
        la = la[:-1]
        lb = lb[:-1]
            
    
    if carry == 1:
        result = "1" + result
    
    return result
    


