distance = int(input("Enter distance of travell:"))

if distance <=3 :
    mode = "Walk"
elif distance >=3 and distance <= 15 :
    mode = "Bike"
else:mode = "Car"

print("Mode of transportation is :",mode)