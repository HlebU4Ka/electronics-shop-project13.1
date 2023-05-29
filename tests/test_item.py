"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


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



