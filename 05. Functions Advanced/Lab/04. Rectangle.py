

def rectangle(length, width):
	result = ""

	if type(length) != int or type(width) != int:
		return "Enter valid values!"

	def area(result):
		result += f"Rectangle area: {length * width}\n"
		return result

	def perimeter(result):
		result += f"Rectangle perimeter: {(length + width) * 2}"
		return result

	result = area(result)
	result = perimeter(result)
	return result


# Test code
print(rectangle(2, 10))
