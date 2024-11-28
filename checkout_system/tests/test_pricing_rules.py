from checkout.models.product import Product
from checkout.rules.individual import IndividualPricingRule
from checkout.rules.group import GroupPricingRule

def test_individual_pricing_rule():
    product = Product("A", 50)
    rule = IndividualPricingRule(product)
    items = [Product("A", 50), Product("A", 50)]
    assert rule.calculate_price('A', 2) == 100

def test_group_pricing_rule():
    product = Product("A", 50)
    rule = GroupPricingRule(product, 3, 130)
    items = [Product("A", 50), Product("A", 50), Product("A", 50), Product("A", 50)]

    assert rule.calculate_price('A', 4) == 180
