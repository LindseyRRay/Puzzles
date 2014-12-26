#Fun with Binary Trees
#Q: Test if a tree is balanced. An unbalanced tree if heights if subtrees difference > 1
from tree import Node, tree1, tree2, tree3 
import pdb

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

#create a balanced binary tree from an array of integers

def create_tree(lst, start, end):
	if end < start:
		return None
	else:
		mid = start + int((end-start)/2)
		root = Node(lst[mid])
		print("Adding %s"%root.value)
		root.left = create_tree(lst, start, mid-1)
		root.right = create_tree(lst, mid+1, end)
		return root


if __name__ == '__main__':
	assert balance_tree(tree1) == 3
	assert main_tree(tree1) == True

	assert balance_tree(tree3) == -1
	assert main_tree(tree3) == False

	head = create_tree([1,2,3,4,5], 0, 4)

	head2 = create_tree([15,16,17,0], 0, 3)


