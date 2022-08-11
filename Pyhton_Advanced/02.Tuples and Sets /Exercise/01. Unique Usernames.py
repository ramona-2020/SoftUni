n = int(input())
unique_usernames = set()

for _ in range(n):
	username = input()
	unique_usernames.add(username)

# Prints result:
print("\n".join([str(el) for el in unique_usernames]))