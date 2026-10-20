from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
    quantity: int


product = Product(
    name="Rice",
    price=975.0,
    quantity=25,
)

print(product)
print(product.name)