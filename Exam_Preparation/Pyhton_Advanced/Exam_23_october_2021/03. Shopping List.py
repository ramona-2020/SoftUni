

def shopping_list(*args, **kwargs):
    cart_items = kwargs.copy()
    basket = {}

    results = []

    if len(args) >= 1:
        money_amount = args[0]
        if money_amount < 100:
            return "You do not have enough budget."

        for product_name, data in cart_items.items():
            current_amount = data[0] * data[1]
            if money_amount >= current_amount:
                money_amount -= current_amount
                basket.update({product_name: current_amount})

                results.append(f"You bought {product_name} for {current_amount:.2f} leva.")

            kwargs.pop(product_name)
            if len(kwargs) == 0 or len(basket) == 5:
                break

        return "\n".join(results)

# Test Code:
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