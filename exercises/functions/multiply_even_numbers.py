def multiply_even_numbers(num_list):
	product = 1
	for num in num_list:
		if num % 2 == 0:
			product *= num
	return product

# def multiply_even_numbers(nbr_list):
# 	product = 1
# 	return product *= nbr for nbr in nbr_list if nbr % 2 == 0

print(multiply_even_numbers([2,3,4,5,6])) # 48

