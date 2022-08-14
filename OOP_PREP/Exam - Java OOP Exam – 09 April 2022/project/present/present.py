from project.utils import Utilities


"""
 Present that a Helper is working on
"""
class Present:

    def __init__(self, name: str, energy_required: int):
        self.name = name
        self.energy_required = energy_required

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        Utilities.empty_value_raise_value_error(
            value,
            "Present name cannot be null or empty.")
        self._name = value

    @property
    def energy_required(self):
        return self._energy_required

    @energy_required.setter
    def energy_required(self, value):
        Utilities.negative_value_raise_value_error(
            value,
            "Cannot create a Present requiring negative energy!")
        self._energy_required = value

    def get_crafted(self):
        self.energy_required -= 10
        if self.energy_required < 0:
            self.energy_required = 0

    def is_done(self):
        return self.energy_required == 0
    
