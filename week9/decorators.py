def decorator(func):
    def wrapper():
        print("A")
        func()
        print("B")

    return wrapper


@decorator
def greet():
    print("Hello")


greet()