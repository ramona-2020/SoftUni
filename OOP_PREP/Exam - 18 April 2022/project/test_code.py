
from project.movie_app import MovieApp
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller

movie_app = MovieApp()
print(movie_app.register_user('Martin', 10))
print(movie_app.register_user('Stefanie', 25))


user = movie_app.users_collection[0]
print(user.age)
movie1 = Action("Name1", 1888, user, 12)  # 12
movie2 = Fantasy("Alpha_Name2", 1999, user, 6)  # 6
movie3 = Thriller("Name3", 1888, user, 16)  # 16

movie_app.upload_movie('Martin', movie3)
movie_app.upload_movie('Martin', movie2)
print(movie_app.like_movie('Stefanie', movie2))
print(movie_app.dislike_movie('Stefanie', movie2))


movie_app.edit_movie('Martin', movie3, year=1999, title="Name33")
print(movie_app.users_collection[0])