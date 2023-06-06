"""Здесь надо написать тесты с использованием pytest для модуля item."""
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


def test_total_price(item1_2):
    assert item1_2[0].calculate_total_price() == 40000
    assert item1_2[1].calculate_total_price() == 5000


def test_discount(item1_2):
    assert item1_2[0].apply_discount() == 40000
    assert item1_2[1].apply_discount() == 5000


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

    assert item.name == "Товар" # name длина не превышает 10
    item.name = "name длина не превышает"


def test_repr_str():
    item = Item("Строка", 10000, 20)
    assert repr(item) == "Item('Строка', 10000, 20)"
    assert str(item) == "Строка"

    item2 = Item("Товар", 500, 10)
    assert repr(item2) == "Item('Товар', 500, 10)"
    assert str(item2) == "Товар"

    item3 = Item("Продукт", 250, 5)
    assert repr(item3) == "Item('Продукт', 250, 5)"
    assert str(item3) == "Продукт"

def test_add():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    phone2 = Phone('Samsung Galaxy', 90000, 3, 1)


    # Сложение двух экземпляров класса Phone
    phone_sum = phone1 + phone2
    print(phone_sum)  # Ожидаемый результат: 8 (сумма количества двух телефонов)
