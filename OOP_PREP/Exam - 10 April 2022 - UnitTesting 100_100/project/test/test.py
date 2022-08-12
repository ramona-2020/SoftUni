from unittest import TestCase
from project.movie import Movie


class MovieTestCase(TestCase):

    def test__init__basic(self):
        m = Movie("Name", 2022, 10)
        self.assertEqual("Name", m.name)
        self.assertEqual(2022, m.year)
        self.assertEqual(10, m.rating)
        self.assertEqual([], m.actors)

    def test__init__advanced(self):
        m = Movie("Name", 2022, 10)
        m.actors = ["A1", "A2", "A3"]

        self.assertEqual("Name", m.name)
        self.assertEqual(2022, m.year)
        self.assertEqual(10, m.rating)
        self.assertEqual(["A1", "A2", "A3"], m.actors)

    def test__name_raises_value_error_for_empty_name(self):
        with self.assertRaises(ValueError) as err:
            Movie("", 2022, 10)

        expected = "Name cannot be an empty string!"
        self.assertEqual(expected, str(err.exception))

    def test__name_raises_value_error_for_invalid_year(self):
        with self.assertRaises(ValueError) as err:
            Movie("Name", 1000, 10)

        expected = "Year is not valid!"
        self.assertEqual(expected, str(err.exception))

    def test__add_actor_return_actor_already_exists(self):
        m = Movie("Name", 2022, 10)
        m.actors = ["A1", "A2", "A3"]
        actor_name = "A1"

        expected = f"{actor_name} is already added in the list of actors!"
        actual = m.add_actor(actor_name)
        self.assertEqual(expected, actual)
        self.assertEqual(["A1", "A2", "A3"], m.actors)
        self.assertTrue("A1" in m.actors)
        self.assertEqual(3, len(m.actors))

    def test__add_actor_with_success(self):
        m = Movie("Name", 2022, 10)
        m.actors = ["A1", "A2", "A3"]
        actor_name = "A4"

        actual = m.add_actor(actor_name)
        self.assertEqual(["A1", "A2", "A3", "A4"], m.actors)
        self.assertTrue("A4" in m.actors)
        self.assertEqual(4, len(m.actors))

    def test__gt__first_movie_better(self):
        m1 = Movie("Name1", 2022, 20)
        m2 = Movie("Name2", 2000, 10)

        m1_rating = m1.rating
        m2_rating = m2.rating

        expected = f'"Name1" is better than "Name2"'
        self.assertEqual(expected, m1 > m2)
        self.assertEqual(20, m1_rating)
        self.assertEqual(10, m2_rating)
        self.assertTrue(m1_rating > m2_rating)

    def test__gt__second_movie_better(self):
        m1 = Movie("Name1", 2022, 5)
        m2 = Movie("Name2", 2000, 20)

        m1_rating = m1.rating
        m2_rating = m2.rating

        expected = f'"Name2" is better than "Name1"'
        self.assertEqual(expected, m1 > m2)
        self.assertEqual(5, m1_rating)
        self.assertEqual(20, m2_rating)
        self.assertTrue(m1_rating < m2_rating)

    def test__repr__with_no_actors(self):
        m1 = Movie("Name1", 2022, 5.20)

        expected = f"Name: Name1\n"
        expected += f"Year of Release: 2022\n"
        expected += f"Rating: 5.20\n"
        expected += f"Cast: "

        self.assertEqual(expected, repr(m1))

    def test__repr__with_actors(self):
        m1 = Movie("Name1", 2022, 5.20)
        m1.actors = ["a1", "a2"]

        expected = f"Name: Name1\n"
        expected += f"Year of Release: 2022\n"
        expected += f"Rating: 5.20\n"
        expected += f"Cast: a1, a2"

        self.assertEqual(expected, repr(m1))