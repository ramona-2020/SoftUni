from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):

    def __init__(self, comfort=5, price=10):
        super().__init__(comfort, price)

    @property
    def decoration_type(self):
        return "Plant"
