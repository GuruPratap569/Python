# n = int(input("Enter a number:"))

# for i in range(1, 11):
#     if i != 5:
#         mult = i*n
#         print(n ,'x', i ,'=', mult)
    
#--------------OR-----------------------

n = int(input("Enter a number:"))

for i in range(1, 11):
    if i == 5:
        continue
    print(n ,'x', i ,'=', n*i)
