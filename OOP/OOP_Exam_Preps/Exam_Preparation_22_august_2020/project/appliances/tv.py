from project.appliances.appliance import Appliance


class TV(Appliance):

	_COST = 1.5

	def __init__(self):
		super().__init__(TV._COST)
