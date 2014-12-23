# #recursion problems
# Again, using no loops, no global variables, and without asking for the length of the array except to check if it's empty, write a function that returns the last index of a given input in a list. Negative one gets returned if the element doesn't occur in the list. Don't go from the back (for why not, see "Linked List Aside") Feel free to change to the signature of the function or use a helper function with a different signature!
# lastIndexOf(5, [1, 2, 4, 6, 5, 2, 7]) -> 4
# lastIndexOf(5, [1, 2, 4, 6, 2, 7]) -> -1
# lastIndexOf(5, [1, 2, 5, 4, 6, 5, 2, 7]) -> 5

def find_last(input_list, to_find, idx):
	if idx < 0:
		return -1
	elif input_list[idx] == to_find:
		return idx
	else:
		return find_last(input_list, to_find, idx-1)

#if we assume we don't want to start from the back, then we can use this
def nonback_find_last(input_list, to_find, idx=0):
	if idx == len(input_list):
		return -1
	else:
		rec_idx = nonback_find_last(input_list, to_find, idx+1)
		if input_list[idx] == to_find:
			last_idx = idx
		if idx > rec_idx:
			return idx
		return rec_idx

#find sum of a list recursively
def find_sum(lst):
	if not lst:
		return 0
	return lst[0] + find_sum(lst[1:])

#find the largest number of a list so far
def max_lst(numbers, largest_far=0):
	if not numbers:
		return largest_far
	next_num = numbers[0]
	if next_num > largest_far:
		return max_lst(numbers[1:], next_num)
	else:
		return max_lst(numbers[1:], largest_far)

def flatten_lst(lst, final_lst=list()):
	for element in lst:
		if isinstance(element, list):
			flatten_lst(element, final_lst)
		else:
			final_lst.append(element)
	return final_lst



print("Answer is %s"%flatten_lst([1,2,[4,4], 5]))


# print("Answer is %s"%nonback_find_last([1,2,3], 10))

# print("Answer is %s"%nonback_find_last([1, 2, 5, 4, 6, 5, 2, 7], 5))

# print("Sum is %s"%find_sum([1, 2, 3, 4, 5]))
# print("Sum is %s"%find_sum([]))


# print("Max is %s"%max_lst([7, 6, 10, 22, 15]))
# print("Max is %s"%max_lst([]))
# print("Max is %s"%max_lst([7, 6, 5, 4, 10, 11]))
