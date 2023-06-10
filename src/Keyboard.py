from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = "EN"

    def change_lang(self, new_lang):
        if new_lang in ["EN", "RU"]:
            self.language = new_lang
            print(f"The keyboard language has been changed to {new_lang}")
        else:
            print("Invalid language. Only EN and RU languages are supported.")

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, new_lang):
        if new_lang in ["EN", "RU"]:
            self._language = new_lang
        else:
            raise AttributeError("Неверный язык. Поддерживаются только EN и RU.")

"""
Разобраться с Миксингом
 
 """