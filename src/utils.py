from typing import Dict, List, Optional
from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int):
        ...

    @property
    @abstractmethod
    def price(self) -> float:
        ...

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        ...

    @abstractmethod
    def __str__(self) -> str:
        ...

    @abstractmethod
    def __add__(self, other: object) -> float:
        ...


class LoggingMixin:
    def __new__(cls, *args, **kwargs):
        inst = super().__new__(cls)
        print(f"{cls.__name__} создан(а) с args={args}, kwargs={kwargs}")
        return inst


class Product(LoggingMixin, BaseProduct):
    """
    Хранит name, description, price и quantity.
    Поддерживает сложение, сравнение и строковое представление.
    """
    def __eq__(self, other: object) -> bool:
        if isinstance(other, Product):
            return (
                self.name == other.name and
                self.description == other.description and
                self.price == other.price and
                self.quantity == other.quantity
            )
        if isinstance(other, str):
            return Product.__str__(self) == other
        return NotImplemented

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: object) -> float:
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Операнд справа должен иметь тот же тип")

    @classmethod
    def new_product(cls, data: Dict) -> "Product":
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )


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

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.model}, {self.memory}, {self.color}, "
            f"{self.price} руб. Остаток: {self.quantity} шт."
        )


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

    def __str__(self) -> str:
        return (
            f"{self.name}, {self.country}, {self.germination_period}, {self.color}, "
            f"{self.price} руб. Остаток: {self.quantity} шт."
        )


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
        self._products: List[Product] = products or []
        Category.category_count += 1
        Category.product_count += len(self._products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты типа Product или его наследников.")
        self._products.append(product)
        Category.product_count += 1
        print("Товар добавлен")
        print("Обработка добавления товара завершена")

    @property
    def products(self) -> List[Product]:
        return self._products

    def get_average_price(self) -> float:
        """Средняя цена всех товаров или 0.0 если нет товаров."""
        if not self._products:
            return 0.0
        return sum(p.price for p in self._products) / len(self._products)

    def __iter__(self):
        return iter(self._products)
