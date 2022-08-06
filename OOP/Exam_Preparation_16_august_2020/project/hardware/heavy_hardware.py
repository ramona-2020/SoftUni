from project.hardware.hardware import Hardware


"""
    • Heavy hardware is a type of hardware, and its type is "Heavy"
    • It has twice more capacity than the given value
    • Its memory is 75% from the given value. The result should be rounded down to the nearest integer.
"""


class HeavyHardware(Hardware):

	def __init__(self, name, capacity, memory):
		super().__init__(name, "Heavy", 2 * capacity, int(0.75 * memory))