import unittest

from project.team import Team


class TeamTests(unittest.TestCase):

    def test__init__basic(self):
        team = Team("Abc")
        self.assertEqual("Abc", team.name)
        self.assertEqual({}, team.members)

    def test__raises_value_error_for_invalid_name(self):
        team = Team("Abc")
        old_team_name = "Abc"

        with self.assertRaises(ValueError) as err:
            Team("14545")
        self.assertEqual("Team Name can contain only letters!", str(err.exception))
        self.assertEqual(old_team_name, team.name)

    def test__valid_name(self):
        team = Team("Abc")
        new_team_name = "Novo"
        team.name = new_team_name

        self.assertEqual(new_team_name, team.name)
        self.assertIsNotNone(team)

    def test__add_member__with_success(self):
        team_name_added = "gosho"
        team = Team("Abc")

        result = team.add_member(gosho=25)

        self.assertEqual("Successfully added: gosho", result)
        self.assertEqual({'gosho': 25}, team.members)
        self.assertEqual(1, len(team.members))
        self.assertIn(team_name_added, team.members)

        self.assertTrue("gosho" in team.members)
        self.assertEqual(25, team.members.get("gosho"))

    def test__add_member__not_added(self):
        team = Team("Abc")
        team.members = {'gosho': 25}

        result = team.add_member(gosho=25)
        self.assertEqual("Successfully added: ", result)    # not add again member with name 'gosho'

        self.assertEqual({'gosho': 25}, team.members)
        self.assertEqual(1, len(team.members))
        self.assertIn("gosho", team.members)
        self.assertTrue("gosho" in team.members)
        self.assertTrue(len(team.members) != 2)

    def test__remove_member_success(self):
        team = Team("Abc")
        team.members = {'gosho': 25, "name1": 14}
        result = team.remove_member('gosho')
        self.assertEqual(f"Member gosho removed", result)
        self.assertEqual({'name1': 14}, team.members)
        self.assertEqual(1, len(team.members))
        self.assertTrue("gosho" not in team.members)
        self.assertFalse("gosho" in team.members)
        self.assertTrue("name1" in team.members)

    def test__remove_member_not_exists(self):
        team = Team("Abc")
        team.members = {'pesho': 25}
        result = team.remove_member('gosho')
        self.assertEqual(f"Member with name gosho does not exist", result)
        self.assertEqual({'pesho': 25}, team.members)
        self.assertEqual(1, len(team.members))
        self.assertNotIn("gosho", team.members)

    def test__gt__first(self):
        team1 = Team("Abc")
        team1.members = {'pesho': 25}

        team2 = Team("Abc")

        self.assertTrue(team1 > team2)

        self.assertEqual({'pesho': 25}, team1.members)
        self.assertEqual({}, team2.members)

        self.assertEqual(1, len(team1.members))
        self.assertEqual(0, len(team2.members))

        self.assertTrue(team1 > team2)
        self.assertTrue(len(team1.members) > len(team2.members))
        self.assertEqual(True, team1 > team2)
        self.assertEqual(False, team1 < team2)

    def test__gt__other(self):
        team1 = Team("Abc")
        team2 = Team("Abc")
        team2.members = {'pesho': 25}

        self.assertFalse(team1 > team2)

        self.assertEqual({}, team1.members)
        self.assertEqual({'pesho': 25}, team2.members)

        self.assertEqual(0, len(team1.members))
        self.assertEqual(1, len(team2.members))

        self.assertTrue(team2 > team1)
        self.assertTrue(len(team2.members) > len(team1.members))
        self.assertEqual(True, team2 > team1)
        self.assertEqual(False, team2 < team1)

    def test__len__with_no_members(self):
        team = Team("Abc")
        team.members = {}

        self.assertEqual({}, team.members)
        self.assertEqual(0, len(team.members))
        self.assertEqual(0, len(team))

    def test__len__with_members(self):
        team = Team("Abc")
        team.members = {'pesho': 25, 'gosho': 4}

        self.assertEqual({'pesho': 25, 'gosho': 4}, team.members)
        self.assertEqual(2, len(team.members))
        self.assertEqual(2, len(team))
        self.assertTrue('pesho' in team.members)
        self.assertEqual(25, team.members['pesho'])

    def test__add__without_members(self):
        team1 = Team("One")
        team2 = Team("Two")

        team_new = team1 + team2
        team_new_name = "OneTwo"
        team_new.members = {}

        self.assertEqual(team_new_name, team_new.name)
        self.assertEqual({}, team1.members)
        self.assertEqual({}, team2.members)
        self.assertEqual({}, team_new.members)
        self.assertEqual(0, len(team1.members))
        self.assertEqual(0, len(team2.members))
        self.assertEqual(0, len(team_new))

    def test__add__with_members(self):
        team1 = Team("One")
        team1.members = {'pesho': 25, 'gosho': 4}

        team2 = Team("Two")
        team2.members = {'stef': 1, 'ani': 7}

        team_new = team1 + team2
        team_new_name = "OneTwo"

        self.assertEqual(team_new_name, team_new.name)

        self.assertEqual({'pesho': 25, 'gosho': 4}, team1.members)
        self.assertEqual({'stef': 1, 'ani': 7}, team2.members)
        self.assertEqual({'pesho': 25, 'gosho': 4, 'stef': 1, 'ani': 7}, team_new.members)

        self.assertEqual(2, len(team1))
        self.assertEqual(2, len(team2))
        self.assertEqual(4, len(team_new))

        self.assertTrue("pesho" in team1.members)
        self.assertTrue("stef" in team2.members)
        self.assertTrue("pesho" in team_new.members)
        self.assertTrue("stef" in team_new.members)

    def test__str__(self):
        team1 = Team("One")
        team1.members = {'pesho': 25, 'gosho': 4, 'stef': 1, 'ani': 7}

        result = "Team name: One\n"
        result += "Member: pesho - 25-years old\n"
        result += "Member: ani - 7-years old\n"
        result += "Member: gosho - 4-years old\n"
        result += "Member: stef - 1-years old"

        self.assertEqual(result, str(team1))
