#Q: find the maximum subarray in a problem - series of numbers that sum to greates
import random

def find_max(array, low, high):
	if high == low:
		return (low, high, array[low])
	else:
		mid = int((low+high)/2)
		left_low, left_high, left_sum = find_max(array, low, mid)
		right_low, right_high, right_sum = find_max(array, mid+1, high)
		cross_low, cross_high, cross_sum = find_max_crossing(array, low, high, mid)
		if left_sum >= right_sum and left_sum >= cross_sum:
			return (left_low, left_high, left_sum)
		elif right_sum >= left_sum and right_sum >= cross_sum:
			return (right_low, right_high, right_sum)
		else:
			return (cross_low, cross_high, cross_sum)

def find_max_crossing(array, low, high, mid):
	left_sum = float("-inf")
	list_sum = 0
	index = mid
	while index >= low:
		list_sum = list_sum + array[index]
		if list_sum > left_sum:
			left_sum = list_sum
			max_left = index
		index -= 1
	right_sum = float("-inf")
	list_sum = 0
	index = mid + 1
	while index <= high:
		list_sum = list_sum + array[index]
		if list_sum > right_sum:
			right_sum = list_sum
			max_right = index
		index += 1
	return (max_left, max_right, left_sum + right_sum)

def check_max(array):
#Brute force method to check sums 
	array_sum = 0
	array_start = 0 
	array_end = 0
	for index, item in enumerate(array):
		list_sums = [(index, index, item)]
		current_sum = item
		start_index = index 
		max_index = index 
		for ind, next_item in enumerate(array[index+1:]):
			current_sum += next_item 
			list_sums.append((start_index, ind + index + 1, current_sum))
		list_sums.sort(key = lambda x: x[-1])
		if list_sums[-1][-1] >= array_sum:
			array_start, array_end, array_sum = list_sums[-1]
	return (array_start, array_end, array_sum)


def run_find_max(num_items):
	array = [random.randint(-500,500) for i in range(num_items)]
	algo_left, algo_right, algo_sum = find_max(array, 0, num_items-1)
	loop_left, loop_right, loop_sum = check_max(array)

	print(array)
	print ("algo sum is %s, start is %s, end is %s"%(algo_sum, algo_left, algo_right))
	print ("Loop sum is %s, start is %s, end is %s"%(loop_sum, loop_left, loop_right))
	assert algo_sum == loop_sum


if __name__ == '__main__':
	run_find_max(10)
	run_find_max(100)

