from project.decoration.base_decoration import BaseDecoration


class Ornament(BaseDecoration):

	@property
	def comfort(self):
		return 1

	@property
	def price(self):
		return 5