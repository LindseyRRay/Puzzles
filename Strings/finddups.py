#find dups
# Q: Given a list of length n+1 with numbers from 1 to n, there will be #at least one duplicate. Find it.
# Running time: O(n). Space: O(1). Or rigorously O(lgn) given that a #constant variable to represent the number "n" grows with lgn.
# http://stackoverflow.com/questions/6420467/find-any-one-of-multiple-possible-repeated-integers-in-a-list/6420503#6420503

#use boolean array of len n, use indices as integers already found
#runs in O(n) worst case time and doesn't alter input array
import random
import pdb


def array_dups(lst):
	max = len(lst)-1
	arr = [False]*max
	n=0
	ind = lst[n]
#while loop that changes elements in array to true when first found
	while arr[ind] == False:
		arr[ind]=True
		n+=1
		ind = lst[n]
	return ind 
#use a cycle

def cycle(lst):
	#declare a fast and slow pointer, fast pointer always moves first
	slow = len(lst)-1
	fast = len(lst)-1
	#pdb.set_trace()
	while True:
		slow = lst[slow]
		fast = lst[lst[fast]]
		if slow == fast:
			break
	#create a finder pointer from end of array and advance until hits pointer
	finder = len(lst)-1
	while True:
		slow = lst[slow]
		finder = lst[finder]

		if slow == finder:
			return slow

#if exactly one duplicate, sum the list, then subtract that from the sum of n to 1
def summation(lst):
	max = len(lst)
	non_dup_sum = actual_sum(max-1)
	#calculate the duplicate by subtracting the two lists
	return sum(lst) - non_dup_sum


def actual_sum(max):
	count = 0
	for x in range(max):
		count += x
	return count



if __name__ == '__main__':

	for fnc in [summation, array_dups, cycle]:
		arr = [n for n in range(100)]
		random.shuffle(arr)
		dups = arr[-1]
		arr.append(dups)
		random.shuffle(arr)
		print("dup is %d"%dups)
		fn_result = fnc(arr)
		assert dups == fn_result


