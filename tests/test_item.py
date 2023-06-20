import csv
import unittest
from io import StringIO
from unittest.mock import patch

import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item1_2():
    Item.pay_rate = 1.0
    return Item("Декстоп", 40000, 1), Item("Клавиатура", 5000, 1)


def test_name(item1_2):
    assert item1_2[0].name == "Декстоп"
    assert item1_2[1].name == "Клавиатура"


# def test_total_price(item1_2):
#     assert item1_2[0].calculate_total_price() == 40000
#     assert item1_2[1].calculate_total_price() == 5000


# def test_discount(item1_2):
#     assert item1_2[0].apply_discount() == 40000
#     assert item1_2[1].apply_discount() == 5000


# def test_csv():
#     items = Item.instantiate_from_csv()
#
#     assert len(items) == 5
#
#     assert items[0].name == "Смартфон"
#     assert items[0].price == 100.0
#     assert items[0].quantity == 1


def test_getter_name():
    item = Item("Товар", 9.99, 10)

    assert item.name == "Товар"
    assert item.price == 9.99
    assert item.quantity == 10


def test_setter():
    item = Item("Товар", 9.99, 10)

    assert item.name == "Товар"  # name длина не превышает 10
    item.name = "name длина не превышает"


# def test_repr_str():
#     item = Item("Строка", 10000, 20)
#     assert repr(item) == "Item('Строка', 10000, 20)"
#     assert str(item) == "Строка"
#
#     item2 = Item("Товар", 500, 10)
#     assert repr(item2) == "Item('Товар', 500, 10)"
#     assert str(item2) == "Товар"
#
#     item3 = Item("Продукт", 250, 5)
#     assert repr(item3) == "Item('Продукт', 250, 5)"
#     assert str(item3) == "Продукт"


def test_add():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    phone2 = Phone('Samsung Galaxy', 90000, 3, 1)

    # Сложение двух экземпляров класса Phone
    phone_sum = phone1 + phone2
    print(phone_sum)  # Ожидаемый результат: 8 (сумма количества двух телефонов)


class InstantiateCSVError(Exception):
    pass


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    @classmethod
    def string_to_number(cls, value):
        pass

    @classmethod
    def instantiate_from_csv(cls):
        file = "..\src\items.csv"
        cls.all = []

        try:
            with open(file, "r", encoding="cp1251") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        name = row["name"]
                        price = cls.string_to_number(float(row["price"]))
                        quantity = cls.string_to_number(int(row["quantity"]))
                        cls(name, price, quantity)
                    except KeyError:
                        raise InstantiateCSVError("Файл item.csv поврежден")
        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл items.csv")


class ItemTest1(Item):

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []

        try:
            with open('./src/items.csv', newline='', encoding="cp1251") as csvfile:  # некорректный путь
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('_Отсутствует файл item.csv_')


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        ItemTest1.instantiate_from_csv()


class ItemTest2(Item):

    @classmethod
    def instantiate_from_csv(cls):
        cls.all = []

        try:
            with open('test_items.csv', newline='', encoding="cp1251") as csvfile:  # некорректный файл
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if len(row) < 3:
                        raise InstantiateCSVError('_Файл item.csv поврежден_')
                    name = row['name']
                    price = cls.string_to_number(row['price'])
                    quantity = cls.string_to_number(row['quantity'])
                    cls(name, price, quantity)
        except FileNotFoundError:
            raise FileNotFoundError('_Отсутствует файл item.csv_')

    def test_instantiate_from_csv_missing_column(self):
        with pytest.raises(InstantiateCSVError) as exc_info:
            ItemTest2.instantiate_from_csv()
        assert str(exc_info.value) == '_Файл item.csv поврежден_'
