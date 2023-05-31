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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        if len(value) <= 10:
            return value
        else:
            print("наименованиe товара больше 10 симвовов")

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

        with open(file, "r", encoding="cp1251") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row["name"]
                price = float(row["price"])
                quantity = int(row["quantity"])
                item = cls(name, price, quantity)
                cls.all.append(item)

        return cls.all

    @staticmethod
    def string_to_number(value):
        try:
            return float(value), int(value)
        except ValueError:
            print("Не преобразовать в строку")
            return None
