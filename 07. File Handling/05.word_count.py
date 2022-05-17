import os

# word
absolute_path = os.path.dirname(os.path.abspath(__file__))
word_file_path = os.path.join(absolute_path, "custom_files", "words.txt")
word_file_obj = open(word_file_path)

text_file_path = os.path.join(absolute_path, "custom_files", "input.txt")
text_file_obj = open(text_file_path)

output_file_path = os.path.join(absolute_path, "custom_files", "output.txt")
output_file_obj = open(output_file_path, 'a')

word_list = word_file_obj.readlines()[0].split()
dict_counter = dict()

for line in text_file_obj:
	for word in word_list:
		if word in line.lower():
			if word not in dict_counter:
				dict_counter[word] = 1
			else:
				dict_counter[word] += 1

sort_word_dict = sorted(dict_counter.items(), key=lambda kvpt: -kvpt[1])
sorted_words = []

for word, count in sort_word_dict:
	result = f"{word} - {count}"
	sorted_words.append(result)

for pair in sorted_words:
	output_file_obj.writelines(pair + "\n")