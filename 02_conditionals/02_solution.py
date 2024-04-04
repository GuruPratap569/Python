age = int(input("Enter your age:"))
price = 12 if age >=18 else 8
day = "Wednesday"

if day == "Wednesday":
    # price = price - 2
    price -= 2
    print("Price of movie ticket for you:",price)

else:
    print("Price of movie ticket for you:",price)