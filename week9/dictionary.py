products = ["Keyboard", "Mouse", "Monitor"]

prices = {}

for product in products:
    prices[product] = len(product)

print(prices)
# Here, len(product) returns the number of characters in each product name.

# using dictionary comprehension
prices = {
    product: len(product)
    for product in products
}

print(prices)

numbers = [1, 2, 3, 4, 5]

squares = {
    number: number ** 2
    for number in numbers
}

print(squares)

numbers = [1, 2, 3, 4, 5, 6]

even_squares = {
    number: number ** 2
    for number in numbers
    if number % 2 == 0
}

print(even_squares)

products = [
    {"name": "Keyboard", "price": 500, "quantity": 10},
    {"name": "Mouse", "price": 250, "quantity": 3},
    {"name": "Monitor", "price": 5000, "quantity": 5},
]
inventory_values = {
    product["name"]: product["price"] * product["quantity"]
    for product in products
}

print(inventory_values)