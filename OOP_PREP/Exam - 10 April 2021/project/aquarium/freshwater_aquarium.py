from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):

    def __init__(self, name: str):
        super().__init__(name, 50)

    @property
    def aquarium_type(self):
        return "FreshwaterAquarium"
