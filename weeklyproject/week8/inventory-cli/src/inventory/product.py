# Product class representing an item in the inventory
class Product:
    """
    Represents a product in the inventory.
    """
    # Initialize the Product class with name, price, and quantity
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Calculate the total value of the product in stock with return of type float
    def total_value(self) -> float:
        """
        This method calculates the total value of the product in stock.
        It multiplies the price of the product by the quantity in stock.
        """
        return self.price * self.quantity

    # Add a specified quantity to the product's stock returning None
    def addProduct(self, quantity: int) -> None:
        """
        Adds a specified quantity to the product's stock.
        Raises a ValueError if the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity must be a positive.")
        
        self.quantity += quantity # equivalent to self.quantity = self.quantity + quantity

    # Remove a specified quantity from the product's stock returning None
    def removeStock(self, quantity:int) -> None:
        """
        Removes a specified quantity from the product's stock.
        Raises a ValueError if the quantity is negative or exceeds the available stock.
        """
        # Check if the quantity to remove is valid
        if quantity < 0:
            raise ValueError("Quantity must be a positive.")
        if quantity > self.quantity:
            raise ValueError("Insufficient stock to remove the specified quantity.")

        self.quantity -= quantity # equivalent to self.quantity = self.quantity - quantity