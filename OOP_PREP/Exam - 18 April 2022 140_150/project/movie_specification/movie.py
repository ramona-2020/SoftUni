from abc import ABC, abstractmethod

from project.user import User


class Movie(ABC):

    MIN_YEAR = 1888
    MIN_AGE_RESTRICTION = 0

    @abstractmethod
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def movie_genre(self):
        return self.__class__.__name__

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value == "":
            raise ValueError("The title cannot be empty string!")
        self._title = value

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if value < self.MIN_YEAR:
            raise ValueError("Movies weren't made before 1888!")
        self._year = value

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, value):
        if not isinstance(value, User):
            raise ValueError("The owner must be an object of type User!")
        self._owner = value

    @property
    def age_restriction(self):
        return self._age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < self.MIN_AGE_RESTRICTION:
            raise ValueError(f"{self.movie_genre} movies must be restricted for audience under {self.MIN_AGE_RESTRICTION} years!")

        self._age_restriction = value

    def details(self):
        return f"{self.movie_genre} - Title:{self.title}, Year:{self.year}, Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"