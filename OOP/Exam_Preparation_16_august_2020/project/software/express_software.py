
from project_test_task.software.software import Software


"""
    • The express software is a type of software, and its type is "Express"
    • It has twice more memory consumption than the given value
"""

class ExpressSoftware(Software):

	def __init__(self, name, capacity_consumption, memory_consumption):
		super().__init__(name, "Express", capacity_consumption, 2 * memory_consumption)
