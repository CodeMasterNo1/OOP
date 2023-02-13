import insect_class as I 

mosquito = I.insect("mosquito",2,4)
housefly = I.insect("housefly",2,4)

mosquito.get_fly()
housefly.get_fly()


print (f"the {mosquito.get_name()} can fly to {mosquito.get_fly()} miles")

print (f"the {housefly.get_name()} can fly to {housefly.get_fly()} miles")