from project.movie_app import MovieApp
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller

ma = MovieApp()

# users
print(ma.register_user('Martin', 6))
print(ma.register_user('Stefanie', 25))
user1 = ma.users_collection[0]
user2 = ma.users_collection[1]

movie1 = Action("Name1", 1888, user1, 13)
movie2 = Fantasy("Alpha_Name2", 1999, user1, 6)
movie3 = Thriller("Alpha_Name3", 2009, user1, 16)
print(ma.upload_movie('Martin', movie1))
print(ma.upload_movie('Martin', movie2))
print(ma.upload_movie('Martin', movie3))

movie4 = Thriller("Name3", 1888, user2, 16)  # 16
print(ma.upload_movie('Stefanie', movie4))

print(ma.like_movie('Stefanie', movie2))
print(user1)
print(user2)