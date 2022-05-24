from project.movie_app import MovieApp
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action

movie_app = MovieApp()
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
a = 5