from project.food.food import Food


class Meat(Food):

    _CALORIES = 70
    _PRICE = 10

    def __init__(self):
        super().__init__(Meat._CALORIES, Meat._PRICE)

    @property
    def food_type(self):
        return "Meat"

