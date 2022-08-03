from unittest import TestCase, main
from project_test.vehicle import Vehicle


class TestCasesVehicle(TestCase):
	def setUp(self) -> None:
		self.vehicle = Vehicle(100, 150)

	def test__init__vehicle(self):
		vehicle = Vehicle(100, 150)
		self.assertEqual(vehicle.fuel, self.vehicle.fuel)
		self.assertEqual(vehicle.capacity, self.vehicle.fuel)
		self.assertEqual(vehicle.horse_power, self.vehicle.horse_power)
		self.assertEqual(vehicle.fuel_consumption, self.vehicle.fuel_consumption)

	def test__drive__with_raise_exception(self):
		with self.assertRaises(Exception) as context:
			result = self.vehicle.drive(100)
		self.assertEqual("Not enough fuel", str(context.exception))

	def test__drive__with_decreased_fuel(self):
		self.vehicle.drive(50)
		self.assertEqual(37.5, self.vehicle.fuel)

	def test__refuel__raised__exception(self):
		with self.assertRaises(Exception) as context:
			self.vehicle.refuel(150)
		self.assertEqual("Too much fuel", str(context.exception))

	def test__refuel__increased_fuel(self):
		self.vehicle.drive(20)
		self.vehicle.refuel(20)

		self.assertEqual(95, self.vehicle.fuel)

	def test__str__vehicle(self):
		expected = f"The vehicle has {self.vehicle.horse_power} " \
				   f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"

		self.assertEqual(expected, str(self.vehicle))









if __name__ == '__main__':
	main()