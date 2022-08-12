from project.supply.supply import Supply


class Food(Supply):

    MIN_ENERGY = 25

    def __init__(self, name: str, energy=MIN_ENERGY):
        super().__init__(name, energy)

    @property
    def type(self):
        return self.__class__.__name__

    def details(self):
        return f"{self.type}: {self.name}, {self.energy}"
