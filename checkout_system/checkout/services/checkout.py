from checkout.models.product import Product

class Checkout:
    def __init__(self, pricing_rules: dict):

        self.pricing_rules: dict = pricing_rules 
        self.cart_items: dict = {}
    
    def __str__(self):
        return f"{self.cart_items}, {self.pricing_rules}"

    def scan(self, product: Product):
        # adding product in cart and updating count of  cart items 
        self.cart_items[product.name] = self.cart_items.get(product.name, 0) + 1

    def calculate_total(self) -> int:
        total_price = 0
        print(f"Calculating total price for {self.cart_items}")
        for product_name, count in self.cart_items.items():
            # getting pricing rule for the product and calling calculate_price function
            total_price += self.pricing_rules[product_name].calculate_price(product_name, count)
        return total_price

    def display_cart(self):
        print("Cart Items:")
        for product_name, count in self.cart_items.items():
            print(f"{product_name}: {count}")
