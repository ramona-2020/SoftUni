from Exams.OOP.Exam_10_April_2022.project import Car


class SportCar(Car):
	DEFAULT_FUEL_CONSUMPTION = 10

	def __init__(self, fuel: float, horse_power: int):
		super().__init__(fuel, horse_power)
