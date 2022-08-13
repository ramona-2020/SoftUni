from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):

    ROOM_COST = 20

    APPLIANCES = [TV(), Fridge(), Laptop()]
    MEMBERS_COUNT = 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.MEMBERS_COUNT)
        self.calculate_expenses(self.appliances)


