username = "chaiaurcode"


def func():
    # username = "chai"
    print(username)

print(username)
func()


#--------------------------------

x = 99
def func2(y):
    z= x+y
    return z

result = func2(6)
print(result)

#-----------------------------

def func3():
    global x   #global x ki value le kr aata h.
    x = 13     # x ki value (99) ko overwrite kr diya gya h, now x=13.(avoid it, not good practice)

func3()
print(x)

#----------------------------------

def f1():
    x = 88
    def f2():
        print(x)
        # y = 125
    f2()
    # print(y)         #we can'nt access chidren's value (y).
f1()

#--------------------------------------

#   <<--- Closures --->>

def func4():
    x= 100
    def func5():
        print(x)

    return func5

myResult = func4()
myResult()

#----------------------

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual


f = chaicoder(2)
g = chaicoder(3)

print(f(4))
print(g(4))