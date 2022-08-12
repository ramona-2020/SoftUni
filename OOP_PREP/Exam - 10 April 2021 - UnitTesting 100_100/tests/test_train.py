import unittest

from project.train.train import Train


class TrainTests(unittest.TestCase):

    def test__init__basic(self):
        t = Train("Name1", 4)
        self.assertEqual("Name1", t.name)
        self.assertEqual(4, t.capacity)
        self.assertEqual([], t.passengers)

    def test__init__advanced(self):
        t = Train("Name1", 4)
        t.passengers = [1, 2, 3]
        self.assertEqual("Name1", t.name)
        self.assertEqual(4, t.capacity)
        self.assertEqual([1, 2, 3], t.passengers)
        self.assertEqual(3, len(t.passengers))
        self.assertTrue(3 in t.passengers)

    def test__raises_value_error_train_is_full(self):
        t = Train("Name1", 3)
        t.passengers = [1, 2, 3]
        passenger_name = "new_passenger"

        with self.assertRaises(ValueError) as err:
            t.add(passenger_name)
        expected = "Train is full"
        self.assertEqual(expected, str(err.exception))
        self.assertEqual(len(t.passengers), t.capacity)
        self.assertEqual(3, len(t.passengers))

    def test__raises_value_error_passenger_exists(self):
        t = Train("Name1", 13)
        t.passengers = ["pass1"]
        passenger_name = "pass1"

        with self.assertRaises(ValueError) as err:
            t.add(passenger_name)
        expected = "Passenger pass1 Exists"
        self.assertEqual(expected, str(err.exception))
        self.assertEqual(["pass1"], t.passengers)
        self.assertTrue("pass1" in t.passengers)
        self.assertEqual(1, len(t.passengers))

    def test__add_with_success(self):
        t = Train("Name1", 13)
        passenger_name = "pass1"
        result = t.add(passenger_name)
        expected = "Added passenger pass1"
        self.assertEqual(expected, result)
        self.assertEqual(["pass1"], t.passengers)
        self.assertTrue("pass1" in t.passengers)
        self.assertEqual(1, len(t.passengers))

    def test__remove_raises_value_error_passenger_not_exists(self):
        t = Train("Name1", 13)
        passenger_name = "pass1"

        with self.assertRaises(ValueError) as err:
            t.remove(passenger_name)

        expected = "Passenger Not Found"
        self.assertEqual(expected, str(err.exception))
        self.assertEqual([], t.passengers)
        self.assertTrue("pass1" not in t.passengers)
        self.assertEqual(0, len(t.passengers))

    def test__removed_with_success(self):
        t = Train("Name1", 13)
        t.passengers = ["pass1"]

        passenger_name = "pass1"
        result = t.remove(passenger_name)
        expected = "Removed pass1"
        self.assertEqual(expected, result)
        self.assertEqual([], t.passengers)
        self.assertTrue("pass1" not in t.passengers)
        self.assertEqual(0, len(t.passengers))
