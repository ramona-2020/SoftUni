from project_test_task.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    def __init__(self, name: str, price: float):
        super().__init__(name, 245, price)
