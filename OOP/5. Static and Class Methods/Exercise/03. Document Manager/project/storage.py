from Exams.OOP.Exam_10_April_2022.project import Category
from Exams.OOP.Exam_10_April_2022.project import Topic
from Exams.OOP.Exam_10_April_2022.project import Document


class Storage:

	def __init__(self):
		self.categories = []
		self.topics = []
		self.documents = []

	def add_category(self, category: Category):
		if category not in self.categories:
			self.categories.append(category)

	def add_topic(self, topic: Topic):
		if topic not in self.topics:
			self.topics.append(topic)

	def add_document(self, document: Document):
		if document not in self.documents:
			self.documents.append(document)

	def edit_category(self, category_id: int, new_name: str):
		category = self.__find_category_by_id(category_id)
		category.edit(new_name)

	def __find_category_by_id(self, category_id: int):
		for category in self.categories:
			if category.id == category_id:
				return category

	def __find_topic_by_id(self, topic_id: int):
		for topic in self.topics:
			if topic.id == topic_id:
				return topic

	def get_document(self, document_id: int):
		for document in self.documents:
			if document.id == document_id:
				return document

	def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
		topic = self.__find_topic_by_id(topic_id)
		topic.edit(new_topic, new_storage_folder)

	def edit_document(self, document_id: int, new_file_name: str):
		document = self.get_document(document_id)
		document.edit(new_file_name)

	def delete_category(self, category_id):
		category = self.__find_category_by_id(category_id)
		self.categories.remove(category)

	def delete_topic(self, topic_id):
		topic = self.__find_topic_by_id(topic_id)
		self.topics.remove(topic)

	def delete_document(self, document_id):
		document = self.get_document(document_id)
		self.documents.remove(document)

	def __repr__(self):
		return '\n'.join(str(document) for document in self.documents)