from collections import deque

readline = "10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *".split(' ')
my_line = deque(n for n in readline)

my_list_chars = []

while my_line:
	current_char = my_line.popleft()
	if current_char not in ["*", "+", "-", "/"]:
		my_list_chars.append(int(current_char))
	else:
		my_vals = my_list_chars
		result = my_vals[0]

		if current_char == "*":
			for val in my_vals[1:]:
				result *= val
		elif current_char == "+":
			for val in my_vals[1:]:
				result += val
		elif current_char == "-":
			for val in my_vals[1:]:
				result -= val
		elif current_char == "/":
			for val in my_vals[1:]:
				result //= val

		my_list_chars = [result]


print(my_list_chars[0])