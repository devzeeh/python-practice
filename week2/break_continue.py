for i in range(10):
    if i == 5:
        break
    print("break",i)

for i in range(10):
    if i % 2 == 0:
        continue
    print("continue",i)