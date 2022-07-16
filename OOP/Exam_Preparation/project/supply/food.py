from project.supply.supply import Supply


class Food(Supply):

    def __init__(self, name: str):
        super().__init__(name, 5)

    @property
    def energy(self):
        return 5
