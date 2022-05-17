
# I Love Python
# -> nohtyP evoL I
input_line = input()

s = []
for ch in input_line:
	s.append(ch)

reversed_string = ""
while s:
	reversed_string += s.pop()

print(reversed_string)
