from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = int(number_of_sim)

    def validate_number_of_sim(self, number_of_sim):
        try:
            number_of_sim = int(number_of_sim)
            if number_of_sim <= 0:
                raise ValueError("The number of physical SIM cards must be an integer greater than zero.")
            return number_of_sim
        except ValueError:
            raise ValueError(u"The number of physical SIM cards must be an integer greater than zero.")

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise None

    def __repr__(self):
        return f"Phone('{self.name}', {int(self.price)}, {self.quantity}, {self.number_of_sim})"







