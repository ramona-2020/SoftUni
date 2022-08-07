from abc import ABC, abstractmethod
from project.common.validator import Validator


class Car(ABC):

    @abstractmethod
    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        Validator.is_model_name_valid(value, f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        Validator.is_speed_limit_between_min_and_man(
            self.min_speed_limit,
            self.max_speed_limit,
            value,
            f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!")
        self.__speed_limit = value

    @property
    def car_type(self):
        return self.__class__.__name__

    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass



