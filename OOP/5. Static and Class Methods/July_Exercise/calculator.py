

class Calculator:

    @staticmethod
    def add(*args):
        result = sum([val for val in args])
        return result

    @staticmethod
    def multiply(*args):
        result = 1
        for val in args:
            result *= val
        return result

    @staticmethod
    def divide(*args):
        result = args[0]
        for val in args[1:]:
            result /= val
        return result

    @staticmethod
    def subtract(*args):
        result = args[0]
        for val in args[1:]:
            result -= val
        return result


# can be called without instantiating the class.
print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
