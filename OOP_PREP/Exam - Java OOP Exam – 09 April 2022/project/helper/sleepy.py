from project.helper.helper import Helper


class Sleepy(Helper):
    def __init__(self, name: str):
        super().__init__(name, 50)

    def work(self):
        self.energy -= 15
        if self.energy < 0:
            self.energy = 0

