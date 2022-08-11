

nice_kids = list()
naughty_kids = list()
not_found_kids = list()


def print_results_list(nice_kids, naughty_kids, not_found_kids):
    result = []
    if nice_kids:
        nice_str = f"Nice: {', '.join(kid for kid in nice_kids)}"
        result.append(nice_str)

    if naughty_kids:
        naughty_str = f"Naughty: {', '.join(kid for kid in naughty_kids)}"
        result.append(naughty_str)

    if not_found_kids:
        not_found_str = f"Not found: {', '.join(kid for kid in not_found_kids)}"
        result.append(not_found_str)

    return '\n'.join(result)


def naughty_or_nice_list(*args, **kwargs):
    santa_list = args[0]
    command_args = args[1:]

    for command_pair in command_args:
        counter = 0
        current_name = None

        command_tokens = command_pair.split('-')
        counting_number = int(command_tokens[0])
        kid_type = command_tokens[1]
        for num, name in santa_list:
            if num == counting_number:
                counter += 1
                current_name = name

        if counter == 1:
            santa_list.remove((counting_number, current_name))

            if kid_type == 'Nice':
                nice_kids.append(current_name)
            else:
                naughty_kids.append(current_name)

    if kwargs:
        for k_name, k_type in kwargs.items():
            counter = 0
            current_item = None

            for item in santa_list:
                santa_num, santa_name = item
                if santa_name == k_name:
                    counter += 1
                    current_item = item

            if counter == 1:
                santa_list.remove(current_item)

                if k_type == 'Nice':
                    nice_kids.append(k_name)
                else:
                    naughty_kids.append(k_name)

    if len(santa_list) > 0:
        for num, name in santa_list:
            not_found_kids.append(name)

    return print_results_list(nice_kids, naughty_kids, not_found_kids)
