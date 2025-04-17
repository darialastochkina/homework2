from src.utils import Product, Category

if __name__ == "__main__":
    phone = Product("Смартфон", "Современный телефон", 10000.0, 5)
    laptop = Product("Ноутбук", "Мощный компьютер", 50000.0, 3)
    electronics = Category("Электроника", "Электронные устройства", [phone, laptop])
    print(f"Категория: {electronics.name}")
    print(f"Описание: {electronics.description}")
    print(f"Количество товаров: {len(electronics.products)}")
    print(f"Общее количество категорий: {Category.category_count}")
    print(f"Общее количество товаров: {Category.product_count}")


class Product:
    """Класс для представления товара в магазине."""

    def __init__(self, name, description, price, quantity):
        """Инициализирует новый объект Product. """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        """Инициализирует новый объект Category."""
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.products)
