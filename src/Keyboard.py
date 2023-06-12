from src.item import Item


class langs_Mixin:
    langs = ["EN", "RU"]
    __language = langs[0]

    @property
    def language(self):
        return self.__language

    @classmethod
    def change_lang(cls):
        cls.langs = [cls.langs[1], cls.langs[0]]
        cls.__language = cls.langs[0]
        return cls


class Keyboard(langs_Mixin, Item):

    def __init__(self, __name: str, price: float, quantity: int):
        super().__init__(__name, price, quantity)




