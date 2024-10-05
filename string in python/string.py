 
chai = "masala chai"
# f = chai[0]
# print(f)

# slice_chai = chai[0 : 6]
# print(slice_chai)


# print(chai[-1])
num_list = "0123456789"
# print(num_list[:])
# print(num_list[3:])
# print(num_list[:7])
# print(num_list[0:7:2])

print(chai.lower())
print(chai.upper())

# string is immutable



coffee = "  Mocha tea lathe  "
# print(coffee) #   Mocha tea lathe  
# print(coffee.strip())
# no space 

# replace command
# print(chai.replace("masala" , "lemon" ))


# string converted to list
x = "Lemon, ginger, masala, mint"
# print(x.split(", "))
# by the basis of , and space



# find the position of any word and letter
# if anything not found return -1
print(chai.find("i")) # 10



# count the word
# chai = "masala chai chai chia chai"
# print(chai.count("chai")) # 3




# {} -- placeholder we can add some variables
  
  
# chia_type = "Masala"
# quantity = 3
# order = "I ordered {} cups of {} chai"
# print(order.format(quantity , chia_type)) #I ordered 3 cups of Masala chai




# list to string
# variety = ["lemon" , "masala" , "ginger"]
# print(", ".join(variety))
# lemon, masala, ginger

# print(len(chai)) # 11



# cold = "He said, \"masala chai is awesome\""
# print(cold)
# He said, "masala chai is awesome"



print("masala" in chai) #True
print("masalaa" in chai) #False
