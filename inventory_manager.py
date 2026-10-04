#Smart Inventory Manager
#Week 5

import json
import os

INVENTORY_FILE = "inventory.json"

# ------------- LOAD JSON -----------------
def load_inventory():
    """ Load product list form inventory.json. If doesnt exist, start empty"""
    if os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} found.")
        try:
            with open(INVENTORY_FILE, "r") as file:
                inventory = json.load(file)
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, OSError):
            print("Could not read the file. Starting with an empty inventory.")
            return []

    print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
    return []

# ------------- Save ---------------
def save_inventory(inventory):
    """Write product list to inventory.json"""
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)
    print(f"Inventory saved successfully to {INVENTORY_FILE}")

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

def update_stock(inventory, product_id, new_stock):
    """Update the stock of a product. Return False if product does not exist"""
    product = search_product(inventory, product_id)
    if product is None:
        return False  # Product does not exist
    product['stock'] = new_stock
    return True  # Stock updated successfully

# ------------- User Input -----------------
def get_int(prompt):
    """Get valid integer input from user, imput >=0 """
    while True:
        try: 
            value = int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if value < 0:
            print("Value cannot be negative. Please enter a whole number greater than or equal to 0.")
            continue
        return value

def get_float(prompt):
    """Get valid float input from user, input >=0 """
    while True:
        try:
            value = float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if value < 0:
            print("Value cannot be negative. Please enter a wholenumber greater than or equal to 0.")
            continue
        return value

# ------------- Menu actions -----------------
def handle_add_product(inventory):
    print("\nAdd New Product")
    product_id = input("Enter product ID: ").strip().upper()
    if product_id == "":
        print("Product ID cannot be empty.")
        return
    if search_product(inventory, product_id) is not None:
        print("Product ID already exists. Cannot add product.")
        return

    name = input("Product Name: ").strip()
    price = get_float("Price: $")
    stock = get_int("Stock Quantity: ")

    if add_product (inventory, product_id, name, price, stock):
        print("Product added successfully.")

def handle_update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter product ID: ").strip().upper()
    product = search_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product found:")
    print(f"Name: {product['name']}")
    print(f"Current Stock: {product['stock']}")
    new_stock = get_int("Enter new stock quantity: ")

    update_stock(inventory, product_id, new_stock)
    print("Stock updated successfully.")

def handle_search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter product ID: ").strip().upper()
    product = search_product(inventory, product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product found:")
    print("-" * 48)
    print(f"ID: {product['id']}")
    print(f"Name: {product['name']}")
    print(f"Price: ${product['price']:.2f}")
    print(f"Stock: {product['stock']}")
    print("-" * 48)

def show_menu():
    print("\n----------- Smart Inventory Manager -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("-----------------------------------------------")

# ------------- Main program -----------------
def main():
    print ("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print ("=" * 40)

    # Load inventory from file
    inventory = load_inventory()

    while True:
        show_menu()
        choice = input("Enter option (1-6): ").strip()

        if choice == "1":
            display_all(inventory)
        elif choice == "2":
            handle_add_product(inventory)
        elif choice == "3":
            handle_update_stock(inventory)
        elif choice == "4":
            handle_search_product(inventory)
        elif choice == "5":
            print("Saving inventory ...")
            save_inventory(inventory)
        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated")
            break
        else:
            print("Invalid option. Please enter a number between 1 to 6.")


# ------------- RUN PROGRAM -----------------
if __name__ == "__main__":
    main()