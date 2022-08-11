from collections import deque

vowels = deque(input().split(' '))
consonants = list(input().split(' '))

words_found = []

words_dict = {
	"pear": list("pear"),
	"flour": list("flour"),
	"pork": list("pork"),
	"olive": list("olive"),
}

while consonants:
	c_vowel = vowels.popleft()
	c_consonant = consonants.pop()

	for word, chars in words_dict.items():
		while c_vowel in chars:
			chars.remove(c_vowel)

		while c_consonant in chars:
			chars.remove(c_consonant)

	vowels.append(c_vowel)

for word, chars in words_dict.items():
	if not chars:
		words_found.append(word)

# Prints result:
print(f"Words found: {len(words_found)}")
for word in words_found:
	print(word)