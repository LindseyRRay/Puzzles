#Q: print all valid (properly) open and closed balanced combinations of 
#n pairs of parenthesis


def bal_parenthesis(left_p=['('], right_p=[')'], current_str ="", combos = list()):
	if len(left_p) == len(right_p) == 0:
		combos.append(current_str)
		return
	else:
		if len(left_p) > 0:
			next_str = current_str.append(left_p.pop())
			bal_parenthesis(left_p, right_p, next_str, combos)

		if len(right_p) > left_p:
			next_str2 = current_str.append(right_p.pop())
			bal_parenthesis(left_p, right_p, next_str, combos)
	
def rec_bal_parens(n, combos= list()):
	if n <= 0:
		combos.append("")
		return 
	else:
		rec_bal_parens(n-1, combos)
		to_add = list()
		for combo in combos:
			for index, char in enumerate(combo):
				if char == '(':
					new_chars = copy_insert(combo, index)
					print("new one")
					print(new_chars)
					print("combos")
					print(combos)
					if new_chars not in combos and new_chars not in to_add:
						print("Adding")
						to_add.append(new_chars)
			first_chars="()"+combo
			if first_chars not in combos and first_chars not in to_add:
				to_add.append(first_chars)

		combos.extend(to_add)


def copy_insert(new_str, index):
	return new_str[:index+1] + '()' + new_str[index+1:]


if __name__ == '__main__':
	combos = list()
	rec_bal_parens(3, combos)
	print(combos)

