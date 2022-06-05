from Exams.OOP.Exam_10_April_2022.project import Car


class FamilyCar(Car):

	def __init__(self, fuel: float, horse_power: int):
		super().__init__(fuel, horse_power)