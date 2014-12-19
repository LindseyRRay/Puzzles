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
print("Answer is %s"%nonback_find_last([1,2,3], 3))

print("Answer is %s"%nonback_find_last([1,2,3], 10))

print("Answer is %s"%nonback_find_last([1, 2, 5, 4, 6, 5, 2, 7], 5))
