from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):

    DEFAULT_FISH_INCREASED_SIZE = 2

    # The FreshwaterFish could only live in FreshwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 5, price)

    @property
    def fish_type(self):
        return "SaltwaterFish"
