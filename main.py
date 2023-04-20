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

    products_list: list = []

    def total_cost(self):
        total_cost = self.price * self.quantity
        return total_cost

    def find_highest_total_cost(self):
        pass


product_1 = Product(product_id="1", name="Tranzistorius", price=0.15, quantity=50)
product_2 = Product(product_id="1", name="Rezistorius", price=1.15, quantity=50)
product_3 = Product(product_id="1", name="Kondensatorius", price=0.75, quantity=50)
product_4 = Product(product_id="1", name="Varistorius", price=2.15, quantity=50)
product_5 = Product(product_id="1", name="Simistorius", price=0.85, quantity=50)

Product.products_list(product_1, product_2, product_3, product_4, product_5)
print(Product.products_list)
print(product_1.total_cost())
