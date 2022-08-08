from project.appliances.appliance import Appliance


class Fridge(Appliance):

	_COST = 1.2

	def __init__(self):
		super().__init__(Fridge._COST)