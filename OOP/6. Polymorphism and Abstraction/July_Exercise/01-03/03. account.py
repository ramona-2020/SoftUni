

class Account:

    def __init__(self, owner: str, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    # a property that returns the sum between the amount and all the transactions
    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        new_balance = account.balance + amount_to_add
        if new_balance < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {new_balance}"

    # Magic methods
    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __reversed__(self):
        return reversed(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, ids):
        return self._transactions[ids]

    # "{first_owner}&{second_owner}"
    def __add__(self, other):
        new_owner = f"{self.owner}&{other.owner}"
        new_amount = self.amount + other.amount
        new_account = Account(new_owner, new_amount)

        new_account._transactions = self._transactions + other._transactions
        return new_account

    # compare instances by account balance
    def __gt__(self, other):
        inst1 = self.balance
        inst2 = other.balance
        return inst1 > inst2

    def __ge__(self, other):
        inst1 = self.balance
        inst2 = other.balance
        return inst1 >= inst2

    def __eq__(self, other):
        inst1 = self.balance
        inst2 = other.balance
        return inst1 == inst2


a = Account("JOHN", 144)
print(a.amount)