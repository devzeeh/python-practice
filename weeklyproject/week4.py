def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

while True:
    try:
        option = int(input("1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit\nChoose: "))
        
        if option == 5:
            print("Goodbye!")
            break
        elif option == 1:
            one = int(input("Enter first number: "))
            two = int(input("Enter second number: "))
            print(f"Result: {add(one, two)}")
        elif option == 2:
            one = int(input("Enter first number: "))
            two = int(input("Enter second number: "))
            print(f"Result: {sub(one, two)}")
        elif option == 3:
            one = int(input("Enter first number: "))
            two = int(input("Enter second number: "))
            print(f"Result: {mul(one, two)}")
        elif option == 4:
            one = int(input("Enter first number: "))
            two = int(input("Enter second number: "))
            print(f"Result: {div(one, two)}")
        else:
            print("Please choose a valid option (1-5).")
        
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")


    # can use this inside try block
    # option = int(input("1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit\nChoose: "))

    #    if option == 5:
    #        print("Goodbye!")
    #        break
    #    elif option in (1, 2, 3, 4):
    #        one = int(input("Enter first number: "))
    #        two = int(input("Enter second number: "))
    #       if option == 1:
    #          result = add(one, two)
    #        elif option == 2:
    #            result = sub(one, two)
    #        elif option == 3:
    #            result = mul(one, two)
    #        elif option == 4:
    #            result = div(one, two)
    #        print(f"Result: {result}")
    #    else:
    #        print("Please choose a valid option (1-5).")