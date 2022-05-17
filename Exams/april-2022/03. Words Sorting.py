

def words_sorting(*args):
    result = []

    my_dict = dict()
    my_dict_sum = 0


    def ascii_sum(word):
        ascii_suma = 0
        for letter in word:
            ascii_value = ord(letter)
            ascii_suma += ascii_value

        return ascii_suma

    for word in args:
        ascii_suma = ascii_sum(word)
        my_dict_sum += ascii_suma
        my_dict.update({word: ascii_suma})

    if my_dict_sum % 2 == 0:
        my_dict = sorted(my_dict.items(), key=lambda kvpt: kvpt[0])
    else:
        my_dict = sorted(my_dict.items(), key=lambda kvpt: -kvpt[1])

    for key, value in my_dict:
        result.append(f"{key} - {value}")

    return "\n".join(result)


# Test Code
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))