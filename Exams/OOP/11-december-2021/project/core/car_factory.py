from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarFactory:

	cars_types = {
		"SportsCar": SportsCar,
		"MuscleCar": MuscleCar,
	}

	@staticmethod
	def create_car(car_type: str, model: str, speed_limit: int):
		if car_type not in CarFactory.cars_types:
			raise RuntimeError("Invalid car type")

		return CarFactory.cars_types[car_type](model, speed_limit)