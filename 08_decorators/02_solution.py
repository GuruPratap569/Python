
def debug(func):                           #Decorator
    def wrapper(*args, **kwargs):
        args_value = ' ,'.join(str(arg) for arg in args)
        kwargs_value = ' ,'.join(f"{k}={v}" for k, v in kwargs.items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        result = func(*args, **kwargs)
        return result
    return wrapper


@debug                  
def hello():            #Decorated function  
    print("hello !")


@debug
def greet(name,fa_name,mo_name, greeting,greeting3="Hello333"):
    print(f"{greeting}, {name}")
    


greet("chai","coffee","greenTea", greeting3="hanji",greeting="Hello")
hello()
