from project.common.validator import Validator


class Planet:

    def __init__(self, name: str):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.raise_if_empty(
            value, f"Planet name cannot be empty string or whitespace!")
        self.__name = value


