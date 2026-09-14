# *args collects any number of positional arguments into a tuple
def add_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_all(1, 2, 3))       # 6
print(add_all(5, 10, 15, 20)) # 50