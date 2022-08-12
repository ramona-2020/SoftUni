from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):

    def __init__(self, name: str):
        super().__init__(name, 25)

    @property
    def aquarium_type(self):
        return "SaltwaterAquarium"

