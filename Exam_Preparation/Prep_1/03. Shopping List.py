def shopping_list(budget, **kwargs):
    my_cart = set()
    products = []

    if budget < 100:
        return "You do not have enough budget."

    for product_name, values in kwargs.items():
        if len(my_cart) == 5:
            break

        price, quantity = values
        product_total_price = price * quantity
        if budget >= product_total_price:
            my_cart.add(product_name)
            products.append(f"You bought {product_name} for {product_total_price:.2f} leva.")

    return "\n".join(products)



print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))