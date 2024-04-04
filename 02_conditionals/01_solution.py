age = input("Enter your age:")
# print(type(age))
age_in_int = int(age)
if age_in_int < 13:
    print("Your age group is Chaild")
elif age_in_int < 20:
    print("Your age group is Teenager")    
elif age_in_int < 60:
    print("Your age group is Adult")
else:
    print("Your age group is Senior")
