#Smart Inventory Manager - object-oriented
#Week 8

import json
import os


from product import Product
from inventory import Inventory

INVENTORY_FILE = "inventory.json"

# ------------- LOAD JSON -----------------
def load_inventory():
    """Read inventory.json and return inventory full of Product objects"""
    inventory = Inventory()

    if not os.path.exists(INVENTORY_FILE):
        print(f"{INVENTORY_FILE} not found. Starting with an empty inventory.")
        return inventory

    print(f"{INVENTORY_FILE} found.")
    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)

        for item in data:
            product = Product(item["id"], item["name"], item["price"], item["stock"])
            inventory.add_product(product)

        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, KeyError, TypeError, OSError):
        print("Could not read the file. Starting with an empty inventory.")
        return Inventory()

    return inventory
    

# ------------- Save ---------------
def save_inventory(inventory):
    """Turn every Product back into a dictionary and write them to inventory.json."""
    data = []
    for product in inventory.get_all_products():
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock(),
        })

    with open(INVENTORY_FILE, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Inventory saved successfully to {INVENTORY_FILE}.")

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
    if inventory.search_product(product_id) is not None:
        print("Product ID already exists. Cannot add product.")
        return

    name = input("Product Name: ").strip()
    price = get_float("Price: $")
    stock = get_int("Stock Quantity: ")

    product = Product(product_id, name, price, stock)   # create object
    inventory.add_product(product)                      # hand it to Inventory
    print("Product added successfully!")

def handle_update_stock(inventory):
    print("\nUpdate Stock")
    product_id = input("Enter product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")
    new_stock = get_int("Enter new stock quantity: ")

    inventory.update_stock(product_id, new_stock)
    print("Stock updated successfully.")

def handle_search_product(inventory):
    print("\nSearch Product")
    product_id = input("Enter product ID: ").strip().upper()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product found:")
    print("-" * 48)
    print(f"ID: {product.get_product_id()}")
    print(f"Name: {product.get_name()}")
    print(f"Price: ${product.get_price():.2f}")
    print(f"Stock: {product.get_stock()}")
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
            inventory.display_all
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