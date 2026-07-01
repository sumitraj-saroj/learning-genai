from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the functions runs")
        func()
        print("After functions runs")

    return wrapper


@my_decorator
def greet():
    print("Hello from my_decorators class")


greet()
print(greet.__name__)
