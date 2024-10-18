# Q:- Sum of Even numbers
# Calculate the sum of even numbers up to a given number n.

num = int(input("Enter the number: "))
sum = 0
for i in range(1, num + 1):
    print(i)
    if (i % 2 == 0):
        sum = sum + i
print("sum of even number " , sum) 