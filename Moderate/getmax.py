#Question: Get max without using any comparison operators
#We need to use bit shifting
# Quick Review of Bitshifting in Python
# x<<y -> bit shifts x to the left by y places (same as x*2^y) converse is true for x>>y
# x&y - each bit of output is 1 if x and y is 1, else 0
# x|y- if x and y 0, returns 0, else 1
# ~x - compelement of x, (switching 1 to 0s and 0s to 1) (same as -x-1)
# x ^y - same as bit in x if y is 0, complement of x if y is 1
from random import randint

def get_max(number1, number2):
	list_nums = [number1, number2]
	return list_nums[(number1 - number2)>>31]


def main():
	for i in range(10):
		nums = [randint(0,100) for i in range(2)]
		assert get_max(*nums) == max(nums)

main()