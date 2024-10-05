tea_types = ("black" , "green" , "ooling")
# print(tea_types) #('black', 'green', 'ooling')

# print(tea_types[0]) #black
# print(tea_types[-1]) #ooling
# print(tea_types[1:]) #('green', 'ooling')


# tea_types[0] = "Lemon"
# print(tea_types) #'tuple' object does not support item assignment


# print(len(tea_types))
 
# more_tea = ("Herbal" , "Earl grey")
# all_tea = more_tea + tea_types
# print(all_tea) #('Herbal', 'Earl grey', 'black', 'green', 'ooling')



# if "green" in all_tea:
#     print("I have green tea")


# more_tea = ("herbal" , "Earl grey" , "herbal")
# print(more_tea.count("herbal")) #2



# black , green , Oolong are act like a variable
# (black , green , Oolong) = tea_types
# print(black)



print(type(tea_types)) #<class 'tuple'>