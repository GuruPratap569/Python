import time

def cache(func):
    chache_vaule = {}
    print(chache_vaule)
    def wrapper(*args):
        if args in chache_vaule:
            return chache_vaule[args]
        result = func(*args)
        chache_vaule[args] = result
        return result
    return wrapper



@cache
def long_running_function(a, b):
    time.sleep(3)   # 3 second
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))

print(long_running_function(57, 3))
