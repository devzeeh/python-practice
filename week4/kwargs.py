# **kwargs does the same thing, but for keyword arguments, collecting them into a dictionary
def describe_student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_student(name="John", age=22, course="CpE")