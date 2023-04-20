# Create a dataclass named "Product" that has the following attributes:
# product_id: int
# name: str
# price: float
# quantity: int

# [x]The class should also have a method named "total_cost" that calculates and returns
# the total cost of the product, which is the price multiplied by the quantity.

# [x]Create a list of Product objects and write a function that takes this list as input
# and returns the product with the highest total cost.

# [x]Write a program that creates a list of 5 Product objects, prints out their attributes,
# and then calls the function to find the product with the highest total cost.

from dataclasses import dataclass


@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int


@dataclass
class ProductList:
    # products_list: List[Product] = field(default_factory=list)
    products_list = []

    def total_cost(self, product: Product) -> float:
        total_cost = product.price * product.quantity
        return total_cost

    def add_product(self, product: Product) -> list:
        self.products_list.append(product)

    def find_highest_total_cost(self) -> None:
        hight_cost = []
        for n in self.products_list:
            count = n.price * n.quantity
            hight_cost.append(count)
        max_cost = max(hight_cost)
        # a = hight_cost.index(max_cost)
        product = self.products_list[hight_cost.index(max_cost)]
        return f"Highest total cost of products '{product.name}' cost is {max_cost}€"

    def print_list(self) -> None:
        for n in self.products_list:
            print(
                f"Product id: {n.product_id}, name: {n.name}, price: {n.price}, quantity: {n.quantity} "
            )
        print(self.find_highest_total_cost())


product_1 = Product(product_id="1", name="Tranzistorius", price=0.15, quantity=50)
product_2 = Product(product_id="2", name="Rezistorius", price=1.15, quantity=50)
product_3 = Product(product_id="3", name="Kondensatorius", price=0.75, quantity=50)
product_4 = Product(product_id="4", name="Varistorius", price=2.15, quantity=50)
product_5 = Product(product_id="5", name="Simistorius", price=0.85, quantity=50)

product = ProductList()

product.add_product(product_1)
product.add_product(product_2)
product.add_product(product_3)
product.add_product(product_4)
product.add_product(product_5)


print(product.find_highest_total_cost())

product.print_list()
