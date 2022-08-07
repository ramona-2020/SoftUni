from project.common.validator import Validator


class Race:

    def __init__(self, name: str):
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.is_name_valid(value, "Name cannot be an empty string!")
        self.__name = value
