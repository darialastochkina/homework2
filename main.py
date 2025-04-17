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
