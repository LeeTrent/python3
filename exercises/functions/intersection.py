def intersection(list1, list2):
	return [element for element in list1 if element in list2]


# Driver Code 
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69] 
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26] 
print(intersection(lst1, lst2))