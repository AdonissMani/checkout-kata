import pytest
from checkout.models.product import Product
from checkout.services.product_catalog import ProductCatalog
from checkout.services.checkout import Checkout
from checkout.rules.group import GroupPricingRule
from checkout.rules.individual import IndividualPricingRule

@pytest.fixture
def setup_checkout():
    # Fixture to provide a product catalog instance with preset products and rules.
    catalog = ProductCatalog()
    product_a = Product("A", 50)
    product_b = Product("B", 30)
    product_c = Product("C", 20)
    product_d = Product("D", 15)
    catalog.add_product(product_a, GroupPricingRule(product_a, 3, 130))
    catalog.add_product(product_b, GroupPricingRule(product_b, 2, 45))
    catalog.add_product(product_c, IndividualPricingRule(product_c))
    catalog.add_product(product_d, IndividualPricingRule(product_d))
    return catalog

def test_scan_items(setup_checkout):
    catalog = setup_checkout
    checkout = Checkout(catalog.get_pricing_rules())
    checkout.scan(catalog.products["A"])
    checkout.scan(catalog.products["A"])
    checkout.scan(catalog.products["A"])  # pricing for A: 3 = 130
    checkout.scan(catalog.products["B"])
    checkout.scan(catalog.products["B"])  # pricing for B: 2 = 45
    assert checkout.cart_items["A"] == 3
    assert checkout.cart_items["B"] == 2
    assert len(checkout.cart_items) == 2
    


def test_calculate_total(setup_checkout):
    catalog = setup_checkout
    checkout = Checkout(catalog.get_pricing_rules())
    checkout.scan(catalog.products["A"])
    checkout.scan(catalog.products["A"])
    checkout.scan(catalog.products["A"])  # Group pricing for A: 3 = 130
    checkout.scan(catalog.products["B"])
    checkout.scan(catalog.products["B"])  # Group pricing for B: 2 = 45
    total = checkout.calculate_total()
    assert total == 175  # 130 (A) + 45 (B)
