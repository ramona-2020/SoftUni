from project_test_task.movie_specification.movie import Movie


class Action(Movie):

	DEFAULT_AGE_RESTRICTION = 12

	def __init__(self, title: str, year: int, owner: object, age_restriction=DEFAULT_AGE_RESTRICTION):
		super().__init__(title, year, owner, age_restriction)
