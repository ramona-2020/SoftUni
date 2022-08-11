import os


def file_manipulator(line: str):
	command_tokens = line.split('-')
	command_name, file_name = command_tokens[0], command_tokens[1]
	filepath = f'./files_directory/{file_name}'

	if command_name == 'Create':
		with open(filepath, 'w') as file:
			pass
	elif command_name == 'Add':
		content = command_tokens[2]
		with open(filepath, 'a') as file:
			file.write(content + '\n')
	elif command_name == 'Replace':
		old_string = command_tokens[2]
		new_string = command_tokens[3]
		replacement = ""
		if not os.path.exists(filepath):
			print("An error occurred")
		else:
			with open(filepath, 'r') as file:
				for line in file:
					line = line.replace(old_string, new_string)
					replacement = replacement + line

			with open(filepath, 'w') as file:
				file.write(replacement)
	elif command_name == 'Delete':
		if not os.path.exists(filepath):
			print("An error occurred")
		else:
			os.remove(filepath)


# Test Code:
while True:
	command_line = input()
	if command_line == 'End':
		break

	file_manipulator(command_line)
