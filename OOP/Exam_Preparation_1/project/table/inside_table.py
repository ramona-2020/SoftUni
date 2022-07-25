from project_01_02.table.table import Table


class InsideTable(Table):

    MIN_NUMBER = 1
    MAX_NUMBER = 50

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)