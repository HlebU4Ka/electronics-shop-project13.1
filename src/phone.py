from src.item import Item


def validate_number_of_sim(number_of_sim):
    if number_of_sim <= 0:
        raise ValueError("The number of physical SIM cards must be an integer greater than zero.")


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = None
        self.number_of_sim = number_of_sim

    def number_of_sim(self, value):
        self._number_of_sim = validate_number_of_sim(value)

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity

    def __repr__(self):
        return f"Phone('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"
