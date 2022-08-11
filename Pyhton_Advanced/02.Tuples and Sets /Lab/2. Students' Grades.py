students_number = int(input())

student_dict = {}
for student in range(students_number):
	name, score = input().split()
	score = float(score)
	if name not in student_dict:
		student_dict[name] = []
	student_dict[name].append(score)

# Prints students dict:
for name, scores in student_dict.items():
	# Mark -> 5.50 2.50 3.46 (avg: 3.82)
	average_grade = sum(scores) / len(scores)
	print(f"{name} -> {' '.join([f'{score:.2f}' for score in scores])} (avg: {average_grade:.2f})")