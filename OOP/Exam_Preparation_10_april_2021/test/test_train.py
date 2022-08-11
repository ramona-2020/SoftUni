from unittest import TestCase, main

from project.train.train import Train


class TrainTests(TestCase):

	def test__init__train(self):
		name = 'My Train'
		capacity = 20
		train = Train(name, capacity)
		self.assertEqual(name, train.name)
		self.assertEqual(capacity, train.capacity)
		self.assertEqual([], train.passengers)

	def test__add_raises_train_is_full(self):
		name = 'My Train'
		capacity = 2
		train = Train(name, capacity)
		train.passengers = ["Passenger1", "Passenger2"]

		with self.assertRaises(ValueError) as err:
			result = train.add("Lilly")
		self.assertEqual("Train is full", str(err.exception))

	def test__add_raises_passenger_exists(self):
		name = 'My Train'
		passenger_name = 'Passenger1'
		capacity = 2
		train = Train(name, capacity)
		train.passengers.append(passenger_name)

		with self.assertRaises(ValueError) as err:
			result = train.add(passenger_name)
		self.assertEqual(f"Passenger {passenger_name} Exists", str(err.exception))

	def test__add_success_passenger(self):
		name = 'My Train'
		capacity = 20
		train = Train(name, capacity)

		passenger_name = 'Passenger1'
		actual_result = train.add(passenger_name)
		self.assertEqual(f"Added passenger {passenger_name}", actual_result)
		self.assertEqual([passenger_name], train.passengers)

	def test__remove_raises_passenger_not_found(self):
		name = 'My Train'
		capacity = 20
		train = Train(name, capacity)

		passenger_name = 'Passenger1'
		with self.assertRaises(ValueError) as err:
			actual_result = train.remove(passenger_name)
		self.assertEqual(f"Passenger Not Found", str(err.exception))

	def test__remove_passenger_success(self):
		name = 'My Train'
		capacity = 20
		train = Train(name, capacity)
		passenger_name = 'Passenger1'
		train.passengers = [passenger_name]

		expected_result = f"Removed {passenger_name}"
		actual_result = train.remove(passenger_name)
		self.assertEqual(expected_result, actual_result)
		self.assertEqual([], train.passengers)


if __name__ == '__main__':
	main()
