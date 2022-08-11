
while True:
	try:
		text = input()
		times = int(input())
		print(text * times)
		break
	except ValueError:
		print("Variable times must be an integer")