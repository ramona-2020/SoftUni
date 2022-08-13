from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):

    ROOM_COST = 10
    APPLIANCES = [TV()]
    MEMBERS_COUNT = 1

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, self.MEMBERS_COUNT)
        self.calculate_expenses(self.appliances)