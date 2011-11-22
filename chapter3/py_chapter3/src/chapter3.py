'''
Created on Nov 22, 2011

@author: ubuntu
'''


dairy_section = ["milk","cream","cheese","butter"]

print( "%s %s"%(dairy_section[0],dairy_section[-1]))

# ex 3.3
milk_expiration = (11,31,2011)

# ex 3.4
print( "The milk will expire on : %i / %i / %i"%milk_expiration)

# ex 3.5 
milk_carton = { "expiration_date" : milk_expiration, "size":5, "cost":22.5, "brand":"Thise"}

# ex 3.6
print( " This is %i oz of %s milk. It will expire on : %i / %i / %i"%( milk_carton["size"],\
                                                                       milk_carton["brand"],\
                                                                       milk_carton["expiration_date"][0],\
                                                                       milk_carton["expiration_date"][1],\
                                                                       milk_carton["expiration_date"][2]
                                                                       ))



