from src.item import Item


class langs_Mixin:
    langs = ["EN", "RU"]
    __language = langs[0]

    @property
    def language(self):
        return self.__language

    @classmethod
    def change_lang(cls):
        cls.__language = "RU" if cls.__language == "EN" else "EN"
        return cls


class Keyboard(langs_Mixin, Item):

    def __init__(self, __name: str, price: float, quantity: int):
        super().__init__(__name, price, quantity)




