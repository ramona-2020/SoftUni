

class Player:

    names = set()

    MIN_AGE = 12

    def __init__(self, name: str, age: int, stamina=100):
        self.name = name
        self.age = age
        self.stamina = stamina

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value in Player.names:
            raise Exception(f"Name {value} is already used!")

        if not value or value.strip() == "":
            raise ValueError("Name not valid!")

        Player.names.add(value)
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < Player.MIN_AGE:
            raise ValueError(f"The player cannot be under {Player.MIN_AGE} years old!")
        self._age = value

    @property
    def stamina(self):
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Stamina not valid!")
        self._stamina = value

    @property
    def need_sustenance(self):
        return self.stamina < 100

    def increase_stamina(self, value):
        if self.stamina + value > 100:
            self.stamina = 100
        else:
            self.stamina += value

    def take_damage(self, enemy):
        # He reduces the other player's stamina by a value equal to one-half of his own (the attacker's) stamina.
        reduced_value = self.stamina / 2

        winner = None
        if self.stamina <= 0:
            # The player immediately loses the duel, and the other player becomes a winner.
            self.stamina = 0
            winner = enemy

        elif enemy.stamina - reduced_value <= 0:
            enemy.stamina = 0
            winner = self
        else:
            enemy.stamina -= reduced_value

        if winner is not None:
            return f"Winner: {winner.name}"

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"

