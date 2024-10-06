#Coffee Customization
#problem: Customer a coffee order:"small" , "medium" , or "Large" with an option for "Extra shot" of espresso


order_size = "medium"
extra_shot = True


if extra_shot:
    coffee = order_size + "coffee with extrashot"
    
else:
    coffee = order_size + "coffee"
    
print("order", coffee)