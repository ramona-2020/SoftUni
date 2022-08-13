from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):

    ROOM_COST = 30

    APPLIANCES = [TV(), Fridge(), Laptop()]
    MEMBERS_COUNT = 2

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        mc = len(children) + 2
        super().__init__(family_name, salary_one + salary_two, mc)
        self.children.extend(children)
        self.calculate_expenses(self.appliances, self.children)
