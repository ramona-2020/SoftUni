

class Validator:

    @staticmethod
    def raise_if_empty(value: str, error_msg: str):
        if value.strip() == "":
            raise ValueError(error_msg)
