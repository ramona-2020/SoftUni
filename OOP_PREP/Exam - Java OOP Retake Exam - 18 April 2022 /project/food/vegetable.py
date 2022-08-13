from project.food.food import Food


class Vegetable(Food):

    _CALORIES = 50
    _PRICE = 5

    def __init__(self):
        super().__init__(Vegetable._CALORIES, Vegetable._PRICE)

    @property
    def food_type(self):
        return "Vegetable"


