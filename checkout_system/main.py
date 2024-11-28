from checkout.models.product import Product
from checkout.rules.individual import IndividualPricingRule
from checkout.rules.group import GroupPricingRule
from checkout.services.product_catalog import ProductCatalog
from checkout.services.checkout import Checkout

if __name__ == "__main__":
    # initializeing ProductCatalog
    catalog = ProductCatalog()

    # creating products 
    product_a = Product("A", 50)
    product_b = Product("B", 30)
    product_c = Product("C", 20)
    product_d = Product("D", 25)
    product_e = Product("E", 35)

    # adding product in catalog with pricing rules
    catalog.add_product(product_a, GroupPricingRule(product_a, 3, 130))
    catalog.add_product(product_b, GroupPricingRule(product_b, 2, 45))
    catalog.add_product(product_c, IndividualPricingRule(product_c))
    catalog.add_product(product_d, IndividualPricingRule(product_d))
    catalog.add_product(product_e, IndividualPricingRule(product_e))

    # displaying product catalog
    catalog.get_all_products()

    # initializing checkout
    checkout = Checkout(catalog.get_pricing_rules())

    # take input
    cart_items = "AAABBABCCDEF"
    # cart_items = input("Enter cart items: ")

    for item in cart_items:
        # not considering product if not in catalog
        if item not in catalog.products:
             print(f"Product {item} not found in catalog")
        # adding product in cart if in catalog
        else:
            checkout.scan(catalog.products[item])

    # Calculate total for remaing items in cart
    total = checkout.calculate_total()
    print(f"Total Cart Value: {total}")