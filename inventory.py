class Inventory:
    """Manages a COLLECTION of Product objects."""

    def __init__(self):
        self.__products = []  # Each inventory starts with empty private list, list holds Product objects, not dictionaries.

    def add_product(self, product):  #  Receives a ready-made Product and puts it in the list, unless that ID already exists.
        """Store a Product. Return False if its ID is already used."""
        if self.search_product(product.get_product_id()) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, product_id):  # Asks each product get_product_id() instead of reading product["id"]
        """Return the Product with this ID, or None if not found."""
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def update_stock(self, product_id, quantity):  # Inventory finds product, tells product to change its own stock, doesn’t touch the stock value itself
        """Find a product and ask it to update its own stock."""
        product = self.search_product(product_id)
        if product is None:
            return False
        return product.update_stock(quantity)

    def display_all(self):  # Loops through products and tells each one to display_information()
        print("\nCurrent Inventory")
        print("-" * 48)
        if not self.__products:
            print("(no products yet)")
        for product in self.__products:
            product.display_information()
        print("-" * 48)

    def get_all_products(self): # Hands out copy of list so the file-saving code can read products without being able to damage the real list.
        """Return a copy of the product list (used when saving to file)."""
        return list(self.__products)