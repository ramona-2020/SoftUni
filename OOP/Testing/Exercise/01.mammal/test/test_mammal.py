from unittest import TestCase, main
from project_test.mammal import Mammal


class TestCasesMammal(TestCase):
	NAME = "Pesho"
	TYPE = "Types"
	SOUND = "Sound"
	KINGDOM = "animals"

	def setUp(self) -> None:
		self.mammal = Mammal(self.NAME, self.TYPE, self.SOUND)

	def test__init__mammal(self):
		self.assertEqual(self.NAME, self.mammal.name)
		self.assertEqual(self.TYPE, self.mammal.type)
		self.assertEqual(self.SOUND, self.mammal.sound)
		self.assertEqual("animals", self.mammal._Mammal__kingdom)

	def test__make_sound__formatted(self):
		expected_result = f"{self.NAME} makes {self.SOUND}"
		actual_result = self.mammal.make_sound()
		self.assertEqual(expected_result, actual_result)

	def test__get_kingdom__animals(self):
		expected_result = self.KINGDOM
		actual_result = self.mammal.get_kingdom()
		self.assertEqual(expected_result, actual_result)

	def test__info__formatted(self):
		expected_result = f"{self.NAME} is of type {self.TYPE}"
		actual_result = self.mammal.info()
		self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
	main()
