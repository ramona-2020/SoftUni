from collections import deque

vowels = deque(v for v in input().split())
consonants = input().split()

is_found_word = False
found_word = ''

words_dict = {
	"rose": list("rose"),
	"tulip": list("tulip"),
	"lotus": list("lotus"),
	"daffodil": list("daffodil"),
}

while vowels and consonants:
	if is_found_word:
		break

	v = vowels.popleft()
	c = consonants.pop()

	for word, chars in words_dict.items():
		if v in chars:
			while v in chars:
				chars.remove(v)
		if c in chars:
			while c in chars:
				chars.remove(c)

		if len(chars) == 0:
			is_found_word = True
			found_word = word
			break

# Prints result:
if is_found_word:
	print(f"Word found: {found_word}")
else:
	print("Cannot find any word!")


if vowels:
	print(f"Vowels left: {' '.join(vowels)}")
if consonants:
	print(f"Consonants left: {' '.join(consonants)}")