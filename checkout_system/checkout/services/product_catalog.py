from typing import List
from checkout.models.product import Product
from checkout.rules.base_rule import PricingRule


class ProductCatalog:
    def __init__(self):
        self.products = {}
        self.pricing_rules = {}

    # adding product
    def add_product(self, product: Product, pricing_rules: dict=None):

        # checking product exstence
        if product in self.products:
            raise ValueError(f"{product} already exists")

        # adding product and its pricing rule
        self.products[product.name] = product
        if pricing_rules:
            self.pricing_rules[product.name] = pricing_rules

    # getting all produts
    def get_all_products(self) -> None:
        print('Product catalog:')
        for name , product in self.products.items():
            group_price = self.pricing_rules[name] if name in self.pricing_rules and hasattr(self.pricing_rules[name], 'group_price') else None
            print(f"Product: {name}, Price: {product.price}, Group Price: {group_price}")
    
    # returning all the pricing rules from the product catalog
    def get_pricing_rules(self) -> dict:
        return self.pricing_rules

    
    # removing product and pricing rule by name from product catalog
    def remove_product(self, product_name: str) -> None:
        if product_name not in self.products:
            raise ValueError("Product not found")
        del self.products[product_name]

        if product_name in self.pricing_rules:
            del self.pricing_rules[product_name]