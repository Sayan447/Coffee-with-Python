# List Uniqueness Checker
# check if all element in a list are unique. if a duplicate is found, exit the loop and print the duplpicate

# items = ["apple" , "banana" , "orange" , "apple" , "mango"]

items = ["apple" , "banana" , "orange" , "apple" , "mango"]

unique_item = set()

for item in items:
    if item in unique_item:
        print("Duplicate" , item)
        break
    else:
        unique_item.add(item)
        # append is used for a list and add() is used for a set