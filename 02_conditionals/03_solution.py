# score = int(input("Enter marks of students : "))

# if score >= 90 :
#     print("Student's Grade is: A")
# elif score >= 80 :
#     print("Student's Grade is: B")
# elif score >= 70 :
#     print("Student's Grade is: C")
# elif score >= 60 :
#     print("Student's Grade is: D")
# else:
#     print("Student's Grade is: F")

#-----------------------------------------------

# score = int(input("Enter marks of students : "))  
 
# if score >= 90:
#     if score <= 100:
#         print("Grade is A")
#     else:
#         print("Enter a valid Marks")
# elif score >= 80:
#     print("Grade is B")
# elif score >= 70:
#     print("Grade is C")
# elif score >= 60:
#     print("Grade is D")
# else: print("Grade is F")

#---------------------OR-------------------

# score = int(input("Enter your Marks:"))

# if score >=101:
#     print("Please verify your grade again")
#     # exit()

# if score >= 90:
#     grade = "A"
# elif score >=80:
#     grade = "B"
# elif score >=80:
#     grade = "C"
# elif score >=80:
#     grade = "D"
# else:
#     grade = "F"

# print("Your Grade is :",grade)

#--------------OR----------------------

score = int(input("Enter your Marks:"))

if score >=101 or score < 0:
    print("Please verify your Marks again")
else:
    if score >= 90:
        grade = "A"
    elif score >=80:
        grade = "B"
    elif score >=80:
        grade = "C"
    elif score >=80:
        grade = "D"
    else:
        grade = "F"

    print("Your Grade is :",grade)