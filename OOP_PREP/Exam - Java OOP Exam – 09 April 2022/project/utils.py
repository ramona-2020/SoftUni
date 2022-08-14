

class Utilities:

    @staticmethod
    def empty_value_raise_value_error(value, error_msg):
        if not value or value.strip() == '':
            raise ValueError(error_msg)

    @staticmethod
    def negative_value_raise_value_error(value, error_msg):
        if value < 0:
            raise ValueError(error_msg)

    @staticmethod
    def negative_or_zero_value_raise_value_error(value, error_msg):
        if value <= 0:
            raise ValueError(error_msg)

    @staticmethod
    def find_object_by_name(searched_name: str, collection: list):
        for item in collection:
            if item.name == searched_name:
                return item
        return None

