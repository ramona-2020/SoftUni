from project_test_task.table.inside_table import InsideTable
from project_test_task.table.outside_table import OutsideTable


class TableFactory:
    table_types = {
        "InsideTable": InsideTable,
        "OutsideTable": OutsideTable
    }

    @staticmethod
    def create_table(table_type, table_number, capacity):
        return TableFactory.table_types[table_type](table_number, capacity)
