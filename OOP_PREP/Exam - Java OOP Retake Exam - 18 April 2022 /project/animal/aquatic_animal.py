from project.animal.animal import Animal


class AquaticAnimal(Animal):

    INITIAL_KG = 2.50
    INCREASE_KG_VALUE = 7.50
    # todo: Can only live in WaterArea!

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, self.INITIAL_KG, price)

    @property
    def animal_type(self):
        return "AquaticAnimal"
