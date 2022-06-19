from collections import deque

meals = deque(input().split(' '))
day_calories = [int(d) for d in input().split(' ')]

number_of_meals = len(meals)


def get_meal_calories(meal):
	meal_dict = {
		"salad": 350,
		"soup": 490,
		"pasta": 680,
		"steak": 790
	}

	return meal_dict.get(meal)


while meals and day_calories:
	current_meal = meals[0]
	current_day_calories = day_calories[-1]

	meal_calories = get_meal_calories(current_meal)
	day_calories[-1] -= meal_calories

	# remove current meal
	meals.popleft()

	if day_calories[-1] == 0:
		day_calories.pop()
	elif day_calories[-1] < 0:
		if len(day_calories) >= 2:
			day_calories[-2] += day_calories[-1]
		day_calories.pop()


# Prints result:
# line 1:
if not meals:
	print(f"John had {number_of_meals} meals.")
	print(f"For the next few days, he can eat {', '.join(str(c) for c in sorted(day_calories))}")
else:
	print(f"John ate enough, he had {number_of_meals - len(meals)} meals.")
	print(f"Meals left: {', '.join(str(c) for c in sorted(meals))}.")