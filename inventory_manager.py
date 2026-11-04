#Smart Inventory Manager - object-oriented
#Week 8

import json
import os


from classes.can_be_shipped import CanBeShipped
from classes.inventory import Inventory
from classes.physical_product import PhysicalProduct
from classes.digital_product import DigitalProduct

INVENTORY_FILE = "inventory.json"

# ------------- FILE HANDLING -----------------
def create_product(item):
    product_type = item.get("type", "physical")    # older files had no type
    if product_type == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"],
                               item["stock"], item.get("weight", 0.0))
    
    if product_type == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"],
                              item["stock"], item["download_size"])
    return None


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
            product = create_product(item)
            if product is None:
                print(f"Skipped an item with unknown type: {item.get('type')}")
            else:
                inventory.add_product(product)

        print("Inventory loaded successfully.")
    except (json.JSONDecodeError, KeyError, TypeError, OSError):
        print("Could not read the file. Starting with an empty inventory.")
        return Inventory()

    return inventory
    

# ------------- Save ---------------
def save_inventory(inventory):
    """Ask every Product to decribe itself, then write list to inventory.json"""
    data = [product.to_dict() for product in inventory.get_all_products()]

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

    print("Product Type:")
    print("1. Physical")
    print("2. Digital")
    type_choice = input("Enter option (1 or 2): ").strip()

    if type_choice == "1":
        weight = get_float("Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, weight)
    elif type_choice == "2":
        download_size = get_float("Download Size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, download_size)
    else:
        print("Invalid product type. Nothing not added.")
        return

    inventory.add_product(product)
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
    product.display_information()
    print(f".   Fulfilment Info: {product.get_fulfilment_info()}")
    if isinstance(product, CanBeShipped):
        print(f".   Shipping Cost: ${product.calculate_shipping_cost():.2f}")
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
            inventory.display_all()
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