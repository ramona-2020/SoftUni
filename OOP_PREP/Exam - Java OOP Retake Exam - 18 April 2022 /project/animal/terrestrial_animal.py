from project.animal.animal import Animal


class TerrestrialAnimal(Animal):

    INITIAL_KG = 5.50
    INCREASE_KG_VALUE = 5.70
    # todo: Can only live in LandArea!

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, self.INITIAL_KG, price)

    @property
    def animal_type(self):
        return "TerrestrialAnimal"
