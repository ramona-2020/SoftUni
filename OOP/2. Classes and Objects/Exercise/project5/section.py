from project5.task import Task


class Section:

	def __init__(self, name):
		self.name = name
		self.tasks = []

	def add_task(self, new_task: Task):
		if new_task in self.tasks:
			return f"Task is already in the section {self.name}"

		self.tasks.append(new_task)
		return f"Task {new_task.details()} is added to the section"

	def get_task_by_task_name(self, task_name: str):
		for task in self.tasks:
			if task.name == task_name:
				return task

	def complete_task(self, task_name: str):
		if not any(task.name == task_name for task in self.tasks):
			return f"Could not find task with the name {task_name}"

		task = self.get_task_by_task_name(task_name)
		task_index = self.tasks.index(task)
		self.tasks[task_index].completed = True
		return f"Completed task {task_name}"

	def clean_section(self):
		removed_tasks = [task for task in self.tasks if task.completed]
		self.tasks = [task for task in self.tasks if task not in removed_tasks]

		return f"Cleared {len(removed_tasks)} tasks."

	def view_section(self):
		result = f"Section {self.name}:\n"
		for task in self.tasks:
			result += task.details() + "\n"

		return result.strip()