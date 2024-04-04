password = input("Enter password : ")
pass_len = len(password)
# print(pass_len)

if pass_len < 6:
    status = "Weak"
elif pass_len <= 10:
    status = "Medium"
else:
    status = "Strong"

print("Your entered password strength is",status)