#movie ticket Pricing
#problem:- Movie ticket are priced based on age:$12 for adult(18 and over),$8 for child. everyone gets a $2 discount on wednesday


age = 26
day = 'Wednesday'

price = 12 if age >= 18 else 8
# means price have to be 12 whenever age is graterthan 18 otherwise price should be the 8
# print(price)
if day == "Wednesday":
    price = price - 2
print(f"the ticket price is ${price}")