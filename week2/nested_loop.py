for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

for i in range(3):
    for j in range(3):
        print(i, j)

row = 5
for i in range(1, row + 1):
    for j in range(i):
        print("*", end="")
    print()


rows = 5
for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()