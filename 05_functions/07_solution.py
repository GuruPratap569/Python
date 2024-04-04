def sum_all(*args):      # (*agrs) more than one argument accept krta hai , where "args" ek variable hai, '*' is imp.
    return sum(args)      #here "sum" is a keyword.

print(sum_all(1, 2, 3))
# print(sum_all(1, 2, 3, 4, 5))
# print(sum_all(1, 2, 3, 4, 5, 6, 7, 8, 9))


#------------------------------


def sum_al(*arg):
    # print(*arg)
    # print(arg)
    for i in arg:
       square = i**2
       print(square)

sum_al(11, 22, 33)