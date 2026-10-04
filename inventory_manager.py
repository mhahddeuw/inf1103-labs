#Smart Inventory Auditor
#Persistent Version

tax_rate = 0.10
overstock_threshold = 500
inventory_file = "inventory.txt"

#Load inventory from file, if file does not exist, read as 0 and empty history
def load_inventory():
    try:
        with open(inventory_file, "r") as file:
            lines = file.read().splitlines()

        if not lines:
            return 0, []

        total = int(lines[0])
        history = [int(line) for line in lines[1:]]
        return total, history

    except FileNotFoundError:
        return 0, []

#Save inventory and transaction history to file
def save_inventory(total_inventory, transaction_history):
    with open(inventory_file, "w") as file:
        file.write(f"{total_inventory}\n")
        file.writelines(f"{amount}\n" for amount in transaction_history)

#User input function to get stock quantity or quit command
def get_user_input():
    user_input = input("Enter stock quantity or 'quit' to exit: ")

    if user_input.lower() == "quit":
            return "quit"

#User input is a valid integer
    elif not user_input.isdigit():
            print("Invalid input. Please enter a valid stock quantity or 'quit' to exit.")
            return None

#User input is a valid integer, return it as an integer
    return int(user_input)

#Function to process delivery and update inventory
def process_delivery(current_total, new_value):
        return current_total + new_value

#Function to calculate tax based on the current inventory
def calculate_tax(amount):
        return amount * tax_rate

#Function to generate a final report of total deliveries and rejected entries
def generate_report(total_units, rejected_entries):
        #Print final report
        print("----- Final Report -----")
        print("Total Deliveries Processed:", total_units)
        print("Number of Failed/Rejected Entries:", rejected_entries)

#Mainframe
def main():
    #Initializing inventory
    inventory, transaction_history = load_inventory()
    rejected_entries = 0

    #Print loaded inventory and transaction history
    print("Loaded starting inventory:", inventory)
    if transaction_history:
        print("Loaded transaction history:", transaction_history)

    #Loop to continuously get user input until 'quit' is entered
    while True:
        result = get_user_input()

        #Check if user wants to quit, if so save inventory and generate report
        if result == "quit":
            save_inventory(inventory, transaction_history)
            generate_report(inventory, rejected_entries)
            print(f"Inventory saved to {inventory_file}. Exiting program.")
            break

        elif result is None:
            rejected_entries += 1
            continue

        quantity = result
        prospective_total = process_delivery(inventory, quantity)

        #Check if the prospective total exceeds the overstock threshold
        if prospective_total > overstock_threshold:
            print("Warning: Overstock threshold exceeded", overstock_threshold, ".Delivery rejected.")
            rejected_entries += 1
            save_inventory(inventory, transaction_history)
            generate_report(inventory, rejected_entries)
            print(f"Inventory saved to {inventory_file}. Exiting program.")
            break

        #Update inventory, transaction history, and calculate tax
        inventory = prospective_total
        transaction_history.append(quantity)
        tax = calculate_tax(inventory)
        print(f"Delivery: {quantity}, Inventory: {inventory}, Tax: {tax}")

if __name__ == "__main__":
    main()
