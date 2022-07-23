

class Validator:

    @staticmethod
    def is_empty_or_whitespace(string: str, msg: str):
        if string.strip() == '':
            raise ValueError(msg)

    @staticmethod
    def is_zero_or_less(value: float, msg: str):
        if value <= 0:
            raise ValueError(msg)

    @staticmethod
    def raise_if_table_number_not_between_start_end(start, end, number, msg):
        if not (start <= number <= end):
            raise ValueError(msg)
