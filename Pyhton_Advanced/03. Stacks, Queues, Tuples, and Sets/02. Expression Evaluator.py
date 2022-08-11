from collections import deque
chars = deque(input().split())
expression = deque()
result = 0
# 6 3 1 - 2 1 * 5 /
# [6, 3]

for i in range(len(chars)):
	element = chars[i]

	if element in "+-*/":
		while len(expression) > 1:
			left = expression.popleft()
			right = expression.popleft()
			if element == '-':
				result = left - right
			elif element == '+':
				result = left + right
			elif element == '*':
				result = left * right
			elif element == '/':
				result = left // right

			expression.appendleft(result)
	else:
		expression.append(int(element))

print(expression.popleft())