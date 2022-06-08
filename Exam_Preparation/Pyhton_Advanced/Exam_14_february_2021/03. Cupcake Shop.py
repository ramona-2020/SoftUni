

def stock_availability(*args):
	stock_list = args[0]
	if args[1] == "delivery":
		if len(args) > 2:
			delivery_list = list(args[2:])
			stock_list += delivery_list
	else:
		if len(args) == 2:
			stock_list = stock_list[1:]
		elif str(args[2]).isdigit():
			boxes_number = args[2]
			stock_list = stock_list[boxes_number:]
		else:
			ordered_flavours = list(args[2:])
			for flavour in ordered_flavours:
				while flavour in stock_list:
					stock_list.remove(flavour)

	return stock_list

# Test Code
# print(stock_availability(["choco", "vanilla", "banana"], "delivery"))
# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))