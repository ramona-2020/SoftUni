from project.utils import Utilities

"""
tool, which a Helper uses to craft Present
"""
class Instrument:

    def __init__(self, power: int):
        self.power = power

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        Utilities.negative_value_raise_value_error(
            value,
            "Cannot create an Instrument with negative power!")
        self._power = value

    def use(self):
        self.power -= 10
        if self.power < 0:
            self.power = 0

    def is_broken(self):
        return self.power == 0
    