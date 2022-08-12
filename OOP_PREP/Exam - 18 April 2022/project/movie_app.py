from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        user_obj = User(username, age)
        if user_obj.username not in [u.username for u in self.users_collection]:
            self.users_collection.append(user_obj)
            return f"{user_obj.username} registered successfully."

        find_user_obj = self.find_user_by_username(username)
        if find_user_obj:
            raise Exception("User already exists!")

    def upload_movie(self, username: str, movie: Movie):
        if username not in [u.username for u in self.users_collection]:
            raise Exception("This user does not exist!")

        movie_obj = self.find_movie_by_title(movie.title)
        if movie_obj:
            raise Exception("Movie already added to the collection!")

        user_obj = self.find_user_by_username(username)
        if movie.owner.username != user_obj.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        # The method adds the movie to the user's movies_owned list as well as the movies_collection list:
        self.movies_collection.append(movie)
        user_obj.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        movie_obj = self.find_movie_by_title(movie.title)
        if not movie_obj:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie_obj.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        for key in kwargs.keys():
            if key in ["title", "year", "age_restriction"]:
                setattr(movie, key, kwargs[key])
        return f"{username} successfully edited {movie_obj.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        movie_obj = self.find_movie_by_title(movie.title)
        if not movie_obj:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie_obj.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie_obj.title}!")

        # deletes the movie given in both movies_collection and user's movies_owned lists
        self.movies_collection.remove(movie_obj)

        user_obj = self.find_user_by_username(username)
        user_obj.movies_owned.remove(movie_obj)
        return f"{username} successfully deleted {movie_obj.title} movie."

    def like_movie(self, username: str, movie: Movie):
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        user_obj = self.find_user_by_username(username)
        if movie.title in [m.title for m in user_obj.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user_obj.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user_obj = self.find_user_by_username(username)
        if movie.title not in [m.title for m in user_obj.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user_obj.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return "No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        return "\n".join([m.details() for m in sorted_movies]).strip()

    def __str__(self):
        result = f"All users: "

        if len(self.users_collection) == 0:
            result += "No users."
        else:
            result += ", ".join([user.username for user in self.users_collection])

        result += f"\nAll movies: "
        if len(self.movies_collection) == 0:
            result += "No movies."
        else:
            result += ", ".join([movie.title for movie in self.movies_collection])

        return result

    def find_user_by_username(self, username: str) -> User or None:
        for user in self.users_collection:
            if user.username == username:
                return user

        return None

    def find_movie_by_title(self, title: str) -> Movie or None:
        for movie in self.movies_collection:
            if movie.title == title:
                return movie

        return None

    def print_users_collection(self):
        return [u.username for u in self.users_collection]

    def print_movies_collection(self):
        return [m.title for m in self.movies_collection]
