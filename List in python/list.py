# tea_varity = ["black" , "green" , "normal"]
# # print(tea_varity)
# print(tea_varity[0])
# print(tea_varity[1])
# print(tea_varity[2])
# print(tea_varity[:2])
# print(tea_varity[:2][0][0]) # black - b

# tea_varity[2] = "Herbal"
# print(tea_varity)


# tea_varity = ["black" , "green" , "normal"]
# print(tea_varity)

# tea_varity[1] = "Lemon"
# # print(tea_varity)
# tea_varity[:] = ["white" , "honey" , "milk"]
# print(tea_varity)

# print(tea_varity[1:1]) []

# tea_varity[1:1] = ["test" , "test"]

# print(tea_varity) #['white', 'test', 'test', 'honey', 'milk']


# print(tea_varity[1:3]) #['test', 'test']

# tea_varity[1:3] = [] # nothing

# print(tea_varity) #['white', 'honey', 'milk']

# for tea in tea_varity:
#     # print(tea)
#     print(tea, end="-")
    




# # append in the last
# tea_varity.append("Oolong")
# print(tea_varity)



# if "Oolong" in tea_varity:
#     print("I've this tea")
    
    
# print(tea_varity.pop()) #Oolong

# print(tea_varity.remove("milk")) #None- doesn't return back anything
# print(tea_varity) #['white', 'honey', 'Oolong']

# tea_varity.insert(1,'green')

# print(tea_varity)


# list comprehention
# squared_num = [x**2 for x in range(10)]

# print(squared_num) #[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]







p ,q , r = int(input("enter the number : "))
print(p,q,r)