# under = input("GIve me a score value: ")
# print(under)

# print(under / 2) 
#TypeError: unsupported operand type(s) for /: 'str' and 'int'
# we have convert it into interger
# under1 = int(under)

# print(under1 / 2) #100.0











#Age Group Categorization
# Classified a person's age group child(<13),Teenager(13-19),Senior(60+)

age = int(input("enter the number"))

if(age<=13):print("Child")
elif(age <= 20): print("Teenager")
elif(age <= 60):print("Adult")
else:
    print("senior")