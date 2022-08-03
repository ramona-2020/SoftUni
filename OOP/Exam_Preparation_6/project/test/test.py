from unittest import TestCase
from project.team import Team


class TeamTest(TestCase):

	NAME = 'MyTeam'

	def setUp(self) -> None:
		self.team = Team(self.NAME)

	def test__init__(self):
		self.assertEqual(self.NAME, self.team.name)
		self.assertEqual({}, self.team.members)

	def test__set__invalid_name_raise_value_error(self):
		with self.assertRaises(ValueError) as error:
			self.team.name = 'My_team_10'
		expected_result = "Team Name can contain only letters!"
		self.assertEqual(expected_result, str(error.exception))

	def test__add__member_with_success_msg(self):
		actual_result = self.team.add_member(name1=10, name2=8)
		expected_result = "Successfully added: name1, name2"
		self.assertEqual(expected_result, actual_result)

	def test__add__member_with_no_success_msg(self):
		self.team.members = {
			'alex': 32
		}

		self.team.add_member(alex=5)
		self.assertEqual({'alex': 32}, self.team.members)

	def test__len__(self):
		expected_result = len(self.team.members)
		self.assertEqual(expected_result, len(self.team))