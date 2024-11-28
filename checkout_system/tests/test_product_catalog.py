import pytest
from checkout.rules.group import GroupPricingRule
from checkout.rules.individual import IndividualPricingRule
from checkout.services.product_catalog import ProductCatalog
from checkout.models.product import Product

@pytest.fixture
def product_manager():
    return ProductCatalog()
def test_add_product(product_manager):
    product_catalog  = product_manager
    product_a = Product("A", 50)
    product_b = Product("B", 30)
    product_catalog.add_product(product_a, GroupPricingRule(product_a, 3, 130))
    product_catalog.add_product(product_b, IndividualPricingRule(product_b))
    assert "A" in product_catalog.products
    assert "B" in product_catalog.products

# Negative test case for adding existing product in catalog
def test_add_existing_product(product_manager):
    product_catalog  = product_manager
    product_catalog.add_product(Product("A", 50))
    with pytest.raises(ValueError, match="Product 'A' already exists."):
        product_catalog.add_product(Product("A", 50))

# positive test for removing product from catalog
def test_remove_product(product_manager):
    product_catalog  = product_manager
    product_catalog.add_product(Product("A", 50))
    product_catalog.remove_product("A")
    assert "A" not in product_catalog.products
    assert len(product_catalog.pricing_rules) == 0

# negative test for removing product from catalog
def test_remove_nonexistent_product(product_manager):
    product_catalog  = product_manager
    with pytest.raises(ValueError, match="Product 'Z' does not exist."):
        product_catalog.remove_product("Z")

