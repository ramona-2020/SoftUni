from unittest import TestCase
from project_tests.plantation import Plantation


class PlantationTest(TestCase):

	SIZE = 5

	def setUp(self) -> None:
		self.plantation = Plantation(self.SIZE)

	def test__init__(self):
		self.assertEqual(self.SIZE, self.plantation.size)
		self.assertDictEqual({}, self.plantation.plants)
		self.assertListEqual([], self.plantation.workers)

	def test__size__raises_value_error_for_negative_size(self):
		with self.assertRaises(ValueError) as error:
			self.plantation.size = self.SIZE -10

		expected_result = "Size must be positive number!"
		self.assertIsNotNone(error.exception)
		self.assertEqual(expected_result, str(error.exception))
		self.assertEqual(self.SIZE, self.plantation.size)

	def test__hire_worker_raises_value_error_for_already_hired_worker(self):
		self.plantation.workers = ["Test1"]
		with self.assertRaises(ValueError) as error:
			self.plantation.hire_worker("Test1")
		expected_result = "Worker already hired!"
		self.assertEqual(expected_result, str(error.exception))

	def test__hire_worker_successfully_hired_worker(self):
		worker = "Test2"
		actual_result = self.plantation.hire_worker(worker)
		self.assertEqual(f"{worker} successfully hired.", actual_result)
		self.assertIn(worker, self.plantation.workers)

	def test__len_return_count_of_plants(self):
		self.plantation.plants = {
			"worker1": ["p1", "p2"],
			"worker2": ["p1", "p2", "p3"],
		}

		expected_length = 5
		actual_length = len(self.plantation)
		self.assertEqual(expected_length, actual_length)

	def test__planting_raises_value_error_worker_not_hired(self):
		worker = "worker"
		plant = "plant"
		with self.assertRaises(ValueError) as error:
			self.plantation.planting(worker, plant)

		self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

	def test__planting_raises_for_fulled(self):
		self.plantation.size = 5
		self.plantation.plants = {
			"worker1": ["p1", "p2"],
			"worker2": ["p1", "p2", "p3"],
		}
		worker = "worker"
		plant = "plant"
		self.plantation.hire_worker(worker)
		with self.assertRaises(ValueError) as error:
			self.plantation.planting(worker, plant)
		expected_result = "The plantation is full!"
		self.assertEqual(expected_result, str(error.exception))

	def test__planting_return_worker_planted(self):
		worker = "worker"
		plant = "plant"
		self.plantation.hire_worker(worker)
		self.plantation.plants = {
			worker: [plant]
		}

		expected_result = f"{worker} planted {plant}."
		actual_result = self.plantation.planting(worker, plant)
		self.assertEqual(expected_result, actual_result)

	def test__planting_return_worker_planting_first_plants(self):
		worker = "worker"
		plant = "plant"
		self.plantation.hire_worker(worker)
		expected_result = f"{worker} planted it's first {plant}."
		actual_result = self.plantation.planting(worker, plant)
		self.assertEqual(expected_result, actual_result)\


	def test__str__(self):
		self.plantation.workers = ["p1", "p2"]
		self.plantation.plants = {
			"worker1": ["p1", "p2"]
		}

		expected_result = f"Plantation size: 5\n"
		expected_result += "p1, p2\n"
		expected_result += "worker1 planted: p1, p2"
		self.assertEqual(expected_result, str(self.plantation))

	def test__repr__(self):
		self.plantation.workers = ["p1", "p2"]
		self.plantation.plants = {
			"worker1": ["p1", "p2"]
		}

		expected_result = f"Size: 5\n"
		expected_result += "Workers: p1, p2"
		self.assertEqual(expected_result, repr(self.plantation))