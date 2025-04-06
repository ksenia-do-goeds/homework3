class Car:
    manufacturer: str = "Generic"   # Атрибут класса
    fuel_type: str = "Gasoline"     # Атрибут класса

    def __init__(self, model: str, year: int, color: str, mileage: float, price: float) -> None:
        """
        Конструктор для создания объекта Car.

        Параметры:
        ----------
        model : str
            Модель автомобиля.
        year : int
            Год выпуска автомобиля.
        color : str
            Цвет автомобиля.
        mileage : float
            Пробег автомобиля в километрах.
        price : float
            Цена автомобиля.
        """
        self.model: str = model           # Атрибут объекта
        self.year: int = year             # Атрибут объекта
        self.color: str = color           # Атрибут объекта
        self.mileage: float = mileage     # Атрибут объекта
        self.price: float = price         # Атрибут объекта

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Car."""
        return f"{self.year} {self.color} {self.model} - {self.mileage} km, ${self.price}"

    def drive(self, km: float) -> None:
        """
        Симулирует поездку на автомобиле.

        Параметры:
        ----------
        km : float
            Пробег, который требуется проехать.
        """
        self.mileage += km

    def update_price(self, new_price: float) -> None:
        """
        Обновляет цену автомобиля.

        Параметры:
        ----------
        new_price : float
            Новая цена автомобиля.
        """
        self.price = new_price

    def is_classic(self) -> bool:
        """Проверяет, является ли автомобиль классическим (более 20 лет)."""
        return (2023 - self.year) > 20

# Создание объектов класса Car
car1 = Car("Toyota Camry", 2015, "Black", 75000.0, 15000.0)
car2 = Car("Ford Mustang", 1965, "Red", 120000.0, 35000.0)

# Примеры использования методов и атрибутов
print(car1)
car1.drive(100)
print(car1.mileage)

print(car2)
print(f"Is classic: {car2.is_classic()}")
car2.update_price(30000.0)
print(car2.price)
