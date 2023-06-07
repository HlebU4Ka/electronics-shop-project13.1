from src.phone import Phone
from src.item import Item


def test_add():
    phone1 = Phone('iPhone 14', 120000, 5, 2)
    phone2 = Phone('Samsung Galaxy', 90000, 3, 1)

    # �������� ���� ����������� ������ Phone
    phone_sum = phone1 + phone2
    print(phone_sum)  # ��������� ���������: 8 (����� ���������� ���� ���������)


def test_valid_symbol():
    phone1 = Phone('iPhone 14', 120000, 5, 2)

    # �������� ��������� ���������� SIM-����
    valid_sim = validate_number_of_sim(2)
    print(valid_sim)  # ��������� ���������: 2

    # �������� ����������� ���������� SIM-���� (������ ����)
    try:
        invalid_sim = validate_number_of_sim(-1)
    except ValueError as e:
        print(e)  # ��������� ����������.

    # �������� ����������� ���������� SIM-���� (������� �����)
    try:
        invalid_sim = validate_number_of_sim(1.5)
    except ValueError as e:
        print(e)  # ��������� ����������.
