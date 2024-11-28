from checkout.models.product import Product
from checkout.rules.base_rule import PricingRule
from typing import List

class GroupPricingRule(PricingRule):
    def __init__(self, product: Product, group_size: int, group_price: int):
        self.product = product
        self.group_size = group_size
        self.group_price = group_price
    
    def __str__(self):
        return f"{self.group_size} for {self.group_price}"

    def calculate_price(self, product_name, count) -> int:
        if product_name == self.product.name:
            group_count = count // self.group_size
            remainder = count % self.group_size
            return group_count * self.group_price + remainder * self.product.price
        return 0
