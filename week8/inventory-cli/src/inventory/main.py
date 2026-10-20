from inventory.product import Product

def main():
    # Create a Product instance
    product = Product(
        name="keyboard",
        price=500.00,
        quantity=12,
    )

    print(f"Product: {product.name}")
    print(f"Price: P{product.price}")
    print(f"Quantity; {product.quantity}")
    print(f"Total Value: P{product.total_value():.2f}")

# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()