from src.phone import Phone
from src.item import Item


def test_add():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    phone2 = Phone('Samsung Galaxy', 90000, 3, 1)

    # Сложение двух экземпляров класса Phone
    phone_sum = phone1 + phone2
    print(phone_sum)  # Ожидаемый результат: 8 (сумма количества двух телефонов)


def test_valid_symbol():
    phone1 = Phone('iPhone 14', 120000, 5, 2)

    # Проверка валидного количества SIM-карт
    valid_sim = validate_number_of_sim(2)
    print(valid_sim)  # Ожидаемый результат: 2

    # Проверка невалидного количества SIM-карт (меньше нуля)
    try:
        invalid_sim = validate_number_of_sim(-1)
    except ValueError as e:
        print(e)  # Ожидаемое исключение.

    # Проверка невалидного количества SIM-карт (нецелое число)
    try:
        invalid_sim = validate_number_of_sim(1.5)
    except ValueError as e:
        print(e)  # Ожидаемое исключение.
