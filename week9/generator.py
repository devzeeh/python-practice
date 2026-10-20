def read_inventory():
    items = ["Keyboard", "Mouse", "Monitor"]

    for item in items:
        yield item


for item in read_inventory():
    print(item)