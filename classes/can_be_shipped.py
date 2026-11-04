from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    """Interface-style contract: anyyth can be shipped must calculate shipping cost"""

    @abstractmethod
    def calculate_shipping_cost(self):
        pass