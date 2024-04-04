year= int(input("Enter year:"))

# if year<400:
#     if year%4==0 and year%100!=0:
#         print("leap year")
#     else:
#         print("Not leap year")
# else:
#     if year%400==0 and year%100==0 and year%4==0:
#         print("leap year")
#     elif year%4==0 or year%400==0:
#         print("leap year")
#     else:
#         print("Not leap year")

#----------OR---------------

if (year%400==0) or (year%4==0 and year%100 != 0):
    print(year,"is leap year")
else:
    print(year,"is Not leap year")