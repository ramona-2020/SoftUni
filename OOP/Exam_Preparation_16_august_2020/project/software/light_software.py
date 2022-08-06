from project.software.software import Software


"""
    • The light software is a type of software, and its type is "Light"
    • It has 50% more capacity consumption than the given value. The result should be rounded down to the nearest integer.
    • It has 50% less memory consumption than the given value. The result should be rounded down to the nearest integer.
"""

class LightSoftware(Software):

	def __init__(self, name, capacity_consumption, memory_consumption: int):
		super().__init__(name,
						 "Light",
						 int(capacity_consumption + 0.5 * capacity_consumption),
						 int(memory_consumption - 0.5 * memory_consumption))