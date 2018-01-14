#
# Cameron Hawtin
# 101047338
# 
# Gaddis, T. (2015). "Starting Out With Python"
#
# This program contains two recursive functions that produce 
# values from a specific sequence of integer values.
#
# The unique recursive sequence assigned is:
# f(0) = 6
# f(1) = 3
# f(2) = 3
# f(3) = 4
# f(4) = 0
# f(5) = 9
# f(n) = f(n-2) - f(n-6) when 5 < n < 12
# f(n) = f(n-1) + ( f(n-4) * f(n-4) ) when 12 <= n
#

num = int(input("Enter a number: "))

# This function takes an integer argument and recursively returns a specific value
def recurse(n):
	list = [6, 3, 3, 4, 0, 9]
	if n >= 0 and n <= 5:
		return list[n] 
	elif n > 5 and n < 12:
		return recurse(n-2) - recurse(n-6)
	elif n >= 12:
		return recurse(n-1) + (recurse(n-4) * recurse(n-4))

# This function takes an integer argument and recursively returns a specfic list of values
def recurseList(n):
	list = [6, 3, 3, 4, 0, 9]
	if n <= 5:
		return list[:n+1]
	elif n > 5 and n < 12:
		while n > 5:
			list.insert(6, recurse(n-2) - recurse(n-6))
			n -= 1
		return list
	elif n >= 12:
		x = n
		for i in range(11, 5, -1):
			list.insert(6, recurse(i-2) - recurse(i-6))
		while n >= 12:
			list.insert(12, recurse(n-1) + (recurse(n-4) * recurse(n-4)))
			n -= 1
		return list
		
print("The first function produces: ", recurse(num))		
print("The second function produces: ", recurseList(num))
input()