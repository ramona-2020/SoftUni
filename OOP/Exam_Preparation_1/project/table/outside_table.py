from project.table.table import Table


class OutsideTable(Table):

    MIN_NUMBER = 51
    MAX_NUMBER = 100

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

