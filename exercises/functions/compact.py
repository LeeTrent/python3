# def compact(list):
# 	truthy = []
# 	for element in list:
# 		if element:
# 			truthy.append(element)
# 	return truthy


def compact(list):
	return [element for element in list if element]

print(compact([0,1,2,"",[], False, {}, None, "All done"])) # [1,2, "All done"]