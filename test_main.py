import pytest
from src.utils import Product, Category


@pytest.fixture
def sample_product():
    """Фикстура для создания тестового продукта."""
    return Product("Смартфон", "Современный телефон с множеством функций", 10000.0, 5)


@pytest.fixture
def sample_category(sample_product):
    """Фикстура для создания тестовой категории с одним продуктом."""
    return Category("Электроника", "Электронные устройства", [sample_product])


def test_product_initialization(sample_product):
    """Тест инициализации объекта Product."""
    assert sample_product.name == "Смартфон"
    assert sample_product.description == "Современный телефон с множеством функций"
    assert sample_product.price == 10000.0
    assert sample_product.quantity == 5


def test_category_initialization(sample_category, sample_product):
    """Тест инициализации объекта Category."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Электронные устройства"
    assert len(sample_category.products) == 1
    assert sample_category.products[0] == sample_product


def test_category_count():
    """Тест подсчета количества категорий."""
    initial_count = Category.category_count
    Category("Категория 1", "Описание 1")
    Category("Категория 2", "Описание 2")
    assert Category.category_count == initial_count + 2


def test_product_count():
    """Тест подсчета количества товаров."""
    initial_count = Category.product_count
    product1 = Product("Товар 1", "Описание 1", 100.0, 10)
    product2 = Product("Товар 2", "Описание 2", 200.0, 20)
    product3 = Product("Товар 3", "Описание 3", 300.0, 30)
    Category("Тестовая категория", "Описание категории", [product1, product2, product3])
    assert Category.product_count == initial_count + 3


def test_empty_category_initialization():
    """Тест инициализации пустой категории без продуктов."""
    category = Category("Пустая категория", "Категория без продуктов")
    assert category.name == "Пустая категория"
    assert category.description == "Категория без продуктов"
    assert category.products == []
