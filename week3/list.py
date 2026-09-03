fruit = ["apple", "banana", "grapes", "watermelon", "lemon"]
print(fruit[0]) # "apple" — indexing starts at 0
print(fruit[-1]) # "cherry" — negative index counts from the end

fruit.append("strawberry") # adds to the end
fruit.remove("lemon") # removes by value
print(fruit)

print(fruit[:3]) # ['apple', 'banana', 'grapes']
print(fruit[-2:]) # ['watermelon', 'strawberry']
print(fruit[1:]) # ['banana', 'grapes', 'watermelon', 'strawberry']