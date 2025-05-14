from typing import Dict
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """
    Абстрактный класс, описывающий общий интерфейс продукта.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value > 0:
            self._price = value
        else:
            raise ValueError("Цена не может быть <= 0")

    @abstractmethod
    def total_cost(self) -> float:
        """
        Должен возвращать общую стоимость (price * quantity).
        """


class InitPrintMixin:
    """
    при создании экземпляра печатает базовую информацию.
    """
    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        print(f"{cls.__name__} создан(а) с args={args}, kwargs={kwargs}")
        return inst


class Product(InitPrintMixin, BaseProduct):
    """
    Хранит name, description, price и quantity.
    Поддерживает сложение и строковое представление.
    """
    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value > 0:
            self._price = value
        else:
            raise ValueError("Цена не может быть <= 0")

    @classmethod
    def new_product(cls, product_data: Dict) -> "Product":
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if not isinstance(other, Product):
            return NotImplemented
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать объекты разных классов")
        return self.total_cost() + other.total_cost()

    def total_cost(self) -> float:
        """Общая стоимость этого продукта."""
        return self.price * self.quantity


class Category:
    category_count = 0
    product_count = 0

    def __init__(
        self,
        name: str,
        description: str,
        products: list[Product] | None = None,
    ):
        self.name = name
        self.description = description
        self.__products = products[:] if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только экземпляры Product или его наследники"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        return "".join(f"{p}\n" for p in self.__products)

    def __str__(self) -> str:
        total = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total} шт."

    def average_price(self) -> float:
        """
        Задача 2: возвращает среднюю цену товаров в категории,
        0.0 если товаров нет.
        """
        try:
            return sum(p.price for p in self.__products) / len(self.__products)
        except ZeroDivisionError:
            return 0.0


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
