

def travel_time(*args):
	my_dict = {}
	town_found = False
	country_found = True

	for line in args:
		line_args = line.split(">")
		country = line_args[0].strip()
		town = line_args[1].strip()
		cost = int(line_args[2].strip())

		if country not in my_dict:
			my_dict[country] = {
				'town': town,
				"cost": cost,
			}

		for t, c in my_dict[country].items():
			if town == t:
				town_found = True
				if cost < c:
					my_dict[country]['cost'] = cost

		if country_found and not town_found:
			my_dict[country].update({
				'town': town,
				"cost": cost,
			})

		town_found = False
		country_found = False

	sorted_dict = sorted(my_dict.items(), key=lambda kv: {kv[0], kv[1]['cost']})
	print(sorted_dict)


travel_time("Bulgaria > Sofia > 500",
	"Bulgaria > Sopot > 800",
	"France > Paris > 2000",
	"Albania > Tirana > 1000",
	"Bulgaria > Sofia > 200")
