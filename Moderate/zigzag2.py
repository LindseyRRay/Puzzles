
def find_next(seq, previous_ind, previous_sign):
	comp_item = seq[previous_ind]
	ind = previous_ind + 1
	while ind < len(seq):
		result = seq[ind] - seq[previous_ind]
		if result != 0 and previous_sign * result < 0:
			return ind
		else:
			ind += 1
	return None

def find_zig(seq):
	if len(seq) < 3:
		return len(seq), seq
	#keep track of best pattern and longest lengths 
	max_len = 0
	best_pattern = None
	starting_index = 0 
	while starting_index < len(seq) - 1:
		next_ind = starting_index + 1
		number_sequence = [seq[starting_index], seq[next_ind]]
		previous_pattern = seq[next_ind] - seq[starting_index]
		while next_ind != None and next_ind < len(seq):
			third_index = find_next(seq, next_ind, previous_pattern)
			if third_index:
				previous_pattern = seq[third_index] - seq[next_ind]
				number_sequence.append(seq[third_index])
			next_ind = third_index
			if len(number_sequence) > max_len:
				max_len = len(number_sequence)
				best_pattern = number_sequence
		starting_index += 1
	return max_len, best_pattern

if __name__ == '__main__':

	print(find_zig([1,3,2]))
	print(find_zig([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]))
	print(find_zig([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
249, 22, 176, 279, 23, 22, 617, 462, 459, 244]))
	
	#assert main([1, 7, 4, 9, 2, 5 ]) == (6, [1, 7, 4, 9, 2, 5 ])


