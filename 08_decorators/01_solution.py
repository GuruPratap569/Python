import time

def timer(func):                    #timer is a Decorator function that takes another function func as an argument and returns a new function wrapper that adds functionality before and after calling func.
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} run in {end-start} sec time")
        return result
    return wrapper

@timer                    #this is "Decorator name. ise lagane ke baad ab function ,timer function se pass hokar hi jayega.
def example_function(n):        #example_function is the decorated function. It is decorated using @timer, which means that when example_function is called, it will actually call the wrapper function created by timer.
    time.sleep(n)

example_function(2)  # 2 second