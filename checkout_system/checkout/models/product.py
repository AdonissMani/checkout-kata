import re


class Product:
    def __init__(self, name: str, price: int):
        # validation for name and price
        self.validate_name(name)
        self.validate_price(price)

        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.price} Rs"
    
    def validate_name(self, name: str):
        # product name should be single uppercase alphabet
        if not re.fullmatch(r"[A-Z]", name):
            raise ValueError("Product name must be single uppercase alphabet character (A-Z)")
        
    def validate_price(self, price: int):
        # product price cannot be negative
        if price < 0:
            raise ValueError("Product price must be non-negative")

    
    