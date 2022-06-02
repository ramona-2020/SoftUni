from project.core.validator import Validator
from project.driver import Driver


class Race:
	MIN_DRIVERS = 3

	def __init__(self, name: str):
		self.name = name
		self.drivers = []

	@property
	def name(self):
		return self.__name

	@name.setter
	def name(self, value):
		Validator.raise_if_len_is_less_than(
			value,
			1,
			"Name cannot be an empty string!")
		self.__name = value

	def register_driver(self, driver: Driver):
		if driver.car is None:
			raise Exception(f"Driver {driver.name} could not participate in the race!")

		if any(d.name == driver.name for d in self.drivers):
			return f"Driver {driver.name} is already added in {self.name} race."

		self.drivers.append(driver)
		return f"Driver {driver.name} added in {self.name} race."

	def start(self):
		if len(self.drivers) < Race.MIN_DRIVERS:
			raise Exception(f"Race {self.name} cannot start with less than {Race.MIN_DRIVERS} participants!")

		result = []
		drivers_winners = sorted(self.drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]
		for driver in drivers_winners:
			driver.number_of_wins += 1
			result.append(f"Driver {driver.name} wins the {self.name} race with a speed of {driver.car.speed_limit}.")

		return "\n".join(result)

