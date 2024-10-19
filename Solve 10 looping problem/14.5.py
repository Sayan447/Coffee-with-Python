# find the first Non-repeated character
n = 'sayan'
count = 0
res = ""

for char in n:
    # print(n[char])
    if n.count(char) == 1:
        print("Char is " , char)
        break