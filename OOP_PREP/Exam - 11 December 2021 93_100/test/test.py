from unittest import TestCase

from project.team import Team


class TeamTests(TestCase):

    def test__init__basic(self):
        name = "TeamName"
        team = Team(name)
        self.assertEqual("TeamName", team.name)
        self.assertEqual({}, team.members)

    def test__init__advanced(self):
        name = "TeamName"
        members = {
            "name1": 4,
            "name2": 5
        }
        team = Team(name)
        team.members = members
        self.assertEqual("TeamName", team.name)
        self.assertEqual({"name1": 4, "name2": 5}, team.members)

    def test__name_raises_value_error_for_invalid_name(self):
        expected = "Team Name can contain only letters!"
        name = "1"

        with self.assertRaises(ValueError) as err:
            team = Team(name)

        self.assertEqual(expected, str(err.exception))

    def test__add_member__with_success(self):
        team = Team("TeamName")
        team.members = {"member3": 16}

        actual = team.add_member(member1=4, member2=5, member3=16)
        expected = f"Successfully added: member1, member2"
        self.assertEqual(expected, actual)
        self.assertDictEqual({"member3": 16, "member1": 4, "member2": 5}, team.members)
        self.assertEqual(3, len(team.members))
        self.assertTrue("member1" in team.members)
        self.assertTrue("member2" in team.members)
        self.assertEqual(4, team.members.get("member1"))
        self.assertEqual(5, team.members.get("member2"))

    def test__add_member__with_no_success(self):
        name = "TeamName"
        team = Team(name)
        team.members = {"member1": 4, "member2": 5}

        team.add_member(member1=4)
        self.assertDictEqual({"member1": 4, "member2": 5}, team.members)
        self.assertEqual(2, len(team.members))
        self.assertTrue("member1" in team.members)
        self.assertEqual(4, team.members.get("member1"))

    def test__remove_member_without_success(self):
        name = "TeamName"
        member1 = "name1"
        team = Team(name)

        result = team.remove_member(member1)
        expected = f"Member with name name1 does not exist"
        self.assertEqual(expected, result)
        self.assertEqual({}, team.members)
        self.assertEqual(0, len(team.members))
        self.assertTrue("name1" not in team.members)
        self.assertFalse("name1" in team.members)

    def test__remove_member_success(self):
        name = "TeamName"
        member1 = "member1"
        team = Team(name)
        team.members = {"member1": 4, "member2": 5}

        result = team.remove_member(member1)
        expected = f"Member member1 removed"
        self.assertEqual(expected, result)
        self.assertEqual({"member2": 5}, team.members)
        self.assertEqual(1, len(team.members))
        self.assertTrue("member2" in team.members)
        self.assertEqual(5, team.members.get("member2"))
        self.assertTrue("member1" not in team.members)

    def test__gt__with_first(self):
        team1 = Team("teamA")
        team1.members = {"member1": 4, "member2": 5}

        team2 = Team("teamB")
        team2.members = {}

        self.assertTrue(team1 > team2)
        self.assertTrue(len(team1.members) > len(team2.members))
        self.assertEqual(True, team1 > team2)
        self.assertEqual(False, team1 < team2)

    def test__gt__with_assert_true(self):
        team1 = Team("teamA")
        team1.members = {"member1": 4, "member2": 5}

        team2 = Team("teamB")
        team2.members = {}

        self.assertTrue(team1 > team2)

    def test__gt__with_assert_false(self):
        team1 = Team("teamA")
        team1.members = {"member1": 4, "member2": 5}

        team2 = Team("teamB")
        team2.members = {}

        self.assertFalse(team2 > team1)

    def test__len__(self):
        team = Team("teamB")
        team.members = {"member1": 4, "member2": 5}

        self.assertEqual({"member1": 4, "member2": 5}, team.members)
        self.assertEqual(2, len(team.members))
        self.assertEqual(2, len(team))

    def test__add__without_members(self):
        team1 = Team("teamA")
        team2 = Team("teamB")

        team_result = team1 + team2
        new_team_name = "teamAteamB"
        self.assertEqual(new_team_name, team_result.name)
        self.assertEqual({}, team1.members)
        self.assertEqual({}, team2.members)
        self.assertEqual({}, team_result.members)
        self.assertEqual(0, len(team1.members))

    def test__add__with_members_with_no_duplicates_advanced(self):
        team1 = Team("teamA")
        team1.members = {"member1": 4, "member2": 5}

        team2 = Team("teamB")
        team2.members = {"member3": 6, "member4": 7}

        team_result = team1 + team2
        new_team_name = "teamAteamB"
        self.assertEqual(new_team_name, team_result.name)
        self.assertDictEqual({"member1": 4, "member2": 5, "member3": 6, "member4": 7}, team_result.members)
        self.assertEqual(4, len(team_result.members))
        self.assertTrue("member1" in team_result.members)
        self.assertTrue("member3" in team_result.members)

    def test__str__with_no_members(self):
        team1 = Team("teamA")

        result = f"Team name: teamA"

        self.assertEqual(result, str(team1))

    def test__str__basic(self):
        team1 = Team("teamA")
        team1.members = {"member1": 4, "member2": 5}

        result = f"Team name: teamA\n"
        result += f"Member: member2 - 5-years old\n"
        result += f"Member: member1 - 4-years old"

        self.assertEqual(result, str(team1))

    def test__str__advanced(self):
        team1 = Team("teamA")
        team1.members = {"member1": 4, "betty": 5, "alan": 5}

        result = f"Team name: teamA\n"
        result += f"Member: alan - 5-years old\n"
        result += f"Member: betty - 5-years old\n"
        result += f"Member: member1 - 4-years old"

        self.assertEqual(result, str(team1))

