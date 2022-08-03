

class Validator:

	@staticmethod
	def raise_if_empty_value(value: str, msg: str):
		if not value.split():
			raise ValueError(msg)

	@staticmethod
	def raise_if_negative_value(value: int, msg: str):
		if value < 0:
			raise ValueError(msg)

	@staticmethod
	def raise_if_age_is_under_min(value: int, min: int, msg: str):
		if value < min:
			raise ValueError(msg)

	@staticmethod
	def raise_if_stamina_is_outside_min_max(value: int, min_value: int, max_value: int, msg: str):
		if not (min_value <= value <= max_value):
			raise ValueError(msg)

	@staticmethod
	def raise_if_name_already_used(players: list, player_name: str, msg: str):
		if player_name in [player.name for player in players]:
			raise Exception(msg)

	@staticmethod
	def raise_if_no_supply_from_sustenance_type(sustenance_type: str, supplies: list, msg: str):
		supplies_by_type = [supply for supply in supplies if supply.type == sustenance_type]
		if len(supplies_by_type) == 0:
			raise Exception(msg)
