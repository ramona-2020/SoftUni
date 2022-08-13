from project.rooms.room import Room


class AloneOld(Room):

    ROOM_COST = 5
    MEMBERS_COUNT = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.MEMBERS_COUNT)
