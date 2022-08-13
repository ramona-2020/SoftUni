from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    ROOM_COST = 10
    APPLIANCES = [TV]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)