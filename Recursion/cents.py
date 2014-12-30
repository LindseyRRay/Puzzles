#Q: Given an infinie number of quarters, dimes, nickels, pennies, calculate number of ways to represent n cents 
from collections import defaultdict

def calculate_change(cents):
	if cents < 0:
		return 0
	elif cents == 0:
		return 1
	elif cents >=25:
		return calculate_change(cents-25) + \
		calculate_change(cents-10) + \
		calculate_change(cents-5) + \
		calculate_change(cents-1)
	elif cents >= 10:
		return calculate_change(cents-10) + \
		calculate_change(cents-5) +\
		calculate_change(cents-1)
	elif cents >=5:
		return calculate_change(cents-5) + \
		calculate_change(cents-1)
	else:
		return calculate_change(cents-1)

def main():
	ways = calculate_change(50)
	print(ways)


main()
