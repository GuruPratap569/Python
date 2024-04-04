def multiply(num1, num2):
    return num1 * num2

num1 = input("Enter 1st num:")
num2 = input("Enter 2nd num:")

if num1.isnumeric() and num2.isnumeric():
    p1 = float(num1)
    p2 = float(num2)
    res = multiply(p1, p2)
    print(res)
elif num1.isnumeric():
    p1 = int(num1)
    p2 = (num2)
    res = multiply(p1, p2)
    print(res)
elif num2.isnumeric():
    p1 = (num1)
    p2 = int(num2)
    res = multiply(p1, p2)
    print(res)
else:
    print("Enter atleast one input as a Number.")
