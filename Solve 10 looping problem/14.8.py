# Prime number Checker
# check if a number is prime

number = int(input("enter the number : "))
is_prime = True


if number >  1:
    for i in range( 2 , number):
        if (number % i) == 0:
            is_prime = False
            break
    
print(number, "is a prime" , is_prime)