
# decorators are a powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. 
# Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

class Decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("Before the function call")
        result = self.func(*args, **kwargs)
        print("After the function call")
        return result
    
    
@Decorator
def say_hello(name):
    print(f"Hello, {name}!")    
say_hello("Puneet")
