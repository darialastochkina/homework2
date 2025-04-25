from typing import List, Optional, Dict


class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер с проверкой на положительное значение."""
        if value > 0:
            self.__price = value
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_data: Dict) -> "Product":
        """Создает экземпляр Product из словаря."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        """Название продукта, X руб. Остаток: X шт."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        """100×10 + 200×2 = 1400 — полная стоимость self + other."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price * self.quantity + other.price * other.quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: Optional[List[Product]] = None
    ):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список и инкрементирует счетчик."""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только экземпляры Product")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, возвращающий все товары через их __str__."""
        return "".join(f"{str(p)}\n" for p in self.__products)

    def __str__(self) -> str:
        """Название категории, количество продуктов: X шт."""
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."
