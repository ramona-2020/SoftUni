

class Player:
	DEFAULT_GUILD = "Unaffiliated"

	def __init__(self, name, hp, mp):
		self.name = name
		self.hp = hp
		self.mp = mp
		self.skills = {}
		self.guild = self.DEFAULT_GUILD

	def add_skill(self, skill_name, mana_cost):
		if skill_name in self.skills:
			return "Skill already added"
		self.skills.update({skill_name: mana_cost})
		return f"Skill {skill_name} added to the collection of the player {self.name}"

	def player_info(self):
		player_info = f"Name: {self.name}\nGuild: {self.guild}\nHP: {self.hp}\nMP: {self.mp}\n"
		for skill_name, skill_mana_cost in self.skills.items():
			player_info += f"==={skill_name} - {skill_mana_cost}\n"

		return player_info.strip()