def isEven(num):
    return num % 2 == 0

# def partition(list, callback):
# 	truthy = []
# 	falsy = []
# 	for element in list:
# 		if callback(element):
# 			truthy.append(element)
# 		else:
# 			falsy.append(element)
# 	return [truthy, falsy]

def partition(lst, fn):
	return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]	

print(partition([1,2,3,4], isEven)) # [[2,4],[1,3]]
