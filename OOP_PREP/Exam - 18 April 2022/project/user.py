

class User:

    MIN_AGE = 6

    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")
        self._username = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < User.MIN_AGE:
            raise ValueError("Users under the age of 6 are not allowed!")
        self._age = value

    def __str__(self):
        result = f"Username: {self.username}, Age: {self.age}\n"
        result += "Liked movies:\n"
        if len(self.movies_liked) == 0:
            result += "No movies liked.\n"
        else:
            movie_details = ""
            for movie in self.movies_liked:
                movie_details += movie.details() + "\n"
            result += movie_details.strip()

        result += "Owned movies:\n"
        if len(self.movies_owned) == 0:
            result += "No movies owned.\n"
        else:
            movie_details = ""
            for movie in self.movies_owned:
                movie_details += movie.details() + "\n"
            result += movie_details.strip()

        return result.strip()
