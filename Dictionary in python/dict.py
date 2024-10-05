chai_type = {'masala' : 'spicy' , "ginger" : "zesty" , "green" : "mild"}
# print(chai_type)

# print(chai_type["masala"])

# print(chai_type.get("gingery")) # None

chai_type['green'] = "fresh"
# print(chai_type)

# for chai in chai_type:
#     print(chai) #keys
    
# for chai in chai_type:
#     print(chai , chai_type[chai]) # keys and values
    
    
    
    
    
    
# for key, value in chai_type.items():
    # print(key,value)
# output:--------
# masala spicy
# ginger zesty
# green fresh



# if "masala" in chai_type:
#     print("Yes")
    
# print(len(chai_type))



# chai_type.pop("ginger")
# print(chai_type)

# lastly add item will be deducted always, here nothing is added
# chai_type.popitem()
# print(chai_type)





# del keyword delete the reference of memory permenently

# del chai_type["green"]
# print(chai_type)
# output - >>
# {'masala': 'spicy'}

tea_shop = {
    "chai" : {"white" : "spicy" , "ginger" : "faltu"},
    "tea" : {"black" : "fresh" , "black" : "strong"}
}


# print(tea_shop)

# print(tea_shop['chai'])

# print(tea_shop['chai']["ginger"])



# //////////////


# square_num = {x:x**2 for x in range(6)}

# print(square_num)
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# square_num.clear()
# print(square_num) #{}
# all the value is cleared





# creating a dictionary
keys = ["masala" , "ginger" , "lemon"]
# print(keys)
default_value = "delicious"
dict1 = dict.fromkeys(keys, default_value)
print(dict1)

dict2 = dict.fromkeys(keys, keys)
print(dict2)