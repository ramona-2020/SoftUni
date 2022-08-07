

class Validator:

    @staticmethod
    def is_model_name_valid(model: str, msg: str):
        if len(model) < 4:
            raise ValueError(msg)

    @staticmethod
    def is_name_valid(name: str, msg: str):
        if name.strip() == "":
            raise ValueError(msg)

    @staticmethod
    def is_speed_limit_between_min_and_man(min_value: int, max_value: int, value: int, msg: str):
        if not (min_value <= value <= max_value):
            raise ValueError(msg)

