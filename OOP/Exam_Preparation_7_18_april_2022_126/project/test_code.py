from project_test_task.movie_app import MovieApp
from project_test_task.movie_specification.fantasy import Fantasy
from project_test_task.movie_specification.action import Action
from project_test_task.user import User

movie_app = MovieApp()

# Users:
print(movie_app.register_user('Katrin', 18))
#print(movie_app.register_user('Qvor', 29))
# "{username} registered successfully."
# print(movie_app.register_user('Katrin', 18)) # raise an Exception with the message "User already exists!"

# Movies:
# (1)
owner = movie_app.users_collection[0]
owner2 = User('Qvor', 29)

movie = Action('The lost city', 1999, owner)
print(movie_app.upload_movie('Katrin', movie))

movie = Action('The lost city', 1999, owner)
movie2 = Action('The lost city', 1999, owner2)
print(movie_app.upload_movie('Qvor', movie2))

# __str__()
print(movie_app)
#  on 2 lines for all users' usernames and movies titles in the following format:
# "All users: No users."
# "All movies: No movies."