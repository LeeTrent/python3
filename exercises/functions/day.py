days_of_week = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}

def return_day(nbr):
	if nbr < 1 or nbr > 7:
		return None
	return days_of_week.get(nbr)

print(return_day(1)) # "Sunday"
print(return_day(2)) # "Monday"
print(return_day(3)) # "Tuesday"
print(return_day(4)) # "Wednesday"
print(return_day(5)) # "Thursday"
print(return_day(6)) # "Friday"
print(return_day(7)) # "Saturday"
print(return_day(41)) # None