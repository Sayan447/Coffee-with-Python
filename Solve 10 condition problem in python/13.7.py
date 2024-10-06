#Password Strength Checker
# Problem : check if a password is "weak" , "medium", or "strong" . Criteria:<6 chars(Weak),6-10 chars(medium), >10 chars(Strong).

password = input("")

if len(password) < 6:
    print("Weak")
elif len(password) <= 10:
    print("medium")
else: print("Strong")