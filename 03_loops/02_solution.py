# n = int(input("Enter a number:"))
# num = []
# sum = 0
# for i in range(1, n+1):    # i=1 
#     if i%2==0:
#         num.append(i)
# print("Even Number is:",num)

# for a in num:
#     sum += a
# print("Sum of even Number is:",sum)

#-------------OR------------------------

n = int(input("Enter a number:"))
sum_even = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum_even += i

print("Sum of even number is:",sum_even)