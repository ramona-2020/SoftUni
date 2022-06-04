from abc import ABC, abstractmethod


class BaseDecoration(ABC):

	@property
	@abstractmethod
	def comfort(self):
		pass

	@property
	@abstractmethod
	def price(self):
		pass
