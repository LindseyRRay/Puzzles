#Fun with Binary Trees
#Q: Test if a tree is balanced. An unbalanced tree if heights if subtrees difference > 1
from tree import Node, tree1, tree2, tree3 


def balance_tree(root):
	#base case for recursion
	if root == None:
		return 0
	#get heights of left and right subtrees
	height_left = balance_tree(root.left)
	height_right = balance_tree(root.right)

	if height_left == -1 or height_right==-1 or abs(height_left - height_right) > 1 :
		return -1
	return 1 + max(height_right, height_left)

def main_tree(root):
	return balance_tree(root) != -1 




if __name__ == '__main__':
	assert balance_tree(tree1) == 3
	assert main_tree(tree1) == True

	assert balance_tree(tree3) == -1
	assert main_tree(tree3) == False



