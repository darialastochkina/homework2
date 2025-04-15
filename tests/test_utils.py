import pytest
from src.utils import Product, Category


@pytest.fixture
def sample_product():
    return Product("Test Product", "Test Description", 100.0, 5)


@pytest.fixture
def sample_category(sample_product):
    return Category("Test Category", "Test Description", [sample_product])


def test_product_initialization(sample_product):
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test Description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 5


def test_category_initialization(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_counter():
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category1 = Category("Category 1", "Description 1", [product1])
    assert Category.category_count == 1
    assert Category.product_count == 1
    assert category1.name == "Category 1"
    category2 = Category("Category 2", "Description 2", [product1, product2])
    assert Category.category_count == 2
    assert Category.product_count == 3
    assert category2.name == "Category 2"
