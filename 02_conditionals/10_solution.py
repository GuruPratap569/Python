pet=input("Enter your pet name(Dog/Cat):").lower()
age =int(input("Enter your pet age:"))

if pet=="dog":
    if age<2:
        food = 'Puppy food'
    else:
        food ='Adult food'


elif pet=="cat":
    if age>5:
        food = 'Senior food'
    else:
        food='Junior food'


print("Recommended food is:",food)