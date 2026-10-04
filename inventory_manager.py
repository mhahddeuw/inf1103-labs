#Smart Inventory Manager
#Week 5

# ------------- Data manipulation functions -----------------
def display_all(inventory):
    """Display all items in the inventory."""
    print("\nCurrent Inventory")
    print("-" * 48)
    if not inventory:
        print("(no products yet)")
    for product in inventory:
        print(
            f"ID: {product['id']} |Name: {product['name']} | "
            f"Price: ${product['price']:.2f} | Stock: {product['stock']}"
        )
    print("-" * 48)

if __name__ == "__main__":
    print(display_all([]))  # Test with an empty inventory
    