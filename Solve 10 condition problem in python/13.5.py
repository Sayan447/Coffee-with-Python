#Transportation Mode Selection
#Problem: Choose a mode of transportation based on the distance(e,g. <3 km: walk, 3-15km:bike, >15km:Car)

distence = int(input("enter the value: "))

if distence < 3:
    transport = "Walk"
elif distence <= 15:
    transport = "Bike"
else:
    transport = "Car"
    
print("AI recommends you the transport of:" , transport)