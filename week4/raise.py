# raise lets you deliberately throw an error when your own logic decides something is invalid 
# even if Python wouldn't normally complain.
def grade(grade):
    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100")
    return grade

try:
    result = grade(-1)
    print(f"Valid grade: {result}")
except ValueError as e:
    print(f"Error: {e}")

try:
    result = grade(85)
    print(f"Valid grade: {result}")
except ValueError as e:
    print(f"Error: {e}")