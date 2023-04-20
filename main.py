# Create a dataclass named "Product" that has the following attributes:
# product_id: int
# name: str
# price: float
# quantity: int

# [x]The class should also have a method named "total_cost" that calculates and returns
# the total cost of the product, which is the price multiplied by the quantity.

# Create a list of Product objects and write a function that takes this list as input
# and returns the product with the highest total cost.
# Write a program that creates a list of 5 Product objects, prints out their attributes,
# and then calls the function to find the product with the highest total cost.

from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    products_list = []

    def total_cost(self):
        total_cost = self.price * self.quantity
        return total_cost

    def find_highest_total_cost(self):
        pass
