from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    DEFAULT_FISH_INCREASED_SIZE = 3

    # The FreshwaterFish could only live in FreshwaterAquarium!
    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, 3, price)

    @property
    def fish_type(self):
        return "FreshwaterFish"
