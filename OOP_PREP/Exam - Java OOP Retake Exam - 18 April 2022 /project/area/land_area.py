from project.area.area import Area


class LandArea(Area):

    CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    @property
    def area_type(self):
        return "LandArea"
