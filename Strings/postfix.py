#infix to postfix calculation
# to_postfix("2+7*5") # Should return "275*+"
# to_postfix("3*3/(7+1)") # Should return "33*71+/"
# to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
# oper preceednce
# Algo- print operand to string
# for operator, if stack empty, push operator
# if operator on top has HIGHER (not equal) precedence, pop it
# print it and then push new operator on 
# when end of input expression, pop and print all op
# left parenthesis have highest precedence in string
# but lowest in stack
# when right paren rad, the stack is popped until left parenthesis
# these are not printed 

def is_number(char):
	try:
		a = int(char)
		return (True, a)
	except:
		return (False, None)

def postfix(infix):
	op_precedence = {'(':-1, '+':0, '-':0, '*':1, '/':1, '^':2}
	output_str = list()
	operator_stack = list()
	for char in infix:
		if is_number(char)[0]:
			output_str.append(str(is_number(char)[1]))
		else:
			#if stack empty, push onto stack or 
			if not operator_stack or char=='(':
				operator_stack.append(char)
			#if you hit a right parens, print until you get left
			elif char == ')':
				while operator_stack[-1] != '(':
					output_str.append(operator_stack.pop())
			#remove the left parens
				operator_stack.pop()
				#if top of stack of lower precendence 
			elif op_precedence[operator_stack[-1]] < op_precedence[char]:
				operator_stack.append(char)
			else:
				#pop stack until hit an operator with lower
				while len(operator_stack) > 0 and op_precedence[operator_stack[-1]] >= op_precedence[char]:
					output_str.append(operator_stack.pop())
				operator_stack.append(char)
	#append all remaining chars in stack to outpu
	while operator_stack:
		output_str.append(operator_stack.pop())

	return ''.join(output_str)

if __name__ == '__main__':
	print(postfix("2+7*5"))

postfix