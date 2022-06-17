

def get_repeating_DNA(dna_sequence):
	my_list = []

	if len(dna_sequence) == 10:
		return f"['{dna_sequence}']"
	else:
		while dna_sequence:
			current_part = dna_sequence[:10:]

			is_found = dna_sequence.find(current_part, 10)
			if is_found != -1:
				my_list.append(current_part)
			dna_sequence = dna_sequence.replace(current_part, '')
		return my_list



# Test Code:
test = "1234567891AAAAAACCCCAAAAAACCCCTTCAAAATCTTTCAAAATCT"
result = get_repeating_DNA(test)
print(result)