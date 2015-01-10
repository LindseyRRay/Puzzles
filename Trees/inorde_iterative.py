#Q: Perform in order tree traversal iteratively
# Algo:
# 1) set current node to root
# 2) push to stack if not null and move to left
# 3) push until no left child
# 4) pop stack, print popped note and set current = node.right
# 5) Repeat 2-4 until stack is empty 
from tree import tree1, tree2, tree3

def traverse_iter(root):
	current = root.left
	stack = [root]
	while len(stack) > 0 or current != None :
		if current != None:
			stack.append(current)
			current = current.left
		else:
			next_node = stack.pop() 
			print(next_node.value)
			current = next_node.right



if __name__ == '__main__':
	print("tree1")
	traverse_iter(tree1)
	print("tree2")
	traverse_iter(tree2)
	print("tree3")
	traverse_iter(tree3)


