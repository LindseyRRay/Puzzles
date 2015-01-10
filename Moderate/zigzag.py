# A sequence of numbers is called a zig-zag sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. 
# A sequence with fewer than two elements is trivially a zig-zag sequence.

# # For example, 1,7,4,9,2,5 is a zig-zag sequence because the differences 
# (6,-3,5,-7,3) are alternately positive and negative. In contrast, 
# 1,4,7,2,5 and 1,7,4,5,5 are not zig-zag sequences, the first because its 
# first two differences are positive and the second because its last 
# difference is zero.

# # Given a sequence of integers, sequence, return the length of the 
# longest subsequence of sequence that is a zig-zag sequence. A subsequence 
# is obtained by deleting some number of elements (possibly zero) 
# from the original sequence, leaving the remaining elements in their 
# original order.
import pdb 

def is_negative(num):
	return num < 0

def compare_nums(num1, num2):
	#tests if two numbers have opposite signs
	return num1 != 0 and num2 != 0 and (is_negative(num1)^is_negative(num2)) 

def check_sign(dif):
	#checks if pattern of numeric differences returns all True
	return all([compare_nums(dif[i], dif[i+1]) for i in range(len(dif)-1)])

def create_pattern(seg, hist):
	#returns list of tuples of num difference and indices ffor given segment
	return [check_sub_exists(seg[x], seg[x+1], hist) for x in range(len(seg)-1)]

def check_sub_exists(ind1, ind2, stored_op):
	if (ind1, ind2) in stored_op.keys():
		# return (stored_op[(ind1, ind2)], (ind1, ind2)) 
		return stored_op[(ind1, ind2)]
	else:
		result = ind2 - ind1
		stored_op[(ind1, ind2)] = result
		#return (result, (ind1, ind2))
		return result 

def return_pattern(pattern, stored_hist):
	print(pattern)
	if tuple(pattern) in stored_hist.keys():
		return stored_hist[tuple(pattern)]
	else:
		result = check_sign(pattern)
		stored_hist[tuple(pattern)] = result
		return result 

def return_newseq(seq, ind, num_deletes):
	#generates sequences of combinations 
	#how to create all permutations of a string
	start_delete = ind+1
	while start_delete + num_deletes < len(seq):
		copy_seq = seq[:]
		for i in range(num_deletes):
			copy_seq.pop(start_delete)
		yield copy_seq
		start_delete += 1

def check_combinations(seq, subs, past_signs, max_len = 0) :
	if len(seq) == 1:
		return (1, seq)
	for index, item in enumerate(seq):
		winning_seq = None
		for to_delete in range(len(seq)-1):
			print("Num to deletes is %s"%to_delete)
			for next_seq in return_newseq(seq, index, to_delete):
				print("next sequence is ")
				print(next_seq)
				if len(next_seq) == 8:
					pdb.set_trace()
				if len(next_seq) > max_len:
					pattern = create_pattern(next_seq, subs)
					print("pattern is ")
					print(pattern)
					result = return_pattern(pattern, past_signs)
					print("Result is %s"%result)
					if result and len(pattern)+1 > max_len:
						max_len = len(pattern) + 1
						winning_seq = next_seq
		return max_len, winning_seq

def main(seq):
	subs = dict()
	hist_patterns = dict()
	return check_combinations(seq, subs, hist_patterns, 0)


def test():
	#assert main([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == (7, [1, 17, 5, 10, 5, 16, 8])
	#assert main([1, 7, 4, 9, 2, 5 ]) == (6, [1, 7, 4, 9, 2, 5 ])
	#print(main([44]))
	#assert main([44]) == (1, [44])

	print(main([70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100]))
	#assert main([374, 40, 854, 203, 203, 156, 362, 279, 812, 955, 
# 600, 947, 978, 46, 100, 953, 670, 862, 568, 188, 
# 67, 669, 810, 704, 52, 861, 49, 640, 370, 908, 
# 477, 245, 413, 109, 659, 401, 483, 308, 609, 120, 
# 249, 22, 176, 279, 23, 22, 617, 462, 459, 244])[0] == 36


test()


			


