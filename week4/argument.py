# Sometimes you want a parameter to have a fallback value if the caller doesn't provide one.

# exponent = 2
def power(base, exponent=2):  # Same with def greet(name, greeting = "Hello")
    return base ** exponent # use ** for exponentiation

print(power(3)) # 3^(2) (default exponent 2)
print(power(4, 5)) # 4^(5)
