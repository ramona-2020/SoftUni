from project.player import Player
from project.supply.supply import Supply


class Controller:

    def __init__(self):
        self.players = []
        self.supplies = []

    def add_player(self, *players: Player):
        result = "Successfully added: "

        successfully_added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                successfully_added_players.append(player.name)

        result += ", ".join(successfully_added_players)

        return result

    def add_supply(self, *supplies: Supply):
        # A supply could be added multiple times
        self.supplies.extend(supplies)

    def sustain(self, player_name: str, sustenance_type: str):
        # check allowed sustain types:
        if sustenance_type not in ["Food", "Drink"]:
            return

        # If the player is not in the players list,
        check_fro_player_obj = self.get_player_by_name(player_name)
        if check_fro_player_obj is None:
            return

        player = self.get_player_by_name(player_name)
        if not player.need_sustenance:
            return f"{player_name} have enough stamina."

        if sustenance_type == "Food" and not any([s for s in self.supplies if s.supply_type == "Food"]):
            raise Exception("There are no food supplies left!")
        if sustenance_type == "Drink" and not any([s for s in self.supplies if s.supply_type == "Drink"]):
            raise Exception("There are no drink supplies left!")

        for index in range(len(self.supplies) - 1, -1, -1):
            supply = self.supplies[index]

            if supply.supply_type == sustenance_type:
                # increase his stamina with the supply's energy value
                player.increase_stamina(supply.energy)

                # remove the supply from the list
                self.supplies.remove(supply)
                return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.get_player_by_name(first_player_name)
        second_player = self.get_player_by_name(second_player_name)
        players_list = [first_player, second_player]

        # players does not have enough stamina and STOP DUEL
        result = ""
        for player in players_list:
            if player.stamina == 0:
                result += f"Player {player.name} does not have enough stamina." + "\n"
        if result:
            return result.strip()

        #  The two players participate in a duel, each of them could only attack once.
        # who attacks first
        attacker = self.get_attacker(first_player, second_player)  # ok
        if attacker == first_player:
            enemy = second_player
        else:
            enemy = first_player


        duels_counter = 0
        while duels_counter < 2:
            duels_counter += 1
            # He reduces the other player's stamina by a value equal to one-half
            # of his own (the attacker's) stamina.
            result = attacker.take_damage(enemy)
            if result:
                return result

            attacker, enemy = enemy, attacker


        # after 2 duels from attacker and enemy are still alive
        # Otherwise, the winner is the player who has left with more stamina !!!
        if attacker.stamina > enemy.stamina:
            return f"Winner: {attacker.name}"
        else:
            return f"Winner: {enemy.name}"

    def next_day(self):
        # First, the stamina of each added player gets reduced by the result of multiplying their age by 2
        for player in self.players:
            reduced_value = player.age * 2
        # If a player's stamina becomes less than 0, it should be set to 0
            if player.stamina - reduced_value < 0:
                player.stamina = 0
            else:
                player.stamina -= reduced_value
            # Then, you need to sustain each player by giving them one food (first) and one drink (second)
            # player_name: str, sustenance_type: st
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def get_player_by_name(self, player_name: str) -> Player or None:
        for player in self.players:
            if player.name == player_name:
                return player
        return None

    def get_supply_by_name(self, supply_name: str) -> Supply or None:
        for supply in self.supplies:
            if supply.name == supply_name:
                return supply
        return None

    def get_supplies_by_type(self, supply_type: str):
        return [supply for supply in self.supplies if supply.supply_type == supply_type]

    def remove_supply_from_supplies_list(self, supply: Supply):
        self.supplies.remove(supply)

    def remove_last_supply_for_supply_type(self, supply_type: str):
        supplies_list = [supply for supply in self.supplies if supply.supply_type == supply_type]
        supplies_list.pop()
        return True

    @staticmethod
    def get_attacker(first_player: Player, second_player: Player) -> Player:
        if first_player.stamina < second_player.stamina:
            return first_player
        return second_player

    def __str__(self):
        result = ""
        for player in self.players:
            result += str(player) + "\n"

        for suppy in self.supplies:
            result += suppy.details() + "\n"

        return result.strip()
