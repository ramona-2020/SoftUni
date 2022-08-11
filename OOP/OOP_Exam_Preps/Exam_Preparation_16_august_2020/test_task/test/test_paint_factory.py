from unittest import TestCase

from project_test_task.factory.paint_factory import PaintFactory


class PaintFactoryTest(TestCase):

	NAME = 'PuffFactoryLtd'
	CAPACITY = 10

	INGREDIENTS = {}
	INITIAL_INGREDIENTS = {
		'cheese': 4,
		'bread': 6
	}

	VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

	def setUp(self) -> None:
		self.factory_obj = PaintFactory(self.NAME, self.CAPACITY)
		self.factory_obj.valid_ingredients = self.VALID_INGREDIENTS

	def test__init__paint_factory_with_no_ingredients_success(self):
		self.assertEqual(self.NAME, self.factory_obj.name)
		self.assertEqual(self.CAPACITY, self.factory_obj.capacity)
		self.assertEqual(self.INGREDIENTS, self.factory_obj.ingredients)
		self.assertEqual(self.VALID_INGREDIENTS, self.factory_obj.valid_ingredients)

	def test__init__paint_factory_with_ingredients_success(self):
		self.factory_obj.ingredients = self.INITIAL_INGREDIENTS
		self.assertEqual(self.NAME, self.factory_obj.name)
		self.assertEqual(self.CAPACITY, self.factory_obj.capacity)
		self.assertEqual(self.INITIAL_INGREDIENTS, self.factory_obj.ingredients)
		self.assertEqual(self.VALID_INGREDIENTS, self.factory_obj.valid_ingredients)

	def test__can_add_return_true(self):
		self.factory_obj.ingredients = self.INGREDIENTS
		added_value = 1
		actual_result = self.factory_obj.can_add(added_value)
		self.assertTrue(actual_result)

	def test__can_add_return_false(self):
		self.factory_obj.ingredients = self.INITIAL_INGREDIENTS
		added_value = 1
		actual_result = self.factory_obj.can_add(added_value)
		self.assertFalse(actual_result)

	def test__add_ingredient_raises_type_error_for_not_allowed_product_type(self):
		product_type = 'coffee'
		with self.assertRaises(TypeError) as context:
			self.factory_obj.add_ingredient(product_type, 5)

		class_name = self.factory_obj.__class__.__name__
		expected_result = f"Ingredient of type {product_type} not allowed in {class_name}"
		self.assertEqual(expected_result, str(context.exception))

	def test__add_ingredient_raises_value_error_for_not_enough_space(self):
		product_type = 'red'
		product_quantity = 1

		with self.assertRaises(ValueError) as context:
			self.factory_obj.ingredients = self.INITIAL_INGREDIENTS
			self.factory_obj.add_ingredient(product_type, product_quantity)
			# return self.capacity - sum(self.ingredients.values()) - value >= 0
			# 10 - 10 - 1 >= 0 FALSE

		expected_result = "Not enough space in factory"
		self.assertEqual(expected_result, str(context.exception))

	def test__add_ingredients_first_adding_product_with_success(self):
		product_type = 'red'
		product_quantity = 1
		self.factory_obj.add_ingredient(product_type, product_quantity)
		self.assertDictEqual({
			'red': 1
		}, self.factory_obj.ingredients)
		self.assertEqual(self.factory_obj.ingredients.get('red'), 1)
		self.assertTrue(self.factory_obj.ingredients.get('red'))

	def test__add_ingredients_second_adding_product_with_success(self):
		product_type = 'red'
		product_quantity = 1

		self.factory_obj.ingredients = {
			'red': 1
		}

		self.factory_obj.add_ingredient(product_type, product_quantity)
		self.assertDictEqual({
			'red': 2
		}, self.factory_obj.ingredients)

		self.assertEqual(self.factory_obj.ingredients.get('red'), 2)
		self.assertTrue(self.factory_obj.ingredients.get('red'))

	def test__remove_ingredient_raises_key_error_for_missing_ingredient(self):
		product_type = 'red'
		product_quantity = 1

		with self.assertRaises(KeyError) as context:
			self.factory_obj.remove_ingredient(product_type, product_quantity)

			expected_result = "No such ingredient in the factory"
			self.assertEqual(expected_result, str(context.exception))
			self.assertDictEqual({}, self.factory_obj.ingredients)

	def test__remove_ingredient_raises_value_error_for_negative_ingredient(self):
		product_type = 'cheese'
		product_quantity = 5
		self.factory_obj.ingredients = self.INITIAL_INGREDIENTS

		with self.assertRaises(ValueError) as context:
			self.factory_obj.remove_ingredient(product_type, product_quantity)
		expected_result = "Ingredients quantity cannot be less than zero"
		self.assertEqual(expected_result, str(context.exception))
		self.assertDictEqual({
				'cheese': 4,
				'bread': 6
			}, self.factory_obj.ingredients)

	def test__remove_ingredient_success(self):
		product_type = 'cheese'
		product_quantity = 4
		self.factory_obj.ingredients = self.INITIAL_INGREDIENTS
		self.factory_obj.remove_ingredient(product_type, product_quantity)
		self.assertDictEqual({
				'cheese': 0,
				'bread': 6
			}, self.factory_obj.ingredients)
		self.assertEqual(6, self.factory_obj.ingredients.get('bread'))
		self.assertEqual(0, self.factory_obj.ingredients.get('cheese'))

	def test__products_list_equal(self):
		self.factory_obj.ingredients = self.INITIAL_INGREDIENTS
		self.assertDictEqual({
				'cheese': 4,
				'bread': 6
			}, self.factory_obj.products)

	def test__repr__with_no_ingredients(self):
		resval = f"Factory name: {self.factory_obj.name} with capacity {self.factory_obj.capacity}.\n"
		self.assertEqual(resval, repr(self.factory_obj))

	def test__repr__with_ingredients(self):
		self.factory_obj.ingredients = {
			'cheese': 4,
			'bread': 6
		}
		resval = f"Factory name: {self.factory_obj.name} with capacity {self.factory_obj.capacity}.\n"
		resval += f"cheese: 4\n"
		resval += f"bread: 6\n"

		self.assertEqual(resval, repr(self.factory_obj))
