#Q What century is it?
# Return the inputted numerical year in century format.
#  For example 2014, would return 21st.

# The input will always be a 4 digit string. 

# Examples:
# Input: 1999 Output: 20th
# Input: 2011 Output: 21st

def get_cent(century):
	return int(century[:2])+1

def get_suffix(last_digit):
	if last_digit == 1:
		return "st"
	elif last_digit == 2:
		return "nd"
	elif last_digit == 3:
		return "rd"
	else:
		return "th"
def calc_century(datestring):
	cent = get_cent(datestring)
	suff = get_suffix((cent%10))
	return str(cent)+suff

if __name__ == '__main__':
	print(calc_century("2011"))