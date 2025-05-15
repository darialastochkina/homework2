import pytest
from src.utils import Product, Category, Smartphone, LawnGrass


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


def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test Product", "Test Description", 100.0, 0)


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

    _ = Category("Category 1", "Description 1", [product1])
    assert Category.category_count == 1
    assert Category.product_count == 1

    _ = Category("Category 2", "Description 2", [product1, product2])
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_average_price():
    product1 = Product("Product 1", "Description 1", 100.0, 5)
    product2 = Product("Product 2", "Description 2", 200.0, 3)
    category = Category("Category", "Description", [product1, product2])
    assert category.get_average_price() == 150.0


def test_average_price_empty_category():
    category = Category("Empty Category", "Description", [])
    assert category.get_average_price() == 0.0


def test_smartphone_initialization():
    sp = Smartphone(
        "Galaxy", "desc", 50000.0, 2,
        efficiency=2.5, model="S23", memory=256, color="Black"
    )
    assert sp.name == "Galaxy"
    assert sp.efficiency == 2.5
    assert sp.model == "S23"
    assert sp.memory == 256
    assert sp.color == "Black"


def test_lawngrass_initialization():
    lg = LawnGrass(
        "Grass", "desc", 100.0, 10, country="USA", germination_period=7, color="Green"
    )
    assert lg.name == "Grass"
    assert lg.country == "USA"
    assert lg.germination_period == 7
    assert lg.color == "Green"


def test_product_addition_same_type():
    a = Smartphone("A", "X", 100.0, 1, 1.0, "M", 128, "Black")
    b = Smartphone("B", "Y", 200.0, 2, 2.0, "N", 64, "White")
    assert a + b == 500.0


def test_product_addition_type_error():
    sp = Smartphone("A", "X", 100.0, 1, 1.0, "M", 128, "Black")
    lg = LawnGrass(
        "Grass", "desc", 100.0, 1,
        country="USA", germination_period=7, color="Green"
    )
    with pytest.raises(TypeError):
        _ = sp + lg


def test_add_product_accepts_subclasses():
    cat = Category("Test", "desc")
    sp = Smartphone("Z", "desc", 150.0, 3, 3.0, "Z1", 512, "Silver")
    cat.add_product(sp)
    assert "Z, 150.0 руб. Остаток: 3 шт." in cat.products


def test_add_product_type_error():
    cat = Category("Test", "desc")
    with pytest.raises(TypeError):
        cat.add_product(123)


def test_print_mixin_on_creation(capsys):
    _ = Smartphone("M", "Mix", 100.0, 2, efficiency=1.0, model="A", memory=32, color="Red")
    out = capsys.readouterr().out
    assert "Smartphone создан(а) с args=('M', 'Mix', 100.0, 2" in out


def test_subclass_init_zero_quantity():
    with pytest.raises(ValueError):
        Smartphone(
            "S", "desc", 100.0, 0,
            efficiency=1.0, model="X", memory=64, color="Black"
        )


def test_zero_quantity_product():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Description", 100.0, 0)


def test_average_price_with_products():
    category = Category("Test", "Description")
    category.add_product(Product("P1", "D1", 100.0, 1))
    category.add_product(Product("P2", "D2", 200.0, 1))
    assert category.get_average_price() == 150.0


def test_product_types():
    smartphone = Smartphone("iPhone", "Cool phone", 1000.0, 1, 0.9, "14 Pro", 256, "Black")
    grass = LawnGrass("Grass", "Green grass", 50.0, 10, "USA", 7, "Green")
    category = Category("Mixed", "Description")
    category.add_product(smartphone)
    category.add_product(grass)
    assert len(list(category)) == 2
    assert category.get_average_price() == 525.0


def test_category_iterator():
    category = Category("Test", "Description")
    products = [
        Product("P1", "D1", 100.0, 1),
        Product("P2", "D2", 200.0, 1)
    ]
    for product in products:
        category.add_product(product)
    for idx, product in enumerate(category):
        assert product == products[idx]
