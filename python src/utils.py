from typing import List, Optional


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: Optional[List[Product]] = None):
        """Добавляет продукт в приватный список и инкрементирует счетчик."""
        if not isinstance(products, list):
            raise TypeError("Можно добавлять только список продуктов")
        self.__products = products
        Category.product_count += len(products)
