# Import the Product class from the product module. 
# "inventory" is the package name, and "product" is the module name.
# and "Product" is the class name within that module.
from inventory.product import Product 

def main():
    # Create a Product instance
    product = Product("keyboard", 500.19, 12)
    """
    Demonstrates the functionality of the Product class.
    """

    print(f"Initial quantity: {product.quantity}")

    add = 10
    product.addProduct(add)
    print(f"Quantity after add stock {add}: {product.quantity}")

    product.removeStock(7)
    print(f"Quantity after removing stock: {product.quantity}")
    
    print(f"Total Value: P{product.total_value():.2f}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()