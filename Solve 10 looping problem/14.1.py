# Q:- Counting Positive Number
# Given a list of numbers, count how many are positive
# number = [1 , -2 , 3 , -4 , 5 , 6 , -7 , -8, 9 , 10]


numbers = [1 , -2 , 3 , -4 , 5 , 6 , -7 , -8, 9 , 10]

positive_num_count = 0

for num in numbers:
    print(num,end=" ")
    if(num > 0):
        positive_num_count += 1
print("final count of positive number is " , positive_num_count)
        