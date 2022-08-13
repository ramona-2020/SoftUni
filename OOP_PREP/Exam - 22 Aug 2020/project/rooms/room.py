

class Room:

    ROOM_COST = 0
    MEMBERS_COUNT = 0

    APPLIANCES = []

    def __init__(self, family_name: str, budget: float, members_count: int):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.expenses = 0

        self.room_cost = self.ROOM_COST

        self.children = []
        self.appliances = self.APPLIANCES * members_count

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        self.expenses = Room._calculate_expenses(*args)

    @staticmethod
    def _calculate_expenses(*args) -> float:
        # args are Appliances list or children list
        total_expense = 0
        for arg in args:
            # arg is appliance list  or child list
            for item in arg:
                total_expense += item.get_monthly_expense()

        return total_expense

    def __str__(self):
        room_monthly_cost = self.expenses + self.ROOM_COST
        family_budget = self.budget
        budget_left = family_budget - room_monthly_cost
        return f"{self.family_name} with {self.members_count} members. Budget: {budget_left:.2f}$, Expenses: {self.expenses:.2f}$"