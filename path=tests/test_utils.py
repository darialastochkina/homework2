import pytest
from src.utils import Product, Category, Smartphone, LawnGrass
from src.utils import BaseProduct


@pytest.fixture
def sample_product():
    return Product("P", "desc", 10.0, 2)


@pytest.fixture
def sample_category(sample_product):
    return Category("Cat", "desc", [sample_product])


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
        "Grass", "desc", 100.0, 10,
        country="USA", germination_period=7, color="Green"
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


def test_baseproduct_cannot_be_instantiated():
    with pytest.raises(TypeError):
        BaseProduct("X", "Y", 1.0, 1)


def test_print_mixin_on_creation(capsys):
    _ = Smartphone("M", "Mix", 100.0, 2, efficiency=1.0, model="A", memory=32, color="Red")
    out = capsys.readouterr().out
    assert "Smartphone создан(а) с args=('M', 'Mix', 100.0, 2" in out
