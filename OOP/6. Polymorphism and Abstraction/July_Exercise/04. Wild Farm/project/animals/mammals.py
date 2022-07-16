from project.animals.animal import Mammal
from project.food import Food, Vegetable, Fruit, Meat


class Mouse(Mammal):

    @property
    def allowed_food_types(self):
        return ['Vegetable', 'Fruit']

    @property
    def weight_incremental_size(self):
        return 0.40

    def make_sound(self):
        return "Squeak"


class Dog(Mammal):
    @property
    def allowed_food_types(self):
        return ['Meat']

    @property
    def weight_incremental_size(self):
        return 0.40

    def make_sound(self):
        return "Woof!"


class Cat(Mammal):
    @property
    def allowed_food_types(self):
        return ['Vegetable', 'Meat']

    @property
    def weight_incremental_size(self):
        return 0.30

    def make_sound(self):
        return "Meow"


class Tiger(Mammal):
    @property
    def allowed_food_types(self):
        return ['Meat']

    @property
    def weight_incremental_size(self):
        return 1.00

    def make_sound(self):
        return "ROAR!!!"
