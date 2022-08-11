

def shopping_cart(*args):
    my_dict = {"Soup": [],
               "Pizza": [],
               "Dessert": []}

    for arg in args:
        if arg == "Stop":
            break

        meal = arg[0]
        product = arg[1]

        if meal == "Soup":
            if product not in my_dict[meal] and len(my_dict[meal]) < 3:
                my_dict[meal].append(product)
        elif meal == "Pizza":
            if product not in my_dict[meal] and len(my_dict[meal]) < 4:
                my_dict[meal].append(product)
        elif meal == "Dessert":
            if product not in my_dict[meal] and len(my_dict[meal]) < 2:
                my_dict[meal].append(product)

    cart_values = [v for v in my_dict.values() if len(v) != 0]
    if len(cart_values) == 0:
        return "No products in the cart!"

    sorted_dict = sorted(my_dict.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    result = []
    for meal, products in sorted_dict:
        str = ""
        str += f"{meal}:\n"

        sorted_products = sorted(products)
        for product in sorted_products:
            str += f" - {product}\n"

        result.append(str)

    return "".join(result)



print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))