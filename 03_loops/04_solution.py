# str = input("Enter a string:")

# for i in range(0, len(str)):
#     num = (len(str)-1) - i
#     print(str[num],end="")

#------------OR----------------------
    
input_str = "GuruPratapGupta"
rev_str = ""

for char in input_str:
    rev_str = char + rev_str

print(rev_str)