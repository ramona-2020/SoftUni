from project.hardware.hardware import Hardware

"""
    • The power hardware is a type of hardware, and its type is "Power"
    • Its capacity is 25% of the given value. The result should be rounded down to the nearest integer.
    • It has 75% more memory than the given value. The result should be rounded down to the nearest integer.
"""


class PowerHardware(Hardware):

	def __init__(self, name, capacity, memory):
		super().__init__(name, "Power", int(0.25 * capacity), int(1.75 * memory))

		# 200, 200 ok
