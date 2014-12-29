#Q: find the magic index- magic index if A[i] = i in an array of SORTED DISTINCT INTEGERS

#option 1-> brute force it by iterating through the array in an intelligent fashion

def jump_array(lst):
	#for the first element in list, jump to the index of that value and
	#continue to do so until hit the end of the list
	#worst case this is O(n)
	i=0
	while i < len(lst):
		print("Checking index %d value %d" % (i, lst[i]))
		val = lst[i]
		if val == i:
			return True
		elif val < 0 or i > val:
			i+=1
		else:
			i=val
	return False

def binary_sort(lst, st, end):
	#note this fails when elements are not distinct
	if st > end:
		return False
	mid = int((end - st)/2) + st
	print("Checking index %d value %d" % (mid, lst[mid]))
	if mid == lst[mid]:
		return True
	if lst[mid] < mid:
		answ = binary_sort(lst, mid+1, end)
	else:
		answ = binary_sort(lst, st, mid-1)
	return answ 

def binary_nondistinct(lst, st, end):
	#need to search both sides of the array because no guarantees arrays are distinct
	if st > end:
		return False
	mid = int((end - st)/2) + st
	print("Checking index %d value %d" % (mid, lst[mid]))
	if mid == lst[mid]:
		return True
	if lst[mid] < mid:
		answ = binary_nondistinct(lst, mid+1, end)
		ans2 = binary_nondistinct(lst, st, lst[mid])
	elif lst[mid] > mid:
		answ = binary_nondistinct(lst, st, mid-1)
		ans2 = binary_nondistinct(lst, lst[mid], end)
	return answ or ans2




if __name__ == '__main__':

	lst1 = [[-10, -5, 0, 15, 20], [-1, 1, 4, 5, 6], [-1, 1, 1, 4, 5, 6]]
	for lst in lst1:
		print("Answer is %s"%jump_array(lst))
		print("Binary Sort Answer is %s"%binary_sort(lst, 0, len(lst)-1))
		print("Non Distinct Binary Sort Answer is %s"%binary_nondistinct(lst, 0, len(lst)-1))


