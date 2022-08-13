from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):

    ROOM_COST = 15
    APPLIANCES = [TV, Fridge]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, 2)