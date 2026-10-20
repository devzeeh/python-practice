def calculate_total(prices: list[float]) -> float:
    return sum(prices)

prices = [10.50, 25.00, 99.99]
print(calculate_total(prices))

stock: dict[str, int] = {
    "rice": 100,
    "sugar": 25,
    "coffee": 15,
}

def get_stock(product_name: str, inventory: dict[str, int]) -> int:
    return inventory.get(product_name, 0)


print(get_stock("rice", stock))
print(get_stock("flour", stock))

categories: set[str] = {"rice", "sugar", "coffee"}

categories.add("milk")
categories.add("rice")  # Already exists

print(categories)