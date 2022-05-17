

def func_executor(func1, func2):
    list_result = []
    func1_tuple = func1[1]
    func2_tuple = func2[1]

    sum1_result = sum_numbers(*func1_tuple)
    prod_result = multiply_numbers(*func2_tuple)

    list_result.append(sum1_result)
    list_result.append(prod_result)

    return list_result


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor((sum_numbers, (10, 2)), (multiply_numbers, (2, 4))))