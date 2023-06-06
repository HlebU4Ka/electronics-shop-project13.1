import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = float(price)
        self.quantity = int(quantity)
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {int(self.price)}, {self.quantity})"

    def __str__(self):
        """Возвращает данные для пользователя"""
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 11:
            self.__name = value
        else:
            print("наименованиe товара больше 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):

        file = "..\src\items.csv"
        cls.all = []

        with open(file, "r", encoding="cp1251") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"]
                price = cls.string_to_number(float(row["price"]))
                quantity = cls.string_to_number(int(row["quantity"]))
                cls(name, price, quantity)

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity


    @staticmethod
    def string_to_number(string):
        try:
            return int(float(string))

        except ValueError:
            print("Не преобразовать в строку")
            return None



