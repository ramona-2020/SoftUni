from project.plantation import Plantation
from unittest import TestCase


class PlantationTests(TestCase):

    # with initial size and empty plants and workers
    def test__init__(self):
        size = 8
        plant1 = Plantation(size)
        self.assertEqual(size, plant1.size)
        self.assertEqual({}, plant1.plants)
        self.assertEqual([], plant1.workers)

    # with initial size and plants and workers
    def test__init__with_workers_and_plants(self):
        size = 8
        workers = ["worker1", "worker2"]

        plant1 = Plantation(size)
        plant1.workers = workers
        plant1.plants = {
            "worker1": ["1"],
            "worker2": ["1", "2"],
        }

        self.assertEqual(size, plant1.size)
        self.assertEqual({'worker1': ['1'], 'worker2': ['1', '2']}, plant1.plants)
        self.assertEqual(['worker1', 'worker2'], plant1.workers)

    def test_size_setter_raises_value_exception(self):
        size = -1
        with self.assertRaises(ValueError) as error:
            Plantation(size)

        self.assertEqual("Size must be positive number!", str(error.exception))

        size = 8
        plant1 = Plantation(size)
        self.assertEqual(8, plant1.size)

    def test_hire_worker_raises_value_error_for_already_hired_worker(self):
        size = 8
        plant1 = Plantation(size)
        worker_name = "worker1"

        self.assertTrue(worker_name not in plant1.workers)
        self.assertEqual([], plant1.workers)
        plant1.workers = [worker_name]

        with self.assertRaises(ValueError) as error:
            plant1.hire_worker(worker_name)
        self.assertTrue(worker_name in plant1.workers)
        self.assertEqual(1, len(plant1.workers))
        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker_successfully_hired_worker(self):
        size = 8
        plant1 = Plantation(size)
        worker_name = "worker1"
        expected = f"{worker_name} successfully hired."
        self.assertEqual(expected, plant1.hire_worker(worker_name))
        self.assertTrue(worker_name in plant1.workers)
        self.assertEqual(1, len(plant1.workers))
        self.assertEqual([worker_name], plant1.workers)

    def test__len__returns_zero(self):
        size = 8
        plant1 = Plantation(size)
        self.assertEqual(0, len(plant1))
        self.assertEqual({}, plant1.plants)

    def test__len__returns_count_of_plants(self):
        size = 8
        plant1 = Plantation(size)
        plant1.plants = {
            "worker1": "1",
            "worker2": "2",
        }
        self.assertEqual(2, len(plant1))
        self.assertEqual({"worker1": "1", "worker2": "2"}, plant1.plants)

    def test_planting_raises_worker_not_hired(self):
        size = 8
        plant1 = Plantation(size)
        worker_name = "worker1"
        plant = "1"

        expected = f"Worker with name {worker_name} is not hired!"
        with self.assertRaises(ValueError) as error:
            plant1.planting(worker_name, plant)
        self.assertEqual(expected, str(error.exception))
        self.assertTrue(worker_name not in plant1.workers)
        self.assertEqual(0, len(plant1.workers))
        self.assertEqual([], plant1.workers)

    def test_planting_raises_plantation_is_full(self):
        size = 2
        plant1 = Plantation(size)
        worker_name = "worker1"
        plant1.plants = {
            "worker1": "1",
            "worker2": "2",
        }
        plant = "3"

        plant1.hire_worker(worker_name)

        expected = "The plantation is full!"
        with self.assertRaises(ValueError) as error:
            plant1.planting(worker_name, plant)
        self.assertEqual(expected, str(error.exception))

        self.assertEqual(2, len(plant1.plants))
        self.assertEqual(2, plant1.size)
        self.assertEqual(len(plant1), plant1.size)

        self.assertEqual({'worker1': '1', 'worker2': '2'}, plant1.plants)

        self.assertTrue(plant not in plant1.plants)

    def test_planing_worker_planted_first_plant(self):
        size = 2
        plant1 = Plantation(size)
        worker_name = "worker1"
        plant = "1"
        plant1.hire_worker(worker_name)

        expected = f"{worker_name} planted it's first {plant}."
        self.assertEqual(expected, plant1.planting(worker_name, plant))
        self.assertTrue(worker_name in plant1.workers)
        self.assertEqual([plant], plant1.plants.get(worker_name))
        self.assertEqual(1, len(plant1.plants.get(worker_name)))
        self.assertEqual({'worker1': ['1']}, plant1.plants)
        self.assertTrue(plant in plant1.plants.get(worker_name))

    def test_planing_worker_planted_plant(self):
        size = 12
        plant1 = Plantation(size)
        worker_name = "worker1"
        plant = "2"

        plant1.workers = ["worker1", "worker2"]
        plant1.plants = {
            "worker1": ["1"],
            "worker2": ["1", "2"],
        }
        expected = f"{worker_name} planted {plant}."
        actual = plant1.planting(worker_name, plant)

        self.assertEqual(expected, actual)
        self.assertTrue(plant in plant1.plants[worker_name])
        self.assertTrue(2, len(plant1.plants[worker_name]))
        self.assertTrue([plant], plant1.plants[worker_name])
        self.assertEqual({'worker1': ['1', '2'], 'worker2': ['1', '2']}, plant1.plants)

    def test__str__with_no_workers_and_not_plants(self):
        plant1 = Plantation(10)
        expected = "Plantation size: 10\n"
        self.assertEqual(expected, str(plant1))

    def test__str__with_one_worker_and_not_plants(self):
        plant1 = Plantation(10)
        plant1.workers = ["worker1"]
        expected = "Plantation size: 10\n"
        expected += "worker1"
        self.assertEqual(expected, str(plant1))

    def test__str__with_workers_and_not_plants(self):
        plant1 = Plantation(10)
        plant1.workers = ["worker1", "worker2"]
        expected = "Plantation size: 10\n"
        expected += "worker1, worker2"
        self.assertEqual(expected, str(plant1))

    def test__str__with_workers_and_plants(self):
        plant1 = Plantation(10)
        plant1.workers = ["worker1", "worker2"]
        plant1.plants = {
            "worker1": ["1"],
            "worker2": ["1", "2"],
        }

        expected = "Plantation size: 10\n"
        expected += "worker1, worker2\n"
        expected += "worker1 planted: 1\n"
        expected += "worker2 planted: 1, 2"
        self.assertEqual(expected, str(plant1))

    def test__repr__with_no_workers(self):
        plant1 = Plantation(10)
        expected = "Size: 10\n"
        expected += "Workers: "

        self.assertEqual(expected, repr(plant1))

    def test__repr__with_one_worker(self):
        plant1 = Plantation(10)
        plant1.workers = ["worker1"]
        expected = "Size: 10\n"
        expected += "Workers: worker1"

        self.assertEqual(expected, repr(plant1))

    def test__repr__with_two_workers(self):
        plant1 = Plantation(10)
        plant1.workers = ["worker1", "worker2"]
        expected = "Size: 10\n"
        expected += "Workers: worker1, worker2"

        self.assertEqual(expected, repr(plant1))
