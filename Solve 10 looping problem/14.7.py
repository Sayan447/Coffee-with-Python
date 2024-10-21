# validate input
# Keep asking the user for input until they enter a number btw 1 and 10

while True:
    number = int(input("enter the value btw 1 and 10: "))
    if 1<= number and number <= 10:
        print("thanks")
        break
    else:
        print("Invalid numer, try again")
        