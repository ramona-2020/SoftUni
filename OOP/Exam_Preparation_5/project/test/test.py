from project_test_task.pet_shop import PetShop
from unittest import TestCase


class PetTests(TestCase):

	NAME = 'My_pets'

	def setUp(self) -> None:
		self.shop = PetShop(self.NAME)

	def test__init__(self):
		self.assertEqual(self.NAME, self.shop.name)
		self.assertEqual({}, self.shop.food)
		self.assertEqual([], self.shop.pets)

	def test__add_food_raise_value_error_for_zero_or_negative_qty(self):
		with self.assertRaises(ValueError) as error:
			self.shop.add_food(self.NAME, -5)
		expected_result = 'Quantity cannot be equal to or less than 0'
		self.assertEqual(expected_result, str(error.exception))

	def test__add_food_successful_add_name_and_qty(self):
		food_name = 'something'
		food_qty = 25
		actual_result = self.shop.add_food(food_name, 25)
		expected_result = f"Successfully added {food_qty:.2f} grams of {food_name}."
		self.assertEqual(expected_result, actual_result)
		self.assertEqual({food_name: food_qty}, self.shop.food)
		self.assertEqual(food_qty, self.shop.food.get(food_name))

	def test__add_pet_by_name_successfully(self):
		pet_name = 'something pet name'
		expected_result = f"Successfully added {pet_name}."
		actual_result = self.shop.add_pet(pet_name)
		self.assertEqual(expected_result, actual_result)

	def test__add_pet_by_name_raise_exception(self):
		self.shop.pets = ['Name1']
		pet_name = 'Name1'
		with self.assertRaises(Exception) as error:
			self.shop.add_pet(pet_name)

		expected_result = "Cannot add a pet with the same name"
		self.assertEqual(expected_result, str(error.exception))
		self.assertEqual([pet_name], self.shop.pets)

	def test_feed_pet_by_name_raise_exception_for_missing_pet_name(self):
		food_name = 'something'
		pet_name = 'Name1'
		with self.assertRaises(Exception) as error:
			self.shop.feed_pet(food_name, pet_name)

		self.assertEqual("Please insert a valid pet name", str(error.exception))
		self.assertEqual([], self.shop.pets)

	def test_feed_pet_by_name_raise_exception_for_missing_food_nane(self):
		food_name = 'something'
		pet_name = 'Name1'
		self.shop.pets = [pet_name]
		actual_result = self.shop.feed_pet(food_name, pet_name)

		self.assertEqual(f"You do not have {food_name}", actual_result)
		self.assertEqual({}, self.shop.food)

	def test_feed_pet_with_qty_below_100(self):
		food_name = 'something'
		food_qty = 50

		pet_name = 'Name1'

		self.shop.food = {food_name: food_qty}
		self.shop.pets = [pet_name]
		expected_result = "Adding food..."
		actual_result = self.shop.feed_pet(food_name, pet_name)
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(food_qty + 1000, self.shop.food.get(food_name))

	def test_feed_pet_successfully(self):
		food_name = 'something'
		food_qty = 200
		self.shop.add_food(food_name, food_qty)

		pet_name = 'Name1'
		self.shop.add_pet(pet_name)

		expected_new_food_qty = self.shop.food.get(food_name) - 100
		actual_result = self.shop.feed_pet(food_name, pet_name)
		expected_result = f"{pet_name} was successfully fed"
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(expected_new_food_qty, self.shop.food.get(food_name))

	def test__repr__(self):
		self.shop.pets = ['Pet1', 'Pet2', 'Pet3']
		expected_result = f'Shop {self.NAME}:\nPets: {", ".join(self.shop.pets)}'
		actual_result = repr(self.shop)
		self.assertEqual(expected_result, actual_result)