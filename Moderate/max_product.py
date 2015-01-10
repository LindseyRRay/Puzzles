#Q: given an array of ints, find the highest product you can get from 3 of the ints
import pdb

def rank_positives(max_list, comp_num):
	if comp_num <= max_list[-1]:
		return False
	elif comp_num > max_list[0]:
		old = max_list[0]
		max_list[0] = comp_num
		rank_positives(max_list, old)
	elif comp_num > max_list[1] and comp_num <= max_list[0]:
		old = max_list[1]
		max_list[1] = comp_num
		rank_positives(max_list, old)
	elif comp_num > max_list[-1] and comp_num <= max_list[1]:
		max_list[-1] = comp_num
		return True
	else:
		raise Exception("Falls into weird category")

def rank_negatives(max_list, comp_num):
	if comp_num >= max_list[-1]:
		return False
	elif comp_num < max_list[0]:
		old = max_list[0]
		max_list[0] = comp_num
		rank_negatives(max_list, old)
	elif comp_num < max_list[1] and comp_num >= max_list[0]:
		old = max_list[1]
		max_list[1] = comp_num
		rank_negatives(max_list, old)
	elif comp_num < max_list[-1] and comp_num >= max_list[1]:
		max_list[-1] = comp_num
		return True
	else:
		raise Exception("Falls into weird category")

def product_list(input_list):
	product = 1
	for integer in input_list:
		product *= integer
	return product

def find_max_product(input_array):
	max_positives = [0, 0, 0]
	max_negatives = [0, 0, 0]
	num_negs = 0
	for num in input_array:
		if num > 0:
			rank_positives(max_positives, num)
		elif num < 0:
			num_negs += 1
			rank_negatives(max_negatives, num)
	neg_list = max_negatives[:2]
	neg_list.append(max_positives[0])
	neg_max = product_list(neg_list)
	pos_max = product_list(max_positives)
	return max(neg_max, pos_max)

if __name__ == '__main__':
	li = [-10, -10, 1, 3, 2]
	print(find_max_product(li))
