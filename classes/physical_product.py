from classes.product import Product


class PhysicalProduct(Product):
    """A product that is stored in a warehouse and shipped."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)   # reuse Product's setup
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()                      # parent prints the common part
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")