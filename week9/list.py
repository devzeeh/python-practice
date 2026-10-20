numbers = [1,2,3,4,5]
square=[]

for number in numbers:
    square.append(number ** 2) # equivalent to square = number * number (number^2)

print(square)

# using list comprehension
squared = [number ** 2 for number in numbers]

print(squared)