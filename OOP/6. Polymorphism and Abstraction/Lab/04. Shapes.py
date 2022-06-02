import math
from abc import ABC, abstractmethod


class Shape(ABC):
	@abstractmethod
	def calculate_area(self):
		pass

	@abstractmethod
	def calculate_perimeter(self):
		pass


class Circle(Shape):

	def __init__(self, r):
		self.__r = r

	def calculate_area(self):
		return math.pi * self.__r ** 2

	def calculate_perimeter(self):
		return 2 * math.pi * self.__r


class Rectangle(Shape):

	def __init__(self, width, height):
		self.__width = width
		self.__height = height

	def calculate_area(self):
		return self.__width * self.__height

	def calculate_perimeter(self):
		return (self.__width + self.__height) * 2

