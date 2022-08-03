from unittest import TestCase, main

from project_test.hero import Hero


class TestHero(TestCase):

	USERNAME = 'Pesho'
	LEVEL = 2
	HEALTH = 50.0
	DAMAGE = 50.0

	BATTLE_LEVEL_INCREMENT = 1
	BATTLE_HEALTH_INCREMENT = 5
	BATTLE_DAMAGE_INCREMENT = 5

	def setUp(self) -> None:
		self.hero = Hero(self.USERNAME, self.LEVEL, self.HEALTH, self.DAMAGE)

	def test__init__hero(self):
		self.assertEqual(self.USERNAME, self.hero.username)
		self.assertEqual(self.LEVEL, self.hero.level)
		self.assertEqual(self.HEALTH, self.hero.health)
		self.assertEqual(self.DAMAGE, self.hero.damage)

	def test__battle__raised__exception(self):
		enemy_hero = Hero(self.USERNAME, 2, 60, 10.5)
		with self.assertRaises(Exception) as context:
			self.hero.battle(enemy_hero)
		self.assertEqual("You cannot fight yourself", str(context.exception))

	def test__battle__raised__value_error_for_hero_death(self):
		enemy_hero = Hero("Lora", 2, 60, 10.5)
		self.hero.health = -100
		with self.assertRaises(ValueError) as context:
			self.hero.battle(enemy_hero)
		self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

	def test__battle_raised__value_error_for_enemy_death(self):
		enemy_hero = Hero("Lora", 2, 0, 10.5)
		with self.assertRaises(ValueError) as context:
			self.hero.battle(enemy_hero)
		self.assertEqual(f"You cannot fight {enemy_hero.username}. He needs to rest", str(context.exception))

	def test__battle__return__draw(self):
		enemy_hero = Hero("Petko", self.LEVEL, self.HEALTH, self.DAMAGE)

		expected_result = "Draw"
		expected_health = self.HEALTH - (self.DAMAGE * self.LEVEL)
		actual_result = self.hero.battle(enemy_hero)
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(expected_health, self.hero.health)
		self.assertEqual(expected_health, enemy_hero.health)

	def test__battle__return__you_win(self):
		enemy_name, enemy_level, enemy_damage = 1, 50, 10
		enemy_hero = Hero("Kostadin", enemy_name, enemy_level, enemy_damage)

		expected_result = "You win"
		enemy_hero_health = enemy_hero.health - (self.DAMAGE * self.LEVEL)

		hero_expected_level = self.LEVEL + self.BATTLE_LEVEL_INCREMENT
		hero_expected_damage = self.DAMAGE + self.BATTLE_DAMAGE_INCREMENT
		hero_expected_health = self.HEALTH - (enemy_hero.damage * enemy_hero.level) + self.BATTLE_HEALTH_INCREMENT

		actual_result = self.hero.battle(enemy_hero)
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(enemy_hero_health, enemy_hero.health)

		self.assertEqual(hero_expected_level, self.hero.level)
		self.assertEqual(hero_expected_health, self.hero.health)
		self.assertEqual(hero_expected_damage, self.hero.damage)

	def test__battle__return__you_lose(self):
		enemy_level, enemy_health, enemy_damage = 1, 50, 10
		attacker = Hero("Kostadin", enemy_level, enemy_health, enemy_damage)

		enemy_hero = Hero("Rosen", self.LEVEL, self.HEALTH, self.DAMAGE)
		enemy_hero_health = enemy_hero.health - (attacker.damage * attacker.level) + self.BATTLE_HEALTH_INCREMENT
		# enemy_hero.health -= player_damage
		#  enemy_hero.health -= self.damage * self.level

		enemy_expected_level = enemy_hero.level + self.BATTLE_LEVEL_INCREMENT
		enemy_expected_damage = enemy_hero.damage + self.BATTLE_DAMAGE_INCREMENT

		expected_result = "You lose"
		actual_result = attacker.battle(enemy_hero)
		self.assertEqual(expected_result, actual_result)
		self.assertEqual(enemy_hero_health, enemy_hero.health)

		self.assertEqual(enemy_expected_level, enemy_hero.level)
		self.assertEqual(enemy_expected_damage, enemy_hero.damage)


	def test__str__hero(self):
		expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
						f"Health: {self.hero.health}\n" \
               			f"Damage: {self.hero.damage}\n"
		self.assertEqual(expected_result, str(self.hero))


if __name__ == '__main__':
	main()