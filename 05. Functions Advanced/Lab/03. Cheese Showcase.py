
def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
    result_sorted = ""

    for name, cheeses_list in sorted_cheeses:
        sorted_cheeses_list = sorted(cheeses_list, reverse=True)

        result_sorted += name + "\n"
        for cheese in sorted_cheeses_list:
            result_sorted += str(cheese) + "\n"

    return result_sorted