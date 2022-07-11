

class Room:

    def __init__(self, number: int, capacity: int):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    def take_room(self, people):
        # guests: 3
        # capacity: 9
        if self.is_taken or self.guests + people > self.capacity:
            return f"Room number {self.number} cannot be taken"

        self.is_taken = True
        self.guests += people

    def free_room(self):
        if self.is_taken:
            self.is_taken = False
            self.guests = 0
        else:
            return f"Room number {self.number} is not taken"
