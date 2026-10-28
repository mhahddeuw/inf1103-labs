class Product: # Create bluprint "Product"
    """Represents ONE product and manages its own state."""

    def __init__(self, product_id, name, price, stock):  # Runs automatically write Product(...)
        # Double underscore = "private" (other code should use the methods below)
        self.__product_id = product_id
        self.__name = name  # Store incoming name inside object, __ makes private
        self.__price = price
        self.__stock = stock

    # ----- Getters: let other code READ the values -----
    def get_product_id(self):
        return self.__product_id

    def get_name(self):  # Read private value
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # ----- Controlled way to CHANGE the stock -----
    def update_stock(self, quantity):  # Change stock, refuse negative and non-intergers
        """Set a new stock level. Return False if the value is not allowed."""
        if not isinstance(quantity, int) or quantity < 0:
            return False
        self.__stock = quantity
        return True

    # ----- Show itself -----
    def display_information(self):  # Product prints inself, replace display_all
        print(
            f"ID: {self.__product_id} | Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | Stock: {self.__stock}"
        )