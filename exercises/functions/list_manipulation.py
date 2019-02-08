def list_manipulation(list, command, location, value=0):
	if command == "remove":
		if location == "end":
			return list.pop()
		if location == "beginning":
			return list.pop(0)
	if command == "add":
		if location == "beginning":
			list.insert(0, value)
			return list
		if location == "end":
			list.append(value)
			return list

print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]
