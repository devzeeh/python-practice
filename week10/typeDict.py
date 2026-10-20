from typing import TypedDict


class ProductDict(TypedDict):
    name: str
    price: float
    quantity: int


product: ProductDict = {
    "name": "Rice",
    "price": 975.0,
    "quantity": 25,
}

print(product["name"])
print(product["price"])