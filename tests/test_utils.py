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


def test_category_initialization(sample_category):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Test Description"
    assert "Test Product, 100.0 руб. Остаток: 5 шт.\n" in sample_category.products


def test_add_product():
    Category.category_count = 0
    Category.product_count = 0

    cat = Category("New Cat", "Desc")
    prod = Product("NewProd", "Desc", 50.0, 2)

    before = Category.product_count
    cat.add_product(prod)
    assert Category.product_count == before + 1
    assert "NewProd, 50.0 руб. Остаток: 2 шт.\n" in cat.products


def test_product_price_setter():
    prod = Product("X", "Y", 100.0, 1)
    prod.price = -10
    assert prod.price == 100.0
    prod.price = 200.0
    assert prod.price == 200.0


def test_new_product_classmethod():
    data = {
        "name": "CP",
        "description": "Desc",
        "price": 300.0,
        "quantity": 10
    }
    cp = Product.new_product(data)
    assert isinstance(cp, Product)
    assert cp.name == "CP"
    assert cp.price == 300.0
    assert cp.quantity == 10


def test_add_product_type_check():
    cat = Category("Sample", "Desc")
    with pytest.raises(TypeError) as exc:
        cat.add_product("не продукт")
    assert "экземпляры Product" in str(exc.value)


def test_product_str():
    prod = Product("AAA", "desc", 50.0, 3)
    assert str(prod) == "AAA, 50.0 руб. Остаток: 3 шт."


def test_product_addition():
    a = Product("A", "X", 100.0, 2)
    b = Product("B", "Y", 200.0, 1)
    assert a + b == 400.0


def test_category_str(sample_category):
    assert str(sample_category) == "Test Category, количество продуктов: 5 шт."
