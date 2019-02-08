def last_element(list):
	if len(list) == 0:
		return None
	return list[-1]

print(last_element([1,2,3])) # 3
print(last_element([])) # None