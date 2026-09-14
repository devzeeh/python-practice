try:
    one = int(input("Enter your first number: "))
    two = int(input("Enter your second number: "))
    divides = one / two
    print(f"Result is {divides}")
except ZeroDivisionError:
    print("Cant divide by zero")
except ValueError:
    print("Not a valid number")


    # Common exception types you'll run into:
    # ValueError — wrong type of value (e.g. int("abc"))
    # ZeroDivisionError — dividing by zero
    # TypeError — using the wrong data type in an operation
    # KeyError — accessing a dictionary key that doesn't exist
    # Exception - handle all error