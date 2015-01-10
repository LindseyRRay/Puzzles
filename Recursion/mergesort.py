#Q: implement mergesort
import pdb

def mergesort(input_list):
	if len(input_list) <= 1:
		return input_list 
	else:
		mid = int(len(input_list)/2)
		low_side = mergesort(input_list[:mid])
		high_side = mergesort(input_list[mid:])
		#combine
		output_list = list()
		low_index = 0 
		high_index = 0
		print(low_side)
		print(high_side)
		#pdb.set_trace()
		while not (len(low_side) == len(high_side)==0):
			if not high_side or (low_side and low_side[0] < high_side[0]):
				output_list.append(low_side.pop(0))
			elif not low_side or (high_side and high_side[0] <= low_side[0]):
				output_list.append(high_side.pop(0))
		return output_list

if __name__ == '__main__':
	print(mergesort([2,1,3]))