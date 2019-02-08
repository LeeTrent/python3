# def multiple_letter_count(str):
# 	return {letter : str.count(letter) for letter in str}

def multiple_letter_count(str):
	return {letter : str.count(letter) for letter in sorted(str)} 

print(multiple_letter_count("awesome"))
