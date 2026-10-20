# Product class representing an item in the inventory
class Product:
    # Initialize the Product class with name, price, and quantity
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Calculate the total value of the product in stock with return of type float
    def total_value(self) -> float:
        return self.price * self.quantity