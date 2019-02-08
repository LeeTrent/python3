def single_letter_count(s1,s2):
	return s1.upper().count(s2.upper())

print(single_letter_count("Hello World", "h")) # 1
print(single_letter_count("Hello World", "z")) # 0
print(single_letter_count("HelLo World", "l")) # 3
