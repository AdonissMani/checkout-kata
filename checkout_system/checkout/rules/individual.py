from checkout.models.product import Product
from checkout.rules.base_rule import PricingRule
from typing import List

class IndividualPricingRule(PricingRule):
    def __init__(self, product: Product):
        self.product = product

    def calculate_price(self,  product_name, count) -> int:
        if product_name == self.product.name: return count * self.product.price if count > 0 else 0
