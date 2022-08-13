from project.area.area import Area


class WaterArea(Area):

    CAPACITY = 10

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    @property
    def area_type(self):
        return "WaterArea"
