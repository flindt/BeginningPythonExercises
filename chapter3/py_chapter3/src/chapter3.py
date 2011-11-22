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

# ex 3.7
print( " 6 cartons of milk will set you back : %i gold coins"%(milk_carton["cost"]*6))

# ex 3.8
cheese_list = ["cheese1", "cheese2"]
dairy_section.extend(cheese_list)
print( dairy_section )

index = 0
cheese_indexes=[]
for product in dairy_section:
    if "cheese" in product:
        print( "cheese found at index %i : %s"%(index,product))
        cheese_indexes.append(index)
    index = index + 1

cheese_indexes.sort(reverse=True)
print( cheese_indexes )

new_cheese_list = []
for index in cheese_indexes:
    new_cheese_list.append(dairy_section.pop(index))
    
print( dairy_section )

# ex 3.9
print ( len(new_cheese_list) )

# ex 3.10
print( new_cheese_list[0][:6])
