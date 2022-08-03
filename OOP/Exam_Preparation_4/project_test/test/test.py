from project_test.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):
	NAME = 'Alabama'
	YEAR = 2006
	RATING = 5

	def setUp(self) -> None:
		self.movie = Movie(self.NAME, self.YEAR, self.RATING)

	def test__init__successful(self):
		self.assertEqual(self.NAME, self.movie.name)
		self.assertEqual(self.YEAR, self.movie.year)
		self.assertEqual(self.RATING, self.movie.rating)
		self.assertEqual([], self.movie.actors)

	def test__init__exception_value_error_for_empty_name_and_invalid_year(self):
		with self.assertRaises(ValueError) as error:
			self.movie.name = ''
		self.assertEqual("Name cannot be an empty string!", str(error.exception))

		with self.assertRaises(ValueError) as error_two:
			self.movie.year = 1880
		self.assertEqual("Year is not valid!", str(error_two.exception))

	def test__add_actor_exception_for_already_added_actor(self):
		movie = Movie(self.NAME, self.YEAR, self.RATING)
		movie.actors = ['Bruce', 'Other']

		actor_name = 'Bruce'
		expected_result = f"{actor_name} is already added in the list of actors!"
		actual_result = movie.add_actor(actor_name)
		self.assertEqual(expected_result, actual_result)

	def test__add_actor_successful(self):
		movie = Movie(self.NAME, self.YEAR, self.RATING)
		actor_name = 'Bruce'

		self.assertEqual([], movie.actors)
		movie.add_actor(actor_name)
		self.assertEqual(['Bruce'], movie.actors)
		self.assertEqual(1, len(movie.actors))
		self.assertTrue('Bruce' in movie.actors)

	def test__compare__actor_rating(self):
		first_movie = Movie("Movie 1", 1999, 5)
		other_movie = Movie("Movie 2", 2000, 1)

		expected_result = f'"{first_movie.name}" is better than "{other_movie.name}"'
		actual_result = first_movie > other_movie
		self.assertEqual(expected_result, actual_result)

	def test__compare__actor_rating_two(self):
		first_movie = Movie("Movie 1", 1999, 5)
		other_movie = Movie("Movie 2", 2000, 10)

		expected_result = f'"{other_movie.name}" is better than "{first_movie.name}"'
		actual_result = first_movie > other_movie
		self.assertEqual(expected_result, actual_result)

	def test__repr__movie(self):
		movie_name = 'My movie'
		movie_year = 2022
		movie_rating = 2
		movie = Movie(movie_name, movie_year, movie_rating)
		movie.add_actor('Super 1')
		movie.add_actor('Super 2')

		expected_result = f"Name: {movie.name}\nYear of Release: {movie.year}\nRating: {movie.rating:.2f}\nCast: {', '.join(movie.actors)}"
		self.assertEqual(expected_result, repr(movie))


if __name__ == '__main__':
	main()
