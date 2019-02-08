# def is_palindrome(val):
# 	forward = val.strip().upper()
# 	backward = val.strip().upper()[::-1]
# 	return forward == backward

def is_palindrome(val):
	return val.strip().upper() == val.strip().upper()[::-1]

print(is_palindrome('testing')) # False
print(is_palindrome('tacocat')) # True
print(is_palindrome('hannah')) # True
print(is_palindrome('robert')) # False
print(is_palindrome('amanaplanacanalpanama')) # True