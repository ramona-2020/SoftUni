from Exams.OOP.Exam_10_April_2022.project import Vehicle


class Car(Vehicle):
	DEFAULT_FUEL_CONSUMPTION = 3

	def __init__(self, fuel: float, horse_power: int):
		super().__init__(fuel, horse_power)