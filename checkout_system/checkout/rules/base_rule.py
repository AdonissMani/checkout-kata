from typing import List
from checkout.models.product import Product

class PricingRule:
    def calculate_price(self, product_name: str, count: int) -> int:
        raise NotImplementedError("calculate_price must be implemented.")
