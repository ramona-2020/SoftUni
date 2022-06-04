from project.decoration.base_decoration import BaseDecoration


class Plant(BaseDecoration):

	@property
	def comfort(self):
		return 5

	@property
	def price(self):
		return 10