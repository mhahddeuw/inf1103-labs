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

def search_product(inventory, product_id):
    """Search for a product by its ID."""
    for product in inventory:
        if product['id'] == product_id:
            return product
    return None

def add_product(inventory, product_id, name, price, stock):
    """Add a new product to the inventory. Return False if product does not exist"""
    if search_product(inventory, product_id) is not None:
        return False  # Product does not exist
    inventory.append(
        {"id": product_id,
         "name": name,
         "price": price,
         "stock": stock}
    )
    return True  # Product added successfully



if __name__ == "__main__":
    print(display_all([]))  # Test with an empty inventory
    print(search_product([], 1))  # Test search with an empty inventory
