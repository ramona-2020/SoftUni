

class Hero:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def defend(self, damage):
		self.health -= damage
		if self.health <= 0:
			self.health = 0
			return f"{self.name} was defeated"

	def heal(self, amount):
		self.health += amount


# Test Code:
hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.health)
print(hero.defend(1))
print(hero.health)