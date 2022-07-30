
def vowel_filter(function):
	def wrapper():
		result = function()  # return ["a", "b", "c", "d", "e"]
		vowels = [a for a in result if a in ["a", "e", "i", "o", "u"]]
		return vowels

	return wrapper


# test code
@vowel_filter
def get_letters():
	return ["a", "b", "c", "d", "e"]

# expected
# ["a", "e"]
print(get_letters())