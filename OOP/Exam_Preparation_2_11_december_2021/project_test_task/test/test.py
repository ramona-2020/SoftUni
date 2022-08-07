from project.team import Team
from unittest import TestCase


class TeamTest(TestCase):

	NAME = 'RGTeam'
	INVALID_NAME = 'RG_Team_2022'
	EMPTY_MEMBERS = {}
	NON_EMPTY_MEMBERS = {
		'Ivan': 39,
		'Boyan': 45,
		'Chudomir': 33,
	}

	def setUp(self) -> None:
		self.team = Team(self.NAME)
		self.team.members = self.EMPTY_MEMBERS

	# Validation tests:
	def test__name__raises_value_error(self):
		with self.assertRaises(ValueError) as context:
			self.team.name = self.INVALID_NAME
			self.assertEqual(
				"Team Name can contain only letters!",
				str(context.exception))

	def test__init__with_no_members(self):
		self.assertEqual(self.NAME, self.team.name)
		self.assertEqual(self.EMPTY_MEMBERS, self.team.members)

	def test__init__with_members(self):
		self.team.members = self.NON_EMPTY_MEMBERS
		self.assertEqual(self.NAME, self.team.name)
		self.assertEqual(self.NON_EMPTY_MEMBERS, self.team.members)

	def test__add_member__with_existing_members(self):
		self.team.members = self.NON_EMPTY_MEMBERS

		add_member_message = f"Successfully added: "
		actual_message = self.team.add_member(Ivan=25)

		self.assertDictEqual(self.NON_EMPTY_MEMBERS, self.team.members)
		self.assertEqual(add_member_message, actual_message)

	def test__add_member__with_not_existing_members(self):
		actual_message = self.team.add_member(Andrei=35, Lora=28)

		added_members_by_name = ['Andrei', 'Lora']
		updated_members_dict = {'Lora': 28, 'Andrei': 35}

		add_member_message = f"Successfully added: {', '.join(added_members_by_name)}"

		self.assertDictEqual(updated_members_dict, self.team.members)
		self.assertEqual(add_member_message, actual_message)

	def test__remove_member__no_success(self):
		name = 'Georgi'
		expected_message = f"Member with name {name} does not exist"
		actual_message = self.team.remove_member(name)
		self.assertEqual(expected_message, actual_message)

	def test__remove_member__with_success(self):
		name = 'Boyan'

		self.team.members = self.NON_EMPTY_MEMBERS

		expected_message = f"Member {name} removed"
		actual_message = self.team.remove_member(name)
		self.assertEqual(expected_message, actual_message)

		d1 = {
			'Ivan': 39,
			'Chudomir': 33,
		}
		d2 = self.team.members
		self.assertDictEqual(d1, d2)

	def test__gt__with_assert_true(self):
		# len(self.members) > len(other.members):
		t1 = self.team
		t1.members = self.NON_EMPTY_MEMBERS

		t2 = Team("TeamTwo")
		t2.members = {}

		self.assertTrue(t1 > t2)

	def test__gt__with_assert_false(self):
		# not len(self.members) > len(other.members):
		t1 = self.team

		t2 = Team("TeamTwo")
		t2.members = self.NON_EMPTY_MEMBERS

		self.assertFalse(t1 > t2)

	def test__str__with_no_members(self):
		name = 'TeamMonie'
		team_obj = Team(name)
		team_obj.members = {}

		expected_result = f"Team name: {name}"
		self.assertEqual(expected_result, str(team_obj))

	def test__str__members_with_different_names_and_years(self):
		name = 'TeamMonie'
		self.team.name = name
		self.team.members = {
			'Ivan': 39,
			'Boyan': 45,
			'Chudomir': 33,
		}
		expected_result = "Team name: TeamMonie"
		expected_result += f"\nMember: Boyan - 45-years old"
		expected_result += f"\nMember: Ivan - 39-years old"
		expected_result += f"\nMember: Chudomir - 33-years old"

		self.assertEqual(expected_result, str(self.team))

	def test__str__members_with_different_same_years(self):
		name = 'TeamMonie'
		self.team.name = name
		self.team.members = {
			'Ivan': 33,
			'Boyan': 33,
			'Chudomir': 33,
		}
		expected_result = f"Team name: {name}"
		expected_result += f"\nMember: Boyan - 33-years old"
		expected_result += f"\nMember: Chudomir - 33-years old"
		expected_result += f"\nMember: Ivan - 33-years old"

		self.assertEqual(expected_result, str(self.team))

	def test__len__with_no_members(self):
		self.team.members = {}
		self.assertEqual(0, len(self.team))

	def test__len_members(self):
		self.team.members = self.NON_EMPTY_MEMBERS
		self.assertEqual(3, len(self.team))

	def test__add__with_members(self):
		t1 = self.team
		t1.members = self.NON_EMPTY_MEMBERS

		t2 = Team("teamtwo")
		t2.members = {
			'Pamela': 21,
			'Kristin': 45,
		}

		resulted_team = t1 + t2
		expected_new_team_name = f"{self.team.name}{t2.name}"
		expected_new_team_members = {
			'Ivan': 39,
			'Boyan': 45,
			'Chudomir': 33,
			'Pamela': 21,
			'Kristin': 45,
		}

		self.assertEqual(expected_new_team_name, resulted_team.name)
		self.assertDictEqual(expected_new_team_members, resulted_team.members)

	def test__add__with_members_two(self):
		t1 = self.team
		t1.members = {}

		t2 = Team("teamtwo")
		t2.members = {
			'Pamela': 21,
			'Kristin': 45,
		}

		resulted_team = t1 + t2
		expected_new_team_name = f"{self.team.name}{t2.name}"
		expected_new_team_members = {
			'Pamela': 21,
			'Kristin': 45,
		}

		self.assertEqual(expected_new_team_name, resulted_team.name)
		self.assertDictEqual(expected_new_team_members, resulted_team.members)

	def test__add__with_no_members(self):
		t1 = self.team
		t1.members = {}

		t2 = Team("teamtwo")
		t2.members = {}

		resulted_team = t1 + t2
		expected_new_team_name = f"{self.team.name}{t2.name}"
		expected_new_team_members = {}
		self.assertEqual(expected_new_team_name, resulted_team.name)
		self.assertDictEqual(expected_new_team_members, resulted_team.members)