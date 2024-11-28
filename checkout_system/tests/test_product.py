import pytest
from checkout.models.product import Product

def test_valid_product_creation():
    product = Product("A", 50)
    assert product.name == "A"
    assert product.price == 50

def test_invalid_product_name_lowercase():
    with pytest.raises(ValueError, match="Product name must be a single uppercase alphabet character \\(A-Z\\)."):
        Product("a", 50)

def test_invalid_product_name_multiple_chars():
    with pytest.raises(ValueError, match="Product name must be a single uppercase alphabet character \\(A-Z\\)."):
        Product("AB", 50)
