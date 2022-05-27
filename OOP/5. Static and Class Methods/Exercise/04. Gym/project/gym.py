from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

	def __init__(self):
		self.customers = []
		self.trainers = []
		self.equipment = []
		self.plans = []
		self.subscriptions = []

	def __add_entity(self, collection, entity):
		if entity not in collection:
			collection.append(entity)

	def __get_entity_by_id(self, collection, entity_id):
		for entity in collection:
			if entity.id == entity_id:
				return entity

	def add_customer(self, customer: Customer):
		self.__add_entity(self.customers, customer)

	def add_trainer(self, trainer: Trainer):
		self.__add_entity(self.trainers, trainer)

	def add_equipment(self, equipment: Equipment):
		self.__add_entity(self.equipment, equipment)

	def add_plan(self, plan: ExercisePlan):
		self.__add_entity(self.plans, plan)

	def add_subscription(self, subscription: Subscription):
		self.__add_entity(self.subscriptions, subscription)

	def subscription_info(self, subscription_id: int):
		subscription = self.__get_entity_by_id(self.subscriptions, subscription_id)
		customer = self.__get_entity_by_id(self.customers, subscription.customer_id)
		trainer = self.__get_entity_by_id(self.trainers, subscription.trainer_id)
		exercise_plan = self.__get_entity_by_id(self.plans, subscription.exercise_id)
		equipment = self.__get_entity_by_id(self.equipment, exercise_plan.equipment_id)

		return repr(subscription) + '\n' + \
			   repr(customer) + '\n' + \
			   repr(trainer) + '\n' + \
			   repr(equipment) + '\n' + \
			   repr(exercise_plan)
