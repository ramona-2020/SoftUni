from Exam_15_august_2021.project import Bird
from Exam_15_august_2021.project import Food, Meat


class Owl(Bird):

    @property
    def allowed_food_types(self):
        return ['Meat']

    @property
    def weight_incremental_size(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):

    @property
    def allowed_food_types(self):
        return ['Vegetable', 'Fruit', 'Meat', 'Seat']

    @property
    def weight_incremental_size(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
