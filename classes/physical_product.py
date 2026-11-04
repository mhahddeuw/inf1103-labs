from classes.product import Product
from classes.can_be_shipped import CanBeShipped

SHIPPING_BASE_COST = 5.00    # flat fee
SHIPPING_COST_PER_KG = 2.00   # xtra per kilogram


class PhysicalProduct(Product, CanBeShipped):
    """A product that is stored in a warehouse and shipped."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)   # reuse Product's setup
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()                      # parent prints the common part
        print(f"    Type: Physical | Weight: {self.__weight:.2f} kg")

    def get_fulfilment_info(self):
        return "Physical product: requires warehouse storage and shipping."

    def calculate_shipping_cost(self):
        return SHIPPING_BASE_COST + (SHIPPING_COST_PER_KG * self.__weight)