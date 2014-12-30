#Q: return all subsets of a set
#trick is to realize each subsequent element inserts itself into each of sets in layer below
import copy 

def find_subsets(sample_set, subsets = list()):	
	#base case
	if not sample_set:
		print("base case")
		subsets.append([])
	else:
		next_el = sample_set.pop()
		find_subsets(sample_set, subsets)
		print(subsets)
		el_subsets= list()
		for lst in subsets:
			new_tup = list()
			for el in lst:
				new_tup.extend([el])
			new_tup.extend([next_el])
			print("adding")
			print(new_tup)
			el_subsets.append(new_tup)
		subsets.extend(el_subsets)
		print(subsets)

#find all permutations of a string

def find_permutations(stri, perms):
	if not stri:
		print("Base case")
		perms.append("")
		return
	else:
		print("rec case")
		next_el = stri[0]
		print(next_el)
		find_permutations(stri[1:], perms)
		to_append= list()
		for perm in perms:
			print(perm)
			index=0
			while index <= len(perm):
				new_perm =""
				new_l2= list(perm)[:]
				new_l2.insert(index, next_el)
				print(new_l2)
				new_perm = "".join(new_l2)
				to_append.append(new_perm)
				index+=1
				del new_l2
			print("perms is ")
			print(perms)

		perms.extend(to_append)



if __name__ == '__main__':
	# new_l = list()
	# find_subsets([0,1, 2], new_l)
	# print(new_l)

	new_perms = list()
	find_permutations("abc", new_perms)
	print(new_perms)

